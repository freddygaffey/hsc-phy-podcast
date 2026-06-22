---
title: "Supplementary Materials — Charge-to-Mass, the Elementary Charge, and the Plum Pudding Model"
module: M8
lesson: "02"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it is the read-along reference.

### Listing 1 — Stage 1: the velocity selector (find the speed)
```text
Both E and B fields ON, forces opposed; beam adjusted until UNDEFLECTED.

Undeflected  ⇒  net force = 0  ⇒  electric force = magnetic force

    F_E = F_B
    qE  = qvB

q cancels (appears on both sides):

    E = vB
    v = E / B

Key point: q cancels, so the selected speed v is INDEPENDENT of the
charge AND the mass of the particle. (q cancels ≠ q is zero.)

Symbols/units:
    F_E, F_B = force (N)
    q = charge (C)
    E = electric field strength (N C⁻¹ = V m⁻¹)
    v = speed (m s⁻¹)
    B = magnetic flux density (T, tesla)
```

### Listing 2 — Stage 2: magnetic-only circular motion (find q/m)
```text
Electric field switched OFF; only B acts.
Magnetic force is ALWAYS perpendicular to v ⇒ does no work ⇒
acts as the centripetal force ⇒ beam follows a circular arc.

    magnetic force = centripetal force
    qvB = m v² / r

Cancel one factor of v and rearrange for q/m:

    qB = m v / r
    q/m = v / (B r)

Substitute v = E/B from Stage 1 to get the combined form:

    q/m = (E/B) / (B r)
    q/m = E / (B² r)

Symbols/units:
    m = mass (kg)
    r = radius of circular path (m)
    q/m = charge-to-mass ratio (C kg⁻¹)
```

### Listing 3 — Worked example: Thomson's q/m for the electron
```text
GIVEN (crossed-fields CRT):
    Undeflected with  E = 5.0 × 10³ N C⁻¹,  B = 2.0 × 10⁻² T
    With E off, circular arc radius  r = 7.1 × 10⁻⁵ m

STAGE 1 — speed:
    v = E / B
    v = (5.0 × 10³) / (2.0 × 10⁻²)
    v = 2.5 × 10⁵ m s⁻¹
    (charge cancelled — speed independent of q and m)

STAGE 2 — charge-to-mass ratio:
    q/m = v / (B r)
    q/m = (2.5 × 10⁵) / (2.0 × 10⁻² × 7.1 × 10⁻⁵)
    q/m = (2.5 × 10⁵) / (1.42 × 10⁻⁶)
    q/m ≈ 1.76 × 10¹¹ C kg⁻¹

INTERPRETATION:
    This is ~1800× the q/m of a hydrogen ion ⇒ electron mass ≈ 1/1800
    that of hydrogen ⇒ first sub-atomic particle ⇒ atom is divisible.
```

### Listing 4 — Magnetic force on an electron (supports Stage 2)
```text
GIVEN:
    q = 1.6 × 10⁻¹⁹ C
    v = 2.5 × 10⁴ m s⁻¹  (perpendicular to B, so sin θ = sin 90° = 1)
    B = 2.0 × 10⁻² T

    F = qvB sin θ
    F = (1.6 × 10⁻¹⁹)(2.5 × 10⁴)(2.0 × 10⁻²)(1)
    F = 8.0 × 10⁻¹⁷ N

The force stays perpendicular to v ⇒ path is CIRCULAR, speed unchanged
(magnetic force does no work; it changes direction, not speed).
```

### Listing 5 — Worked example: Millikan oil drop (charge + electron count)
```text
GIVEN:
    drop mass  m = 6.8 × 10⁻⁶ g
    plate separation  d = 3.5 mm = 3.5 × 10⁻³ m
    plate voltage  V = 110 V
    g = 9.8 m s⁻²,   e = 1.6 × 10⁻¹⁹ C

(a) FIELD STRENGTH:
    E = V / d
    E = 110 / (3.5 × 10⁻³)
    E ≈ 3.1 × 10⁴ V m⁻¹   (3.143 × 10⁴)

(b) CHARGE (suspended ⇒ qE = mg):
    convert mass: 6.8 × 10⁻⁶ g = 6.8 × 10⁻⁹ kg   ← grams → kg!
    q = mg / E
    q = (6.8 × 10⁻⁹ × 9.8) / (3.143 × 10⁴)
    q = (6.664 × 10⁻⁸) / (3.143 × 10⁴)
    q ≈ 2.1 × 10⁻¹² C

(c) NUMBER OF EXCESS ELECTRONS (q = n e):
    n = q / e
    n = (2.1 × 10⁻¹²) / (1.6 × 10⁻¹⁹)
    n ≈ 1.3 × 10⁷ electrons   (whole number ⇒ charge is quantised)
```

### Listing 6 — Combining Thomson and Millikan to get the electron mass
```text
Thomson gives the RATIO:   q/m = 1.76 × 10¹¹ C kg⁻¹
Millikan gives the CHARGE:  e   = 1.6 × 10⁻¹⁹ C

Electron mass = charge ÷ (charge-to-mass ratio):

    m = e ÷ (q/m)
    m = (1.6 × 10⁻¹⁹) / (1.76 × 10¹¹)
    m ≈ 9.1 × 10⁻³¹ kg

Neither experiment alone gives the mass; together they do.
Trap: Thomson = ratio only; Millikan = charge only.
```

### Listing 7 — Key values, constants and milestones
| Quantity / item | Value / fact |
|---|---|
| Electron charge-to-mass ratio (q/m) | 1.76 × 10¹¹ C kg⁻¹ (precise 1.759 × 10¹¹; ≈ 1.8 × 10¹¹) |
| Elementary charge (e) | 1.6 × 10⁻¹⁹ C (precise 1.602 × 10⁻¹⁹ C) |
| Electron mass | 9.1 × 10⁻³¹ kg |
| Proton / hydrogen-ion mass | 1.67 × 10⁻²⁷ kg |
| Mass ratio electron : hydrogen | electron ≈ 1/1800 of hydrogen (modern ≈ 1/1837) |
| Gravitational acceleration (g) | 9.8 m s⁻² (Millikan equilibrium) |
| J.J. Thomson | measured q/m in 1897; discovered the electron; plum pudding model ~1904 |
| Robert A. Millikan | oil-drop experiment ~1909 (refined ~1913); Nobel Prize 1923 |
| Velocity-selector condition | undeflected ⇒ qE = qvB ⇒ v = E/B (charge cancels) |
| Centripetal condition | qvB = mv²/r ⇒ q/m = v/(Br) ⇒ q/m = E/(B²r) |

### Listing 8 — Memory hooks
```text
WHO FOUND WHAT (the #1 lost mark):
    Thomson  → The ratio (q/m).      "Thomson Tangled them."
    Millikan → the Magnitude (e).    "Millikan Measured one."
    Mass of electron = combine both.

ORDER OF THE ATOMIC MODELS (P-N-L-W):
    Plum pudding  (Thomson)      ← we are here
    Nucleus       (Rutherford, gold foil)
    Levels        (Bohr energy levels)
    Waves         (Schrödinger / matter waves)
    Image: a plum pudding cracked open to a hard nucleus,
    organised into neat levels, dissolving into a blur of waves.

EVALUATE STRUCTURE (plum pudding):
    Strengths (electrons in, neutral atom, divisible atom)
    → Limitation (positive distribution untested)
    → Judgement (reasonable for the time; overturned by gold foil).
    Use contrast words: "but", "whereas", "in contrast".
```
