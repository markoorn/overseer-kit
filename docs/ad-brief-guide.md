# ad-brief: getting started

`ad-brief` turns "we need an ad for X" into three or four concepts a human can choose
between, each with real copy, a named format, the assets it needs, and the evidence it
rests on. It never generates imagery and never spends. The point of the gate is that
briefs are free and disposable and generation is not, so a person picks before money
moves.

This page is the orientation: what to ask it for, what it needs from you to be any good,
and why the production side of the kit assumes a particular generation platform.

## What to ask it for

Each of these is a different job, and the skill treats them differently.

**A feature launch.** "Brief an ad for the new matchplay scoring." The skill first checks
the feature is actually live on the production branch and in the store release notes,
then reads the real screens and harvests any user-facing copy that already ships (the
best line in one round was already live in an upsell card). If the feature is not in
production it stops and offers a coming-soon teaser instead. Expect concepts that name a
screen and a state for every screenshot they need.

**A campaign slot.** "Brief slot 3 of the relaunch campaign." The campaign record already
settles the slot's job, channel, audience and any prize, so the skill briefs to that job.
A "show what followers get" slot is not a feature launch; a prize post is not the whole
proposition. Prize claims come only from the record's prize section, never from memory.

**An evergreen benefit.** "Something about never losing a scorecard again." No launch to
verify, but every product claim still gets checked in code, and the voice check works
harder, because evergreen copy is where generic SaaS lines creep in.

**A milestone or social proof.** "We just passed 20,000 users." The store rating and
review count are usable copy; the skill reads them live rather than from memory. The
number goes somewhere it reads as a product-wide claim, not attached to one feature where
it may be false.

**A community or winner post.** "Announce this month's giveaway winner." No product claim
to verify; the skill skips the shipping check but still runs the premise check on the
copy and the reason-to-follow test (why does someone keep following after the incentive
ends?).

**A B2B angle.** "An ad aimed at club managers rather than players." Different audience,
different register, different evidence; the brand voice doc should list the audiences so
the skill does not write the player ad with a club manager's nouns swapped in.

**Open-ended.** "We need some ads." It does a light pass of what shipped recently and
opens loose ("anything in mind? otherwise matchplay just shipped") rather than handing
you a form.

What it will not do: write a launch ad for unshipped work, infer how many or how often
something happens from the code (code proves a mechanism exists, not its scale), invent
hashtags, or generate a single image.

## What it needs from you, and why

The skill reads three brand documents and one set of campaign records. The setup skill
creates them from templates. Here is what each section is for, so you know which ones are
worth real effort.

### brand-visual.md

- **Colours with hex and ratio.** Image models and site CSS both produce near-miss
  colours; one brand had four almost-identical reds in circulation and the site's own
  token layer conflated two of them. The ad uses the one hex, every time.
- **Typefaces.** Headlines are set in the real typeface in a compositing step, never
  rendered as pixels by a model. The skill needs to know what the typeface is to say so
  per concept.
- **Logo files and the prohibitions.** Every "never" in a logo guide (re-drawn, outlined,
  recoloured, rotated, locked up with other words) is a standard image-model failure. The
  logo is composited from the file or it does not appear.
- **The ad layout system.** Where the headline band, the product and the footer sit, and
  the frame sizes per placement. This is the composition vocabulary; without it concepts
  describe pictures instead of layouts. Reverse-engineer it from the creatives that have
  actually run.
- **Device frames.** A bare screenshot reads as a pasted image; the same capture in a
  phone reads as somebody's phone.

### brand-voice.md

- **Audiences.** Two or three groups that want genuinely different ads. The skill asks
  which one each brief is for.
- **The two registers.** Most brands run a punchy in-image register and a looser caption
  register in the same post. Collapsing them is the commonest reason a draft reads flat:
  a caption written in the headline register is just a second headline.
- **Real on-voice headlines.** Three to five lines that have run. These are the benchmark
  the voice check compares every draft against. Adjectives ("cheeky", "confident") do not
  calibrate a model; quoted lines do.
- **Off-voice lines with the reason.** Each rejection stops the same mistake being
  re-drafted.
- **Rules with teeth.** Self-deprecation targets the brand, never the audience. Never
  "in the app" as filler. Local specificity if it is a pillar. Banned claims. Numbers only
  when checked.
- **Standing hashtags.** The ones every post starts from, so a publisher has a placement
  choice (caption or first comment) and the account does not split across three spellings
  of the same tag.
- **Running bits.** Recurring characters and phrases the audience recognises, with the
  rule for each.

### creative-playbook.md

The method and the lessons. It starts with the kit's `docs/generation-lessons.md` as its
lessons section and fills over time. The method part the skill relies on: benefit first,
humour earns its place; artwork and caption have different jobs; present the whole post
as a rough before the rationale; aim at the joy of the feature, not its machinery.

### Campaign records

Three records the skill reads before proposing anything, so it never re-proposes a
rejected idea or duplicates what is queued: the idea pile with every rejection and its
reason, the content versions with exact approved copy, and the publications with where
and when anything ran. `templates/campaigns/README.md` has the layout. The rejections are
the most valuable part.

### What happens with thin inputs

The skill flags what is missing rather than guessing. With no on-voice examples, expect
competent generic copy and a note saying so. With no layout system, expect concepts that
describe photographs. With no rejections on file, expect it to re-propose things you have
already turned down. Fill the voice doc first; it moves the output most.

## Why Higgsfield

The brief itself is platform-neutral. The production guidance in the skill (the Hybrid
Reel section and the generation order) and most of `docs/generation-lessons.md` were
learned on Higgsfield, for reasons that are practical rather than loyal:

- **One metered account covers the whole pipeline**: image stills, video, text-to-speech,
  voice cloning, video-to-video edits. Casting stills, plates, clips and a cap added to a
  winning take all come from one ledger, which is what makes spend reconciliation
  possible.
- **It has an MCP server**, so an agent can drive it from a coding session: generate,
  poll, download, and reference a prior job by id instead of re-uploading. Most of the
  lessons about references and continuity depend on that.
- **Cost preflight without creating a job.** The spend discipline in the lessons (quote
  the exact call, read the exact credit figure, reconcile against the transaction ledger)
  is only possible because the platform exposes those.
- **Multiple models behind one API.** The single most useful finding in the lessons,
  "compare models before spending rounds on one", needs several models reachable with the
  same prompt and the same references.

What it is not: an endorsement that it produces the best people or the best motion.
Those are dated observations; the lessons say so and say to re-check each campaign. If
you use a different platform, keep the shape of the discipline (one ledger, preflight,
references by id, bounded comparisons) and record what your platform does and does not
expose. The setup skill asks which account you use and what your spend rule is; "none,
briefs only" is a valid answer, and the skill then stops at the brief.

## A worked path, start to finish

1. Run `/overseer-kit:setup`, say yes to marketing, fill the voice doc properly.
2. `/overseer-kit:ad-brief` for the feature. Read the four concepts. Pick one, or send it
   back with what is off.
3. The skill scaffolds the campaign directory and records; nothing is generated.
4. Approve a credit figure for the stills round. Cast stills, plates, spares. Compare
   faces. Pick.
5. Approve a figure for the video round. One beat per clip. Review at 0.25 s.
6. Composite: real screens in a phone, logo from the file, headline in the real
   typeface, end card.
7. Export with sound on and off, listening review by a person, AI label if there are
   generated people or video, reconcile spend against the ledger, write the record.

Everything in steps 4 to 7 has a lesson behind it in `docs/generation-lessons.md`.
