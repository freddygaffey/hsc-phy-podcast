---
title: "Supplementary Materials — The Motor Effect: Why a Wire Moves"
module: M6
lesson: "05"
script: script.md
---

# Supplementary Materials

Key equations, the mark-earning mechanism, worked numerical solutions, and reference data for this episode. Nothing here is spoken in the audio — it is the read-along reference.

### Listing 1 — The "explain why" mechanism: weak vs strong answer
```text
QUESTION (3–4 marks): "Use magnetic field interactions to explain WHY a
current-carrying conductor experiences a force in a magnetic field."

WEAK ANSWER (band 4 — scores almost nothing):
    "A force acts because F = BIL."
    → quotes a formula; describes no interaction; not an explanation.

STRONG ANSWER (full marks):
    1. The current-carrying conductor produces its OWN magnetic field —
       concentric circles around the wire (right-hand grip rule).
    2. This field is superimposed on the EXTERNAL uniform magnetic field.
    3. On one side the two fields REINFORCE   → stronger combined field.
       On the other side they partially CANCEL → weaker combined field.
    4. The conductor experiences a NET FORCE directed FROM the region of
       stronger field TOWARD the region of weaker field.

KEY DISTINCTION:
    F = BIL sin θ        → gives the MAGNITUDE (a calculation tool).
    Right-hand push rule → gives the DIRECTION (a memory aid only).
    Two-field interaction → is the EXPLANATION of WHY (the marks).
    NEVER answer "explain why" with the formula or the hand rule.
```

### Listing 2 — F = BIL sin θ: the three worked examples
```text
EQUATION:  F = B I L sin θ
  F = force on conductor            (newton, N)
  B = external field strength       (tesla, T = N A^-1 m^-1)
  I = current                       (ampere, A)
  L = length of conductor IN field  (metre, m)   [textbook uses lowercase l]
  θ = angle between WIRE and FIELD  (NOT wire-to-force)
  θ = 90°  → sin θ = 1 → MAXIMUM force (wire ⊥ field)
  θ = 0°   → sin θ = 0 → ZERO force    (wire ∥ field)

ALWAYS CONVERT TO SI FIRST: cm→m, mA→A, mT→T.

--- WORKED EXAMPLE A (all three angle cases) ---
Given: L = 8.0 cm = 8.0 × 10^-2 m
       I = 30 mA  = 3.0 × 10^-2 A
       B = 0.25 T

(a) θ = 90°:
    F = 0.25 × (3.0 × 10^-2) × (8.0 × 10^-2) × sin 90°
    F = 0.25 × (3.0 × 10^-2) × (8.0 × 10^-2) × 1
    F = 6.0 × 10^-4 N        (maximum force)

(b) θ = 30°:
    F = 6.0 × 10^-4 × sin 30°
    F = 6.0 × 10^-4 × 0.5
    F = 3.0 × 10^-4 N        (halved — sin dropped from 1 to 0.5)

(c) θ = 0° (parallel):
    F = 6.0 × 10^-4 × sin 0°
    F = 6.0 × 10^-4 × 0
    F = 0 N                  (no force)

--- WORKED EXAMPLE B ("maximum force" ⇒ θ = 90°, sin θ = 1) ---
Given: L = 5 cm = 5 × 10^-2 m, B = 2 × 10^-4 T, I = 200 mA = 0.200 A
    F = B I L = (2 × 10^-4)(0.200)(5 × 10^-2)
    F = 2 × 10^-6 N    (perpendicular to both I and B)
    Since F ∝ I and F ∝ B: doubling I OR B doubles the force.

--- WORKED EXAMPLE C (rearrange for B) ---
Given: L = 10 cm = 0.10 m, I = 15 A, F = 3.5 N (max ⇒ θ = 90°)
    F = B I L   →   B = F / (I L)
    B = 3.5 / (15 × 0.10)
    B = 3.5 / 1.5
    B = 2.3 T   (2.33 T)
```

### Listing 3 — Exam Question 3, full worked solution
```text
Q: L = 12 cm, I = 0.5 A, θ = 40° to a field B = 0.8 T. Find F.

Convert:  L = 12 cm = 0.12 m   (I and B already SI)

F = B I L sin θ
F = 0.8 × 0.5 × 0.12 × sin 40°
sin 40° ≈ 0.643
F = (0.8 × 0.5 × 0.12) × 0.643
F = 0.048 × 0.643
F ≈ 0.031 N   ≈ 3.1 × 10^-2 N

Marks: (1) correct equation  (2) substitution with SI units  (3) answer in N.
```

### Listing 4 — The four factors that change the force (F ∝ B I L sin θ)
| Change | Effect on F | Relationship | Reason (in terms of moving charges) |
|--------|-------------|--------------|--------------------------------------|
| Increase current I | increases | F ∝ I | more charges flow per second → more individual charge-forces summed |
| Increase length L in field | increases | F ∝ L | more current-carrying charges lie inside the field region |
| Increase field strength B | increases | F ∝ B | larger force on each moving charge |
| Increase angle θ (0°→90°) | increases as sin θ | F ∝ sin θ | larger perpendicular velocity component; max at 90°, zero at 0° |

### Listing 5 — Direction rules and conventions (do not mix them up)
| Tool / symbol | What it finds / means | How |
|---------------|------------------------|-----|
| Right-hand GRIP rule | direction of the wire's OWN circular field | thumb = conventional current, curled fingers = field direction |
| Right-hand PUSH (palm) rule | direction of the FORCE on the conductor | fingers = field B (N→S), thumb = current I, palm pushes = force F |
| Conventional current | direction positive charge would move | OPPOSITE to electron drift — reverse electron-flow before applying rules |
| Dot (·) in a circle | field / current OUT of the page | arrow-tip flying toward you |
| Cross (×) in a circle | field / current INTO the page | arrow-tail (fletching) flying away |
| Force direction | always ⊥ to BOTH I and B | perpendicular to the plane containing I and B |

### Listing 6 — Reference data and key terms
| Item | Value / definition |
|------|--------------------|
| Motor effect (definition) | the force experienced by a current-carrying conductor in an external magnetic field |
| Discovery (textbook) | attributed to Michael Faraday, 1821 |
| Tesla (unit of B) | 1 T = 1 N A^-1 m^-1 |
| Force equation | F = BIL sin θ (data sheet) |
| Max force | θ = 90° (wire ⊥ field), sin θ = 1, F = BIL |
| Zero force | θ = 0° or 180° (wire ∥ field), sin θ = 0 |
| Electron charge magnitude | 1.6 × 10^-19 C |
| Electron mass | 9.1 × 10^-31 kg |
| Permeability of free space μ₀ | 4π × 10^-7 N A^-2 (parallel-wire context only — background) |
| k = μ₀ / 2π | 2.0 × 10^-7 N A^-2 (parallel-wire context only — background) |
