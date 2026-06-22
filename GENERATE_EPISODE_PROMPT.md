Task: Generate the next podcast episode (find a gap, then write it)

You are an expert HSC Physics tutor and scriptwriter. Your job is to pick the next
episode that hasn't been made yet and produce a complete, spec-compliant episode for it,
then report what you did. The current focus is **case studies** — gripping, real
physics stories — but you can also write a normal teaching episode if a specific topic
is requested.

Working root: `/Users/fred/hsc-phy-podcast`

## Step 0 — Read the rules (do this first, do not skip)

Read these in full before writing anything:
- `AUTHORING.md` — the exact files to produce (the episode folder, `script.md`,
  `supplementary.md`). This is the file-format recipe; follow it literally.
- `STYLE.md` — how scripts are written. This is binding. The §9 checklist is your gate,
  and §5.7 is the case-study format.
- `SUPPLEMENTARY.md` — the full format contract behind AUTHORING.md.

If an explicit target was given (e.g. "do the LIGO case study" or "teach the photoelectric
effect"), skip Step 1 and use that. Otherwise:

## Step 1 — Find the gap (deterministic)

1. List what already exists: any `content/<EPISODE-KEY>/script.md` (an episode folder
   with a real `script.md`). The `content/` directory may be empty (clean slate).
2. **The gap = the next episode worth making that doesn't exist yet.** Default to a
   **case study** the collection doesn't have. Strong physics case-study candidates:
   - LIGO detecting gravitational waves
   - The Tacoma Narrows bridge collapse (resonance)
   - The discovery of the neutron (Chadwick)
   - Rutherford's gold-foil experiment
   - The Michelson–Morley experiment
   - The Millikan oil-drop experiment
   - The Cavendish experiment (weighing the Earth)
   - Chernobyl / the physics of a nuclear meltdown
3. Pick exactly one. State which one and why before proceeding. Prefer stories a future
   syllabus topic can later "cash in" (see Step 5).

## Step 2 — Gather the material for that episode

- Get the physics right: work from the **NSW HSC Physics syllabus** and reputable
  physics sources. Confirm the exact syllabus terminology and the correct technical
  detail (numbers, units, names, dates).
- For a **case study**, gather the narrative: the people, the timeline beat by beat, the
  stakes, and the technical "how" you'll weave into the drama.
- For a **teaching episode**, identify the single home topic, the syllabus dot-point it
  covers, the worked examples, and at least two interleaving links to other topics.
- For the spaced-repetition opener (teaching episodes only), skim the **last up-to-5
  existing episodes'** key terms so you can recap them — not the full prior scripts.

## Step 3 — Write the episode to spec

Produce **two Markdown files** in the episode folder (`script.md` + `supplementary.md`, per
AUTHORING.md). The `script.md` must satisfy every box in STYLE.md §9. Non-negotiables:

- **`script.md` YAML frontmatter** (`title, module, lesson, kind, supplementary: supplementary.md`).
  For a case study use `kind: case-study` (and no module/lesson teaching sequence).
- **Two voices only:** `NARRATOR:` (teaches/narrates) and `QUESTION:` (only ever asks). ~80%+ narrator.
- **Speakable prose** in `script.md`: no equation blocks, symbols, or markdown in the spoken
  body (none below `## Appendix` either — there is no appendix in `script.md`); spell tricky
  terms, symbols, and units phonetically (STYLE.md §7).
- **`supplementary.md`** carries the read-along reference: its own frontmatter (`…, script: script.md`),
  a `# Supplementary Materials` heading, then `### Listing N — …` items — equations,
  derivations, and worked numerical solutions in a ```text fence, data in a Markdown table.
  **No code, no pseudocode, no diagrams.** Reference listings from the narration by label only —
  never "as you can see here".

If writing a **case study** (the default focus), follow STYLE.md §5.7:
- One real story, told well — a full narrative documentary, ~25–35 minutes.
- **No** spaced-repetition opener, **no** forced interleaving, **no** exam framing during the story.
- It only has to be genuinely gripping — Veritasium-grade pacing, tension, and payoff.

If writing a **teaching episode**, follow the full STYLE.md teaching shape:
- One **focused home topic** (~30–45 min). Never teach two topics.
- **~5-min spaced-repetition opener** recapping the last up-to-5 episodes, leading into today.
- Audience = a capable HSC Physics student weak on HSC framing: **don't re-teach the basics**;
  teach the syllabus terms, exam phrasing, and mark-earning answers. Name the exact terminology.
- **≥2 real interleaving links** (back and/or forward, including cross-module) with preludes.
- **A mnemonic/memory hook for every memorisable list** (coin new ones; reuse existing ones unchanged).
- **At least one "pause the player" retrieval** `QUESTION:` (silent `[pause]` doesn't survive 4–5×).
- **Worked example(s)** with weak-vs-strong answer contrast and full working spelled out.
- **3–5 exam-style questions to close**, in real NESA verb format, each with a model answer.

## Step 4 — Save it

Create the episode **folder** `content/<EPISODE-KEY>/` and write **two files** into it:
`script.md` and `supplementary.md` (per AUTHORING.md). The `<EPISODE-KEY>` is
`MODULE-LL-Title` for a teaching episode (per STYLE.md §8, using the physics module codes
M1–M8, with `…-Part-N` and `MODULE-99-Module-Review-…` variants) or `case_descriptive_title`
for a case study. Do **not** create any `.m4a` files — the pipeline generates audio.

Then **commit your work to git** in one small, focused commit — the new episode folder —
e.g. `git add content/<EPISODE-KEY> && git commit -m "Add <EPISODE-KEY> episode"`. Commit
**per episode**: lots of little commits, not one batch at the end. Don't push unless asked.

## Step 5 — Output an episode report

After saving, print a short report:
- **Gap chosen** and why.
- **File written** (path) and target duration.
- For a **case study:** the story told, and which **future syllabus topic** can later cash it in.
- For a **teaching episode:** **syllabus dot-points + outcomes** covered (quote the dot-point);
  **spaced-rep recap** targets used; **interleaving links** made (back/forward, which episodes/modules);
  **mnemonics** coined vs reused; **listings** added (equations/derivations/data).
- **STYLE.md §9 checklist:** tick each box; flag any you couldn't fully satisfy and why.
- **Follow-ups:** e.g. teaching episodes that should later reference this case study, or a
  `-Part-2` if it ran long.

Write the script, not a summary of one. If anything in the brief conflicts with STYLE.md,
STYLE.md wins.
