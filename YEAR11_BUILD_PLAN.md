# Year 11 Build Plan (M1–M4) + Quizzes

**Goal:** generate the four Year 11 teaching modules (lessons + supplementaries) and a `quiz.json` for every episode, by self-paced loop, running until **1 AM local time** then stopping (usage rollover).

**Source material (NEW):** `text book.pdf` = *Jacaranda Physics 11* (394 pp), extracted once to
`facts/extracted/textbook_jacaranda_physics11.txt` (read THIS, never the 36 MB PDF). Exact NESA
dot-points: `facts/extracted/docx_syllabus.md` → "Outcomes and content for Year 11".

**Authoring rules (unchanged, module-agnostic):** `STYLE.md`, `SUPPLEMENTARY.md`, `AUTHORING.md`.
Quiz format: `tools/QUIZ_STYLE_GUIDE.md` (10 Q's, exactly 4 options, zero-based `answer`, explanation).

---

## The clock / stop rule (important — sandbox clock is wrong)

The Bash `date` reads ~8 h behind real local time (sandbox offset), so DO NOT trust it.
**Real local time comes from the `ScheduleWakeup` tool result** (it echoes the real clock, e.g.
"Next wakeup scheduled for 23:14"). At launch, real local time ≈ **22:30 (23 Jun)**, deadline ≈
**01:00 (24 Jun)** → ~2.5 h budget. **Stop rule:** when a `ScheduleWakeup` result shows a time
at/after **01:00** (and before ~12:00), do NOT schedule again — print `YEAR 11 RUN PAUSED — 1 AM`.
This is a multi-session build; it resumes later from the same gap-detection.

---

## Module → textbook topic map (Jacaranda Physics 11)

| Module | Topics (grep `^TOPIC n ` in the extracted text) |
|--------|--------------------------------------------------|
| **M1 Kinematics** | T2 Motion in a straight line · T3 Motion in a plane |
| **M2 Dynamics** | T4 Forces · T5 Energy and work · T6 Momentum, energy and simple systems |
| **M3 Waves & Thermodynamics** | T7 Wave properties · T8 Wave behaviour · T9 Sound waves · T10 Ray model of light · T11 Thermodynamics |
| **M4 Electricity & Magnetism** | T12 Electrostatics · T13 Electric circuits · T14 Magnetism |

(Topic 1 "Learning to think like a physicist" = working-scientifically skills — NOT an episode.)

## Canonical episode set (gap-detection target)

```
M1: M1-01 Motion in a Straight Line · M1-02 Velocity-Time and Displacement Graphs ·
    M1-03 Equations of Uniformly Accelerated Motion · M1-04 Vectors and Motion in a Plane · M1-99 Review
M2: M2-01 Forces and Newton's Laws · M2-02 Friction, Inclined Planes and Net Force ·
    M2-03 Work, Energy and Power · M2-04 Momentum, Impulse and Collisions · M2-99 Review
M3: M3-01 Wave Properties and the Wave Equation · M3-02 Wave Behaviour (Reflection, Refraction,
    Diffraction, Superposition) · M3-03 Sound Waves, Resonance and Standing Waves ·
    M3-04 Ray Model of Light · M3-05 Thermodynamics: Temperature and Heat ·
    M3-06 Heat Transfer and Latent Heat · M3-99 Review
M4: M4-01 Electrostatics: Charge and Fields · M4-02 Electric Circuits: Ohm's Law and Power ·
    M4-03 Series and Parallel Circuits · M4-04 Magnetism and Magnetic Fields · M4-99 Review
```
22 episodes → folders `Mx-LL-Title-Case-With-Hyphens` (STYLE §8); reviews `Mx-99-Module-Review-…`.

---

## Phases (one unit of work per loop iteration, in priority order)

0. **Missing lesson plan** → write `TEACHING_LESSON_PLAN_Mx.md` for the first module lacking one
   (M1 done first by hand as the template; loop writes M2, M3, M4).
1. **Missing episode** → first expected episode (module→lesson order) lacking `script.md`/`supplementary.md`.
2. **Missing quiz** → first Year 11 episode that has both `.md` files but no `quiz.json` (10 Q's).
3. **Backfill quiz** (only if Year 11 fully done & time remains) → existing M6/M7/M8/case episode with no `quiz.json`.
4. **Done / 1 AM** → clean tree + `YEAR 11 BUILD COMPLETE` (or `… PAUSED — 1 AM`).

Driven by `GENERATE_YEAR11_PROMPT.md`. One focused commit per unit (pre-commit hook refreshes
`manifest.json`, which auto-sets `quizPath` when `quiz.json` exists). No `.m4a` audio (separate pipeline).

## Verification ("make sure it all works") — done before unattended run

- M1 lesson plan written. ✅ (`TEACHING_LESSON_PLAN_M1.md`)
- M1-01 episode: `script.md` (two-voice, no leaked symbols, ~4.5–6.5k words) + `supplementary.md`
  (listings, balanced fences) + `quiz.json` (valid JSON, 10 Q's, `answer` index in range).
- Manifest picks up the new `quizPath` automatically via the hook.

## Mnemonic registry (Year 11 — keep EXACT once coined; extend as episodes are written)

- Equations of motion (suvat): coin a stable hook in M1-03 and reuse in M1-99.
- Newton's three laws / vector addition / energy conservation / momentum conservation: hooks in M2.
- v = f λ, EM-free wave properties, Snell's law: hooks in M3. Heat-transfer trio (conduction/convection/radiation).
- Series-vs-parallel rules, right-hand rules for magnetic fields: hooks in M4.
- Carry Year-12 hooks where they connect forward (e.g. M4 fields → M6 motor effect).
