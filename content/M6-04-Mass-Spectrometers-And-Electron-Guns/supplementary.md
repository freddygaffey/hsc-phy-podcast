---
title: "Supplementary Materials — Mass Spectrometers and Electron Guns: Fields Applied"
module: M6
lesson: "04"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it is the read-along reference for the worked examples narrated in the script.

### Listing 1 — Electron gun: energy gained and exit speed (V = 100 V)

```text
An electron starts from rest and is accelerated through V = 100 V.
Constants:  m = 9.1 × 10^-31 kg,   q = 1.6 × 10^-19 C

(a) ENERGY GAINED — work done by the field becomes kinetic energy
W = qV
W = (1.6 × 10^-19)(100)
W = 1.6 × 10^-17 J          (this is also the KE gained)

(b) EXIT SPEED — all the work becomes kinetic energy (starts from rest)
qV = (1/2) m v^2
v  = sqrt( 2W / m )
v  = sqrt( (2 × 1.6 × 10^-17) / (9.1 × 10^-31) )
v  = sqrt( 3.516 × 10^13 )
v  = 5.9 × 10^6 m/s          (≈ 2% of the speed of light)

Equivalent single formula:  v = sqrt( 2qV / m )
```

### Listing 2 — Magnetic deflection: radius of the electron's path

```text
The 5.9 × 10^6 m/s electron enters a uniform magnetic field
B = 6.0 mT = 6.0 × 10^-3 T, perpendicular to its velocity.

The magnetic force supplies the centripetal force:
qvB = m v^2 / r
=> r = m v / (q B)

r = (9.1 × 10^-31 × 5.9 × 10^6) / (1.6 × 10^-19 × 6.0 × 10^-3)
r = (5.369 × 10^-24) / (9.6 × 10^-22)
r = 5.6 × 10^-3 m = 5.6 mm

Note: the speed is UNCHANGED by the magnetic field (it does no work);
the field only bends the path. Light particle => small radius.
```

### Listing 3 — Velocity selector: the pass-through condition

```text
Crossed (perpendicular) E and B fields. Two forces on a moving ion,
arranged to point in OPPOSITE directions:

  electric force   F_E = qE        (independent of speed)
  magnetic force   F_B = qvB       (increases with speed)

The ion passes straight through (zero net force) when the forces balance:
F_E = F_B
qE  = qvB

q cancels from both sides:
E = vB
=> v = E / B

Only this ONE speed passes. Faster ions: F_B > F_E, deflected one way.
Slower ions: F_E > F_B, deflected the other way — both are blocked.

Underlying law (full force in combined fields) — the Lorentz force:
F = qE + q v × B
The selector sets the qE term and the q v × B term equal and opposite.

KEY POINT: v = E/B contains no m and no q — the selector sorts by SPEED,
not by mass. It guarantees every ion exits at the same speed.
```

### Listing 4 — Full mass spectrometer: separating Ne-20 and Ne-22

```text
Singly-ionised neon, q = 1.6 × 10^-19 C, accelerated through V = 1000 V,
through a velocity selector, then into B = 0.50 T.
Masses:  Ne-20  m = 3.32 × 10^-26 kg ;  Ne-22  m = 3.65 × 10^-26 kg

STAGE A — Accelerate: speed after acceleration (use Ne-20)
qV = (1/2) m v^2
v  = sqrt( 2qV / m )
v  = sqrt( (2 × 1.6 × 10^-19 × 1000) / (3.32 × 10^-26) )
v  = sqrt( 9.64 × 10^9 )
v  = 9.8 × 10^4 m/s
(the velocity selector then ensures BOTH isotopes travel at this v)

STAGE D — Deflect: radius r = m v / (q B)

Ne-20:
r = (3.32 × 10^-26 × 9.8 × 10^4) / (1.6 × 10^-19 × 0.50)
r = (3.25 × 10^-21) / (8.0 × 10^-20)
r = 0.041 m ≈ 4.1 cm

Ne-22 (same q, same selected v, same B; only m is larger):
r = (3.65 × 10^-26 × 9.8 × 10^4) / (8.0 × 10^-20)
r = 0.045 m ≈ 4.5 cm

RESULT: Ne-22 lands ~4 mm further out than Ne-20.
Same q, same v, same B  =>  r ∝ m  =>  separation is by MASS alone.
Detector POSITION identifies the isotope; NUMBER of hits gives abundance.

CAVEAT — which model applies:
 • WITH a velocity selector (all ions same v = E/B):   r ∝ m
 • WITHOUT a selector (all ions same qV, so v depends on m):
     v = sqrt(2qV/m)  =>  r = sqrt(2mV/q)/B  =>  r ∝ sqrt(m/q)
The standard HSC velocity-selector spectrometer uses r ∝ m.
```

### Listing 5 — Exam question 2 worked (electron through 200 V)

```text
Electron from rest through V = 200 V. Find the final speed.
m = 9.1 × 10^-31 kg,  q = 1.6 × 10^-19 C

qV = (1/2) m v^2
v  = sqrt( 2qV / m )
v  = sqrt( (2 × 1.6 × 10^-19 × 200) / (9.1 × 10^-31) )
v  = sqrt( (6.4 × 10^-17) / (9.1 × 10^-31) )
v  = sqrt( 7.03 × 10^13 )
v  = 8.4 × 10^6 m/s

Check: doubling V (100 V -> 200 V) multiplies v by sqrt(2),
since v ∝ sqrt(V).  5.9 × 10^6 × sqrt(2) ≈ 8.4 × 10^6 m/s.  ✓
```

### Listing 6 — Equations used in this episode (HSC formula sheet)

```text
uniform field strength (parallel plates):  E = V / d
electric force on a charge:                 F = qE
Newton's second law (gun acceleration):     F = ma
work done by the field:                     W = qV   (also W = qEd)
kinetic energy:                             K = (1/2) m v^2
energy balance (accelerated from rest):     qV = (1/2) m v^2  =>  v = sqrt(2qV/m)
magnetic force on a moving charge:          F = qvB = qvB sin(theta)   (max at theta = 90°)
velocity-selector pass speed:               v = E / B   (from qE = qvB)
magnetic force = centripetal force:         qvB = m v^2 / r
radius of circular path:                    r = m v / (q B)   =>   m = r q B / v
Lorentz force (combined fields):            F = qE + q v × B
```

### Listing 7 — Key constants and particle data

| Quantity | Symbol | Value | Note |
|----------|--------|-------|------|
| Elementary charge | e | 1.6 × 10^-19 C | electron charge = −e; use magnitude in qV and r |
| Electron mass | m_e | 9.1 × 10^-31 kg | ~1/1836 of a proton |
| Proton mass | m_p | 1.67 × 10^-27 kg | ~1836× the electron → much larger radius |
| Alpha particle charge | — | +3.2 × 10^-19 C (= +2e) | doubly ionised helium nucleus |
| Alpha particle mass | — | ≈ 6.64 × 10^-27 kg | ≈ 4 × proton mass |
| Neon-20 mass | — | 3.32 × 10^-26 kg | lighter isotope, tighter radius |
| Neon-22 mass | — | 3.65 × 10^-26 kg | heavier isotope, wider radius |
| Reference: 100 V electron gun exit speed | — | 5.9 × 10^6 m/s | ≈ 2% of c |
| Reference: that electron in 6.0 mT | r | 5.6 mm | from r = mv/(qB) |

### Listing 8 — Field roles and the three-stage (ASD) summary

```text
THE ONE-LINE SPINE
  Electric field  -> changes SPEED / energy; DOES work.
  Magnetic field  -> changes DIRECTION only; does NO work (speed constant).

ELECTRON GUN (one field)
  thermionic emission  -> E field accelerates  ->  qV = (1/2)mv^2
  Function: a beam of electrons at a known, tunable speed (set by V).

MASS SPECTROMETER — mnemonic "ASD" (Accelerate, Select, Deflect)
  A  Accelerate   electric field    qV = (1/2)mv^2     (gives the ions speed)
  S  Select       crossed E and B   v = E/B            (one speed passes; not mass)
  D  Deflect      magnetic field    r = m v / (q B)    (r ∝ m: heavier = wider)
  Readout: detector POSITION = mass;  NUMBER of hits = isotopic abundance.
```
