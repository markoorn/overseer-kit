---
name: ad-brief
description: Turn a feature launch, a campaign slot or another angle into 3-4 grounded social ad concepts (Instagram or Facebook) with real headline, subhead and caption copy in the brand's voice, a named ad format, and the specific assets each one needs, verified against what actually shipped. Produces a brief only, generates no imagery and spends no credits, then scaffolds the campaign directory once a concept is picked. Use when someone asks for an ad, ad ideas, or creative for a feature or a campaign slot. Needs the brand documents and marketing paths from OVERSEER.md § Marketing.
---

You are writing an ad **brief**, not making an ad. Local rough layouts are part of
briefing; do not generate paid imagery or spend generation credits. That separation is the
whole point: briefs are free and disposable, generation costs real money on a metered
account, so a human reads the brief and picks before paid production begins. Don't skip
ahead to producing creative even if asked nicely; hand off per step 7 instead.

## 0. Locate the inputs and check what tools you actually have

Read `OVERSEER.md` § Marketing at the repo root. It names:

- the **brand directory** holding `brand-visual.md`, `brand-voice.md` and
  `creative-playbook.md`;
- the **campaign records** directory (the three records in step 4 live there);
- the **production branch**, the only true source for what is live;
- the **App Store id** and **Google Play package**, or "not an app";
- the **generation account** and its spend rule, or "none, briefs only".

If the section is empty or the brand documents do not exist, stop and say so: run
`/overseer-kit:setup` first. You cannot write on-brand copy without `brand-voice.md`, and
you cannot verify a launch without knowing which branch is production.

You need web access for the store check in step 2; plain `curl` via bash is enough for
Apple's unauthenticated lookup. If the product is not an app, the equivalent "what the
public was told" source is the changelog, release notes page or newsletter archive; ask
which if the profile does not say.

## 1. Scope it, but ground lightly first, then offer

**If the ad is for a campaign slot, read its campaign record first.** It already settles
most of what this step asks: the slot's job and CTA, the channel, the audience, the reason
to follow, and the prize if there is one. Brief to the slot's job. A "show what followers
get" slot is not a feature launch, and a prize post is not the campaign's only proposition.

If the ask already names the feature and audience, work with that.

If it's open-ended ("we need some ads"), don't interrogate the person with a form. Do a
light pass of step 2 first, then open loose with what's actually live and recently
shipped: _"Anything specific in mind? Otherwise <feature> just shipped and there's the
<milestone> going spare."_ That's the shape, not a script.

Four things you need settled before writing concepts, so ask for whatever's still missing:

- **The feature or angle**: a launch, an evergreen benefit, a seasonal push, a milestone,
  or a campaign slot's job.
- **The channel.** Facebook and Instagram are both first-class; don't default to one. A
  campaign slot names its channel.
- **Which audience.** Most products address two or three distinct audiences that want
  genuinely different ads (`brand-voice.md` lists them, or the store listing shows them).
  Name the one this ad is for.
- **Placement and aspect ratio, because the placement fixes the frame.** A feed cut is
  **1080×1350**; a story or reel is **1080×1920**. A feed shows 4:5 at the tallest and
  centre-crops anything taller, so a 9:16 still briefed for a feed loses its top and
  bottom bands, which is usually where the headline and the footer sit. **If the
  composition will not fit the frame, change the composition, never the frame.** Where an
  ad will run on a feed and as a story, brief both cuts as one content version: same copy,
  two renditions. Flag 1:1 as undetermined unless the brand has a worked example.
- **Static, video, or both.**

## 2. Verify what actually shipped; do not take the feature name at face value

The highest-value thing this skill does. An ad for a feature that isn't live yet is a
real, public mistake, so establish ground truth before writing a word of copy:

1. **Store release notes and listing**: what was actually announced to users, and when.
   For an iOS app:
   ```
   curl -s "https://itunes.apple.com/lookup?id=<APP_STORE_ID>&country=<cc>"
   ```
   Read `releaseNotes`, `version`, `currentVersionReleaseDate`, `description`,
   `averageUserRating`, `userRatingCount`. Ratings and counts are usable ad copy in their
   own right. For Android, read the Play listing page for the package.
2. **The production branch, not main.** `git log origin/<production>` is the only true
   source for what's live. Something merged to the default branch is **not** advertisable
   unless the profile says main is production.
3. **The ticket**, if a ticket connector exists: search for the ticket or epic, to
   understand intent and scope rather than just the diff. If none exists, ask for a paste.
4. **The real screens**: find the actual components so the concept describes what the
   feature looks like, not what you'd guess it looks like.
5. **Harvest the user-facing strings while you are in there.** Grep the feature's screens
   for copy that already ships: empty states, upsell cards, tooltips, prompt cards. In one
   real round, the best line in the whole exercise was already live in an upsell card and
   beat four concepts written from scratch. **If something in-product is funnier or
   sharper than your brief, that is the benchmark**; inherit its structure rather than
   writing a homage to it.

**This step is for product claims.** A campaign slot with no product claim (a
self-deprecating relaunch, a community question, a winner announcement) has no feature to
verify; skip to step 3, but verify any product claim it does make. **Prize claims are
verified against the campaign record's prize section**, not against memory or the
conversation: the exact prize, quantity, restrictions, entry method and closing time. If a
detail is not in that section, it does not go in the copy. Never say or imply that
following, tagging or sharing is required to enter unless the campaign's rules say so.

**Hard gate:** if the feature is not in production, stop and say so plainly. Offer to brief
it as a coming-soon teaser instead, but never write a launch ad for unshipped work.

## 3. Read both halves of the brand

- **`brand-visual.md`**: colours and their ratios, typefaces, the logo prohibitions,
  photography direction, and the ad layout system. Read the layout section properly; it's
  your composition vocabulary.
- **`creative-playbook.md`**: the canonical creative process and its evidence-labelled
  lessons. It owns the concept-development method, the brief template, and the production
  checks learned from real campaigns. **Do not restate its contents here**; reference it,
  so there is one place to update. For a **video** brief it carries the checks this skill
  does not duplicate (cast distinction at true phone size, the cast reference sheet,
  performance-and-edit rules, the export-with-sound-on-and-off check, and the rule that
  speech presence and intelligibility are listening-review findings an agent leaves
  pending rather than infers from waveforms).
- **`brand-voice.md`**: the registers. Most brands have a declarative, punchy in-image
  register and a looser caption register; don't collapse them.

Three constraints that shape every concept whatever the brand, so state them per concept
rather than leaving them implied:

- **The logo is composited from the real file, never generated.** Logo prohibitions are
  standard image-model failure modes.
- **Headlines are set in the real typeface**, not rendered as pixels by a model.
- **App UI, when a concept shows it, is a real screenshot.** Generated approximations of a
  product's own screens read as uncanny to exactly the users being targeted. Not every
  concept needs the app on screen. Real screens come from whatever capture route the repo
  has (a capture harness, Playwright, a simulator); name the screen and state and say who
  captures it.

Plus the brand's own: the exact brand hex values and any lookalike the UI tokens confuse
with them are in `brand-visual.md`; cite them per concept.

## 4. Check what's already been made

Read all three records before proposing. Don't re-propose a concept already built or
explicitly rejected; reference it and go somewhere new instead. The layout is in the kit's
`templates/campaigns/README.md`; the profile names where it lives.

| Source | What it answers |
| --- | --- |
| `campaigns/_ideas/` | the pile, and every rejection with its reason. **The rejections are the point**; they are what stops the same idea coming back in six months |
| `campaigns/<feature>/FEATURE.md` | product truth and copy guardrails for the feature, plus the running order, which says what that feature is meant to post next |
| `campaigns/<feature>/<ad>/POST.md` | what exact artefact is approved, with what exact copy |
| `campaigns/_published/` | where and when anything actually ran |

**These are three different records and the difference matters.** An idea marked `Built`
means approved creative exists; it says nothing about whether it was ever posted. Check
`_published/` before saying anything ran.

**Read the feature's running order before proposing anything.** A concept that duplicates
what is already queued is a worse use of the slot than one that does not.

If a source doesn't exist yet, don't create it here; that's the scaffolding step's job.

## 5. Write the concepts: fixed structure, every time

Three to four, not a long list. Before drafting, follow the playbook's method sections
(benefit first, humour earns its place; artwork and caption have different jobs; present
the whole post as a rough before the rationale). Include a straightforward benefit-led
route.

For static concepts, present concrete rough layouts first, with the intended social
caption in a clearly separated area beneath the artwork in the same review image. That
caption area is excluded from the published artwork export. Local sketches, cutouts and
typesetting are allowed during briefing; paid image generation stays in production. Do not
substitute descriptions of photographs for rough compositions. Keep the following
supporting fields after the previews.

Each concept records:

- **Headline**: the actual copy, not a description of it. In the headline typeface, in
  the in-image register, aim for six words or fewer; punctuation that serves the idea.
- **Subhead**: the actual copy. Body typeface, sentence case, one or two lines, ends in a
  full stop.
- **Caption**: the actual post caption, written **with** the image, not bolted on
  afterwards. It is a designed slot, not a fallback. Rules that each cost a rejected draft:
  - **It must link to the image.** A caption that would work beside any picture is not
    finished.
  - **Short beats.** "Ask Johan. He's two under." beats "He'll tell you he's having a
    good round."
  - **Do not explain away the joke**; a plain product descriptor in the artwork is welcome.
  - **Set a specific lie against the visible evidence**, so caption and image argue.
  - **A CTA question should presume guilt and use real speech**, and lead with your own
    absurd specific before asking.
- **Hashtags**: the actual tags, **written separately from the caption, never inside it**.
  Instagram takes them in the caption or the first comment, and that is a placement
  decision a publishing tool has to make. Start from the brand's standing hashtags
  (`brand-voice.md`), then add post-specific tags, broadest first, six to ten in total,
  grounded in what the account actually uses (`_published/` records), never invented.
  Tags that describe the joke rather than the category are usually dead weight.
- **Visual**: one sentence. Say explicitly which parts are generated photography and which
  are composited assets.
- **Format**: a named format, not a vague genre. For statics the ones that usually fit an
  app are `Then vs Now`, `App Screenshot`, `Bold Statement`, `Hero Statement`,
  `Comparison Table`, `Benefits Checklist`, `Star Review`, `Customer Quote`,
  `Social Proof`, `Stat Surround`. For video, most generation presets are physical-product
  shaped (unboxing, try-on) and useless for an app; the live options are
  `ugc-website-video` (real screenshots as overlay cards, the strongest fit),
  `Direct-to-Camera`, `Selfie Testimonial`, `Before and After`, `Tutorial`, `TV Spot`,
  `Wild Card`. **For a feature Reel, propose the Hybrid Reel first** (see the section
  below): it is the one video shape that has worked end to end, and it needs no preset.
- **Assets needed**: name the specific screenshot by **screen and state**
  (`round-summary` / `three-players-tied`, not "the summary screen") and any device frame
  or mockup file from the brand directory. Capturing is free and local, so a rough may use
  a real capture during briefing; say who captures it if the current session cannot.
- **Grounding**: the real commit, ticket, release note, review count, brand doc or
  campaign record this is based on. A concept that can't point at something real isn't
  ready to include.
- **Reason to follow** (campaign slots): why someone who saw this keeps following after
  any incentive ends. A concept that only works while a prize is on offer isn't finished.
- **Publication route**: feed stills and Reels can publish automatically through a
  publishing tool if the records carry what it needs (a 9:16 H.264 or HEVC file, AAC at
  48 kHz or lower, 3 to 90 s for Facebook, a chosen cover frame, an explicit AI label).
  Story stills are usually posted by hand so they can carry music and link stickers.
  Video stories and carousels are published by hand. Say who does it, so nobody discovers
  that at launch.
- **Confidence**: how solid the grounding is, and say it honestly.
- **Why it might not work**: one line. Every concept has a weakness; naming it is what
  makes the set decidable rather than four things that all sound good.

## 6. Voice-check the copy before showing it

The failure mode here isn't being wrong, it's being bland. Read every headline against the
real on-voice examples in `brand-voice.md` and cut anything that could belong to any
product in the category.

- **Self-deprecation targets the brand, never the audience.**
- **One round's register is an example, not the house style.** An accusatory CTA that
  suited one feature does not make every caption an accusation; a straightforward
  benefit-led or community caption is often right.
- **On Facebook, the caption can carry a real link.** Instagram's `link in bio` becomes a
  URL (with the campaign's UTM, if it has one).
- **Insider specifics are the point**, not a risk to manage. Generic SaaS benefit copy
  with category nouns dropped in is the thing to avoid.
- **Local specificity lands** when it is a stated brand pillar: currency, slang, place
  names. Check `brand-voice.md` for which.
- **Never tell people the product is an app.** "In the app", "with the app" as filler:
  they know. Name the thing itself. **How many, how often and through which channel are
  operational facts; ask, don't infer them from a resolver.** Code proves a mechanism
  exists, not its scale.
- **Cut AI cadence.** No self-narrating hedges, no "in today's fast-paced world", no
  three-clause em-dash sentences, no "Every X has a Y" aphorisms, no jargon triplets.
- **The two registers resolve per slot, not per ad.** In-image headline and subhead take
  the in-image register; the caption takes the caption register. Writing the caption in
  the headline register turns it into a second headline, which is exactly why flat drafts
  read flat.
- **Aim at the joy of the feature, not its machinery.** State what the joy of the feature
  actually is before concepting, then check the concepts point at it. Concepts built on
  "the app remembers what you did" lose to concepts built on "permission to be petty".
- **Verify anything the audience would enjoy correcting.** Avoid a number you have not
  checked; conversely, check a fact that would strengthen a line.
- **Read each line against its neighbours, not just on its own.** A count must say what it
  counts ("14 posts", not "14 more"); every number in the caption must match the number in
  the artwork, and a number that moves with time is re-checked on the day of approval; a
  subhead's pronouns must agree with the headline's; a time reference must hold for the
  date the post actually lands.
- Judge the complete artwork, not the headline in isolation. It must convey the feature
  and benefit without requiring the caption.

## 7. Hand off: offer, don't generate

Close by stating plainly that nothing has been generated and nothing has been spent, then
offer the choice: which concept (or concepts) to take into production, or another pass at
the brief. Note the current credit state if you know it. If the profile says "none, briefs
only", say that production happens outside this session.

Never start generating imagery off your own judgment because a concept seems obviously
best. The gate between free briefing and paid generation is deliberate.

## 8. When a concept is greenlit, scaffold the campaign before generating

Only once someone picks a concept; this step never runs off your own judgment.

Create the campaign directory in the campaign records location, in the **main checkout,
not a worktree**. Scripts and records can be authored in a worktree; the campaign's media
cannot live in one, because a worktree is disposable and `git worktree remove` takes
gitignored files with it that no remote can restore.

**Pick the bucket first.** Most ads are bucketed by the product capability they promote,
and a new feature ad almost always belongs to one that already exists. Only create a new
feature when nothing fits, and give it a `FEATURE.md` when you do. A campaign slot goes in
its campaign's directory beside the campaign record.

```
campaigns/<feature>/FEATURE.md      exists already, or you create it
campaigns/<feature>/<ad>/
  archive/              every generated asset, render, build artefact (gitignored)
  BRIEF.md              the brief this skill just produced
  POST.md               the content version record, see templates/campaigns/README.md
  logs/generation-log.md
```

**`<ad>` is the hook, and the hook alone.** The feature is already the directory above it.
Never name an ad for its mechanism; name it for what a reader would recognise.

**A second format of the same hook is not a new ad.** A static and a reel of one idea live
in the same directory as `POST.md` and `POST--<variant>.md`, each with its own content
version id. Different hooks get different directories.

**Also update the records, in the same pass.** Scaffolding a directory and leaving the
pile saying `Exploring` is how the three records drift apart.

1. **The idea**: in its `_ideas/` entry, set the status to in production, the campaign
   path and the date. If the concept did not come from the pile, add an entry.
2. **The content version**: allocate `CV-<feature>-<ad>-01` and write `POST.md` opening
   with the record block from the campaigns README. It starts as `Draft`. A `CV-` id is
   allocated once and never changes, even if the directory is later renamed.
3. **The feature's running order**: add the new ad to `FEATURE.md`, in the position it
   should actually run and with one line saying why.

`Approved` requires an approver, a date, a fingerprint and the exact copy. Missing any one
and it stays `Draft`, however finished the artwork looks. Never set `Approved` off your own
judgment; a human approves.

**The caption and the hashtags each go in a fenced block** under their own headings, so a
publishing tool can read them verbatim. Plain paragraphs under those headings read as no
caption at all.

Fingerprint stills by **pixels**, not file bytes: `magick <asset> -depth 8 RGBA:- | shasum -a 256`.
Image tools stamp a creation date into every PNG, so a rebuild of an identical image has
different file bytes every time. Video is not reproducible; record `Reproducible: no` and
keep the file hash as a tamper check only.

Getting the directory right up front matters more than it sounds: doing it afterwards on
one real campaign took an afternoon, moved gigabytes twice, and at one point had the
entire campaign invisible on the default branch because its branch was never merged.

## The Hybrid Reel: the proven video format

The one video shape that has worked end to end for an app feature. Four parts, about
20 to 25 s:

1. **Hook cutaway (generated, about 2 s).** One moment that sets up the story's premise.
   It plays under the first title.
2. **Phone segment (real).** Real screen captures in a phone that floats over a generated
   background plate. The phone rises in tilted, pushes in slowly and swings at every cut,
   so the cuts work as transitions on their own; scrolls stay as scrolls. One plain-sentence
   title per beat sits in the band above the phone. Every core-feature screen stays in;
   cutaways are added around the screens and never replace a feature beat. A short
   synthesised transition sound on the rise-in and each cut (but not on the hand-off into
   the punchline) reads better than a stock whoosh; under music, keep music around
   -22 LUFS, effects +6 dB with a sidechain duck, and check the effect still reads in its
   own band. Offer the cut with and without the sound.
3. **Punchline cutaway (generated, about 3 s).** It replaces a screen that would only
   repeat, and plays its title as the payoff. **Underplay it.** Give the model the
   situation and let the face stay flat; directed gloats read as overdone. When fixing a
   defect in a take the human liked, recreate that still with the fix as the first image
   reference and re-roll its original prompt; don't reinterpret the take.
4. **End card.** A solid field, logo centred, one headline line in the brand colour, a
   rule, then the subhead. Avoid busy diagonal treatments.

The compositing (floating phone, end card, transition sound) is a small set of scripts the
brand builds once and reuses; the kit does not ship them. Describe the required output in
the brief and let production own the tooling.

**Generation, in order.** Each round needs an approved credit figure; the profile's spend
rule applies. The Higgsfield-specific notes below are what has worked there; another
metered account needs its own preflight.

1. **Stills round.** 6 to 8 image stills at 9:16: the hook's start frame, the punchline's
   start frame, two or three background plates (dark, low-detail, no people), plus spares.
   Spares are cheap.
2. **Cast continuity: one face per character, across every clip.** Generate the first cast
   still, then pass its job id as an image reference to every later still that features the
   same people. In the prompt, describe each person by clothing and say "the same N people,
   identical faces and clothing". Compare faces side by side with a frame from the first
   clip before you animate anything.
3. **Video round.** A 5 s 9:16 clip per beat with sound off (on Higgsfield, pass the
   string `"off"`; a boolean false silently falls back to sound on, at a higher price).
   Preflight every clip's cost. Give each clip **one beat**: name who does what and add
   "nobody speaks". If the tool offers a preset instead, decline it and generate the prompt
   as written.
4. **Review at 0.25 s and trim to the clean window.** Models draw extra objects, celebrate
   before the event, and drift people out of frame; a 5 s clip often has 2 s that are
   usable. Record each clip's usable window in the generation log.
5. **Reconcile against the account's transactions ledger, not the balance.** Other
   sessions may spend on the same account at the same time.

**Rules that still hold:**

- **No screens in generated shots.** No generated shot shows a phone face to camera.
- **Real screens only.** App screens are always real captures in a phone frame.
- **AI label.** Generated people and video mean the Reel carries the AI label on publish.
- **Titles.** Plain sentences, not staccato fragments ("15 ROUNDS. ONE TABLE." reads as
  AI). A dark gradient scrim behind titles over video; none needed over the plate.
- **Credits.** Re-preflight every time; prices move. Record the round's total in the
  generation log so the next brief has a real figure to quote.

**Then read `creative-playbook.md` before the first generation.** It is the production
process; this skill only gets you to an approved concept. Its stage gates exist because
every expensive failure recorded in it was a gate someone skipped.
