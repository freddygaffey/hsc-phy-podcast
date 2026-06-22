---
title: "Supplementary Materials — Torque on a Current Loop: Why the Motor Spins"
module: M6
lesson: "06"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it is the read-along reference.

### Listing 1 — Torque on a coil, worked example (τ = nBIA cos θ)
```text
τ = nBIA cos θ      (θ = angle between the field B and the PLANE of the coil)

Given:
n = 50 turns
A = 0.080 m × 0.050 m = 4.0 × 10^-3 m^2     (convert cm → m BEFORE substituting)
I = 2.0 A
B = 0.25 T

(a) Plane PARALLEL to field → θ = 0°, cos 0° = 1  (maximum torque)
τ = 50 × 0.25 × 2.0 × (4.0 × 10^-3) × 1
50 × 0.25 = 12.5
12.5 × 2.0 = 25
25 × (4.0 × 10^-3) = 0.10
τ = 0.10 N·m        (maximum torque)

(b) Plane at 60° to field → cos 60° = 0.50
τ = 0.10 × 0.50
τ = 0.050 N·m       (half the maximum)

(c) Plane PERPENDICULAR to field → θ = 90°, cos 90° = 0
τ = 0 N·m
Reason (earns the understanding mark): the forces are STILL B I L (not zero);
the torque is zero because they act along the axis → perpendicular distance = 0.

Unit note: torque is in newton metres (N·m), NEVER joules — even though
N·m and J are dimensionally identical.
```

### Listing 2 — First-principles cross-check (τ = Fd, the couple)
```text
Force on ONE active side (length L = 0.080 m), perpendicular to B (sin 90° = 1):
F = BIL = 0.25 × 2.0 × 0.080 = 0.040 N   (per turn)

The two active sides form a COUPLE.
At the plane-parallel position the lever arm = full coil width = 0.050 m.

Torque from the couple, one turn:
τ (1 turn) = F × width = 0.040 × 0.050 = 2.0 × 10^-3 N·m

For all n = 50 turns:
τ = 50 × 2.0 × 10^-3 = 0.10 N·m   ✓  (matches Listing 1 part a)

Insight: nBIA is just (force on a side) × (coil width) × (number of turns).
```

### Listing 3 — Torque vs coil orientation (reference)
| Position of coil | Angle θ (field-to-plane) | cos θ | Torque | Why |
|---|---|---|---|---|
| Plane PARALLEL to field | 0° | 1 | MAXIMUM = nBIA | Forces act at full perpendicular distance from axis |
| Plane at 60° to field | 60° | 0.5 | half of max | Lever arm reduced |
| Plane PERPENDICULAR to field (normal ∥ B) | 90° | 0 | ZERO | Forces act along/through the axis — no turning effect |

### Listing 4 — Exam question 3 worked solution (maximum torque)
```text
Given: n = 100, A = 2.0 × 10^-3 m^2, I = 1.5 A, B = 0.4 T
Maximum torque → plane parallel to field → θ = 0°, cos 0° = 1

τ = nBIA = 100 × 0.4 × 1.5 × (2.0 × 10^-3)
100 × 0.4 = 40
40 × 1.5 = 60
60 × (2.0 × 10^-3) = 0.12
τ = 0.12 N·m
```

### Listing 5 — The cos-vs-sin convention (the #1 mark-loser)
```text
SAME PHYSICS, two conventions for the angle θ — always check which the question gives:

Textbook / Surfing Physics convention (used in this episode):
  θ = angle between the field and the PLANE of the coil
  τ = nBIA cos θ
  Maximum torque when plane ∥ field  (θ = 0°)

NESA formula-sheet convention:
  θ = angle between the field and the NORMAL (area vector) of the coil
  τ = nBIA sin θ
  Maximum torque when normal ⊥ field

Why both are correct:
  plane-angle + normal-angle = 90°  (the two angles are complements)
  ⇒ cos(plane-angle) = sin(normal-angle)
  ⇒ both formulae trace the identical curve.

Rule: read which angle the diagram/wording defines, THEN choose cos or sin.
Do NOT blindly copy "cos" onto a normal-angle question, or "sin" onto a plane-angle one.
```

### Listing 6 — Underlying motor-effect force (F = BIL sin θ) and reference values
```text
F = BIL sin θ   (force on one straight current-carrying side)
F = force (N)
B = magnetic field strength / flux density (T)
I = current (A)
L = length of conductor in the field (m)
θ = angle between current direction and B  (F max at 90°, zero at 0°)
For the active sides of a coil: θ = 90°, sin θ = 1, so F = BIL.

Reference worked force example (Jacaranda Sample Problem 1):
L = 8.0 × 10^-2 m, I = 3.0 × 10^-2 A, B = 0.25 T
(a) θ = 90° (sin = 1):  F = 3.0×10^-2 × 8.0×10^-2 × 0.25 × 1 = 6.0 × 10^-4 N
(b) θ = 30° (sin = 0.5): F = 6.0×10^-4 × 0.5            = 3.0 × 10^-4 N
(c) θ = 0°  (sin = 0):   F = 0 N

General torque definition (slide 171 example):
τ = rF sin θ = 2 m × 5 N × sin 90° = 10 N·m
```
