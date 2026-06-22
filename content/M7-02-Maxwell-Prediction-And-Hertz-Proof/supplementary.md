---
title: "Supplementary Materials — Maxwell's Prediction and Hertz's Proof: Calculating and Measuring c"
module: M7
lesson: "02"
script: script.md
---

# Supplementary Materials

Key equations, derivations, worked numerical solutions, and reference data for this episode. Nothing here is spoken in the audio — it is the read-along reference.

### Listing 1 — Maxwell's speed of light, calculated from the two constants
```text
Equation:   c = 1 / sqrt(μ0 × ε0)

μ0 (permeability of free space) = 4π × 10^-7 = 1.2566 × 10^-6   (m kg C^-2 ; std H m^-1 / T m A^-1)
ε0 (permittivity of free space) = 8.854 × 10^-12               (C^2 s^2 kg^-1 m^-3 ; std F m^-1)

Step 1 — multiply the constants:
  μ0 × ε0 = (1.2566 × 10^-6) × (8.854 × 10^-12)
          = 1.1127 × 10^-17   (s^2 m^-2)

Step 2 — square root:
  sqrt(1.1127 × 10^-17) = 3.336 × 10^-9   (s m^-1)

Step 3 — reciprocal:
  c = 1 / (3.336 × 10^-9) = 2.998 × 10^8 m/s

Answer:  c ≈ 3.0 × 10^8 m/s  (exact accepted value 299 792 458 m/s)

Key point for the discussion mark: μ0 and ε0 are measured in electric and
magnetic experiments INDEPENDENT of light, yet predict the measured speed of
light → light is an electromagnetic wave.
```

### Listing 2 — Measuring c in the lab (microwave standing-wave method), worked example
```text
Method (required practical):
  transmitter → metal reflector → incident + reflected waves form a standing wave
  probe slid along the path locates nodes (minima) and antinodes (maxima)

Key relationship:  adjacent NODES are λ/2 apart   →   λ = 2 × (node spacing)
Speed:             v = f × λ

Worked values:
  f = 10.5 GHz = 1.05 × 10^10 Hz
  node spacing = 14.3 mm = 14.3 × 10^-3 m

Step 1 — wavelength:
  λ = 2 × 14.3 × 10^-3 = 2.86 × 10^-2 m

Step 2 — speed:
  v = f × λ = (1.05 × 10^10) × (2.86 × 10^-2) = 3.00 × 10^8 m/s

Step 3 — assess accuracy:
  % error = |3.00 × 10^8 − 2.998 × 10^8| / (2.998 × 10^8) × 100 ≈ 0.07%  (excellent)

Dominant error: node-location uncertainty (nodes are broad, shallow minima)
  → reduce by averaging over many node spacings.
Other errors: transmitter frequency drift; stray reflections; probe-position reading error.
Trap: forgetting the factor of 2 in λ = 2 × (node spacing) halves the computed speed.
```

### Listing 3 — Exam question 4, worked solution (microwave at 9.4 GHz)
```text
Given:  f = 9.4 × 10^9 Hz ;  adjacent node spacing = 16 mm = 16 × 10^-3 m

λ = 2 × (node spacing) = 2 × 16 × 10^-3 = 3.2 × 10^-2 m

v = f × λ = (9.4 × 10^9) × (3.2 × 10^-2) = 3.0 × 10^8 m/s

Main error: node-location uncertainty (broad minima) → average over many nodes.
```

### Listing 4 — Maxwell's four equations (qualitative, in story order)
| # | Name | What it states | Key constant |
|---|------|----------------|--------------|
| 1 | Gauss's law (electricity) | Electric charge produces an electric field; field lines start/end on charge | permittivity ε0 |
| 2 | Gauss's law (magnetism) | No magnetic monopoles; net magnetic flux through any closed surface = 0 | — |
| 3 | Faraday's law | A changing magnetic field induces an electric field | — |
| 4 | Ampère–Maxwell law | A current, or a changing electric field, induces a magnetic field | permeability μ0 |

Memory hook (this order): **G**auss's **G**lorious **F**ields **A**re **M**ine — Gauss(E), Gauss(M), Faraday, Ampère–Maxwell. Laws 3 + 4 are the self-propagating "leapfrog" that gives light.

### Listing 5 — Who did what: prediction vs verification (the marks-saving trap)
| Person | Date | Role | Did | Did NOT |
|--------|------|------|-----|---------|
| James Clerk Maxwell | 1864 (theory) | Theory / prediction | Unified E & M; predicted EM waves and their speed c = 1/√(μ0ε0) | Did not measure c; did not detect EM waves (died 1879) |
| Heinrich Hertz | 1886–1888 (experiment) | Experiment / verification | Produced, detected & measured EM waves; showed reflection, refraction, polarisation; speed = c | Did not predict the waves |

Mnemonic: **Maxwell predicts, Hertz proves.** Theory → experiment.

### Listing 6 — Hertz's apparatus and the chain of reasoning
```text
TRANSMITTER — spark-gap oscillator:
  induction coil → high oscillating voltage across gap between two spherical electrodes
  → sparks = ACCELERATING charges → radiate EM waves   (links to M7-01 production)

RECEIVER — loop antenna:
  wire loop with a tiny gap, NO power source, placed metres away
  → spark jumps its gap → an EM wave crossed the room, induced a current (Faraday)
  → first deliberate detection of EM waves (1886/87)

CONFIRMED same nature as light:
  Reflection (off metal sheet)
  Refraction (through pitch/wax prism)
  Polarisation (rotate loop: PARALLEL = max spark, PERPENDICULAR = no spark)  → transverse wave
  Speed measured via standing waves, v = f λ  → equals c   (confirms Maxwell)

Result: same nature as light, lower frequency = radio waves. Unit "hertz" named for him.
Forward irony (M7-11): UV from the spark gap caused the photoelectric effect — seed of
the particle model of light, found at the bench that proved light is a wave.
```

### Listing 7 — c as a defined standard (since 1983) and the metre/second
```text
Speed of light (since 1983): DEFINED exactly
  c = 299 792 458 m/s   (no uncertainty — not measured)

The second (caesium-133 atomic clock):
  1 s = duration of 9 192 631 770 oscillations of the Cs-133 transition

The metre (defined FROM c):
  1 m = distance light travels in vacuum in 1 / 299 792 458 s

Consequence (examinable): c cannot be "measured more accurately" — it is fixed by
definition. Better experiments now refine the METRE, not c.
```

### Listing 8 — Reference data: constants, values, dates
| Quantity | Symbol | Value | Notes |
|----------|--------|-------|-------|
| Speed of light (defined) | c | 299 792 458 m/s ≈ 3.0 × 10^8 m/s | exact since 1983 |
| Permittivity of free space | ε0 | 8.854 × 10^-12 | C^2 s^2 kg^-1 m^-3 (std F m^-1) — from electric experiments |
| Permeability of free space | μ0 | 4π × 10^-7 = 1.257 × 10^-6 | m kg C^-2 (std H m^-1, T m A^-1) — from magnetic experiments |
| Caesium-133 second | — | 9 192 631 770 oscillations | defines the second |
| Wave equation | c = f λ | — | f in Hz, λ in m, c in m/s |
| Node spacing | — | λ/2 | adjacent nodes; λ = 2 × spacing |
| Maxwell | — | 1831–1879 | predicted c, 1864; died before Hertz |
| Hertz | — | 1857–1894 | produced/detected/measured EM waves, 1886–88 |
| Fizeau (1849) | — | 313 000 km/s | spinning toothed wheel |
| Foucault (1862) | — | 298 000 km/s | rotating mirror |
| Michelson (early 1900s) | — | 2.99796 × 10^8 m/s | rotating 8-sided mirror |
