---
title: "Supplementary Materials — Charged Particles in Magnetic Fields: Circular Motion and the Cyclotron"
module: M6
lesson: "02"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it is the read-along reference. Reference figures and constants follow the NSW HSC Physics data sheet.

### Listing 1 — Magnetic force on a moving charge
```text
F = qv⊥B = qvB sin θ

F  = magnitude of the magnetic force        (newtons, N)
q  = magnitude of the charge                (coulombs, C)
v  = speed of the charge                    (metres per second, m s^-1)
B  = magnetic field strength (flux density) (teslas, T)
θ  = angle between the velocity v and the field B
v⊥ = component of velocity perpendicular to B = v sin θ

θ = 90°  (v perpendicular to B): sin θ = 1 → F = qvB   (MAXIMUM)
θ = 0° or 180° (v parallel to B): sin θ = 0 → F = 0     (no force)
v = 0  (charge at rest):                       F = 0    (no force)

Direction: perpendicular to BOTH v and B.
Right-hand push (palm) rule — for a POSITIVE charge:
  fingers → external field B (N to S)
  thumb   → velocity of positive charge (= conventional current)
  force   → straight out of the palm
For a NEGATIVE charge (e.g. an electron): reverse the result
  (or point the thumb opposite to the electron's velocity, or use the left hand).
```

### Listing 2 — Deriving r = mv/qB (equate magnetic force and centripetal force)
```text
Newton's second law, magnetic force the only force:
    F_net = ma          and        F_magnetic = qvB
=>  qvB = ma

The acceleration is centripetal:   a = v^2 / r
=>  qvB = m v^2 / r        ← THE KEY STEP: magnetic force PROVIDES the centripetal force

Cancel one factor of v from both sides:
    qB = m v / r

Rearrange for the radius:
    r = mv / (qB)

Behaviour:
    r ∝ m   (heavier  → larger circle)
    r ∝ v   (faster   → larger circle)
    r ∝ 1/q (more charge → tighter circle)
    r ∝ 1/B (stronger field → tighter circle)
```

### Listing 3 — Worked Example A: radius of an electron's path
```text
An electron at v = 5.9 × 10^6 m s^-1 enters B = 6.0 mT perpendicular to its motion.
Find the radius r.

Data:  m = 9.1 × 10^-31 kg,  q = 1.6 × 10^-19 C
Convert: 6.0 mT = 6.0 × 10^-3 T   ← millitesla-to-tesla conversion

r = mv / (qB)
r = (9.1 × 10^-31 × 5.9 × 10^6) / (1.6 × 10^-19 × 6.0 × 10^-3)

  numerator   = 5.369 × 10^-24
  denominator = 9.6   × 10^-22

r = 5.6 × 10^-3 m = 5.6 mm
```

### Listing 4 — Worked Example B: force, then radius
```text
Electrons at v = 1.2 × 10^6 m s^-1 enter B = 2.6 × 10^-3 T at right angles (θ = 90°).
(a) force on each electron   (b) radius of the path

(a)  θ = 90° → sin θ = 1, so F = qvB
     F = (1.6 × 10^-19)(1.2 × 10^6)(2.6 × 10^-3)
     F = 5.0 × 10^-16 N

(b)  r = mv / (qB)
     r = (9.1 × 10^-31 × 1.2 × 10^6) / (1.6 × 10^-19 × 2.6 × 10^-3)
       numerator   = 1.092 × 10^-24
       denominator = 4.16  × 10^-22
     r = 2.6 × 10^-3 m = 2.6 mm
```

### Listing 5 — Worked Example C: reverse problem, find the speed from the radius
```text
Find the speed of an electron moving in an arc of radius r = 5.00 mm in a field B = 5.00 mT.

Convert: r = 5.00 × 10^-3 m,  B = 5.00 × 10^-3 T

Rearrange r = mv/(qB)  →  v = rqB / m
v = (5.00 × 10^-3 × 1.6 × 10^-19 × 5.00 × 10^-3) / (9.1 × 10^-31)

  numerator   = 4.0 × 10^-24
  denominator = 9.1 × 10^-31

v ≈ 4.4 × 10^6 m s^-1
```

### Listing 6 — Cyclotron period: why the speed cancels (extension / Module 8 link)
```text
Period = circumference / speed:
    T = 2πr / v

Substitute r = mv / (qB):
    T = 2π (mv / (qB)) / v
    T = 2π m v / (qB v)
        ↑ the v cancels
    T = 2π m / (qB)

The period T does NOT depend on v or r — only on m, q and B.
(This is the cyclotron principle. NOTE: not an explicit M6 dot-point —
 the cyclotron is a Module 8 application; treat as insight, not a quoted M6 formula.)

Related forms:
    cyclotron frequency  f = 1/T = qB / (2π m)
    angular frequency    ω = qB / m
```

### Listing 7 — Worked Example D: proton period is independent of speed
```text
Proton: m = 1.67 × 10^-27 kg,  q = 1.6 × 10^-19 C,  in B = 1.5 T.
Find the period of its circular motion.

T = 2π m / (qB)
T = (2π × 1.67 × 10^-27) / (1.6 × 10^-19 × 1.5)

  numerator   = 1.049 × 10^-26
  denominator = 2.4   × 10^-19

T ≈ 4.4 × 10^-8 s   (≈ 44 nanoseconds, independent of the proton's speed)
```

### Listing 8 — Exam Question 4 worked solution: electron radius
```text
Electron at v = 3.0 × 10^7 m s^-1 enters B = 0.20 T at right angles. Find r.

r = mv / (qB)
r = (9.1 × 10^-31 × 3.0 × 10^7) / (1.6 × 10^-19 × 0.20)

  numerator   = 2.73 × 10^-23
  denominator = 3.2  × 10^-20

r ≈ 8.5 × 10^-4 m ≈ 0.85 mm
```

### Listing 9 — Reference data: particle masses, charges, and relative radius
| Particle           | Mass (kg)        | Charge magnitude (C) | r relative to electron (same v, B) |
|--------------------|------------------|----------------------|------------------------------------|
| Electron (β⁻)      | 9.1 × 10⁻³¹      | 1.6 × 10⁻¹⁹ (−e)     | 1 (tightest curve)                 |
| Proton             | 1.67 × 10⁻²⁷     | 1.6 × 10⁻¹⁹ (+e)     | ≈ 1836                             |
| Alpha (⁴₂He nucleus) | 6.64 × 10⁻²⁷   | 3.2 × 10⁻¹⁹ (+2e)    | ≈ 3650                             |

### Listing 10 — Electric field vs magnetic field on a moving charge (contrast for M6-03)
| Property                  | Electric field (M6-01)              | Magnetic field (M6-02)                          |
|---------------------------|-------------------------------------|-------------------------------------------------|
| Force law                 | F = qE                              | F = qvB sin θ                                   |
| Acts on a stationary charge? | Yes                              | No — requires motion (v = 0 → F = 0)            |
| Force direction           | Along the field (sign-dependent)    | Perpendicular to BOTH v and B                   |
| Does the force do work?   | Yes — changes speed and KE          | No — speed and KE constant, direction only      |
| Trajectory (projected across field) | Parabola                  | Circle (helix if v has a component along B)     |
| Energy relation           | W = qV = ½mv²                       | W = 0 always                                    |
