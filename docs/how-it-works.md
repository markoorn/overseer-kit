# How it works

## The shape

One overseer, three kinds of worker, one worktree per initiative, and a rule that nothing
is "done", only "verified" or "unverified" with the evidence named.

```
you ──► overseer ──► investigator (read-only: code, git, tickets, logs, web)
              │
              ├────► builder      (edits in a worktree, with tests; reports real output)
              │
              └────► verifier     (fresh instance, never the builder; re-runs everything;
                                   PASS / FAIL / UNVERIFIABLE with counts)
```

The overseer's tools are deliberately few: it can read, grep, run git plumbing, publish an
artifact, ask you questions, and edit prose it can check in a diff. It has no ticket, logs
or database tools of its own. Everything that touches the real system goes through a
worker, so the overseer's context stays small and its reports stay about evidence rather
than about what it did.

## A run, stage by stage

**Session start.** The overseer resolves the repo, reads `OVERSEER.md`, lists worktrees,
takes a connector inventory (which of tickets, code hosting, logs, errors, database are
connected on this machine, by whatever server name they carry), and asks what the
initiative is. Anything not connected has a standing fallback: paste the ticket, use `gh`,
mark logs and numbers as not checkable.

**Three lanes.** The process scales to the work, and the overseer says which lane it chose:

- *Direct*: a small, named change (a doc line, a wording fix, a commit). The overseer does
  prose and git itself, or sends one builder for code, then reads the diff. No plan, no
  verifier.
- *Standard*: a bug fix or contained feature, through the stages below.
- *Investigation*: a question, review or research. Investigators only.

Every worker costs usage, so the overseer spawns one only when it buys something it cannot
get more cheaply itself.

**1. Intake.** Restates the ask in two sentences, classifies it, sizes it, lists unknowns,
gets the ticket read (by an investigator, or by you pasting it). Asks if the ask has more
than one reading.

**2. Frame.** Turns each unknown it cannot close with one quick look into a narrow question
for an investigator. Several run in parallel; they are read-only. Every brief is
pre-flighted: paths checked with `ls`, branch freshness checked with a fetch. An
investigator that hits a missing input replies `ERROR:` and stops rather than improvising.

**3. Plan.** Steps, which worker does each, the worktree slug and branch name, what
"verified" will concretely mean, whether commits follow each passing check, and what the
overseer will ask you before doing. This is a hard stop: nothing is created until you say
go.

**4. Execute.** The overseer creates the worktree itself (git plumbing). The first builder's
first act is the install command from `OVERSEER.md`. Builders run one at a time per
worktree. Verification is proportional: for a behaviour change, a fresh verifier gets the
claim and the scope only, never the builder's reasoning, so it cannot inherit the builder's
blind spots; one verifier covers a coherent piece of work before its commit. Prose edits
and "the file exists" are checked by the overseer reading them. The overseer commits after
the check passes. Two verifier failures on the same piece stop the run and bring both
reports to you.

**5. Hand back.** Two lines you can read cold ("What this was", "What changed this
round"), the worktree and branch, the commits, what was verified with the evidence, what
was not and why, open questions, out-of-scope flags, and "Worth remembering": operational
facts the run surfaced, each proposed as a line for `OVERSEER.md` § Known traps.

The overseer never pushes, opens a PR, merges or spends without an explicit yes for that
specific action. "Looks good" is not a yes. A yes for one push is not a yes for the next.

## Why these rules

- **Worktree per task.** Two sessions editing one checkout clobber each other's
  uncommitted changes silently. A worktree per initiative removes the possibility rather
  than hoping. The optional hook enforces it.
- **The verifier never sees the builder's reasoning.** A verifier that reads "I tested X
  and it passed" tends to check X and nothing else. Given only the claim, it has to work
  out what would falsify it.
- **Counts, not colours.** Task runners have made whole suites skip while reporting green.
  Verifiers report passed, skipped and failed, and any skip or a suspiciously low count
  triggers a baseline run on the default branch.
- **Briefs carry exact commands.** Workers follow multi-step prose selectively. A command
  whose output you asked to see cannot be skipped invisibly.
- **"Not found" has levels.** Not found locally (stale checkout?), searching the remote,
  found on the remote but not locally, not found anywhere. Only the last one means absent.
- **Questions get answers, not implementations.** "Why did this fail?" is answered, then
  the overseer asks whether you want it fixed.
- **Connectors are optional and named per machine.** The investigator inherits whatever
  MCP servers your session has rather than listing server names in its tools fence, because
  the names differ between machines and a fence by name silently has no Jira on a machine
  where Jira is `claude.ai Atlassian Rovo`.
- **Secrets never print.** Not even masked. A mask that fails silently leaks the value. The
  connector inventory is a filtered `claude mcp list` for the same reason: the bare command
  prints connection strings.

## The skills

- **setup** is an interview the overseer runs with you, not a worker task. It writes
  `OVERSEER.md` and, if you will use ad-brief, the brand documents from templates.
- **mockup** is coordinated: builders capture and draw, investigators gather evidence, the
  overseer publishes one private artifact with a "Start here" page, you pick, then the
  build goes through the normal stages.
- **ad-brief** is an investigator task for the grounding and the concept writing, reviewed
  by the overseer against the voice check, with every generation or spend a checkpoint. It
  produces a brief and, after a pick, a campaign directory. It never generates imagery.

## What is yours and what is the kit's

Yours: `OVERSEER.md`, the brand documents, the campaign records, any hook you installed.
The kit's: the agent files and the skills. Updates to the kit never touch yours.
