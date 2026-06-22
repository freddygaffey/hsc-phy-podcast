---
title: "Supplementary Materials — Electromagnetic Waves: Production, Propagation, and the One Constant Speed"
module: M7
lesson: "01"
script: script.md
---

# Supplementary Materials

Key equations, the production-and-propagation chain, worked numerical solutions, and reference data for this episode. Nothing here is spoken in the audio — it is the read-along reference.

### Listing 1 — Wave equation: frequency of 300 nm light (worked example)
```text
c = f λ          (speed of an EM wave = frequency × wavelength)

Want frequency, so rearrange:   f = c / λ

Given:
  λ = 3.00 × 10^-7 m   (300 nm, near-UV, just past the violet edge)
  c = 3.00 × 10^8 m s^-1   (speed of light in vacuum)

Substitute:
  f = (3.00 × 10^8) / (3.00 × 10^-7)
  f = 1.00 × 10^15 Hz

Photon-energy cross-check (E = hf, previews M7-09):
  h = 6.63 × 10^-34 J s
  E = (6.63 × 10^-34)(1.00 × 10^15)
  E = 6.63 × 10^-19 J     (energy of one such photon)

Point: a radio wave (low f, long λ) and a gamma ray (high f, short λ)
both satisfy c = f λ with the SAME c. Only f and λ trade off.
```

### Listing 2 — Band-6 model extended-response answer
```text
Q: "Describe how electromagnetic waves are produced and propagated,
    and explain why all electromagnetic waves travel at the same speed
    in a vacuum. Relate your answer to Maxwell's electromagnetic theory." (6 marks)

PRODUCTION
- An EM wave is produced by an ACCELERATING electric charge — e.g. electrons
  oscillating in a radio transmitter antenna, driven by an alternating current.
- A stationary charge → only a static electric field (no wave).
- A charge at constant velocity (steady DC) → only a steady magnetic field (no wave).
- ONLY an accelerating charge (velocity changing) radiates.

PROPAGATION (the self-regenerating chain)
- The oscillating charge produces a CHANGING ELECTRIC FIELD.
- Ampère–Maxwell law: a changing electric field induces a changing magnetic field
  (at right angles to it).
- Faraday's law: that changing magnetic field induces a changing electric field.
- The two fields CONTINUOUSLY REGENERATE ONE ANOTHER and propagate outward.
- It is a TRANSVERSE wave: E ⊥ B, and both ⊥ to the direction of travel.
- It is an oscillation of the FIELDS themselves → needs NO MEDIUM; the
  luminiferous aether was never found and is unnecessary → travels through vacuum.

CONSTANT SPEED (Maxwell)
- v = 1 / √(μ₀ ε₀): speed set only by the permittivity ε₀ and permeability μ₀
  of free space.
- These are FIXED constants of the vacuum → regeneration rate fixed → speed fixed.
- So EVERY EM wave travels at the same c ≈ 3.0 × 10^8 m s^-1 in a vacuum,
  regardless of frequency.
- Radio → microwave → infrared → visible → UV → X-ray → gamma differ only in
  frequency and wavelength, related by c = f λ.

WEAK ANSWER (for contrast — scores almost nothing):
  "EM waves are made by electricity and travel through space."
  (No accelerating charge, no Faraday/Ampère–Maxwell coupling, no transverse
   geometry, no reason for constant speed.)
```

### Listing 3 — The three tiers of charge motion (what radiates)
| Charge motion | Field produced | Radiates an EM wave? |
|---------------|----------------|----------------------|
| Stationary charge | Static (unchanging) electric field | No |
| Constant velocity (steady DC current) | Steady (unchanging) magnetic field | No |
| Accelerating / oscillating charge (AC) | Changing electric AND magnetic fields | Yes |

### Listing 4 — The propagation loop and key equations (in words and symbols)
```text
THE SELF-PROPAGATING LOOP  (memory hook: FAME)
  changing E field --(Ampère–Maxwell)--> changing B field
  changing B field --(Faraday's law)----> changing E field
  ... repeats, regenerating itself, forever, with no medium.
  FAME = Faraday→Electric,  Ampère–Maxwell→Magnetic.

WAVE-SPEED RELATION
  c = f λ
  c = speed in vacuum (m s^-1); f = frequency (Hz); λ = wavelength (m).
  c fixed ⇒ f and λ inversely related (higher f ⇒ shorter λ).

MAXWELL'S SPEED PREDICTION  (number is owned by M7-02)
  v = 1 / √(μ₀ ε₀)
  μ₀ = permeability of free space (how readily a B field forms in vacuum)
  ε₀ = permittivity of free space (how readily an E field forms in vacuum)
  Both are fixed vacuum constants ⇒ v is a fixed constant of the vacuum.

PHOTON-ENERGY PREVIEW  (owned by M7-09; flag only)
  E = hf  = hc/λ
  Higher f ⇒ higher-energy photon ⇒ ionising (UV, X-ray, gamma).

REFRACTIVE INDEX  (why light slows in a medium, NOT a change in c)
  n = c / v_medium     (light at c in vacuum; slowed in glass/water by
                        absorption and re-emission delay)
```

### Listing 5 — Reference data: constants and the EM spectrum
| Quantity | Symbol | Value |
|----------|--------|-------|
| Speed of light in vacuum | c | 3.0 × 10^8 m s^-1 (exact: 299 792 458 m s^-1) |
| Permittivity of free space | ε₀ | 8.854 × 10^-12 F m^-1 |
| Permeability of free space | μ₀ | 4π × 10^-7 ≈ 1.257 × 10^-6 T m A^-1 |
| Planck's constant (preview) | h | 6.63 × 10^-34 J s |
| Power-line AC frequency (radiates EM waves) | f | 50–60 Hz |
| Maxwell predicts (theory) | — | 1864 |
| Hertz verifies (experiment) | — | 1887 |

### Listing 6 — EM spectrum order (mnemonic) and ionising power
| Region | Order | Frequency / energy | Ionising? |
|--------|-------|--------------------|-----------|
| Radio | 1 (longest λ) | lowest | No |
| Microwave | 2 | low | No |
| Infrared | 3 | low | No |
| Visible | 4 | medium | No |
| Ultraviolet | 5 | high | Yes |
| X-ray | 6 | higher | Yes |
| Gamma | 7 (shortest λ) | highest | Yes |

Mnemonic (increasing frequency): **R**aging **M**artians **I**nvaded **V**enus **U**sing **X**-ray **G**uns — Radio, Microwave, Infrared, Visible, Ultraviolet, X-ray, Gamma.
