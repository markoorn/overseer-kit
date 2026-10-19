# Campaign records

Three records, deliberately separate, because they answer three different questions and
every time one record tried to answer all three it drifted:

| Record | Question it answers | Where |
| --- | --- | --- |
| The pile | What has been proposed, and why each rejected idea was rejected | `_ideas/` |
| Content versions | What exact artefact is approved, with what exact copy | `<feature>/<ad>/POST.md` |
| Publications | Where and when anything actually ran | `_published/` |

An idea marked `Built` means approved creative exists; it says nothing about whether it
was posted. Check `_published/` before saying anything ran.

## Layout

```
campaigns/
  README.md                     this file
  _ideas/
    <round>.md                  one file per brainstorming round; every idea with a status
  _published/
    <YYYY-MM-DD>-<cv-id>.md     one file per publication: platform, URL, tags used
  <feature>/
    FEATURE.md                  product truth, copy guardrails, and the running order
    <ad>/
      BRIEF.md                  the ad-brief output
      POST.md                   the content version record (below)
      POST--<variant>.md        a second format of the same hook (static + reel)
      archive/                  every generated asset and render (gitignored)
      logs/generation-log.md    each generation round: prompts, costs, usable windows
```

`<feature>` is the product capability being promoted. `<ad>` is the hook alone, named for
what a reader would recognise, never for the comic mechanism.

## Idea entry

```markdown
### IDEA-<YYYYMMDD>-<slug> <title>

**Status:** Exploring | Rejected | In production | Built
**Feature:** <feature>
**Campaign:** <feature>/<ad> (once scaffolded)
**Updated:** <date>
**Rejected because:** <the reason, so it does not come back>
```

## Content version record (`POST.md`)

```markdown
## Record

**Feature:** <feature>
**Content version:** CV-<feature>-<ad>-01
**Status:** Draft | Approved | Published | Retired
**Idea:** IDEA-<YYYYMMDD>-<slug>
**Asset:** <path, or "— (not built)">
**Rebuild:** <command that reproduces it, or —>
**Rebuild commit:** <sha, or —>
**Fingerprint (pixels):** <sha256 of `magick <asset> -depth 8 RGBA:-`, or —>
**Reproducible:** yes | no (video is never reproducible; keep the file hash as a tamper check)
**Approved by:** —
**Approved on:** —
**Permitted use:** <organic, paid, both>
**Placements:** instagram, facebook
**Publications:** none

## Caption

```
The caption, exactly as it will post.
```

## Hashtags

```
#brand #category #market
```

## Caption (facebook)

```
Replaces the caption on Facebook; may carry a real link.
```

## Hashtags (facebook)

```
Added to the common tags on Facebook.
```
```

A `CV-` id is allocated once and never changes, even if the directory is renamed or
moved: it appears in publication records and approval history, so editing one orphans a
receipt.

`Approved` requires an approver, a date, a fingerprint and the exact copy. Missing any one
and it stays `Draft`, however finished the artwork looks. A human approves.

The caption and the hashtags each go in a fenced block under their heading; a publishing
tool reads the first fenced block verbatim and nothing else. Plain paragraphs under those
headings read as no caption at all.

## Publication record

```markdown
**Content version:** CV-<feature>-<ad>-01
**Platform:** instagram | facebook
**Surface:** feed | story | reel
**Posted at:** <ISO 8601 with offset>
**URL:** <permalink>
**Tags used:** <the tags as posted, so the next brief grounds its tags in reality>
**Posted by:** <tool or person>
```
