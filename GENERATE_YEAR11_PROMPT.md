Task: Generate the next Year 11 unit of work (lesson plan, episode, or quiz), then stop.

You are an expert HSC Physics tutor and scriptwriter. Each run completes **exactly one unit of
work**, commits it, then stops. Run on a loop; it converges and ends itself, OR pauses at 1 AM.
Working root: `/Users/fred/hsc-phy-podcast`. See `YEAR11_BUILD_PLAN.md` for the master plan.

## HARD CONSTRAINTS — read first
- Work **directly in this one chat context**. Do **NOT** use Workflows or subagents (re-reads specs
  per agent, burns huge usage). Read spec files **once per session**, reuse across iterations.
- Source = `facts/extracted/textbook_jacaranda_physics11.txt` (Jacaranda Physics 11, already extracted).
  **Never open `text book.pdf`** (36 MB — slow/expensive). Find a topic with `grep -n "^TOPIC n "`.
- Do **NOT** generate `.m4a` audio (separate `generate_all_voices.sh` pipeline).
- **1 AM STOP:** the Bash `date` is ~8 h behind real time — ignore it. Real local time is shown in the
  `ScheduleWakeup` tool result. When that result shows **≥ 01:00** (and < ~12:00), do NOT reschedule;
  print `YEAR 11 RUN PAUSED — 1 AM (usage rollover)` and stop. Otherwise keep looping.

## Step 0 — Read the rules ONCE (skip if already in context)
- `STYLE.md` (binding; §9 the gate, §5 the teaching shape), `SUPPLEMENTARY.md` (the `### Listing N —`
  contract), `AUTHORING.md` (the two files). `tools/QUIZ_STYLE_GUIDE.md` (the quiz contract).
- One finished Year-12 episode as the gold standard, e.g. `content/M7-12-Photoelectric-Effect-Part-2/`.
- `YEAR11_BUILD_PLAN.md` (module→topic map, canonical episode list, phases).

## Step 1 — Find the gap (deterministic; do ONE then stop), in this priority order
0. **Missing lesson plan:** first module in M1,M2,M3,M4 with no `TEACHING_LESSON_PLAN_Mx.md`.
   Write it (Step 2A), commit, stop.
1. **Missing episode:** first expected episode (per the canonical list, module→lesson order) whose
   folder is missing or lacks `script.md`/`supplementary.md`/valid frontmatter. Write it (Step 2B), stop.
2. **Missing quiz:** first Year 11 episode that has both `.md` files but no `quiz.json`. Write it (Step 2C), stop.
3. **Backfill quiz:** ONLY if every Year 11 episode + quiz exists and time remains — first existing
   `content/M6-*|M7-*|M8-*|case_*` folder with no `quiz.json`. Write it (Step 2C), stop.
4. **Done:** else print `YEAR 11 BUILD COMPLETE`, confirm clean tree, end the loop (no wakeup).

Detect state with `ls content/<EP>/` and `git status --short`. Honour an explicit target if given.

## Step 2A — Write a lesson plan (`TEACHING_LESSON_PLAN_Mx.md`)
Match the format of `TEACHING_LESSON_PLAN_M7.md`: intro (what these episodes are / aren't, the
extended-response problem they fix, the target listener), then one `### Mx-LL — Title` section per
episode in the canonical list with **Theory focus**, **Extended response prep** (incl. a weak-vs-strong
contrast), **Memorisable lists needing mnemonics (§5.4)**, **Syllabus dot-points served** (lift exact
wording from the textbook topic intro — the "Inquiry question / Students:" block with ACSPH codes
at the start of each TOPIC; `docx_syllabus.md` is Year-12-heavy, so use the textbook for Year 11),
**Cross-links** (incl. forward links to Year 12: M1/M2→M5/M6, M3 waves→M7,
M4 fields→M6, M4 electricity→M6). End with a Recommended Production Order table. Source physics/values
from the textbook topic(s) for that module (grep the extracted text).

## Step 2B — Write an episode (two files in `content/<Mx-LL-Title>/`)
Follow AUTHORING.md + STYLE.md exactly, as the Year-12 episodes do:
- `script.md` frontmatter: `title, module, lesson, kind: lesson` (or `module-review`), `supplementary: supplementary.md`.
- Two voices only (`NARRATOR:` teaches, `QUESTION:` only asks); ~80%+ narrator. **Speakable prose**:
  spell out every number/symbol/operator ("nine point eight metres per second per second", "v equals u
  plus a t"), NO equations/markdown/scientific-notation in the spoken body, NO `## Appendix`.
- Shape: ~5-min spaced-rep opener recapping the last up-to-5 episodes (reuse mnemonics); weak-vs-strong
  contrast for the headline extended response; **≥2 real interleaving links** (incl. forward to Year 12);
  a mnemonic for every memorisable list (reuse the registry); **≥1 "pause the player" retrieval**;
  3–5 closing exam questions in NESA-verb format with full model answers (calcs → a Listing).
- `supplementary.md`: own frontmatter (`script: script.md`), `# Supplementary Materials`, `### Listing N —`
  items (equations/derivations/worked solutions in ```text fences one step per line; data in Markdown
  tables). Narration references each listing by label; every listing is referenced.
- **~4500–6500 spoken words** (reviews may run longer).

## Step 2C — Write a quiz (`content/<EP>/quiz.json`)
Per `tools/QUIZ_STYLE_GUIDE.md`, from the episode's own `script.md`:
- Valid JSON object `{"questions":[ … ]}`, **exactly 10** questions.
- Each: `id` = `m<module><lesson>-q<NN>` (e.g. `m101-q01`), `q` (HSC verb), `options` (**exactly 4**,
  all plausible), `answer` (**zero-based** index 0–3 of the correct option), `explanation` (2–4 sentences,
  same language as the script, names the tempting distractor and any episode mnemonic).
- Mix: ~2–3 recall, 3–4 describe/explain, 2–3 compare, **≥1 scenario/calculation** with 4 plausible numeric
  options. Use exact syllabus terminology. JSON only — no markdown fences inside the file.

## Step 3 — Format gate before committing
- Episode: `script.md` valid frontmatter + only `NARRATOR:`/`QUESTION:` labels + no leaked
  symbols/equations/markdown in the spoken body; `supplementary.md` valid frontmatter +
  `# Supplementary Materials` + balanced ```text fences + every referenced Listing present.
- Quiz: `python3 -c "import json,sys;d=json.load(open(PATH));assert len(d['questions'])==10;[(_q['answer'] in range(4) and len(_q['options'])==4) for _q in d['questions']]"` passes.

## Step 4 — Commit (one focused commit per unit, straight to `main`)
e.g. `M1: add kinematics lesson plan`, `M1-01: add motion in a straight line episode`,
`M1-01: add quiz`. Pre-commit hook refreshes `manifest.json` (auto-sets `quizPath`); if not, run
`python3 tools/generate_manifest.py` — BUT it rewrites audio URLs to local paths, so prefer the hook;
if you ran it and only URLs changed, `git checkout manifest.json`. End commit messages with the
co-author trailer the harness specifies. Don't push.

## Step 5 — Report briefly, then continue or stop
- What unit was produced (path) + key specifics (dot-points / mnemonics / listings / quiz mix).
- STYLE §9 / quiz-gate checklist: tick; flag anything unmet.
- State the next gap. Then: if a `ScheduleWakeup` would land **≥ 01:00**, STOP and print the 1 AM
  pause line; else `ScheduleWakeup` (~60 s) with this prompt to continue. If everything is done,
  print `YEAR 11 BUILD COMPLETE` and do not reschedule.

Write the artifact, not a summary of one. If anything conflicts with STYLE.md, STYLE.md wins.
