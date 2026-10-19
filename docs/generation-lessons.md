# Generation lessons

What a few months of making ads with AI image, video and voice models taught, with the
brand stripped out. Every rule here cost real credits or a rejected cut. The setup skill
copies this file into your creative playbook as its starting "lessons" section; add your
own under it with the same shape (observation, interpretation, reusable change) and the
evidence that earned each one.

Most of these were learned on Higgsfield (`docs/ad-brief-guide.md` says why that
platform), but the shape of each problem transfers to any metered generation account.
Model names, prices and capabilities are dated observations, never properties; re-check
them at the start of every campaign.

## What matters, in order

1. **Believable people and conversational delivery.** Do they sound and behave like
   people who know each other?
2. **The story working as a joke**: setup, product evidence, the human retreat, the
   payoff.
3. **Clear product evidence and coherent continuity.**
4. **Cosmetic cleanup.**

A take that fails 1 or 2 does not advance because it passes 3 or 4. Everything below is
in service of this ordering.

- **Technical compliance is not creative approval, and must never be reported as it.**
  "Both lines present, correct speaker, clean hands" means a take is eligible for review.
  Report the checks and the creative question separately.
- **Keep observations, explanations and hypotheses apart.** "This take faded the character
  in" is an observation. "The empty start frame caused it" is an explanation to test.
  "A peeking element will fix it" is a hypothesis. One run is a hypothesis; two agreeing
  is a weak one; neither is a rule about a model.
- **Do not use measurement to validate, or argue with, a perceptual verdict.** Measure
  level, duration, timing, silence, frame counts and spend, where the number is the
  answer. A facial-motion metric predicted the wrong take twice; a detail metric scored a
  rejected model higher. When a reviewer says "feels generated", record it and act on it.

## Before you spend

- **Write a scene blueprint before generating any shot.** Each character (story name, a
  cast thumbnail, screen position), exact dialogue and who says it, each beat's action and
  purpose, prop position at the start and end of each shot, who looks at whom, the exact
  product capture shown and which detail supports the joke, shot size, transitions, timing
  budget, CTA. State the facts that must be true; let acting be acting.
- **Build a timed animatic from the blueprint before paying for a performance shot.**
  Existing footage and stills, labelled placeholders, the real product capture (never a
  placeholder for evidence), scratch audio from the OS voice (free, and sounds nothing
  like the real thing, which is a feature for a placeholder). Check duration and pacing
  first. Expect system TTS to run shorter than a real delivery.
- **A proof test must falsify what is most likely to kill the idea.** A new audio-driven
  model was proof-tested for sync, passed, and was then rejected on sight because the
  people looked generated. Realism was the risk; sync was merely measurable. For
  generated people the killer is almost always believability, judged by a person.
- **A promising still is not proof of a working sequence.** Test the interaction most
  likely to break the concept (the cause-and-effect beat) before building the gag around
  a frame that looks great.
- **Test the hardest impossible element on its own first**, with one cheap clip, before
  committing to the whole skit.
- **Compare models before spending rounds on one.** Two days on one model never landed; a
  single bounded comparison (four models, two prompts) found the best take the brand ever
  got, on the cheapest model per take.
- **Change one variable per experiment, with the take budget set before you start.**
  Composition, reference, settings, prompt or model, one at a time. A day that changed
  method every round failed in a new way each time and taught little.
- **A model's capabilities are a dated observation.** Record model, version, mode and
  date next to any capability finding. "No model does both" means "none of the ones
  tested that day".
- **Precise human timing is often better filmed than generated.** A golfer at address
  has an overwhelming "swing now" prior; an impossible event has a weak one. Film the
  person on a phone and generate or composite only the impossible part.

## Spend discipline

- **Authorisation is a specific figure for a specific batch.** A large balance, a
  subscription tier or a promotion is not permission. Before each batch, state the
  cumulative figure against the standing cap and the amount left inside the last explicit
  approval, and say when a batch would cross either. Unused headroom is not a reason to
  spend it.
- **Preflight the exact call you will make.** Most platforms return a cost without
  creating a job. A quote is valid only for that call shape: a `count: 3` quote may price
  one; a batch of text-to-speech calls bills per string length, so preflight the strings
  you will send, not the shortest one. Read the exact credit figure, not the rounded
  display value.
- **Price the returned output, not the requested settings.** A job that priced the same at
  720p and 1080p returned 720p either way. Measure the delivered file; record an upscale
  as an upscale. And when a requested setting is ignored, check whether a different
  parameter (a quality mode) governs the thing you want before concluding the output is
  the best the model can do.
- **Reconcile against the platform's transaction ledger, never your own tally.** A
  hand-kept tally drifted 38 credits under over one campaign, silently and in the
  flattering direction. Other sessions may spend on the same account at the same time.
- **Log a generation round when it returns**, while prompt, intent and verdict are all
  still to hand. Two rounds that contained the shot the ad shipped were never written up
  and had to be reconstructed from job history.
- **Track exploration spend separately from production spend.** On one campaign 63% of
  the total went on model exploration; nobody could answer "what did the ad cost".
- **Stills are cheap; video is where the money goes.** Quote before video; run stills
  inside an approved cap and report the running total.
- **Keep a model's "sound off" as the documented string, not a boolean.** On one platform
  `false` silently fell back to sound on, at a higher price.

## Casting and references

- **One face per character across every clip.** Generate the first cast still, then pass
  it (by job id or upload) as an image reference to every later still and clip with the
  same people. Describe each person by clothing and say "the same N people, identical
  faces and clothing". Compare faces side by side before animating anything. A trophy
  clip with a different man from the putt clip was sent straight back.
- **Cast-distinction check at true phone width** (about 393px for a 9:16 Reel) before
  any animation. Can a viewer instantly tell the characters apart, and follow who speaks,
  who presents the evidence and who reacts? Differ on face, silhouette and wardrobe with
  a hard value contrast. Clothing alone is not enough.
- **Keep a cast reference sheet**: role, appearance, wardrobe, reference asset, with
  working names used for continuity and never shown on screen.
- **Verify a start frame's hands and composition at native size before paying to animate
  it.** Stills cost a fraction of a clip. Reject on cropped heads or bad hands there.
- **A start frame constrains frame zero, not the clip.** A chest that was clean at 0.0s
  grew a logo-shaped glyph at 2.6s, inside the spoken line, so no trim recovered it.
  Repeat positive descriptions ("smooth, unbroken navy fabric") in every prompt; scan the
  whole clip at a tight crop for wardrobe and prop drift; prefer placing a risky detail
  where it could be cropped out.
- **The start frame carries its flaws through.** A posed start frame gives a posed clip.
  Start candid, mid-action, imperfect.
- **Anchor a re-roll on a frame from the take you approved.** Extract a clean frame and
  pass it as the start image; it carries cast, wardrobe, location and light while the
  action changes. Pick the anchor frame on its merits (the first frame may have a bad
  prop). It fixes frame one, not the performance.
- **For a hard cut, feed the neighbour's actual boundary frame** as start or end image
  alongside the cast reference. It matched pose closely twice; check every time.
- **Start frames are honoured; end frames are only approximated.** Chain from a clip's
  actual last frame, never from the frame it was aiming at.
- **Put shot size in the blueprint.** At phone size you cannot read expression in a wide
  two-shot. Faces large enough to read; no bright backlit wall behind them (flat even
  light is an AI tell; warm light with falloff flatters). A reference still's framing
  becomes every shot's framing.
- **A combined reference still can recast an actor from an earlier generation**: pass both
  actors' prior stills as separate references on one new still, saying which maps to
  which side. Worked once; check it like any casting still.

## Prompting performance and dialogue

- **Direct intention, not facial mechanics.** Say who the people are to each other and
  what each is trying to do. Prescribing smiles, pauses and gesture timing produces
  compliance and kills the performance.
- **Say nothing at all about the non-speaking actor's face.** The listener given no
  direction was "by far the best"; the one given behaviour was passive; the one given
  intention was in between.
- **Give the model the line, the accent, and one delivery note. Then stop.** Line plus
  blocking plus rhythm plus faces gave eight stiff rolls. Line plus one note gave a take
  that invented a better beat than any prompt. No line at all gave a different ad. Count
  the direction clauses before submitting; more than one is this mistake in progress.
- **A broad one-line prompt matched or beat the directed one on every model tried.**
  Describe the idea and let the model stage it. Get the performance first, add the brand
  after (a cap was added to the winning take with a video-to-video edit, timing intact).
- **Name characters for attribution and blocking; never put a name near a quoted line.**
  "Call him Sipho" came back as the actor saying "Sipho" over the silent beat.
- **Name a prop distinctly at every reference.** "Takes hold of it" with three glasses on
  the table had him take his own beer. A character behaving oddly toward an object is a
  reference bug until proven otherwise; do not "fix" the performance direction.
- **Body sides are ambiguous when the frame has a left and right too.** Describe a hand by
  relation: the one nearer the other character, the outer one.
- **For a state that must persist through an action, say it positively and name the hand
  that moves.** A capitalised "NEVER puts the phone down" did not hold; "his phone hand
  stays where it is; only the other hand moves" gives the model something to do.
- **Open on a beat of silence.** The first second is scroll, not attention; ask for it in
  the prompt ("for the first full second nobody speaks"), because you cannot trim it in
  afterwards. Budget the breather when choosing clip length.
- **Budget the take's length to its content.** Every approved take in one campaign was
  8 s or shorter; moving to 12 s to fit a beat produced eight consecutive "slow and
  forced" rejections. Cut a beat rather than extend.
- **Accent: name it per character, state what it must not be (the default is American),
  and treat prompting as the cheap first attempt only.** The same paragraph produced a
  winner one day and failed six of six the next, in the same model. Escalating the prose
  did not help. What delivered the accent was a consented cloned voice laid over approved
  picture. Do not keep buying takes to fix an accent after the second failed round.
- **Write dialogue in phonemes the model can say.** Regional words ("sjoe", "boet") failed
  across five voice architectures; an ordinary English tag ("hey?") carried the region and
  came back right first time. Check homographs: "putting" is read as the verb; "putts"
  and "putted" are not. The rule applies to the prompt's prose too, since an unscripted
  model paraphrases direction into dialogue.
- **These video models write their own dialogue.** A quoted line was not followed; captions
  authored separately disagreed with the audio. Where the model authors speech, derive
  every caption from the transcript, verbatim. Where exact words matter, place the line
  over a shot with no visible speaking mouth, or script it to a dedicated TTS engine and
  drive the shot from that audio. Budget spoken duration from the generated audio, not
  from reading the line in your head (3.5 s estimated came back at 6.9 s).
- **A cutaway can carry a line the generated mouth cannot.** Decide before generating
  which lines need a visible speaking face. An insert costs screen time, so extend one
  because it earns attention, never to hide a problem.
- **Premise check, separate from the claim check.** "Mm. Should we check?" asserted
  nothing false and still argued against a product whose point is that it kept the
  record. "Shame. It's already logged." asserts the record exists, carries the comedy in
  one local word, names no product, and still motivates the cut. Ask whether a line
  assumes the product's job is still to be done.
- **Name the offence; do not make the viewer derive it.** State the claim in the caption
  and let the capture support it; check the wording against what the capture can
  substantiate.

## Causality and action

- **The models ignore causal order.** "Screams before the shot, causing the duff" came back
  as a reaction to a bad shot. Make each beat its own short shot and let the cut set the
  order.
- **Never split a fast continuous action at a generation boundary.** A follow-through and
  the top of a backswing look alike as stills; a continuation built from one gave a second
  swing. Keep the whole action in one generation.
- **An emergence must read as movement through an opening.** Generated takes tend to
  materialise (fade or morph) rather than move. A local fix: a clean plate of the opening
  plus an opaque cut-out moved behind a mask of the rim. Never an opacity fade.
- **A small accident reads as intent in a wide shot.** Pick an unmistakable action.
- **The storyboarded action may not be in the delivered clip.** Treat the prompt as a
  request and the clip as the fact. Build a frame sheet across the whole source before
  setting any in-point; prompting an order does not buy an order.
- **The performance usually arrives in the back half of a short clip.** Buy a little
  more duration than the beat needs; cost is linear in seconds.
- **Review at 0.25 s intervals and trim to the clean window.** Models draw extra objects
  and celebrate early; a 5 s clip often has 2 s that are usable. A 1 fps contact sheet
  made an agent call a putt a nudge; judge timing from dense strips.
- **A constraint that removes an artefact will also change the performance.** Pinning
  both hands removed a malformed thumb and turned a shrug into a grin. Decide which loss
  is worse and keep both takes reachable.
- **Accept or reject a take as a whole.** Accepting on picture "and fix the audio later"
  spawned a voice clone, engine comparisons, a measured lip offset and an alternative
  workflow. The distinguishing question: have we already done this exact repair
  successfully on this footage? If yes it is an editing plan; if no it is a bet, priced
  as one.
- **Once a take is good, buy variance, not another edit.** Seven rounds and sixteen takes
  went on "targeted repairs" that each broke something already working, because every
  clause competes for the model's attention. If one thing is wrong, solve it in the edit;
  if it cannot be, re-roll the identical prompt. Save the good take first: a re-roll keeps
  the recipe, not the performance. Reserve prompt edits for faults that appear in every
  take (and for ambiguities: a name instead of a position, a prop instead of "it").
- **Do not splice a missing action in from another take of the same locked-off framing.**
  Two takes are not two angles; it reads as a continuity error.
- **Re-framing one take licenses a time cut.** A cut between two crops of the same take
  removed four seconds of dead air cleanly. Run scene detection on the seam: if it sees
  no change, the edit will not read as deliberate.
- **Recheck both transitions whenever a shot is added, removed or replaced**: repeated or
  missing action, prop position, eyelines, who speaks, ambience level.
- **A story revision invalidates footage through props and hands, not performance.**
  Audit each approved clip against the new blueprint: is every prop present, each hand
  free or occupied as required, the action in the new order, the right character
  speaking. Assign hands in the blueprint; arm choreography that needs explaining is arm
  choreography the model will not perform.

## Product screens

- **Never let a product screen face the camera in a generated shot.** "The camera only
  ever sees the back of the phone" held across every frame of an 8 s take; "holding up
  his phone showing a leaderboard" invented a UI. You cannot fix a handheld screen in
  post (planar tracking, corner-pin), and keeping screens out of the setup makes the first
  real screen the reveal.
- **A screenshot always goes inside a phone frame.** A bare capture reads as a pasted
  image; the same capture in a device reads as somebody's phone. The capture fits the
  opening whole, no crop, no distortion, placed and scaled as a unit.
- **A composited screen needs four checks**: orientation, boundary (sample the device's
  edges, not the centre), perspective, legibility at true playback size. A successful warp
  is not one of them. Finish with a visual review.
- **An illustrated walkthrough is not evidence that a journey works.** It shows what each
  state looks like and their order; copy must not claim more.
- **A click-through needs a ripple and a click from one timeline**, the tap landing a
  beat before the screen responds, never simultaneously. Measure tap coordinates from the
  capture; two of three eyeballed targets were wrong.
- **Reuse the campaign's own rendered assets** (the end card is the static ad's PNG,
  copy lives once), and then **re-read the pixels**: an asset built from a stale capture
  shipped a wrong name in nineteen versions because nobody re-reads small print inside a
  phone inside an end card after the first sign-off. When a capture is re-taken,
  re-render everything downstream.

## Review

- **Never infer speech from waveforms or mouth movement.** Presence, intelligibility and
  script-accuracy of speech are listening findings. An agent that cannot listen says
  "pending human review" and never reports an absence. Levels find where to look, ASR
  suggests what was probably said, mouth crops rule speech in but never out, and only
  listening settles it.
- **Transcribe before you cut.** Energy dips are where a comedian stands, so cutting on
  them halves sentences. Cut only in transcribed gaps between words, then transcribe the
  finished export and read it back. A complete exchange inside one take is not a cut at
  all; change the caption on the word boundaries instead.
- **Transcription verifies the word, never the pronunciation.** ASR returns the most
  probable intended word; "three pooted" transcribed as "three putted". Record
  pronunciation as unverified until a person has listened. When a word is a known
  offender, change the phrasing rather than fight the pronouncer.
- **Whisper hallucinates over near-silence** ("Thanks for watching!" over bare ambience)
  and an incomplete transcript read mid-run reported "no dialogue" on a clip with three
  lines.
- **Check the whole clip, not the start frame**, for wardrobe, props and anything the
  model re-invents as it runs.
- **Check final exports with sound on and off.** Three black beats and a clipped line were
  invisible in the timeline preview and obvious in the file. The message must land with
  sound off, since captions carry it in feed.
- **Scan generated audio for discontinuities before accepting a take**, because the fix is
  a regeneration, not an edit. But the site count carries no quality signal: the worst
  reading of any take was the one the reviewer called a winner. Use it only to point a
  human at a timestamp.
- **Identify an event before removing it; "nobody heard it on one pass" is not an
  identification.** Unresolved events get their measured level and window recorded and
  revisited, not closed.
- **Record an artefact's measured level and window next to any decision to defer it**, and
  assert the trim actually excludes it. "One quiet blip, handled by trim" shipped at
  dialogue level because "quiet" was an adjective and the trim was never checked.
- **Label AI-generated video and people.** Any ad with generated video, or generated
  people or voices presented as real, carries the platform's AI label. Disclosure
  volunteered costs nothing; disclosure extracted costs trust. A static that places a real
  product in a generated scene needs no label, but the record still says what is
  generated.

## Audio and assembly

- **Normalise once, on the finished mix, to a stated target**, never clip by clip. Use
  two-pass loudness normalisation (measure, then apply one constant gain): single-pass is
  dynamic and makes the noise floor "fade in and out" by up to 6 dB.
- **When you raise one region of a normalised mix, measure a region you did not change.**
  The normaliser can silently take your change back elsewhere.
- **Carry room tone across every beat, at the measured floor of the talking clips.** A
  still beat on digital silence sounds like a fault.
- **A short bed looped under a card becomes a sound effect.** A 0.6 s slice looped 3.3
  times read as a bird call; a 0.8 s loop under a cut was spotted instantly. Periodicity is
  worse than unevenness. Build a bed longer than the cut from quiet runs across every
  clip the campaign generated (keep runs of 1 s or more, trim the ends, reject on peak as
  well as RMS, gain-match, crossfade joins) and use it once.
- **What makes a bed sound smooth is content, not level.** Dense room tone at -40 dB
  reads as a room; sparse birds at -51 dB read as a hole. Bring the effect down, not the
  bed up.
- **Denoise with a sampled profile or it barely works**, and heavy denoise widens the
  floor spread while lowering it. Keep an inaudible floor so samples never hit zero.
- **Assemblies fail silently, so assert.** An end card that never attached, a mix
  truncated at the first input's length (`amix=duration=longest`), a crossfade that
  returned the wrong length three ways. Scripts probe every window that must carry sound
  and throw below a floor; the end-card step checks the video stream actually grew.
- **Measure a cue the way its defect would show.** Peak for a transient, mean for a
  sustained bed or line; per channel, not a stereo fold (3 dB hotter); a ceiling as well
  as a floor; and bound a cue against what actually limits it (a click never overlapped
  the dialogue it was being sized against). When a level has been wrong twice, render
  three gains and let a person pick by ear.
- **Measure a cut's level step on the windows immediately adjacent to it.** A 150 ms
  look-back caught a word's decaying tail and reported an 18 dB step at a seam that
  measured 0.0.
- **A measurement window belongs to one timeline.** Timestamps chosen on one cut landed on
  dialogue in the other and reported speech as background.
- **Assemble in one filter graph**, one video encode, one audio encode. Joining separately
  encoded segments left a 78 ms gap in the audio stream that no loudness check saw.
  Normalise frame rate and timebase before concatenating sources. Verify cut points by
  decoding in sequence, not by seeking.
- **Anything timed against a sum of clip lengths is timed against the wrong number** once
  each clip rounds to whole frames. Time on one timeline and measure the delivered file.
- **Measure a transition against its destination image, not one of its colours**, and
  verify the progress variable's direction from rendered frames (`xfade`'s `P` runs
  1 to 0).
- **Check a card against the placement's chrome by measuring clearance.** Store badges sat
  38 px clear of the band Instagram covers in one variant and 52 px inside it in another.
  Draw the covered regions and measure ink extents.
- **`enable=` gates time, not space.** To clip spatially, composite into a canvas of the
  target size and overlay the canvas.
- **Confirm the local encoder has the filter you are designing around** (`drawtext` was
  missing on one machine) before building a caption pipeline.
- **Set `LC_ALL=C` in measurement scripts.** A comma-decimal locale parsed `9.65` as `9`
  and manufactured a false finding.

## Replacing a line in approved footage

- **Repair a one-word defect locally; do not regenerate an approved performance.** Replace
  the word with gain-matched room tone from the same take, stream-copy the video, widen
  the window once for the leading consonant, verify by transcript (token absent) then by
  ear.
- **Lift replacement audio from inside connected speech; never generate a fragment.**
  Thirteen standalone interjections on a cloned voice sounded like a stranger; the same
  words cut from the middle of a carrier sentence were approved immediately. Identity
  lives in formant trajectories across connected speech.
- **Match the mouth's posture, not just the duration.** Parted lips with teeth take /h/,
  open vowels and sibilants and refuse /p/ /b/ /m/; closed lips the reverse. Reading
  posture off the frames generates candidates as well as rejecting them.
- **The mouth is only readable while the head is still.** Put the best-matched sound where
  the head is still and the weaker one under the turn.
- **The anchor moment depends on the consonant**: plosives by onset, nasals by release.
- **Prove a conditioning input was actually used.** "The API accepted it" is not "the model
  used it": nine generations with a voice reference returned someone else, every job
  succeeding. The test is a control generation with the input removed. Pitch can rule a
  voice out, never in; a preview byte-identical to the upload proves storage, not
  cloning; and conditioning is not resemblance, which stays a listening call.

## Records and rights

- **Set up the campaign layout on day one**: deliverable at the campaign root, everything
  else under `archive/` (gitignored), scripts and records tracked. Media never lives in a
  worktree, because `git worktree remove` takes gitignored files with it. An unmerged
  campaign branch makes the whole campaign invisible.
- **An assembly built outside the committed script stops being reproducible, silently.**
  Test it: delete the intermediates, re-run the one command, compare hashes.
- **Correct a superseded asset by adding a new one, not overwriting**, once an export has
  been shown to anyone.
- **Record permission for a cloned voice; a fingerprint cannot supply it.** Whose voice,
  who supplied it, that they knowingly supplied it for this purpose, and that the
  permission covers cloning and advertising use. Never clone an identifiable third party
  or public figure. A clean fingerprint means "not a known blocked source", not
  "cleared".
- **Cast to reflect the audience naturally**, across leading, supporting and professional
  roles, varying who occupies which role, and never tying identity to who is the butt of
  the joke.
- **Promote a lesson here when it changes a future decision**, with precise evidence
  labels: direction approved; rendered and inspected; workflow reproduced; audience
  feedback observed; performance measured. These are separate claims. A clear correctness
  defect justifies an immediate rule; an aesthetic preference does not.
