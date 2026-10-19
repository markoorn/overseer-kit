#!/usr/bin/env python3
"""PreToolUse hook: stop secrets in .env files from being printed into the transcript.

Bash: any command that references a .env file (.env, .env.local, ... but not
.env.example/.sample/.template/.dist) is denied unless every reference is one of the
non-printing forms below. Read/Grep: denied outright on .env files.

Allowed Bash forms:
  K=$(grep -E '^NAME=' .env | cut -d= -f2-)   capture a value into a variable
  cut -s -d= -f1 .env / ... .env | cut -s -d= -f1
                                               variable names only; -s is required,
                                               because cut prints a line with no '='
                                               (e.g. `KEY: value`) whole
  awk -F= 'NF>1{print $1}' .env                variable names only
  source .env / . ./.env                       load without printing
  ls / test -f / [ -f ] / git check-ignore     existence checks
  cp <src> <dest>                              seeding a worktree: allowed when the
                                               destination is under a .worktrees/
                                               directory and -v is not passed

Fails open (allows) on malformed input so a hook bug never blocks all tools.
"""
import json
import os
import re
import shlex
import sys

TEMPLATE_SUFFIXES = {".example", ".sample", ".template", ".dist"}

ENV_REF = re.compile(r"(?:^|(?<=[\s/'\"=<(]))\.env((?:\.[\w-]+)*)\b")

SAFE_PATTERNS = [
    # VAR=$( ... ) capture, one level of nesting is enough for grep|cut pipelines
    re.compile(r"\b[A-Za-z_]\w*=\$\((?:[^()]|\([^()]*\))*\)"),
    # names only via awk; NF>1 skips lines without '='. cut is checked by
    # is_names_only_cut because its flags can come in any order.
    re.compile(r"awk\s+-F\s*['\"]?=['\"]?\s+['\"]NF\s*>\s*1\s*\{\s*print\s+\$1\s*\}['\"][^|;&()]*"),
    re.compile(r"(?:^|(?<=[\s;&|(]))(?:source|\.)\s+[^\s;&|]*\.env[\w.-]*"),
    re.compile(r"(?:^|(?<=[\s;&|(]))(?:ls|stat|test)\b[^|;&()]*"),
    re.compile(r"\[\[?\s+-[efsr]\s+[^\]]*\]\]?"),
    re.compile(r"git\s+(?:check-ignore|ls-files|status)\b[^|;&()]*"),
]

REASON = (
    "Blocked by the overseer-kit env-secrets guard: this would print .env "
    "contents (secrets) into the transcript. Use a non-printing form instead:\n"
    "  value into a variable: K=$(grep -E '^EXACT_NAME=' path/.env | cut -d= -f2-)\n"
    "  names only:            cut -s -d= -f1 path/.env   (-s is required: without it,\n"
    "                         lines with no '=' such as `KEY: value` print whole)\n"
    "  compare names:         diff <(cut -s -d= -f1 .env.example) <(cut -s -d= -f1 .env)\n"
    "  load for a command:    set -a; source path/.env; set +a; <command>\n"
    "  seed a worktree:       cp path/.env <worktree-root>/.worktrees/<slug>/path/.env\n"
    "Never echo/print the captured variable. If a search pattern merely mentions "
    "'.env' (e.g. grep for process.env), escape it as '\\.env'."
)


def is_secret_env(suffix: str) -> bool:
    return not any(suffix.endswith(t) for t in TEMPLATE_SUFFIXES)


def has_secret_env_ref(text: str) -> bool:
    return any(is_secret_env(m.group(1)) for m in ENV_REF.finditer(text))


def is_secret_env_path(path: str) -> bool:
    name = os.path.basename(path.rstrip("/"))
    if not (name == ".env" or name.startswith(".env.")):
        return False
    return is_secret_env(name[len(".env"):])


# `cut ...`, optionally preceded by `<producer> |`, up to the next separator.
CUT_SEGMENT = re.compile(r"(?:[^|;&()]*\|\s*)?\bcut\b([^|;&()]*)")


def is_names_only_cut(args: str) -> bool:
    """True for a cut that prints field 1 split on '=' and only delimited lines (-s)."""
    try:
        tokens = shlex.split(args)
    except ValueError:
        return False
    delimiter = fields = None
    only_delimited = False
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in ("-s", "--only-delimited"):
            only_delimited = True
        elif token.startswith("--delimiter="):
            delimiter = token[len("--delimiter="):]
        elif token.startswith("--fields="):
            fields = token[len("--fields="):]
        elif token.startswith("-") and not token.startswith("--") and len(token) > 1:
            flags = token[1:]
            for j, flag in enumerate(flags):
                if flag == "s":
                    only_delimited = True
                elif flag in "df":
                    value = flags[j + 1:]
                    if not value and i + 1 < len(tokens):
                        i += 1
                        value = tokens[i]
                    if flag == "d":
                        delimiter = value
                    else:
                        fields = value
                    break
                else:
                    return False
        i += 1
    return delimiter == "=" and fields == "1" and only_delimited


def strip_names_only_cuts(command: str) -> str:
    return CUT_SEGMENT.sub(
        lambda m: " " if is_names_only_cut(m.group(1)) else m.group(0), command
    )


# Copying a .env into a fresh worktree is allowed: cp prints nothing unless -v is
# passed, and the destination must resolve to a path under a `.worktrees/` directory,
# so `cp .env /dev/stdout` still fails.
CP_SEGMENT = re.compile(r"(?:^|(?<=[\s;&|(]))cp\b([^|;&()<>]*)")


def is_worktree_seed_copy(args: str, cwd: str) -> bool:
    try:
        tokens = shlex.split(args)
    except ValueError:
        return False
    paths = []
    for token in tokens:
        if token.startswith("-"):
            if token in ("--verbose",) or (not token.startswith("--") and "v" in token):
                return False
            continue
        paths.append(token)
    if len(paths) < 2:
        return False
    dest = os.path.realpath(os.path.join(cwd, os.path.expanduser(paths[-1])))
    return (os.sep + ".worktrees" + os.sep) in dest + os.sep


def strip_worktree_seed_copies(command: str, cwd: str) -> str:
    return CP_SEGMENT.sub(
        lambda m: " " if is_worktree_seed_copy(m.group(1), cwd) else m.group(0),
        command,
    )


def bash_is_unsafe(command: str, cwd: str = "") -> bool:
    if not has_secret_env_ref(command):
        return False
    stripped = strip_names_only_cuts(command)
    stripped = strip_worktree_seed_copies(stripped, cwd or os.getcwd())
    for pattern in SAFE_PATTERNS:
        stripped = pattern.sub(" ", stripped)
    return has_secret_env_ref(stripped)


def deny() -> None:
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": REASON,
            }
        },
        sys.stdout,
    )


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (ValueError, OSError):
        return
    tool = payload.get("tool_name")
    tool_input = payload.get("tool_input") or {}

    if tool == "Bash":
        if bash_is_unsafe(
            str(tool_input.get("command", "")), str(payload.get("cwd") or "")
        ):
            deny()
    elif tool == "Read":
        if is_secret_env_path(str(tool_input.get("file_path", ""))):
            deny()
    elif tool == "Grep":
        targets = [str(tool_input.get("path", "")), str(tool_input.get("glob", ""))]
        if any(is_secret_env_path(t) or has_secret_env_ref(t) for t in targets if t):
            deny()


if __name__ == "__main__":
    main()
