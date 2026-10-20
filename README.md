# overseer-kit

A way of running an AI coding agent that refuses to call anything done without evidence.

One **overseer** agent frames each task, plans it, and hands every piece of real work to
three workers: an **investigator** (read-only research), a **builder** (edits inside a git
worktree, with tests) and a **verifier** (re-runs everything independently and reports
PASS or FAIL with counts). The overseer never edits code, never runs a build, never pushes,
and never takes a builder's word for it. You get a verified, committed worktree and a
report that says what was checked, how, and what was not.

Two skills come with it: **ad-brief** turns a feature or campaign slot into grounded ad
concepts without spending a credit, and **mockup** puts the current state and three
options on one shared page before anyone builds anything. A third, **setup**, interviews
you once and writes the one file the agents read instead of guessing about your repo.

Everything repo-specific (commands, worktree location, branch naming, which ticket or log
tools you have, house style) lives in `OVERSEER.md` in your repo. The kit never needs
editing to fit a project.

## Contents

```
.claude-plugin/plugin.json      the plugin manifest
.claude-plugin/marketplace.json lets you install straight from this repo
agents/                         overseer, investigator, builder, verifier
skills/setup/                   first-run interview, writes OVERSEER.md
skills/ad-brief/                grounded ad concepts, no spend
skills/mockup/                  current state + options on one shared artifact
templates/OVERSEER.md           the profile the agents read
templates/brand/                brand-visual, brand-voice, creative-playbook skeletons
templates/campaigns/README.md   the three campaign records ad-brief keeps
addons/hooks/                   optional enforcement hooks (worktree guard, env secrets)
docs/                           how it works, house style, Codex and other-tool install,
                                ad-brief getting started, generation lessons
```

If you are here for the ad side, read `docs/ad-brief-guide.md` first: what to ask
ad-brief for, which brand documents actually move the output, and why the production
guidance assumes Higgsfield. `docs/generation-lessons.md` is the distilled production
playbook (about ninety lessons from real campaigns, brand stripped out); setup seeds your
own playbook with it.

## Install: Claude Code

Three ways. The first is the one to use once you have settled in; the second is for
trying it; the third is the plain-files route that also works for the agents on every
Claude Code version.

**1. From this repo as a marketplace** (updates arrive with `claude plugin update`):

```bash
claude plugin marketplace add markoorn/overseer-kit
claude plugin install overseer-kit@overseer-kit
```

The repo is private, so your `gh auth status` or git credentials must have access.

**2. For one session, from a clone:**

```bash
git clone git@github.com:markoorn/overseer-kit.git
claude --plugin-dir ./overseer-kit
```

**3. As plain files in a repo** (no plugin mechanism at all):

```bash
cp -r overseer-kit/agents/*  <your-repo>/.claude/agents/
cp -r overseer-kit/skills/*  <your-repo>/.claude/skills/
```

With routes 1 and 2 the skills are `/overseer-kit:setup`, `/overseer-kit:ad-brief`,
`/overseer-kit:mockup` and the agents are `overseer-kit:overseer` and so on. With route 3
they are `/setup`, `/ad-brief`, `/mockup` and `overseer`.

## First run

1. Open a session in your repo and run the setup interview:
   `/overseer-kit:setup` (or `/setup` with route 3). It detects what it can (package
   manager, scripts, branch prefixes, which MCP connectors are configured), asks about the
   rest, and writes `OVERSEER.md` at the repo root. Every connector is optional; it tells
   you what the fallback is for each one you do not have.
2. Launch the overseer as the main session:

   ```bash
   claude --agent overseer            # route 3, or any route on a version that scopes plugin agents this way
   claude --agent overseer-kit:overseer   # routes 1 and 2
   ```

   It orients itself, lists which connectors are connected, and asks what initiative you
   are overseeing. From there it runs Intake, Frame, Plan (a hard stop for your go),
   Execute (worktree, builders, verifiers) and Hand back. `docs/how-it-works.md` walks
   through a full run.

3. Optional hooks. The agents follow the worktree-per-task and never-print-secrets rules as
   policy; `addons/hooks/` turns them into something the harness enforces. The setup
   interview offers them; `addons/hooks/README.md` has the install.

## Models

Everything runs on `opus`, set in each agent's frontmatter. When the overseer is launched
with `--agent`, its frontmatter `model:` sets the session's model; `--model` on the command
line overrides it. A stronger, pricier model for the overseer is rarely worth it: in
practice the overseer was most of a run's cost while doing no hands-on work, and on plans
where the top model has its own weekly cap it draws down the shared limit faster. Change the
lines if your account has a different strong model.

## House style

The agents write in a particular way by default: plain English, no em dashes, no time
estimates (sizes are trivial to very-large), evidence before opinion, numbered questions
with numbered options, never "you're absolutely right". That is one person's style, not a
law; `docs/house-style.md` explains each rule, and the setup interview lets you keep it,
tweak it, or describe your own in `OVERSEER.md` § House style.

## Other tools

The skills follow the open Agent Skills format (`SKILL.md` with `name` and `description`
frontmatter), so Codex, Cursor and anything else that reads that format can use them
unchanged. The agents are Claude Code subagent files; their bodies work as system prompts
anywhere, but the delegation between them is a Claude Code feature.

- `docs/install-codex.md`: Codex, which is the tested second platform.
- `docs/install-other.md`: Cursor and anything else.

## Updating

Route 1: `claude plugin update overseer-kit`. Route 2: `git pull` in the clone and
`/reload-plugins` in a running session. Route 3: copy the files again. `OVERSEER.md` and
the brand documents are yours and never touched by an update.
