---
name: mockup
description: Mock it up before building it, on one shared Claude artifact. Two modes. Rework an existing screen - capture it as it is today with real app code and invented data, list what's wrong with file:line evidence, draw the current state plus three options (small to large), recommend one. Something new (a portal, a section, a landing page) - a short brief, a map of what the code already supports, two or three structure directions, then a full clickable mock-up of the chosen one for team review. Either way the user picks, then it's built on a branch, captured, and optionally recorded on a ticket with screenshots (only after asking). Use when someone says a UI is bad, asks for options or alternatives for a screen, flow or dialog, wants a new page, portal or feature mocked up, or wants something to share with the team before it's built. Not for a design-system pass or a one-line copy tweak.
---

# Mockup: show it before you build it

Every one of these conversations needs the same things: the truth about what exists today
(in code, not by impression), a small set of concrete options with honest costs, and one
place where the team can see everything and pick.

The user picks. You recommend, but you never choose for them, and you never start building
before they've picked.

Read `OVERSEER.md` at the repo root first: it names the worktree root, the install and
check commands, whether a database connector exists (for real numbers), whether a ticket
connector exists (for the optional recording step), and the conventions file.

## Pick the mode

- **A · Rework an existing screen.** There's a screen, dialog or flow today and it's not
  good enough. Output: the current state plus three options on one canvas.
- **B · Something new.** Nothing exists yet: a new portal, a new section, a new page.
  Output: structure directions first, then one full mock-up of the chosen direction.

If it's a mix (a new section inside an existing app), use B, and treat the existing screens
around it as the "what exists" ground truth in B2.

---

## Mode A · Rework an existing screen

### A1. Capture the current state for real

Use whatever real-screenshot route the repo has: a capture harness with typed fixtures, a
Playwright script against a dev server, a simulator. If the repo has a capture skill, read
and follow it. Never describe the current screen from memory, never draw it, and never use
a production screenshot with real people in it.

- **Typed fixtures with invented data.** Reuse an existing fixture set where one fits;
  otherwise add fixtures for the data the screen needs. Make the data show the problem: if
  ties are the bug, put two entries on the same score; if the empty state is the bug,
  capture it empty too.
- **Capture the awkward states**, not just the happy one: the dropdown open, nothing
  selected, empty, the result after a choice.
- **Fixtures may not be on the default branch.** Check whether the data you need lives on
  an unmerged branch (`git branch -a`, recent tags). If it does, make your own worktree
  from that branch rather than editing another task's worktree.
- **Open every image you capture** before using it.

### A2. List what's wrong, with evidence

For each problem, name what the code actually does and where: `path:line`. "It feels
confusing" is not a finding; "every press re-randomises because nothing is saved
(`route.ts:76-79`)" is.

- Read the component, its query and anything it calls (domain functions, API routes).
  Problems often hide one layer down: a screen can look like a UI problem while its
  ranking is backwards because of how a lower layer reports a result.
- Separate what you confirmed from what you inferred.
- If a number would help (how often each option is used, how many accounts hit a case),
  get it from the database when a connector exists rather than guessing. With none, mark
  the number "needs the database" and leave it empty.

### A3. Current state plus three options

Three options, ordered small → large. For each:

- **What it is**, in one paragraph a non-engineer can follow.
- **Size**: trivial / small / medium / large / very large. Never a time estimate.
- **What it needs**: screen only, or an API / schema / migration change. This is usually
  what decides the pick.
- **The honest limit**: e.g. "remembered in this browser only", "assumes everyone opted
  in".

Then **one recommendation and why**. A common shape: ship the small one now, plan the
medium one, keep the large one for later.

Canvas layout: a top row with the current-state screenshots (uploaded as assets, one
artboard each) and a red sticky listing the problems; a second row with the three option
artboards, each with a blue sticky underneath (name, size, needs, limit).

---

## Mode B · Something new

### B1. A short brief

Before drawing anything, ask a handful of questions and write the answers down (they go on
the canvas as a sticky):

- **Who uses it**, and what role they have.
- **Their top three to five jobs**: what they come to it to do.
- **What must be in the first version**, and what's explicitly later.
- **Where it lives**: a new app, a section of an existing app, a public page.

A mock-up without this comes out generic. If the user can't answer something, note it as
an open question rather than inventing an answer.

### B2. Ground it in what exists

This replaces "capture the current state". Three parts:

1. **A capability map.** For each job from B1, what the API and schema already support,
   checked in code with `path:line` (queries, mutations, models, permissions). Mark each
   planned screen **exists**, **needs API** or **needs schema**. This is the same
   discipline as A2's evidence, and it turns the mock-up into tickets later.
2. **The product's look.** Find the nearest existing screens and components (layouts,
   tables, forms) and capture one or two as reference, so the new thing looks like the
   product and not a template.
3. **Realistic data.** Real shapes and sizes from the database when one is connected: how
   many members a typical account has, how many records a month, how long names get.
   Invented names, real proportions.

### B3. Structure first, cheaply

Two or three structure directions as rough sketches on one canvas page: navigation and
layout, not finished screens (a sidebar with sections vs a dashboard-first home vs a single
page with tabs). Each gets a sticky: what it's good at, what it's bad at, size. Recommend
one. The user picks before anything is drawn in detail.

### B4. The full mock-up of the chosen direction

One clickable mock-up of every main page, in the product's look, with consistent invented
data.

- **On a Design canvas**: one artboard per page, joined with links
  (`<a href="Members.dc.html">`) so people can click through it, and
  `"is_interactive": true` on artboards whose controls work. Group areas onto canvas
  pages.
- **Mark what each page needs**: a small exists / needs API / needs schema note per
  artboard (a sticky beside it, not inside the design).
- **A single page** (a landing page) can be one HTML artifact instead of a canvas.
- **Open questions** from B1 go on a sticky, not into the design as guesses.

### B5. Team review

The user shares it; people comment on the artifact. Each round of feedback becomes a new
version at the same link, not a new artifact. Keep a short "changes in this version"
sticky.

---

## Rules for every mock-up

- **Only what exists, or what the option / the new build would add.** Don't show a feature
  that isn't built and isn't part of the proposal. Label anything new as new.
- **Invented numbers are labelled "illustrative"** on the board itself.
- **Keep data consistent across boards.** The same people, scores, members and dates
  everywhere. A board that says "6 players, 12 twos" next to one showing five players and
  six 2s undermines the whole page.
- **No real customer or person names.** Invented names; a real place name only if the
  user has cleared it.
- **Look like the product**: its type, colours, spacing and real components.
- **Accessible as drawn**: real `<button>`, `<label>`, `<a href>` and `<table>` markup,
  text contrast at 4.5:1, touch targets 44px or more.
- **Rationale goes in stickies and your reply**, never inside an artboard.

## One shared artifact

Everything goes on one Claude artifact so the team sees it in one place. If the session
has an Artifact tool with a **Design** canvas type, use it; otherwise publish a single HTML
page; with no artifact tool at all, write the HTML locally and tell the user where it is.

- **One canvas page per screen or area** (`pages` in the index, `page` on each board and
  note), and page 1 is a "Start here" artboard rather than stickies: brief, decisions made
  (D1...), decisions needed (N1...), open questions (Q1...), status legend, a numbered page
  index saying what to review on each page, changes in this version, corrections (C1...).
  Every other page is numbered ("3 Overview") and has exactly one sticky, to the right of
  its first board at the top, with four headings: STATUS, EVIDENCE (path:line), MISSING
  (numbered), REVIEW (R1...). Options under comparison get one sticky under each option
  board; rejected options move to the directions page with a "rejected" sticky. Boards
  placed thousands of pixels below the first ones are easy to miss, and stickies scattered
  under boards of different heights read as noise.
- **The artifact starts private.** Tell the user others can't open it until they share it.
  Don't share or post it yourself.
- **If you delegate** (one subagent per screen or area): give each its own worktree, have
  it write artboard files with a placeholder for screenshot URLs (e.g.
  `src="SCREENSHOT:<file>.png"`), and publish them yourself, so two agents never write the
  canvas index at once. Read every file a subagent wrote before you publish it.
- If the canvas changed since you last read its index (the page saves too), re-read it
  and merge before publishing.

## Wait for the pick, then build

Present it: the findings in a few lines, each option or direction with size and needs,
your recommendation. Then stop and let the user choose.

Once they pick:

1. **Break it into pieces** (mode B especially): one piece per screen or capability, in an
   order that ships something usable early. "Needs schema" pieces usually go first.
2. **Branch**: build on the feature's branch if one exists (a single long-lived branch is
   common for a group of related pieces); otherwise a new one per the profile's naming.
   One worktree per task.
3. **Build and test** each piece. Tests for every changed function and component.
4. **Capture the built result** the same way as A1, so it can be compared with the
   mock-up (or, in mode A, with the before). If you borrowed another branch's fixtures to
   capture, put that branch back exactly as you found it (unique backup names, or
   `git stash push -m` with a unique tag; never two backups with the same basename).
   Reach every captured state the way a user would, by **real clicks** from the screen
   before it, at least once. A state opened straight from a deep link proves the page
   renders, not that you can get to it: side tabs that put state in the URL have looked
   fine opened by link, passed a unit test that mocked the router, and done nothing when
   clicked.
5. **Show the user the screenshots** before any PR. No PR until they've reviewed the
   result. Commit and push only when asked.
6. **When the PR is opened**, its description carries the final output as proof: final
   screenshots embedded (a table for several) and videos linked, referenced by commit SHA,
   invented data labelled, anything still off noted, and how it was tested. Final versions
   only, never superseded renders.

## Optional: record it on a ticket

Only if a ticket connector is available in this session **and** the user says yes. Ask
first, every time, e.g. "Want me to add this to the ticket with a screenshot?" Without a
connector, or if they decline, the record is the artifact plus the branch's commits, and
you say the ticket step was skipped.

If they say yes:

- **One ticket per refresh or build**, carrying a group of related pieces: add a bullet
  under a **Done** heading in its description for each piece as it's finished.
- **Attach a screenshot** of each built piece. Some ticket MCP servers run in a container
  and can't read local files; if attaching through the tool fails, say so and hand the
  upload to the user rather than printing credentials.
- **Options or pieces that aren't being built now but are worth keeping** can be logged as
  their own tickets, in whatever column the team uses for ideas. Ask before logging, and
  ask which column if you don't know. Attach each one's mock-up as an image (render the
  artboard at 2× with Playwright; swap any remote asset URLs for local files first).
- If ticket searches come back empty for things that obviously exist, the credentials have
  probably expired. Say so; don't conclude the issues don't exist.

## Checklist before you present

Mode A:

- [ ] Every current-state image is a real capture, opened and checked.
- [ ] Every problem has file:line evidence; confirmed vs inferred is marked.
- [ ] Three options, small → large, each with size, needs and limit; one recommendation.

Mode B:

- [ ] The brief is on the canvas, with open questions marked as questions.
- [ ] Every page is marked exists / needs API / needs schema, with file:line evidence for
      "exists".
- [ ] Structure directions came first and the user picked one before the full mock-up.
- [ ] The full mock-up clicks through.

Both:

- [ ] Data is consistent across boards; invented numbers are labelled.
- [ ] Nothing promises something that isn't built and isn't part of the proposal.
- [ ] One canvas page per screen or area, with a Start here page.
- [ ] The user knows the artifact is private until they share it.
