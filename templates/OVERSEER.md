# OVERSEER.md

The overseer and its workers read this file at the start of every session. It holds
everything about this repo and this machine that the agents must not guess. `/overseer-kit:setup`
writes it through an interview; edit it by hand whenever something changes.

Lines marked `<...>` are placeholders. An empty section means "not configured", and the
agents treat it as such rather than assuming a default.

## Repo

- **Name:** <repo name>
- **Default branch:** main
- **Primary checkout:** <absolute path>
- **Worktree root:** <absolute path, default: the directory above the primary checkout, plus `/.worktrees`>
- **Branch naming:** <e.g. `fix/<TICKET>-<slug>` for bugs, `feat/<TICKET>-<slug>` for features; or "no convention">
- **Conventions file:** <path to AGENTS.md, CONTRIBUTING.md or CLAUDE.md that holds code style; or "none">

## Commands

The builder runs these for the workspaces it touched; the verifier re-runs them independently.

- **Install (first act in a fresh worktree):** <e.g. `bun install`, `npm ci`, `pnpm install`>
- **Build, when needed:** <e.g. `bun run build`; or "not needed">
- **Codegen, when needed:** <e.g. `bun run codegen`; or "none">
- **Env files a fresh worktree needs:** <e.g. "copy `apps/web/.env` from the primary checkout"; or "none">

| Workspace | Typecheck | Lint | Test | Runner |
| --- | --- | --- | --- | --- |
| <path> | <command> | <command> | <command> | <jest / vitest / pytest / ...> |

## Connectors

Which external systems this machine can reach from a Claude Code session, and how. Each one
is optional. The overseer lists their status at session start; the investigator uses whichever
are present. For anything marked "none" the overseer uses the standing fallback (paste the
ticket, use the `gh` CLI, mark logs or numbers as not checkable).

- **Tickets:** <e.g. "Jira via the `atlassian` MCP server, project key ABC"; "GitHub Issues"; "Linear"; or "none">
- **Code hosting:** <e.g. "GitHub via `gh`"; "GitHub MCP"; "GitLab via `glab`">
- **Logs:** <e.g. "Datadog MCP, filter `environment:production`"; or "none">
- **Errors:** <e.g. "Sentry MCP"; or "none">
- **Database:** <e.g. "Postgres MCP, read-only user, a QA copy of prod"; or "none">

## Compatibility rules

- **Shipped clients the API cannot break:** <e.g. "mobile apps in the stores, so every API change is additive"; or "none">
- **Other invariants:** <anything a builder must never do, one per line>

## Review and release

- **PR reviewers:** <handles; or "ask">
- **Merge policy:** <e.g. "PR required, squash merge"; "direct to main allowed in this repo">
- **Ticket automation:** <e.g. "branch and PR names move tickets; never transition by hand"; or "none">

## Known traps

One per line. Things that only hurt once you hit them: a hook that fails in a fresh worktree
until install has run, a flag that silently skips tests, a token scope that breaks one `gh`
subcommand. The overseer copies the relevant ones into worker briefs.

- <trap>

## House style

How the overseer and its workers write. The default is the kit's house style (see
`docs/house-style.md` in the kit): plain English, no em dashes, no time estimates, sized as
trivial / small / medium / large / very large, evidence before opinion, numbered questions.

- **Style:** <"kit default" or "custom, see below">
- <custom rules, one per line, each with an example sentence that is right and one that is wrong>

## Marketing (only if you use ad-brief)

- **Brand directory:** <path holding `brand-visual.md`, `brand-voice.md`, `creative-playbook.md`>
- **Campaign records:** <path holding `campaigns/`, see the kit's `templates/campaigns/README.md`>
- **Production branch:** <the branch that reflects what is live, e.g. `production`; or "main is production">
- **App Store id:** <numeric id for the iTunes lookup; or "not an app">
- **Google Play package:** <e.g. `com.example.app`; or "not an app">
- **Generation account:** <e.g. "Higgsfield, metered, spend above N credits needs a yes"; or "none, briefs only">
