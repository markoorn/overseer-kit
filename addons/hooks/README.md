# Optional hooks

The agents follow these rules as policy whether or not the hooks are installed. The hooks
turn two of the rules into something the harness enforces, so a worker that drifts gets
blocked instead of trusted. They are add-ons: nothing in the kit depends on them, and the
plugin does not install them for you (a plugin's `hooks/hooks.json` fires in every session
where the plugin is enabled, which would make them mandatory). Install the ones you want,
where you want them.

Both are `PreToolUse` hooks that return a deny decision with a reason the agent can read.
Both fail open on malformed input, so a hook bug never blocks every tool.

## worktree-guard.json

**What it blocks:** any `Edit`, `Write` or `NotebookEdit` whose target is inside a git
checkout but not inside a `.worktrees/` directory. This is the worktree-per-task rule: two
concurrent sessions editing the same primary checkout silently clobber each other's
uncommitted changes, and the only thing that ever caught it was luck.

**What it allows:** paths under `.worktrees/`, plus `OVERSEER.md`, `.claude/`, `CLAUDE.md`
and `docs/` anywhere (prose the overseer may edit in place). Set `OVERSEER_GUARD_OFF=1` in
the environment for a session you are driving live in the main checkout.

**Needs:** `jq` and `git` on PATH.

**Install:** merge the `hooks` object into the `hooks` object of one of:

- `~/.claude/settings.json` (every project on this machine)
- `<repo>/.claude/settings.json` (this repo, committed, everyone who clones it)
- `<repo>/.claude/settings.local.json` (this repo, only you)

If the file has no `hooks` key yet, you can paste the whole object in. If it already has
`PreToolUse` entries, append this one to that array.

## block-env-secrets.py

**What it blocks:** a `Bash` command that would print the contents of a `.env` file
(`.env`, `.env.local`, `.env.production`, ... but not `.env.example` and the other
template suffixes), and `Read` or `Grep` aimed at one. A mask that fails silently leaks
the whole value, so the rule is "never print", not "print carefully".

**What it allows:** the non-printing forms the agents are told to use:

```
K=$(grep -E '^NAME=' .env | cut -d= -f2-)    capture a value without echoing it
cut -s -d= -f1 .env                          variable names only
awk -F= 'NF>1{print $1}' .env                variable names only
source .env / . ./.env                       load without printing
ls / test -f / [ -f ] / git check-ignore     existence checks
cp <src> <dest>                              seeding a worktree, when the destination
                                             is under a .worktrees/ directory and -v
                                             is not passed
```

**Needs:** `python3` on PATH.

**Install:** copy the script somewhere stable, for example `~/.claude/hooks/`, make it
executable, and add this to the `hooks` object of a settings file (same choice of file as
above):

```json
{
  "PreToolUse": [
    {
      "matcher": "Bash|Read|Grep",
      "hooks": [
        {
          "type": "command",
          "command": "python3 /absolute/path/to/block-env-secrets.py",
          "timeout": 5
        }
      ]
    }
  ]
}
```

## Check they fire

Start a session in the repo and ask Claude to edit a file in the primary checkout; the
worktree guard should refuse with its reason. Ask it to `cat .env`; the secrets guard should
refuse. Hooks that exit 0 show nothing, so the only visible sign of a healthy hook is the
refusal when you provoke it.
