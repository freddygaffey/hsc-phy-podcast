Task: Generate the next podcast episode (find the gap, write it, commit it)

You are an expert HSC Physics tutor and scriptwriter. Each time you run this, you complete
**exactly one unit of work** — usually one episode — then stop. Run on a loop (see the very
bottom); the loop converges and ends itself when the collection is complete.

Working root: `/Users/fred/hsc-phy-podcast`

## HARD CONSTRAINT — read first

Work **directly in this one chat context**. Do **NOT** use Workflows or spawn subagents —
that re-reads every spec file per agent and burns huge usage, which is exactly what we avoid.
Read the spec files **once per session** and reuse the loaded context across loop iterations.
Do **not** generate `.m4a` audio — a separate pipeline (`generate_all_voices.sh`) does that.

## Step 0 — Read the rules ONCE (skip anything already in your context)

- `AUTHORING.md` — the exact files to produce (episode folder, `script.md`, `supplementary.md`).
- `STYLE.md` — how scripts are written. Binding. **§9 is the gate; §5 the teaching shape;
  §5.7 the case-study format.**
- `SUPPLEMENTARY.md` — the `supplementary.md` format contract (`### Listing N —`, ```text fences, tables).
- `TEACHING_LESSON_PLAN_M7.md` and `TEACHING_LESSON_PLAN_M8.md` — full per-episode specs (theory
  focus, weak-vs-strong answers, dot-points, cross-links, mnemonics). The teaching backlog lives here.
- One **finished** episode as the gold-standard template, e.g.
  `content/M7-12-Photoelectric-Effect-Part-2/` (both files). Match its depth, voice, listing style.

If these are already loaded from an earlier iteration, **don't re-read them** — go to Step 1.

## Step 1 — Find the gap (deterministic, do ONE then stop)

The episodes that *should* exist are defined by the two lesson plans: M7-01…M7-15 + M7-99 and
M8-01…M8-14 + M8-99. (M5 is **skipped** — practice only. M6 is complete.) In priority order:

1. **Incomplete teaching/review episode.** Find the first expected episode (module → lesson
   order) whose folder is missing, or missing `script.md` or `supplementary.md`, or whose files
   are empty / lack valid frontmatter. **Write the missing file(s) for that ONE episode** (Steps
   2–4), then stop. Use `ls content/<EPISODE>/` and `git status --short` to detect state.
2. **Uncommitted complete work.** Else if a complete episode folder, or `TEACHING_LESSON_PLAN_*.md`,
   is uncommitted, commit the next one (Step 4), then stop.
3. **Stale manifest.** Else run `python3 tools/generate_manifest.py`; if `manifest.json` changed,
   commit it, then stop.
4. **A missing case study** (only once 1–3 are exhausted, and only if more are wanted). Default
   candidates: LIGO; Tacoma Narrows; Chadwick's neutron; Rutherford gold foil; Michelson–Morley;
   Millikan oil-drop; Cavendish; Chernobyl. Pick one, write it (Steps 2–4 in case-study mode), stop.
5. **Done.** Else print `PODCAST BUILD COMPLETE`, run `git status` to confirm a clean tree, and
   **end the loop** (do not schedule another wakeup).

If an explicit target was given ("do the LIGO case study", "write M7-10"), use that instead of Step 1.

### Known remaining teaching backlog (verify against disk each run)

Both files unless noted:
- `M7-10-Black-Body-Radiation-And-Wien-Law` — BOTH
- `M7-11-Photoelectric-Effect-Part-1` — BOTH
- `M7-13-Frames-Of-Reference-And-Einstein-Postulates` — BOTH
- `M7-15-Relativistic-Momentum-And-Mass-Energy` — BOTH
- `M8-09-Mass-Defect-Binding-Energy-And-E-Equals-Mc-Squared` — `supplementary.md` ONLY (script
  exists; Read it first; match its Listings: 1 = He-4 working, 2 = masses/constants, 3 = D-T
  fusion ≈17.6 MeV, 4 = U-236 fission both methods ≈160 MeV).
- `M8-10-Nuclear-Fission-And-The-Reactor` — CREATE folder + BOTH (plan heading "### M8-10 —
  Nuclear Fission and the Reactor").
- `M8-99-Module-Review-From-The-Universe-To-The-Atom` — `supplementary.md` ONLY (script exists;
  Read it first; supply every Listing it names, incl. 5 = binding-energy-curve landmarks, 6 =
  atomic-model-development skeleton).

~24 prior-workflow drafts + the two lesson-plan files are also uncommitted on `main`. The manifest
currently lacks M6-13 and M6-15.

## Step 2 — Gather material for that episode

- Find its section in the lesson plan (e.g. "### M7-10") and follow it closely: theory focus, the
  weak-vs-strong extended-response contrast, dot-points, cross-links.
- Read the relevant facts source for exact physics/values/worked numbers:
  - M7-10, M7-11 → `facts/extracted/pdf_jacaranda_ch10_quantum_model_light.md` (+ `pptx_light_quantum_model.md`)
  - M7-13, M7-15 → `facts/extracted/pdf_jacaranda_ch11_special_relativity.md` (+ `pptx_special_relativity.md`)
  - M8-09, M8-10 → `facts/extracted/pdf_jacaranda_ch15_properties_nucleus.md`
- For the spaced-rep opener, **glance at the adjacent already-written episodes on disk** for their
  exact key terms so the recap is accurate — not the full prior scripts.
- For a case study: gather the narrative — people, timeline beat by beat, stakes, the technical "how".

## Step 3 — Write the episode to spec

Two Markdown files in the folder (per AUTHORING.md). `script.md` must satisfy every STYLE.md §9 box.

- **`script.md` frontmatter:** `title, module, lesson, kind` (lesson | case-study | module-review),
  `supplementary: supplementary.md`.
- **Two voices only:** `NARRATOR:` (teaches) and `QUESTION:` (only ever asks). ~80%+ narrator.
- **Speakable prose:** no equations, symbols, scientific notation, or markdown anywhere in the spoken
  body — spell everything out ("six point six three times ten to the minus thirty-four", "lambda",
  "equals"). No `## Appendix` in `script.md`.
- **`supplementary.md`:** own frontmatter (`…, script: script.md`), `# Supplementary Materials`
  heading, then `### Listing N — …` items — equations/derivations/worked solutions in ```text fences
  (one step per line), data in Markdown tables. No code, no diagrams. Narration references each
  listing by label only, never "as you can see here", and every listing is referenced.
- **~4500–6500 spoken words** (module reviews may run longer).

**Teaching episode** (full STYLE.md shape):
- One focused home topic. **Don't re-teach basics**; teach syllabus terms, exam phrasing, mark-earning answers.
- **~5-min spaced-rep opener** recapping the last up-to-5 episodes, leading into today — reuse the registry mnemonics.
- **Weak-vs-strong answer contrast** for the headline extended response.
- **≥2 real interleaving links** (back/forward, incl. cross-module) with preludes; cross-link relevant
  case studies by folder name (e.g. `case_photoelectric_effect`, `case_michelson_morley_experiment`,
  `case_nuclear_fission_manhattan_project`, `case_chernobyl_physics_of_meltdown`).
- **A mnemonic for every memorisable list** — reuse the registry below unchanged; coin new ones only when needed.
- **≥1 "pause the player" retrieval** `QUESTION:` (silent `[pause]` doesn't survive 4–5×).
- **3–5 closing exam questions** in real NESA-verb format, each with a full model answer (calculations
  referenced to a Listing).

**Module review** (`kind: module-review`, STYLE.md §5.3): integrative, second-voice-heavy, multi-topic
exam questions tying the whole module together; can run long.

**Case study** (STYLE.md §5.7): one real story, ~25–35 min, Veritasium-grade. **No** spaced-rep opener,
**no** forced interleaving, **no** exam framing during the story. Just be gripping.

### MNEMONIC REGISTRY — keep EXACT across episodes (already established on disk)

- **EM spectrum** (Radio Microwave Infrared Visible Ultraviolet X-ray Gamma, low→high freq):
  **"Raging Martians Invaded Venus Using X-ray Guns"** (M7-03). Ionising = top three U, X, G.
- **E=hf** (short wavelength → high energy): **"short wave, big punch"** (M7-09).
- **Four photoelectric observations:** **DENF** — no **D**elay, **E**nergy from frequency, **N**umber
  from intensity, threshold **F**requency. ⚠️ Coined in **M7-11 (Part 1)**; M7-12 recaps it as DENF.
  Use **DENF**, NOT the lesson plan's "DTIF".
- **Photoelectric K_max-vs-f graph:** **GIN** — **G**radient = Planck's constant (same for all metals
  → parallel lines), x-**I**ntercept = threshold frequency, y-i**N**tercept = **N**egative work function (M7-12).
- **Wien's law direction** (hotter → shorter peak wavelength): **"hot and blue, short and true"** —
  coin in **M7-10**, reuse after.
- **Spectral classes** O B A F G K M: **"Oh Be A Fine Girl, Kiss Me"** (M8-99).
- **Six quarks** (Up Down Charm Strange Top Bottom): **"Up Down, Cute Strange Top Bottoms"** (M8-99).
- **Four forces** (Strong EM Weak Gravity): **"Some Energetic Wizards Govern"** — gluon / photon /
  W and Z / **no carrier for gravity** (flag the exception) (M8-99).
- **Four reactor components** (Fuel Control-rods Moderator Coolant): **"Fast Cars Make Crashes"** —
  provide / absorb / slow / cool. ⚠️ moderator *slows*, control rods *absorb* (M8-10, M8-99).
- **Binding-energy-per-nucleon curve:** the **"iron throne"** — peak at iron-56; fusion climbs the
  left, fission the right, energy released moving *toward* iron (M8-09).
- **Atomic-model order** (Cathode Plum Gold Bohr Waves): **"Can Plum Give Birth, Wonderful"** (M8-99).
- **pp chain** (p+p→deuterium, +p→He-3, He-3+He-3→He-4): **"Pair, Plus, Produce"** (M8-99).
- **Element-origin tiers:** big bang (H, He, Li) → stellar fusion (up to iron) → supernova (beyond iron) (M8-99).

Spoken-text constants: Planck six point six three times ten to the minus thirty-four joule seconds;
c three times ten to the eight metres per second; electron charge one point six times ten to the minus
nineteen coulombs; one atomic mass unit ↔ nine hundred and thirty-one point five mega-electron-volts
(⚠️ the 931.5 already includes c-squared — multiply by 931.5 and stop).

## Step 4 — Save and commit

Write the two files into `content/<EPISODE-KEY>/` (`MODULE-LL-Title`, or `case_descriptive_title`).
**Format gate before committing:** `script.md` has valid frontmatter + no leaked symbols/equations/
markdown in the spoken body + only `NARRATOR:`/`QUESTION:` labels; `supplementary.md` has valid
frontmatter + `# Supplementary Materials` + balanced ```text fences + every script-referenced Listing present.

Then **one focused commit per episode**, straight to `main` (matching prior episodes), e.g.
`M7-10: add black-body radiation and Wien's law episode` or `M8-09: add supplementary.md`. A
pre-commit hook refreshes `manifest.json`; if not, run `python3 tools/generate_manifest.py` and
include it. End every commit message with the co-author trailer the harness specifies. Don't push unless asked.

## Step 5 — Report briefly, then stop

- Episode written (path) + kind + target duration; or the commit / manifest action taken.
- Teaching episode: dot-points covered, spaced-rep targets used, interleaving links, mnemonics
  reused vs coined, listings added. Case study: story told + which future topic cashes it in.
- STYLE.md §9 checklist: tick each; flag any you couldn't satisfy and why.
- State what the next iteration will pick up. If everything is done, print `PODCAST BUILD COMPLETE`.

Write the script, not a summary of one. If anything conflicts with STYLE.md, STYLE.md wins.

---

## Loop usage

Self-paced (nothing external to wait for — proceed promptly each iteration):

```
/loop Follow GENERATE_EPISODE_PROMPT.md: do exactly one unit of work, then stop.
```

Each iteration writes and commits one episode (or the next commit / the manifest); the loop
re-fires for the next and terminates itself when every expected episode exists and `git status`
is clean (`PODCAST BUILD COMPLETE`).
