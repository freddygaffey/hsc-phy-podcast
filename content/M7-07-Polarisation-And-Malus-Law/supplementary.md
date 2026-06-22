---
title: "Supplementary Materials — Polarisation and Malus's Law: The Plane of the Electric Field"
module: M7
lesson: "07"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. These listings are the read-along reference; the audio is self-contained and never depends on them, though it speaks the key results in words.

### Listing 1 — The two equations and the benchmark cosine-squared values
```text
TWO FILTERS, TWO RULES

FIRST FILTER (the POLARISER), acting on UNPOLARISED light:
  I = ½ I₀
    I  = intensity of emerging polarised light   (W m⁻²)
    I₀ = intensity of incident unpolarised light (W m⁻²)
  → Always one HALF. Independent of the filter's orientation.
  → No angle, no cosine in this step.

SECOND FILTER (the ANALYSER), acting on ALREADY-POLARISED light:
  I = I_max cos²θ          ← Malus's law (syllabus form)
    I     = transmitted intensity                       (W m⁻²)
    I_max = polarised intensity arriving at analyser     (W m⁻²)  (value at θ = 0°)
    θ     = angle between the analyser's transmission axis
            and the plane of polarisation of the incident light  (degrees)

WHY THE SQUARE (the key conceptual point):
  Transmitted field amplitude  E = E₀ cos θ      (resolving the vector)
  Intensity ∝ amplitude²       I ∝ E²
  ⇒ I = I_max cos²θ            (the cosine gets squared with the amplitude)
  Mnemonic: "Malus loves to square."

BENCHMARK VALUES (memorise — use to sanity-check answers):
  θ = 0°   →  cos²0°  = 1      →  ALL transmitted
  θ = 30°  →  cos²30° = 0.75   →  three-quarters transmitted
  θ = 45°  →  cos²45° = 0.5    →  HALF transmitted
  θ = 60°  →  cos²60° = 0.25   →  one-quarter transmitted
  θ = 90°  →  cos²90° = 0      →  NONE transmitted (crossed filters)
```

### Listing 2 — Worked example: three filters in series (forward direction)
```text
SETUP: unpolarised light I₀ → polariser → analyser (60° to polariser)
       → second analyser (30° to first analyser).
Find the intensity after each stage as a % of I₀.

(a) After the POLARISER  (unpolarised → polarised, the ½ step):
      I_a = ½ I₀
      I_a / I₀ = 0.5 = 50 %

(b) After the FIRST ANALYSER, 60° to the polariser  (Malus's law):
      I_b = I_a cos²(60°)
          = 0.5 I₀ × (0.5)²
          = 0.5 I₀ × 0.25
          = 0.125 I₀
      I_b / I₀ = 12.5 %

(c) After the SECOND ANALYSER, 30° to the FIRST analyser  (Malus's law):
      Use θ = 30° — the angle between ADJACENT filters, NOT 90° back to the polariser.
      I_c = I_b cos²(30°)
          = 0.125 I₀ × (0.8660)²
          = 0.125 I₀ × 0.75
          = 0.0938 I₀
      I_c / I₀ ≈ 9.4 %
      → Light DOES emerge, even though the first and last filters are crossed at 90°.
        The middle filter re-projects the polarisation onto a new plane (three-polariser result).

(d) REMOVE the middle analyser (polariser + final analyser only, crossed at 90°):
      I_d = I_a cos²(90°)
          = 0.5 I₀ × 0
          = 0
      I_d / I₀ = 0 %
      → With the middle filter gone, total extinction. The middle filter was the whole story.
```

### Listing 3 — Reverse problem: finding the angle (square-root FIRST)
```text
PROBLEM: Polarised light I_max passes through one analyser; the transmitted
         intensity is ⅛ I_max. Find the angle θ.

  I = I_max cos²θ
  ⅛ I_max = I_max cos²θ
  cos²θ = 0.125              ← divide (I_max cancels)
  cos θ = √0.125 = 0.3536    ← SQUARE-ROOT FIRST (do NOT inverse-cos 0.125)
  θ = cos⁻¹(0.3536) = 69.3°  ≈ 69°

METHOD:  divide → root → inverse-cosine.   ("Malus makes you root.")
TRAP:    skipping the root and taking cos⁻¹(0.125) gives ≈ 82.8°  — WRONG.
```

### Listing 4 — Exam Question 3, worked (polariser + analyser at 30°)
```text
Unpolarised light I₀ → polariser → analyser at 30°.  Find final I as % of I₀.

  After polariser (½ step):      I₁ = ½ I₀
  Through analyser (Malus):      I₂ = I₁ cos²(30°)
                                    = ½ I₀ × 0.75
                                    = 0.375 I₀
                                    = ⅜ I₀
  I₂ / I₀ = 37.5 %

Marks: (1) ½ for the first filter; (2) cos²θ (not cos θ) for the analyser;
       (3) correct final value 37.5 %.
```

### Listing 5 — Exam Question 5, worked (find θ given I = ¼ I_max)
```text
Plane-polarised light → analyser; transmitted intensity = ¼ of incident polarised intensity.
Find θ.

  ¼ I_max = I_max cos²θ
  cos²θ = 0.25
  cos θ = √0.25 = 0.5          ← square-root FIRST
  θ = cos⁻¹(0.5) = 60°

WHY A BARE COSINE FAILS:
  Intensity ∝ amplitude²; the analyser passes a field component ∝ cos θ,
  so intensity ∝ cos²θ. Using a bare cosine you'd solve cos θ = 0.25
  → θ ≈ 75.5°, which is WRONG (it ignores intensity ∝ amplitude²).
```

### Listing 6 — Key terms, names and contexts to get right
| Item | What to say in the exam |
|------|--------------------------|
| Plane of polarisation | Defined by the **electric field** (not the magnetic field) |
| Unpolarised light | Electric field oscillates in **all** planes perpendicular to propagation |
| Plane / linearly polarised | Electric field oscillates in **one** plane (synonyms) |
| Polariser | First filter: unpolarised → polarised, intensity → **½ I₀** |
| Analyser | Second filter on polarised light: obeys **I = I_max cos²θ** |
| Transmission axis | The single direction a filter lets the field component through |
| Why transverse | Only **transverse** waves can be polarised; longitudinal (e.g. sound) cannot |
| Huygens | Proposed light was **longitudinal** — corrected by polarisation |
| Malus | Étienne-Louis Malus; the cosine-**squared** law bears his name |
| Hertz | Polarised radio waves by **rotating the receiver loop** (same physics) |
| Sunglasses | **Vertical** transmission axis blocks horizontally-polarised glare off water |
| Three pillars (wave model) | **D**iffraction, **I**nterference, **P**olarisation — "DIP"; P is the transverse clincher |
| Intensity unit | watts per square metre (W m⁻²); angle in degrees |
