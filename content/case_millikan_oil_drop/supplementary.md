---
title: "Supplementary Materials — The Millikan Oil-Drop Experiment"
kind: case-study
script: script.md
---

# Supplementary Materials

### Listing 1 — The two governing equations of the balanced drop

```text
Stage 1 — Find the mass (field OFF, drop falls at terminal velocity v_g)
At terminal velocity:  weight = drag (Stokes' law)

(4/3) * pi * r^3 * (rho_oil - rho_air) * g  =  6 * pi * eta * r * v_g

Solve for the drop radius r:
r = sqrt( 9 * eta * v_g / ( 2 * g * (rho_oil - rho_air) ) )

Then the mass:
m = (4/3) * pi * r^3 * rho_oil

Stage 2 — Find the charge (field ON, forces balanced)
The drop is in equilibrium either held stationary OR moving at
constant (uniform) velocity. Either way the net force is zero:

Weight force (down):    F_g = m * g
Electric force (up):    F_E = E * q
For equilibrium:        F_g = F_E   ->   m * g = E * q

Electric field from the plates:
E = V / d

Therefore the charge on the drop:
q = m * g / E = m * g * d / V
```

### Listing 2 — Stokes' law small-drop correction (Millikan's refinement)

```text
For very small drops (radius near the mean free path of air ~70 nm),
plain Stokes' law overestimates the drag. Millikan corrected it:

F_drag_corrected = 6 * pi * eta * r * v * 1 / ( 1 + b / (p * r) )

where
b = empirical constant = 7.88 x 10^-3 Pa*m
p = air pressure
r = drop radius

This correction was Millikan's key methodological contribution
beyond the basic balanced-drop idea.
```

### Listing 3 — Demonstrating quantisation of charge

```text
Measure the charge q on many different drops, and on single drops
before and after ionising them with X-rays. Every value satisfies:

q = n * e        where n = 1, 2, 3, 4, ... (a whole number)

e = the fundamental (elementary) charge = charge on one electron

Key evidence:
- No drop ever carries a fractional multiple of e
- X-rays change a single drop's charge by exactly +/- e, +/- 2e, ...
- Conclusion: electric charge is QUANTISED
```

### Listing 4 — Key values and constants

| Quantity | Value |
|----------|-------|
| Millikan's 1913 published charge | 1.5924 x 10^-19 C |
| Modern fixed value (since 2019) | 1.602176634 x 10^-19 C |
| Discrepancy (cause: air viscosity) | ~0.6% |
| Plate separation d | ~16 mm = 0.016 m |
| Voltage across plates V | ~5000 V |
| Resulting field E = V/d | ~313 kV/m |
| Oil density rho_oil | 919.9 kg/m^3 |
| Air density rho_air | ~1.2 kg/m^3 |
| Air viscosity eta (~23 C) | 1.820 x 10^-5 kg/(m*s) |
| Typical drop radius | 1–3 micrometres |
| Typical drop mass | 10^-14 to 10^-13 kg |
| Drops in notebooks vs published | ~175 recorded, 58 published |
| Thomson's charge-to-mass ratio (measured) | ~1.8 x 10^11 C/kg |
| Thomson's charge-to-mass ratio (modern value) | 1.759 x 10^11 C/kg |
| Elementary (quantum of) charge e | 1.6 x 10^-19 C |
| Acceleration due to gravity g (used) | 9.8 m/s^2 |
| Nobel Prize in Physics | 1923 |

### Listing 5 — Worked example: charge on a suspended drop

```text
A charged oil drop of mass 6.8 x 10^-15 kg is held stationary
between two plates 16 mm apart with 5000 V across them.

Step 1 — Electric field between the plates:
E = V / d
E = 5000 / 0.016
E = 3.125 x 10^5 V/m

Step 2 — At balance, electric force = weight:
q * E = m * g
q = m * g / E
q = (6.8 x 10^-15 * 9.8) / (3.125 x 10^5)
q = (6.664 x 10^-14) / (3.125 x 10^5)
q = 2.13 x 10^-19 C

Step 3 — Number of excess electrons:
n = q / e = 2.13 x 10^-19 / 1.6 x 10^-19
n ~ 1.3  ->  rounds to 1 excess electron (within experimental error)

Note: real drops typically carried 5–30 electrons; the charge always
came out as a whole-number multiple n of e, never a fraction.
```

### Listing 6 — Consequences unlocked by knowing e

```text
1. Mass of the electron (using Thomson's charge-to-mass ratio):
   m_e = e / (e/m) = e / (1.759 x 10^11)
   m_e ~ 9.109 x 10^-31 kg

2. Avogadro constant (from Faraday's constant F = N_A * e):
   N_A = F / e   -> confirmed atomic theory, counts atoms per mole

3. The electronvolt energy unit:
   1 eV = 1.602 x 10^-19 J
```
