---
title: "Supplementary Materials — The Great Comparison: Fields, Forces and Paths"
module: M6
lesson: "03"
script: script.md
---

# Supplementary Materials

Key equations, derivations, the four-scenario comparison, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it is the read-along reference.

### Listing 1 — The same electron through an electric field, then a magnetic field (worked example)
```text
Constants:
  electron charge magnitude  q = 1.6 × 10^-19 C
  electron mass              m = 9.1 × 10^-31 kg

STAGE 1 — Electric field accelerates the electron (does work, changes speed)
An electron starts from rest, accelerated through V = 100 V (electron gun).

(a) Work done by the field = kinetic energy gained:
    W = qV = (1.6 × 10^-19)(100) = 1.6 × 10^-17 J

(b) Equate to kinetic energy and solve for speed:
    W = ½mv²
    v = √(2W / m)
    v = √[ 2(1.6 × 10^-17) / (9.1 × 10^-31) ]
    v = 5.9 × 10^6 m s^-1     (≈ 2% of the speed of light)

  → The E-field DID work (1.6 × 10^-17 J) and INCREASED the speed from 0.

STAGE 2 — That same electron enters a magnetic field (does no work, bends into a circle)
The electron (v = 5.9 × 10^6 m s^-1) enters a uniform field
B = 6.0 mT = 6.0 × 10^-3 T, perpendicular to its velocity.

    r = mv / (qB)
    r = (9.1 × 10^-31)(5.9 × 10^6) / [ (6.0 × 10^-3)(1.6 × 10^-19) ]
    r = 5.6 × 10^-3 m = 5.6 mm

  → The B-field does NO work — speed stays 5.9 × 10^6 m s^-1 —
    but the perpendicular force bends it into a circle of radius 5.6 mm.

CONTRAST: same electron, two fields.
  Electric field  → did work, changed speed, parabola if launched across the field.
  Magnetic field  → no work, speed unchanged, circle.
```

### Listing 2 — The four scenarios compared by axis (the structure of a band-6 answer)
| Comparison axis | Uniform gravity (projectile) | Satellite orbit (radial gravity) | Uniform electric field | Uniform magnetic field |
|---|---|---|---|---|
| Force law | F = mg | F = GMm/r² | F = qE | F = qvB sin θ |
| Force depends on | mass | mass and 1/r² | charge | charge AND speed |
| Acts on a stationary object? | Yes | Yes | Yes | No — motion required |
| Direction of force | along field (attractive, "down") | toward central body (attractive) | along field (+q) / opposite (−q): attract or repel | perpendicular to both v and B |
| Does the field do work? | Yes | No (circular) / Yes (elliptical) | Yes | No (F ⊥ v always) |
| Path projected across the field | parabola | circle / ellipse (orbit) | parabola | circle |

### Listing 3 — The key field equations, in symbols and units
```text
GRAVITATIONAL (uniform / surface):
  F = mg                F in N, m in kg, g in N kg^-1 (≡ m s^-2)
  g = GM/r²             field strength, N kg^-1

GRAVITATIONAL (orbital / radial):
  F_g = GMm/r²          attractive, toward central body; r = centre-to-centre (m)
  v = √(GM/r)           orbital speed (derived: F_g = F_c)
  F_c = mv²/r,  a_c = v²/r        centripetal force / acceleration

ELECTRIC (uniform field, parallel plates):
  E = V/d               field strength, N C^-1 (≡ V m^-1)
  F = qE                electric force, q in C
  a = qE/m              constant acceleration (from F = ma)
  W = qV = qEd          work done on charge as it moves ALONG the field, J
  K = ½mv²              kinetic energy gained, J
  across field: x = v_x t ;  along field: y = ½at², v_y = at  (the parabola)

MAGNETIC:
  F = qvB sin θ         θ = angle between v and B; max at 90°, zero if v ∥ B or v = 0
  B in tesla (T)
  magnetic force does ZERO work (F ⊥ v at all times)
```

### Listing 4 — Derivations of orbital speed and magnetic radius (equate to the centripetal force)
```text
ORBITAL SPEED — equate gravitational force to the centripetal force:
  GMm/r² = mv²/r
  GM/r   = v²
  v      = √(GM/r)
  → larger orbital radius r  ⇒  lower orbital speed and longer period.

MAGNETIC RADIUS — equate magnetic force to the centripetal force:
  qvB = mv²/r
  qB  = mv/r
  r   = mv/(qB)
  → larger mass m or speed v  ⇒  larger radius (heavier isotope, bigger arc).
  → larger charge q or field B ⇒  smaller radius (tighter curve).

THE UNIFYING POINT:
  In every scenario the stated force is the NET force, so F = ma applies to all four.
  The differences are entirely in (i) the force law and (ii) the direction of the
  force relative to v:
    force fixed in direction  → parabola, field does work
    force ⊥ to velocity       → circle,  field does no work
```

### Listing 5 — Reference values and constants
| Quantity | Value |
|---|---|
| Electron charge magnitude | 1.6 × 10^-19 C |
| Electron mass | 9.1 × 10^-31 kg |
| Proton mass | 1.67 × 10^-27 kg (≈ 1836 × electron) |
| Proton charge magnitude | 1.6 × 10^-19 C |
| Speed after 100 V acceleration (electron) | 5.9 × 10^6 m s^-1 |
| E-field for 100 V across 5.0 cm plates | E = V/d = 2000 V m^-1 |
| Universal gravitational constant G | 6.67 × 10^-11 N m² kg^-2 |
| g at Earth's surface | 9.8 N kg^-1 (≡ m s^-2) |
| Orbital speed, ~250 km altitude LEO | ≈ 7.75 × 10^3 m s^-1 (~27 900 km h^-1) |
