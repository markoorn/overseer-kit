# Using the kit with Cursor and other tools

The kit is three things with different portability:

| Piece | Format | Works in |
| --- | --- | --- |
| Skills (`skills/*/SKILL.md`) | Agent Skills (open format: `SKILL.md` with `name` + `description` frontmatter) | Claude Code, Codex, Cursor, and any tool that reads the format |
| Agents (`agents/*.md`) | Claude Code subagent files | Claude Code as four agents; anywhere else as system-prompt text |
| Hooks (`addons/hooks/`) | Claude Code `PreToolUse` hooks | Claude Code only |

## Cursor

Cursor reads skills from `.cursor/skills/<name>/SKILL.md` (check your version's docs for
the exact path; it has moved). Copy the kit's skill directories there:

```bash
cp -r overseer-kit/skills/* <your-repo>/.cursor/skills/
```

For the overseer's discipline, add the portable sections of `agents/overseer.md` (Hard
constraints, Working principles, Verification protocol, Reading a report) to a Cursor rule
file (`.cursor/rules/overseer.mdc`, set to always apply). Leave out Session start,
Lifecycle, Writing a brief and Skills and who runs them; those describe Claude Code's
delegation.

Put `OVERSEER.md` at the repo root as usual; the skills read it by path.

## Any other tool

If it reads `SKILL.md` files: copy `skills/` wherever it looks.

If it does not: the skill bodies are plain Markdown procedures. Paste the one you need
into the conversation, or point the tool at the file.

For the agents, the system-prompt route works everywhere: take `agents/overseer.md` from
"## Who you are" to the end of "## Working principles", plus "## Verification protocol"
and "## Reading a report", and use that as the tool's standing instructions. The verifier's
"## Procedure" is a good pre-merge checklist on its own.

## What does not transfer

- The split between builder and verifier as separate contexts. The nearest substitute in a
  single-agent tool is a second, fresh conversation given only the claim and the worktree.
- The hooks. The worktree-per-task and never-print-secrets rules become policy in your
  rules file; a git pre-commit hook can enforce the first.
- Claude artifacts for `mockup`. The skill already falls back to a single HTML page written
  locally when there is no artifact tool.
