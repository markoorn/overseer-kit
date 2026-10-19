# Using the kit with Codex

Codex discovers skills from `.agents/skills/<name>/SKILL.md` in the repo (and from the
user-level equivalent). The kit's skills follow the open Agent Skills format, so they work
there unchanged. The agents are Claude Code subagent files; what carries over to Codex is
their bodies as instructions, not the delegation between them.

## Skills: copy the directories

```bash
git clone git@github.com:markoorn/overseer-kit.git
mkdir -p <your-repo>/.agents/skills
cp -r overseer-kit/skills/* <your-repo>/.agents/skills/
```

They are then `$setup`, `$ad-brief` and `$mockup` in Codex (or whatever your Codex version
uses to invoke a skill by name). `setup` writes `OVERSEER.md` the same way it does in
Claude Code; the only Claude-specific step inside it is the connector inventory command
(`claude mcp list`), which you can skip and answer by hand.

Keep the copies in sync with a one-line script rather than editing them in place, so an
update to the kit does not get lost:

```bash
rsync -a --delete overseer-kit/skills/ <your-repo>/.agents/skills/
```

## The overseer as instructions

Codex does not have Claude Code's subagent delegation, so the four-agent split cannot run
as four processes. What transfers is the discipline:

1. Put `OVERSEER.md` in your repo (run the setup skill or fill `templates/OVERSEER.md` by
   hand).
2. Add the overseer's working principles to your repo's `AGENTS.md`. The sections that
   carry over cleanly, and that Codex reads on every turn, are:
   - Hard constraints (worktree per task, never bare `git stash`, no push or PR without a
     yes, secrets never print)
   - Working principles (confidence and claims, verify assumptions, blockers and
     fallbacks, questions get answers, disagree when wrong, the after-a-mistake checklist,
     OIVV for "verify everything", test failures as design questions)
   - Verification protocol (what counts as verification and what does not)
   - Reading a report (how to check your own work before claiming it)

   Copy them from `agents/overseer.md`; they are plain prose with no Claude-specific
   tool names. Leave out "Session start", "Lifecycle", "Writing a brief" and "Skills and
   who runs them", which describe the delegation.
3. Use the verifier's procedure (`agents/verifier.md` § Procedure) as the checklist you
   run before declaring a change done: diff against the default branch, run the checks
   with counts, baseline on any skip, check tests were added, grep for stubs, check scope.
   Codex can run it as a second pass in a fresh thread, which gets most of the value of a
   separate verifier: a fresh context that has not seen the reasoning that produced the
   change.

## Hooks

`addons/hooks/` are Claude Code hooks and do not run in Codex. The worktree-per-task rule
stays policy there; put it in `AGENTS.md` and, if you want enforcement, a git pre-commit
hook that refuses commits from the primary checkout is the nearest equivalent.

## What you lose, honestly

The separation between the agent that built something and the agent that verified it. In
Claude Code the verifier is a fresh instance that never sees the builder's reasoning; in a
single Codex thread the same context does both, and it tends to check what it remembers
doing. A second Codex thread with only the claim and the worktree path is the workaround.
