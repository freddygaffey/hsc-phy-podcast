---
title: "Supplementary Materials — Diffraction and Interference: Why the Double-Slit Pattern Forms"
module: M7
lesson: "05"
script: script.md
---

# Supplementary Materials

Key equations, the worked double-slit example, the model extended-response answer, and the reference values for this episode. Nothing here is spoken in the audio — it is the read-along reference.

### Listing 1 — Worked example: sodium light through a double slit
```text
GIVEN
  λ = 589 nm  = 589 × 10^-9 m      (sodium yellow, monochromatic)
  d = 0.100 mm = 1.0 × 10^-4 m     (slit separation)
  L = 1.50 m                        (slit-to-screen distance)

CONDITION FOR A BRIGHT FRINGE (maximum)
  d sin θ = mλ        m = 0, 1, 2, 3, …  (m = 0 is the central maximum)

(a) FIRST-ORDER MAXIMUM, m = 1 — angle and screen distance
  sin θ = mλ / d
        = (1 × 589 × 10^-9) / (1.0 × 10^-4)
        = 5.89 × 10^-3
  θ = sin^-1 (5.89 × 10^-3) = 0.337°

  Screen distance (small angle, x = L sin θ):
  x₁ = L sin θ = 1.50 × 5.89 × 10^-3
     = 8.8 × 10^-3 m = 8.8 mm

(b) THIRD-ORDER MAXIMUM, m = 3 — distance from centre
  Maxima are evenly spaced, so:
  x₃ = 3 × x₁ = 3 × 8.8 mm = 26.4 mm

  (Check via x = mλL/d:
   x₃ = (3 × 589×10^-9 × 1.50) / (1.0×10^-4) ≈ 26.5 mm  — rounding-consistent.)

ANSWERS
  (a) θ ≈ 0.337°,  x₁ ≈ 8.8 mm
  (b) x₃ ≈ 26.4 mm
```

### Listing 2 — Symbols, meanings and SI units
| Symbol | Meaning | SI unit |
|--------|---------|---------|
| d | slit separation (centre-to-centre distance between the two slits) | metre (m) |
| θ (theta) | angle from the central axis to the fringe | degree or radian (dimensionless) |
| m | order number of the fringe (m = 0 is the central bright fringe) | none (integer) |
| λ (lambda) | wavelength of the light | metre (m); 1 nm = 10^-9 m |
| x | distance on the screen from the central maximum to the m-th maximum | metre (m) |
| L | perpendicular distance from the slits to the screen | metre (m) |

### Listing 3 — The two interference conditions and the screen relation
```text
CONSTRUCTIVE INTERFERENCE — bright fringe (maximum)
  path difference = whole number of wavelengths
  d sin θ = mλ                m = 0, 1, 2, 3, …
  → waves arrive IN PHASE (crest meets crest) → reinforce → BRIGHT

DESTRUCTIVE INTERFERENCE — dark fringe (minimum)
  path difference = half-integer number of wavelengths
                    (½λ, 1½λ, 2½λ, … i.e. a whole number minus a half)
  d sin θ = (m − ½)λ          m = 1, 2, 3, …
  → waves arrive EXACTLY OUT OF PHASE (crest meets trough) → cancel → DARK

SMALL-ANGLE SCREEN RELATION (the practical workhorse)
  for small θ,  sin θ ≈ tan θ  →  sin θ ≈ mλ/d ≈ x/L
  →  x = mλL / d

MEMORY HOOK:  "Whole is bright, half is dark."
NOTE ON SYMBOLS: the data sheet uses m and d sin θ = mλ. Some textbooks
write the order as n and minima as (n − 0.5)λ — identical physics. Use the
data-sheet symbol m in the exam.
```

### Listing 4 — Model extended-response (5 marks)
```text
Q: Explain, in terms of interference, the formation of the bright and dark
   bands in a double-slit pattern, and account for why small slit gaps are used.

MODEL ANSWER
  • When monochromatic light passes through the two narrow, closely spaced
    slits, each slit DIFFRACTS the light — spreads it out — because the slit
    width is comparable to light's very small wavelength.
  • By HUYGENS'S PRINCIPLE each slit acts as a source of secondary wavelets;
    because both are lit by the same wavefront the two sources are COHERENT
    (same wavelength, constant phase relationship).
  • The two diffracted waves overlap on the screen and SUPERPOSE.
  • The pattern depends on the PATH DIFFERENCE — the difference in distance the
    light travels from each slit to a point on the screen.
  • Where the path difference is a WHOLE NUMBER of wavelengths, the waves arrive
    IN PHASE, crest reinforces crest → CONSTRUCTIVE interference → BRIGHT band.
  • Where the path difference is a WHOLE NUMBER PLUS A HALF, the waves arrive
    EXACTLY OUT OF PHASE, crest meets trough → DESTRUCTIVE interference → DARK band.
  • Small slit gaps are essential because diffraction (and hence the overlap
    that allows interference) is only significant when the gap is of the same
    order as the wavelength of light, which is only a few hundred nanometres. A
    large gap → negligible spreading → no overlap → no pattern.
  • The appearance of DARK bands — where light added to light gives darkness —
    cannot be explained by a particle model and is therefore strong evidence
    for the WAVE MODEL of light.
```

### Listing 5 — Key terms, names and reference values
| Item | Value / meaning |
|------|-----------------|
| Christiaan Huygens | Proposed Huygens's Principle: every point on a wavefront acts as a source of secondary circular wavelets; the new wavefront is their envelope. (Thought light was longitudinal — wrong.) |
| Thomas Young (1773–1829) | Performed the double-slit experiment (~1801); definitive quantitative evidence of light interference. |
| Monochromatic | Single wavelength (one pure colour). |
| Coherent | Same wavelength AND constant phase relationship. |
| Incoherent | Random phase relationship (e.g. two separate lamps) → no stable pattern. |
| Constructive interference | In phase → reinforcement → bright maximum. |
| Destructive interference | Exactly out of phase → cancellation → dark minimum (energy redistributed, not destroyed). |
| Path difference | Difference in path lengths from the two slits to a screen point. |
| Order number m | m = 0 central maximum, m = 1 first-order, m = 2 second-order, … |
| Visible wavelength range | ≈ 400 nm (violet) to 700 nm (red). |
| Sodium-lamp wavelength | 589 nm (yellow). |
| Speed of light c | 3.0 × 10^8 m s^-1 (data sheet); c = fλ. |
| White light through slits | Central maximum stays white (zero path difference for all λ); outer fringes smear into coloured spectra. |
| Unit conversions | 1 nm = 10^-9 m; 1 mm = 10^-3 m; 1 µm = 10^-6 m. |
