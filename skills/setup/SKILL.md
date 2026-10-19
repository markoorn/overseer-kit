---
name: setup
description: First-run walkthrough for the overseer kit. Writes OVERSEER.md at the repo root (repo layout, commands, optional connectors, compatibility rules, reviewers, known traps, house style) and, if ad-brief will be used, the brand documents it needs. Run once per repo, and again whenever something changes. Use when the overseer says OVERSEER.md is missing, when adopting the kit in a new repo, or when asked to set up, configure or re-configure the overseer.
disable-model-invocation: true
---

You are setting the overseer kit up for this repo and this machine. The output is one
file, `OVERSEER.md` at the repo root, written from the kit's template, plus the brand
documents if ad-brief will be used. Nothing the agents later rely on may be guessed; what
you cannot detect you ask, and what the human does not know you leave marked as not
configured.

This is a walkthrough, not a questionnaire. Detect first, then take the human through
one section at a time with the interactive question tool, where what you detected is the
recommended option and they can accept it with one keypress. Never put more than one
section's questions in front of them at once, and never dump the whole interview as a
numbered list in a text message. Write each section into the file as soon as it is
answered, so progress survives if the session ends early.

## 1. Locate the template and the repo

- The template is `templates/OVERSEER.md` in the kit. When the kit is loaded as a plugin,
  `${CLAUDE_PLUGIN_ROOT}` is its root; otherwise find it next to this skill
  (`../../templates/OVERSEER.md`). If the template is missing, say so and stop.
- REPO is `git rev-parse --show-toplevel`. If that fails, ask where the repo is. If REPO
  is a worktree (`git rev-parse --git-common-dir` differs from `.git`), the primary
  checkout is the parent of the common dir; `OVERSEER.md` normally belongs there, and the
  first question settles it.
- If `OVERSEER.md` already exists, read it and run the walkthrough as an update: each
  step shows the current value as the recommended option.

## 2. Detect before asking

Run these and keep the output for the questions. Say in one line that you are detecting;
do not narrate each command.

```
git -C "$REPO" remote -v | head -2
git -C "$REPO" symbolic-ref refs/remotes/origin/HEAD 2>/dev/null || git -C "$REPO" branch -r | head -5
git -C "$REPO" branch -a | sed 's#remotes/origin/##' | grep -oE '^(fix|feat|feature|chore|bug|hotfix|content)/' | sort | uniq -c | sort -rn | head
ls "$REPO"/AGENTS.md "$REPO"/CONTRIBUTING.md "$REPO"/CLAUDE.md "$REPO"/.claude/CLAUDE.md 2>/dev/null
ls "$REPO"/package.json "$REPO"/pnpm-workspace.yaml "$REPO"/bun.lock "$REPO"/bun.lockb "$REPO"/package-lock.json "$REPO"/yarn.lock "$REPO"/pyproject.toml "$REPO"/go.mod "$REPO"/Cargo.toml 2>/dev/null
```

From the lockfile, infer the package manager and the install command. From `package.json`
(root and each workspace), list the `typecheck`, `lint`, `test` and `build` scripts per
workspace: `find "$REPO" -maxdepth 3 -name package.json -not -path '*/node_modules/*'`
then read each one's `scripts`. For non-JS repos, read the obvious equivalents
(`Makefile`, `pyproject.toml` `[tool.*]`, `justfile`). Read the conventions file and any
existing agent files for rules already written down (branch naming, compatibility
invariants, reviewers, traps); detected rules become recommended options, never silent
defaults.

Take the connector inventory with exactly this command, never bare `claude mcp list`,
which prints connection strings with credentials:

```
claude mcp list 2>/dev/null | awk -F' - ' '/ - /{split($1,a,": "); print a[1] " - " $NF}'
```

Also run `gh auth status 2>&1 | head -3` (and `glab auth status` if `glab` exists).

Check for the kit's hooks: `grep -l 'worktrees' ~/.claude/settings.json "$REPO"/.claude/settings.json 2>/dev/null` and `grep -l 'block-env-secrets' ~/.claude/settings.json 2>/dev/null`.

## 3. The walkthrough

Open with one short message: the repo you detected, the one-line connector summary, and
that there are up to ten short steps, each answerable with one choice. Then offer the
fast path as the first interactive question:

> **How do you want to do this?** 1) Accept everything detected and only ask me about
> the gaps (Recommended when the detection looks right). 2) Walk through every section.

With the fast path, write every section whose value was detected, then ask only about
sections with no detected value (usually connectors you did not have, compatibility,
house style, hooks, marketing). With the full walk, do every step.

Each step is **one call to the interactive question tool** (`AskUserQuestion` in Claude
Code), with at most three questions in it, each with two to four options, the detected
value first and marked "(Recommended)", and the evidence for it in the question text
in one line ("73 feat/ and 17 fix/ branches; CLAUDE.md documents `fix/<TICKET>-<slug>`").
Keep option labels short; put the detail in the description. The human can always type
something else. If the session has no interactive question tool (another harness), ask
the same step as a short numbered list in text, one step per message, and wait.

After each answer, write that section of `OVERSEER.md` immediately and say in one line
what was written. Then the next step.

The steps, in order:

1. **Where the file goes.** Only when REPO is a worktree: primary checkout (Recommended,
   it is prose, the agents read it before any worktree exists, and the worktree guard
   allows it by name) or this worktree only.
2. **Repo and branches.** Default branch, branch naming with the prefix counts, the
   conventions file, the worktree root (propose the directory above the primary checkout
   plus `/.worktrees`, and say why in the description: worktrees must not sit inside the
   checkout).
3. **Commands.** Show the per-workspace table in the message before the question, then
   ask: confirm, or name what to change. Include the install command, build, codegen and
   the env files a fresh worktree needs (names only; never read their contents).
4. **Connectors.** One question per kind that was detected (tickets, code hosting, logs,
   errors, database), grouped three per call: the detected server as the recommended
   option, "none" as the second. For a kind with nothing detected, ask "none, or is there
   one under another name?". For tickets also ask the project key. Say once, in the first
   connector question's description, that each is optional and what the fallback is when
   it is "none" (paste the ticket; use the `gh` CLI; logs and numbers marked not
   checkable).
5. **Compatibility.** Shipped clients the API cannot break (if the conventions file says
   so, that is the recommended option; otherwise "none" is), and any other invariants
   already written down, offered as a list to accept or trim.
6. **Review and release.** Reviewers, merge policy, ticket automation that reacts to
   branch or PR names. Detected from the conventions file where possible.
7. **Known traps.** If existing agent files or docs already list traps, offer them as a
   list: all of them (Recommended), only the ones that are generic to any checkout of this
   repo, or none. Otherwise ask for anything that has already bitten, with the two the kit
   knows about as examples (install before hooks work in a fresh worktree; a task runner
   that silently skips tests).
8. **House style.** Describe the kit default in the question text in two lines (plain
   English, no em dashes, no time estimates, sizes as trivial to very-large, evidence
   before opinion, numbered questions, never "you're absolutely right"). Options: keep
   it (Recommended), keep it with changes, describe your own. For the last two, ask for
   each rule as a concrete example: one sentence that is right and one that is wrong,
   because adjectives like "friendlier" do not calibrate an agent and quoted sentences do.
9. **Hooks.** If both add-ons are already installed, say so and skip the question. Else
   offer each one with what it blocks; install only on a yes, per the add-on README.
10. **Marketing.** Will ad-brief be used here? If no, write the section as not configured
    and finish. If yes: brand directory (propose `<repo>/brand/` or a sibling marketing
    repo; if brand documents already exist, that path is the recommended option and the
    templates are not copied over them), the branch that reflects what is live, store ids
    or "not an app", generation account and spend rule (none, or a metered account with
    the credit figure above which a round needs an explicit yes). Then, if the brand
    documents are new, run the brand interview in step 5 below; if they exist, offer a
    quick check that they cover every section ad-brief reads, or skip.

## 4. Finish OVERSEER.md

Keep the template's headings exactly, because the agents grep for them. Replace every
`<...>` placeholder with the answer or with "not configured". Do not invent values. Close
with a short summary: the path, which sections are not configured, and offer to open the
file. Re-running the skill updates the file section by section rather than overwriting
it.

## 5. Brand documents (only when ad-brief will be used and they do not exist yet)

Copy the three templates from the kit's `templates/brand/` to the brand directory, then
fill them the same way: one section per interactive question, with what you can detect
(from existing creatives, a brand guide in the repo, the store listing) as the recommended
option. Each template says which sections ad-brief reads and why; do not skip a section
because it is hard, mark it "not yet decided" so ad-brief can flag it.

- `brand-visual.md`: colours with hex values and the ratio they are used in, typefaces for
  headlines and body, logo files and the ways the logo must never be rendered, photography
  direction, the ad layout system (where the headline, the product and the footer sit),
  frame sizes per placement.
- `brand-voice.md`: the registers (an in-image headline register and a caption register,
  if they differ), three to five real example headlines that are on-voice, three that are
  off-voice, standing hashtags, words and claims that are banned, what self-deprecation is
  allowed to target.
- `creative-playbook.md`: the concept-development method, the brief template, and the
  lessons. Seed its lessons section by copying the kit's `docs/generation-lessons.md` in
  whole (under the template's "Lessons" heading), so the brand starts with every
  production lesson the kit has rather than an empty list; it fills with the brand's own
  from there.

Also create the campaign records directory from `templates/campaigns/README.md` if it does
not exist, and record its path in `OVERSEER.md` § Marketing.

## 6. Close

Say what was written, where, and which sections are "not configured". Then tell the human
how to start the overseer (the kit README has the exact command for their install path).
