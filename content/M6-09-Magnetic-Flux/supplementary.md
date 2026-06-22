---
title: "Supplementary Materials — Magnetic Flux: What It Actually Means"
module: M6
lesson: "09"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it is the read-along reference.

### Listing 1 — The flux equation and three worked angle cases

```text
THE DEFINITION (HSC data sheet)

  Φ = B A cos θ

  Φ = magnetic flux                        (weber, Wb)
  B = magnetic field strength              (tesla, T)
  A = area of the loop / surface           (m^2)
  θ = angle between B and the AREA VECTOR (the normal to the loop)
      — NOT the angle between B and the plane of the loop

  Equivalent form:  Φ = B⊥ A,  where B⊥ = B cos θ
      (only the component of B perpendicular to the face threads the loop)

  Flux density:  B = Φ / A   →  field strength IS the flux per unit area
  Units:  1 Wb = 1 T·m^2 = 1 V·s ;   1 T = 1 Wb·m^-2


GIVEN (all three versions)
  radius        r = 8.0 cm = 0.080 m      (convert BEFORE squaring)
  field         B = 0.20 T
  area          A = π r^2 = π (0.080)^2
                  = π × 0.0064
                  = 0.020106... m^2       (keep full precision)


VERSION A — field straight through the loop (θ = 0°)
  cos 0° = 1
  Φ = B A cos θ = 0.20 × 0.020106 × 1
  Φ = 0.0040 Wb = 4.0 × 10^-3 Wb = 4.0 mWb     ← MAXIMUM flux


VERSION B — field at 60° to the area vector (θ = 60°)
  cos 60° = 0.5
  Φ = 0.20 × 0.020106 × 0.5
  Φ = 0.0020 Wb = 2.0 × 10^-3 Wb = 2.0 mWb     ← HALF of A
  Note: B and A are unchanged. The flux halves purely because
        the loop is tilted — fewer field lines thread it.


VERSION C — field lying in the plane of the loop (θ = 90°)
  cos 90° = 0
  Φ = 0.20 × 0.020106 × 0
  Φ = 0 Wb                                       ← ZERO flux
  No field lines pass through; they all skim across the face.
```

### Listing 2 — Flux vs angle (cos θ intuition), for max flux B·A = 4.0 mWb

| Angle θ (field to normal) | Orientation | cos θ | Flux Φ |
|---|---|---|---|
| 0° | field straight through loop face (plane ⊥ field) | 1.000 | 4.0 mWb (maximum) |
| 30° | tilted slightly | 0.866 | 3.5 mWb |
| 60° | tilted more | 0.500 | 2.0 mWb |
| 90° | field in plane of loop (plane ∥ field) | 0 | 0 mWb |

### Listing 3 — Rectangular loop flux (and the Faraday preview, NOT solved here)

```text
GIVEN
  loop dimensions  0.25 m × 0.30 m
  field            B = 0.66 T, perpendicular to loop (θ = 0°)

AREA
  A = length × width = 0.25 × 0.30 = 0.075 m^2

FLUX (θ = 0°, cos θ = 1)
  Φ = B A cos θ = 0.66 × 0.075 × 1
  Φ = 0.0495 Wb ≈ 0.05 Wb

PREVIEW ONLY — belongs to M6-10 (Faraday), do NOT solve in this episode:
  If this flux is removed over Δt = 2.0 s in an N = 1 loop,
  Faraday's law ε = −N (ΔΦ / Δt) would give |ε| = 0.0495 / 2.0 ≈ 0.025 V.
  Today's job is only step one: finding the flux Φ.
```

### Listing 4 — Exam worked solution: circular coil, two orientations

```text
GIVEN
  radius   r = 0.10 m
  field    B = 0.40 T

AREA
  A = π r^2 = π (0.10)^2 = π × 0.010 = 0.031416 m^2

(i) AREA VECTOR PARALLEL TO FIELD  (θ = 0°, cos θ = 1)
  Φ = B A cos θ = 0.40 × 0.031416 × 1
  Φ = 0.01257 Wb ≈ 0.013 Wb ≈ 13 mWb

(ii) AREA VECTOR AT 60° TO FIELD   (θ = 60°, cos θ = 0.5)
  Φ = 0.40 × 0.031416 × 0.5
  Φ = 0.00628 Wb ≈ 0.0063 Wb ≈ 6.3 mWb   (exactly half of (i))

MARK-EARNING POINTS
  • radius converted/kept in metres before squaring
  • θ measured from the AREA VECTOR (normal), so cos used correctly
  • both answers quoted in webers (Wb), not tesla
```
