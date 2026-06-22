---
title: "Supplementary Materials — Charged Particles in Electric Fields: The Conceptual Picture"
module: M6
lesson: "01"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it's the read-along reference.

### Listing 1 — Field strength of a uniform field (E = V/d), worked
```text
Uniform field between parallel plates:
E = V / d

  E = electric field strength      (V m^-1, equivalently N C^-1)
  V = potential difference         (volts, V)
  d = plate separation             (metres, m)

Worked: V = 100 V, d = 5.0 cm = 5.0 × 10^-2 m

E = 100 / (5.0 × 10^-2)
E = 2000 V m^-1   (= 2000 N C^-1)

Unit check:  1 V m^-1 = 1 N C^-1   (the two units of E are identical)
Direction:   field points from the + plate to the − plate
```

### Listing 2 — Direction conventions and key constants
| Quantity / rule | Value or statement |
|---|---|
| Field line direction | From the + plate to the − plate |
| Force on a + charge | Along E (toward the − plate) |
| Force on a − charge (electron) | Opposite to E (toward the + plate) |
| Field defined by | Force per unit charge on a small + test charge |
| Electron charge | −1.6 × 10^-19 C (magnitude 1.602 × 10^-19 C) |
| Proton charge | +1.60 × 10^-19 C |
| Electron mass | 9.1 × 10^-31 kg |
| Proton mass | 1.67 × 10^-27 kg |
| Proton / electron mass ratio | ≈ 1836 (electron's acceleration ~1836× larger, opposite sign) |
| Units of E | N C^-1 = V m^-1 (identical) |
| Unit of V | volt = J C^-1 |
| Units of W, K | joule (J) |
| Path: fired across the field | Parabola (projectile-motion structure) |
| Path: released from rest / along the field | Straight-line uniform acceleration |

### Listing 3 — From force and work to E = V/d and v = √(2qV/m)
```text
Core relations:
  Force on a charge:        F = qE
  Newton's second law:      F = ma   →   a = F/m = qE/m
  Work through a p.d.:       W = qV
  Work as force × distance:  W = qEd   (d = distance moved along the field)
  Kinetic energy:            K = ½mv²

Show E = V/d falls out of the energy picture:
  qEd = qV          (equate the two expressions for W)
  cancel q:  Ed = V
  E = V / d                          ✓ (matches Listing 1)

Speed gained from rest through voltage V:
  W = qV  and  W = K = ½mv²
  qV = ½mv²
  v² = 2qV / m
  v = √(2qV / m)

Unit notes:
  1 V = 1 J C^-1     (a volt is joules per coulomb)
  so qV  →  (C)(J C^-1) = J  = energy  ✓
```

### Listing 4 — Worked Example A: electron gun (energy → speed)
```text
An electron, from rest, accelerated through V = 100 V.
  e  = 1.6 × 10^-19 C   (magnitude of electron charge)
  mₑ = 9.1 × 10^-31 kg

(a) Energy gained:
    W = qV = (1.6 × 10^-19)(100)
    W = 1.6 × 10^-17 J

(b) This work becomes kinetic energy:  W = ½mv²
    1.6 × 10^-17 = ½ (9.1 × 10^-31) v²
    v² = (2 × 1.6 × 10^-17) / (9.1 × 10^-31)
    v² = 3.516 × 10^13
    v  = 5.9 × 10^6 m s^-1

Sanity check: ≈ 5900 km s^-1 ≈ 2% of c → classical mechanics is fine.
Context: cathode (−, hot filament) emits electrons (thermionic emission);
the field accelerates them to the anode (+); a hole forms the beam (cathode ray).
```

### Listing 5 — Worked Example B: proton fired sideways (parabolic trajectory)
```text
Horizontal parallel plates, d = 5 cm = 0.05 m, V = 2.56 V, upper plate +.
Proton fired horizontally just below the top plate. Gravity ignored.
  mₚ = 1.67 × 10^-27 kg
  qₚ = +1.60 × 10^-19 C

(a) Field strength:
    E = V/d = 2.56 / 0.05 = 51.2 V m^-1   (directed downward, + → −)

(b) Force on proton (positive ⇒ force ALONG E, i.e. downward):
    F = qE = (1.60 × 10^-19)(51.2) = 8.192 × 10^-18 N
    a = F/m = (8.192 × 10^-18)/(1.67 × 10^-27) = 4.9 × 10^9 m s^-2 (down)

(c) Time to cross the gap (vertical: u = 0, s = ½at²):
    0.05 = ½ (4.9 × 10^9) t²
    t² = 0.10 / (4.9 × 10^9) = 2.04 × 10^-11
    t  = 4.5 × 10^-6 s   (4.5 μs)

(d) Vertical velocity gained:  v_vert = a t = (4.9 × 10^9)(4.5 × 10^-6)
    v_vert = 2.2 × 10^4 m s^-1 (downward)

(e) Horizontal velocity: UNCHANGED throughout (no horizontal force)
    = the injection speed.

(f) Resultant = constant horizontal + growing vertical  →  PARABOLA.
    Exit angle matches a gravitational projectile of the same horizontal speed.

Why ignore gravity here:
    electric force ≈ 8 × 10^-18 N;  weight = mₚg ≈ 1.6 × 10^-26 N.
    Electric force ~ 10^8 × larger → gravity negligible (justified).
```
