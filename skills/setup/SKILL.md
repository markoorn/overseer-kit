---
name: setup
description: First-run interview for the overseer kit. Writes OVERSEER.md at the repo root (repo layout, commands, optional connectors, compatibility rules, reviewers, known traps, house style) and, if ad-brief will be used, the brand documents it needs. Run once per repo, and again whenever something changes. Use when the overseer says OVERSEER.md is missing, when adopting the kit in a new repo, or when asked to set up, configure or re-configure the overseer.
disable-model-invocation: true
---

You are setting the overseer kit up for this repo and this machine. The output is one
file, `OVERSEER.md` at the repo root, written from the kit's template, plus the brand
documents if ad-brief will be used. Nothing the agents later rely on may be guessed; what
you cannot detect you ask, and what the human does not know you leave marked as not
configured.

Work in two passes: detect what you can from the repo, then ask about the rest. Keep the
interview short. Every question is a numbered list with numbered options, so the human can
answer by number, and each question carries what you found, so they can correct it rather
than restate it.

## 1. Locate the template and the repo

- The template is `templates/OVERSEER.md` in the kit. When the kit is loaded as a plugin,
  `${CLAUDE_PLUGIN_ROOT}` is its root; otherwise find it next to this skill
  (`../../templates/OVERSEER.md`). If the template is missing, say so and stop.
- REPO is `git rev-parse --show-toplevel`. If that fails, ask where the repo is.
- If `OVERSEER.md` already exists, read it and run the interview as an update: show each
  section's current value and ask only what the human wants changed.

## 2. Detect before asking

Run these and keep the output for the questions:

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
(`Makefile`, `pyproject.toml` `[tool.*]`, `justfile`).

Take the connector inventory with exactly this command, never bare `claude mcp list`,
which prints connection strings with credentials:

```
claude mcp list 2>/dev/null | awk -F' - ' '/ - /{split($1,a,": "); print a[1] " - " $NF}'
```

Also run `gh auth status 2>&1 | head -3` (and `glab auth status` if `glab` exists).

Check for the kit's hooks: `grep -l 'worktrees' ~/.claude/settings.json "$REPO"/.claude/settings.json 2>/dev/null` and `grep -l 'block-env-secrets' ~/.claude/settings.json 2>/dev/null`.

## 3. The interview

Ask these as numbered questions, in one or two rounds, each with what you detected as
option 1 where you detected something. Skip a question whose answer is already certain
from detection, but say what you took.

1. **Repo and branches.** Default branch, branch naming (show the prefixes you counted),
   conventions file. Worktree root: propose the directory above the primary checkout plus
   `/.worktrees`, and say why (worktrees must not sit inside the checkout).
2. **Commands.** Show the per-workspace table you built. Ask them to confirm, correct, or
   name anything a fresh worktree needs: build, codegen, env files to copy (paths only).
3. **Connectors.** Show the inventory. For each of tickets, code hosting, logs, errors,
   database: which server is it, or none. For tickets also the project key or the issue
   tracker's convention. Make clear every one is optional and what the fallback is when it
   is "none" (paste the ticket; use the `gh` CLI; logs and numbers marked not checkable).
4. **Compatibility.** Are there shipped clients the API cannot break (mobile apps in
   stores, third-party integrations)? If yes, the agents treat every API change as
   additive. Any other invariant a builder must never cross.
5. **Review and release.** Reviewers, merge policy, ticket automation that reacts to
   branch or PR names.
6. **Known traps.** Anything that has already bitten: a hook that fails in a fresh
   worktree until install runs, a flag that silently skips tests, a token scope gap. Offer
   the two the kit already knows about as examples; do not add them unless they apply.
7. **House style.** Explain the kit default in two lines (plain English, no em dashes, no
   time estimates, sizes as trivial to very-large, evidence before opinion, numbered
   questions, never "you're absolutely right"). Options: 1) keep the default; 2) keep it
   with a few changes; 3) describe your own. For 2 and 3, ask for each rule as a concrete
   example: one sentence that is right and one that is wrong, because adjectives like
   "friendlier" do not calibrate an agent and quoted sentences do.
8. **Hooks.** Offer the two optional add-ons under the kit's `addons/hooks/` (worktree
   guard, env-secrets guard) and say what each blocks. Install only on a yes, per the
   add-on README; never silently.
9. **Marketing.** Will ad-brief be used here? If no, leave the section empty and stop
   after writing. If yes:
   - Where do brand documents live (propose `<repo>/brand/` or a sibling marketing repo)?
   - Which branch reflects what is live (a `production` branch, or main)?
   - App Store id and Google Play package, or "not an app".
   - Generation account: none (briefs only), or Higgsfield (or another metered account)
     with the spend rule: the number of credits above which a round needs an explicit
     yes. Explain that the agents never spend without a figure and a yes.
   - Then run the brand interview in step 5.

## 4. Write OVERSEER.md

Fill the template with the answers. Keep the template's headings exactly, because the
agents grep for them. Replace every `<...>` placeholder with the answer or with "not
configured". Do not invent values. Show the human the finished file (open it with
`open <path>` if they want to read it) and ask for a yes before you consider setup done.

If the repo is one the human edits in worktrees, write `OVERSEER.md` in the primary
checkout anyway: it is prose, it is the one file the agents read before any worktree
exists, and the worktree guard add-on allows it by name.

## 5. Brand documents (only if ad-brief will be used)

Copy the three templates from the kit's `templates/brand/` to the brand directory, then
fill them by interview. Each template says which sections ad-brief reads and why; do not
skip a section because it is hard, mark it "not yet decided" so ad-brief can flag it.

- `brand-visual.md`: colours with hex values and the ratio they are used in, typefaces for
  headlines and body, logo files and the ways the logo must never be rendered, photography
  direction, the ad layout system (where the headline, the product and the footer sit),
  frame sizes per placement.
- `brand-voice.md`: the registers (an in-image headline register and a caption register,
  if they differ), three to five real example headlines that are on-voice, three that are
  off-voice, standing hashtags, words and claims that are banned, what self-deprecation is
  allowed to target.
- `creative-playbook.md`: the concept-development method, the brief template, lessons
  from real campaigns with the evidence for each. Starts nearly empty; it fills over time.

Also create the campaign records directory from `templates/campaigns/README.md` if it does
not exist, and record its path in `OVERSEER.md` § Marketing.

## 6. Close

Say what was written, where, and which sections are "not configured". Then tell the human
how to start the overseer (the kit README has the exact command for their install path)
and that re-running `/overseer-kit:setup` updates the file rather than overwriting it.
