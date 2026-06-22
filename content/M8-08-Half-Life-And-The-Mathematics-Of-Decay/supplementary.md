---
title: "Supplementary Materials — Half-Life and the Mathematics of Decay"
module: M8
lesson: "08"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it's the read-along reference.

### Listing 1 — The decay law and the decay-constant / half-life relationship
```text
Defining differential equation (conceptual root):
  dN/dt = −λN          rate of decay ∝ number of undecayed nuclei present

Integrates to the decay law (on the HSC data sheet):
  N_t = N₀ e^(−λt)
    N₀  = number of undecayed nuclei at t = 0
    N_t = number remaining at time t
    λ   = decay constant (probability of decay per nucleus per unit time), unit s⁻¹
    t   = elapsed time (same time unit as λ)
    e   ≈ 2.718

Activity follows the SAME exponential, since A = λN:
  R_t = R₀ e^(−λt)
    R = activity, unit becquerel (Bq) = 1 decay per second = 1 s⁻¹

Derive λ = ln2 / t½ by asking "when is N = ½N₀?":
  ½N₀ = N₀ e^(−λt½)
  ½   = e^(−λt½)
  ln(½) = −λt½
  −ln2  = −λt½
  λ = ln2 / t½   (data sheet),   equivalently   t½ = ln2 / λ ≈ 0.693 / λ
    ln2 = 0.6931

Fraction-remaining shortcut (whole/simple numbers of half-lives only):
  N_t / N₀ = (½)^(t / t½) = (½)ⁿ ,   n = t / t½ = number of half-lives
```

### Listing 2 — Worked example: amount remaining (iodine-123 tracer)
```text
Problem: 20 mg of iodine-123 (t½ = 13 h). How much remains after 24 h?
24 h is NOT a whole number of half-lives → use N_t = N₀ e^(−λt).

Step 1 — find λ FIRST (the law needs λ, not t½):
  λ = ln2 / t½ = 0.6931 / 13 h = 0.0533 h⁻¹   (unit per HOUR, because t½ in hours)

Step 2 — substitute into the decay law (keep t in hours to match λ):
  N_t = 20 × e^(−0.0533 × 24)
      = 20 × e^(−1.279)

Step 3 — evaluate:
  e^(−1.279) = 0.278
  N_t = 20 × 0.278 = 5.57 mg

Step 4 — sanity check with the shortcut:
  n = 24 / 13 = 1.846 half-lives
  (½)^1.846 = 0.278  →  20 × 0.278 = 5.57 mg  ✓  (textbook 5.56 mg)

Answer: ≈ 5.6 mg remains after 24 h.

Whole-number-of-half-lives versions (no calculator):
  After 26 h = 2 half-lives: 20 → 10 → 5 mg  (5 mg remains)
  Activity 8.0 MBq, t½ = 10.0 min, reach 1.0 MBq: 8→4→2→1 = 3 halvings = 30 min
```

### Listing 3 — Worked example: decay constant and half-life from a drop in activity
```text
Problem: activity falls from 600 counts/min to 100 counts/min in 6 hours.
Find the decay constant and the half-life.

Step 1 — activity follows the same exponential:
  100 = 600 × e^(−λ·6)

Step 2 — divide by 600:
  100/600 = 1/6 = 0.1667 = e^(−6λ)

Step 3 — take natural log of both sides:
  ln(0.1667) = −1.7918 = −6λ

Step 4 — solve for λ:
  λ = 1.7918 / 6 = 0.299 h⁻¹   (PER HOUR — t was in hours)

Step 5 — convert to half-life:
  t½ = ln2 / λ = 0.6931 / 0.299 = 2.32 h

Answer: λ ≈ 0.30 h⁻¹ (= 8.3 × 10⁻⁵ s⁻¹),  t½ ≈ 2.32 h

UNIT TRAP: λ here is per HOUR, not s⁻¹. A "per second" label would give a
sub-second half-life, contradicting a source still active after 6 hours.
Always keep λ and t in the same time unit.
```

### Listing 4 — Worked example: closing exam question 4 (activity 800 → 200 Bq in 12 h)
```text
Problem: activity falls from 800 Bq to 200 Bq in 12 hours.
Find the decay constant and the half-life.

  200 = 800 × e^(−λ·12)
  200/800 = 1/4 = e^(−12λ)
  ln(1/4) = −1.386 = −12λ
  λ = 1.386 / 12 = 0.116 h⁻¹      (per hour — t in hours)
  t½ = ln2 / λ = 0.6931 / 0.116 = 6.0 h

Check: 800 → 400 → 200 is 2 halvings; 12 h / 6 h = 2 half-lives.  ✓
Answer: λ ≈ 0.116 h⁻¹,  t½ = 6.0 h
```

### Listing 5 — Half-life and use of selected radioisotopes
| Radioisotope    | Half-life          | Emission (key)      | Typical use                                  |
|-----------------|--------------------|---------------------|----------------------------------------------|
| Technetium-99m  | ~6 hours           | gamma               | Most common medical diagnostic tracer        |
| Iodine-123      | 13 hours           | gamma               | Thyroid diagnostic tracer                    |
| Iodine-131      | 8.0 days           | beta + gamma        | Thyroid diagnosis and treatment              |
| Thallium-201    | ~73 days           | gamma (via EC)      | Imaging damaged heart tissue                 |
| Iridium-192     | 74 days            | gamma + beta        | Industrial: locating weaknesses/leaks in pipes |
| Cobalt-60       | 5.3 years          | gamma               | Long-lived gamma source / radiotherapy       |
| Sodium-24       | 15 hours           | beta + gamma        | Decay-graph example (100 g → 50 g at 15 h)   |
| Carbon-14       | 5730 years         | beta                | Radiocarbon dating                           |
| Americium-241   | 432 years          | alpha               | Smoke detectors                              |
| Uranium-238     | 4.5 × 10⁹ years    | alpha               | Very long half-life (≈ age of the Earth)     |
| Polonium-218    | 1.5 × 10⁻⁴ s       | alpha               | Very short half-life                         |

### Listing 6 — Diagnostic-tracer suitability: "GET OUT, GET CLEARED"
```text
Match the PROPERTY to the PURPOSE (the marking key).

GET OUT   — radiation type = GAMMA
  • Penetrating  → escapes the body to reach an external detector (gamma camera) → image
  • Weakly ionising → minimal damage to healthy tissue as it passes out
  Contrast: ALPHA is unsuitable — barely penetrating (absorbed inside, not detectable
  externally) AND strongly ionising (high, damaging internal dose).

GET CLEARED — half-life trade-off
  • Long enough  → administer, distribute to target organ, complete the scan
  • Short enough → decays/clears quickly afterwards → patient's total dose minimised
  Too long → over-irradiates patient;  too short → decays before scan completed.

Industry flips the half-life: a permanent gauge / pipe-leak source needs a LONGER half-life
(e.g. iridium-192 ~74 d, cobalt-60 ~5 yr) so it stays useful — same principle, opposite pull.
```

### Listing 7 — Scientists' contributions to radio-medicine
| Scientist            | Year / contribution                                                                 |
|----------------------|-------------------------------------------------------------------------------------|
| Henri Becquerel      | 1896 — discovered radioactivity (uranium salt fogged a wrapped photographic plate); SI unit of activity (becquerel) named after him |
| Marie & Pierre Curie | Isolated and identified new radioactive elements (polonium, radium); coined "radioactivity"; pioneered its study and medical use, opening the path to radiotherapy and diagnostic imaging |
