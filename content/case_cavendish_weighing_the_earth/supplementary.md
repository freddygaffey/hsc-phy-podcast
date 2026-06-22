---
title: "Supplementary Materials — The Cavendish Experiment — Weighing the Earth"
kind: case-study
script: script.md
---

# Supplementary Materials

### Listing 1 — From the twisting wire to big G (the torsion-balance method)

```text
SET-UP
  Horizontal rod of length L hangs from a thin wire at its midpoint.
  A small ball (mass m) sits at each end of the rod.
  A large ball (mass M) is brought close to each small ball.
  Centre-to-centre separation of a large/small pair = r.

STEP 1 — Find the wire's stiffness (torsion constant, kappa) by timing the swing.
  The hanging rod is a torsional oscillator with period T.
    T = 2 * pi * sqrt( I / kappa )
  Moment of inertia of two small balls on the rod (each at L/2 from the axis):
    I = 2 * m * (L/2)^2 = m * L^2 / 2
  Rearrange the period equation for the torsion constant:
    kappa = 4 * pi^2 * I / T^2
    kappa = 2 * pi^2 * m * L^2 / T^2
  (Timing the oscillation gives kappa WITHOUT applying any known force.)

STEP 2 — At rest, gravitational torque balances the wire's restoring torque.
  Gravitational force on each small ball:
    F = G * M * m / r^2
  This force acts at each end of the rod (lever arm L/2), on both ends:
    gravitational torque = 2 * F * (L/2) = F * L
  Restoring torque of the twisted wire (twist angle theta, in radians):
    wire torque = kappa * theta
  At equilibrium the two are equal:
    F * L = kappa * theta

STEP 3 — Solve for big G.
  Substitute F = G*M*m / r^2 and kappa = 2*pi^2*m*L^2 / T^2:
    (G * M * m / r^2) * L = (2 * pi^2 * m * L^2 / T^2) * theta
  The small-ball mass m cancels. Rearranging:
    G = 2 * pi^2 * L * r^2 * theta / ( M * T^2 )

  L     = rod length
  r     = centre-to-centre separation of a large/small ball pair
  theta = equilibrium twist angle (radians)
  M     = large-ball mass
  T     = oscillation period of the balance
```

### Listing 2 — Worked example: weighing the Earth from big G

```text
GOAL: find the mass of the Earth once big G is known.

At the Earth's surface, gravitational field strength is g.
The gravitational field strength of a planet (Newton's law with one unit mass) is:
    g = G * M_Earth / R_Earth^2
Note: g (N kg^-1) is numerically equal to the acceleration due to gravity (m s^-2).

Rearrange for the mass of the Earth:
    M_Earth = g * R_Earth^2 / G

SUBSTITUTE (modern values):
    g       = 9.81 N kg^-1
    R_Earth = 6.371 x 10^6 m
    G       = 6.674 x 10^-11 m^3 kg^-1 s^-2

    M_Earth = ( 9.81 * (6.371 x 10^6)^2 ) / ( 6.674 x 10^-11 )
    M_Earth = ( 9.81 * 4.059 x 10^13 ) / ( 6.674 x 10^-11 )
    M_Earth = ( 3.982 x 10^14 ) / ( 6.674 x 10^-11 )
    M_Earth = 5.97 x 10^24 kg

(Using the rounded HSC data-sheet values g = 9.8 N kg^-1, R = 6.371 x 10^6 m,
 G = 6.67 x 10^-11, this gives M_Earth = 5.96 x 10^24 kg, which the data sheet
 itself rounds to 6.0 x 10^24 kg.)

CROSS-CHECK via density:
    rho_Earth = M_Earth / ( (4/3) * pi * R_Earth^3 )
    rho_Earth = 5.97 x 10^24 / ( (4/3) * pi * (6.371 x 10^6)^3 )
    rho_Earth = 5.51 x 10^3 kg m^-3  =  5.51 g/cm^3
    (i.e. ~5.5 times the density of water — confirming a dense metallic core)
```

### Listing 3 — The apparatus (Cavendish, 1797–98)

| Component | Value |
|-----------|-------|
| Torsion rod (beam) length | 1.8 m (6 feet) |
| Small lead spheres (one each end) | 0.73 kg each, 51 mm (2 in) diameter |
| Large lead spheres (two) | 158 kg each, 300 mm (12 in) diameter |
| Centre-to-centre separation (large–small) | 0.225 m (8.85 in) |
| Housing case (mahogany) | ~1.98 m wide, sealed against air currents |
| Measured gravitational force per pair | ~1.7 x 10^-7 N (order of ~10^-7 N, a few hundred nN) |
| Oscillation period (initial wire) | ~15 minutes per full swing |
| Oscillation period (stiffened wire) | ~7.5 minutes per full swing |
| Number of trials | 17 |
| Read-out | telescopes through the shed wall; ropes/pulleys to move large spheres |

```text
NOTE on the force figure:
  A naive point-mass calculation, F = G*M*m / r^2, with M = 158 kg,
  m = 0.73 kg and r = 0.225 m gives F ~ 1.5 x 10^-7 N (~150 nN).
  The commonly quoted ~1.7 x 10^-7 N reflects the true geometry of the
  swinging rod and the fact that BOTH large spheres act on the beam at once.
  Either way the force is of order 10^-7 N — roughly the weight of a grain
  of fine sand — which is the point of the story: an astonishingly tiny force.
```

### Listing 4 — Key results, then and now

| Quantity | Cavendish (1798) | Modern accepted |
|----------|------------------|-----------------|
| Density of Earth (published) | 5.480 g/cm^3 | — |
| Density of Earth (Baily's 1821 correction) | 5.448 g/cm^3 | 5.514 g/cm^3 |
| Accuracy vs modern | within ~1.2% | — |
| Big G (implied) | ~6.74 x 10^-11 | 6.67430(15) x 10^-11 |
| Mass of Earth (derived) | ~5.9 x 10^24 kg | 5.97 x 10^24 kg |

Note: Cavendish's paper was titled *Experiments to Determine the Density of the Earth*. It contains no value for big G and does not use the symbol G — that framing came later (C.V. Boys, 1889). The symbol G entered common use around 1873.

### Listing 5 — Why big G is the least-precisely-known constant

| Constant | Relative uncertainty (approx.) |
|----------|--------------------------------|
| Speed of light, c | exact (defined) |
| Planck's constant, h | exact (defined since 2019 SI) |
| Fine structure constant | ~0.15 parts per million |
| Gravitational constant, G | ~22 parts per million |

```text
WHY G IS SO HARD:
  - Gravity is by far the weakest fundamental force.
  - There is NO way to shield against gravity (unlike electric/magnetic fields).
  - Lab measurements are perturbed by the masses of walls, the experimenter,
    groundwater, distant terrain — none of which can be switched off.
  - Since ~1990, high-precision experiments disagree with each other by far more
    than their stated error bars (up to ~0.05%), implying hidden systematic errors.
  - Determining G to high precision remains an open problem in metrology.
```

### Listing 6 — The relevant HSC equations (Module 5)

```text
Newton's law of universal gravitation (force between two masses):
    F = G * M * m / r^2
  - F is proportional to each mass; inverse-square in separation r.
  - r is measured centre-to-centre.

Gravitational field strength of a planet (force per unit mass):
    g = G * M / r^2
  - Independent of the test mass placed in the field.
  - Numerically, g (N kg^-1) = acceleration due to gravity (m s^-2).
  - At the surface r = R; at altitude h use r = R + h:
        g = G * M / (R + h)^2
  - A radial field approximates a UNIFORM field close to the surface
    (over a small region g is nearly constant in size and direction).

Mass of a planet from its surface field:
    M = g * R^2 / G

OFFICIAL HSC DATA-SHEET VALUES (2019 onwards):
    G        = 6.67 x 10^-11  N m^2 kg^-2   (= m^3 kg^-1 s^-2)
    M_Earth  = 6.0 x 10^24 kg
    R_Earth  = 6.371 x 10^6 m
    g (surface) = 9.8 m s^-2  (= 9.8 N kg^-1)
    density of water = 1.00 x 10^3 kg m^-3

(The Jacaranda textbook quotes the more precise M_Earth = 5.97 x 10^24 kg and
 R_Earth = 6.37 x 10^6 m; the data sheet rounds these for exam use.)
```
