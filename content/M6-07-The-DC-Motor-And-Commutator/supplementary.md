---
title: "Supplementary Materials — The DC Motor: Components, Function, and the Commutator's Role"
module: M6
lesson: "07"
script: script.md
---

# Supplementary Materials

Key equations, the marked-up model answer, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it's the read-along reference.

### Listing 1 — Model answer: "Explain the role of the split-ring commutator" (3–4 marks), broken into scoring points
```text
Q: Explain the role of the split-ring commutator in a simple DC motor. (3–4 marks)

WEAK ANSWER (~1 mark):
  "The commutator reverses the current."
  → States what it does, but no WHEN, no WHY, no link to torque/rotation.

STRONG ANSWER (full marks), mark by mark:

[Set-up: torque]   The rotor coil carries current in a magnetic field, so the
                   motor effect produces a force on the two coil sides
                   perpendicular to the field (F = nBIL). These opposite forces
                   on opposite sides of the axis form a couple → a torque
                   (τ = nBIA cos θ) that rotates the coil.

[The problem]      As the coil rotates toward the position where its plane is
                   perpendicular to B — the zero-torque position — torque falls
                   to zero; the coil's momentum carries it PAST this point. The
                   forces have NOT changed direction, so the torque would now
                   push the coil BACK → the coil would OSCILLATE about the
                   zero-torque position, not rotate.

[The mechanism]    The split-ring commutator is a metal ring split into two
                   insulated halves, each connected to one end of the coil,
                   rotating with the coil while stationary brushes maintain
                   contact. Just as the coil passes the zero-torque position,
                   the insulating gap aligns with the brushes (circuit briefly
                   broken); as rotation continues, each brush contacts the
                   OPPOSITE segment → current direction through the coil reverses.

[The result]       Reversing the current reverses the force on each side, so the
                   torque keeps acting in the SAME rotational direction.
                   → Reverses current every half-turn at the zero-torque point,
                     converting oscillation into CONTINUOUS one-way rotation.

RULE: every time you write "reverses the current", attach the WHEN
(every half-turn, at the zero-torque position) and the WHY
(so torque keeps acting one way → continuous rotation).
```

### Listing 2 — Worked example: torque on a coil (magnitude)
```text
Given:  n = 15 turns
        B = 7.6 mT = 7.6 × 10^-3 T
        I = 15 mA = 1.5 × 10^-2 A
        coil = 8.0 cm × 12.0 cm
        θ = 30°  (angle between the COIL PLANE and B → use cos θ)

Area:   A = 0.080 m × 0.120 m = 9.6 × 10^-3 m²

Equation:  τ = n B I A cos θ

Substitute and step through:
        15 × (7.6 × 10^-3)            = 0.114
        0.114 × (1.5 × 10^-2)         = 1.71 × 10^-3
        (1.71 × 10^-3) × (9.6 × 10^-3) = 1.6416 × 10^-5
        × cos 30° (= 0.8660)          = 1.422 × 10^-5

Answer:  τ ≈ 1.4 × 10^-5 N m
```

### Listing 3 — Right-hand push (palm) rule, and the rotation direction
```text
RIGHT-HAND PUSH (PALM) RULE — convention used here:
  Fingers  → magnetic field B   (from N pole to S pole)
  Thumb    → conventional current direction (flow of positive charge)
  Palm     → pushes in the direction of the FORCE on that conductor

Procedure for rotation direction:
  1. Pick ONE identified side of the coil.
  2. Note the current direction in that side and the field direction (N→S).
  3. Apply the push rule → read the force direction on that side.
  4. That force, offset from the axis, gives the rotation sense.

For the Listing 2 coil:
  Applying the push rule to the LEFT-HAND side → force rotates it ANTICLOCKWISE.

Result:  τ ≈ 1.4 × 10^-5 N m, rotating ANTICLOCKWISE.
  (In a real motor the commutator then reverses the current to keep it
   turning the same way.)
```

### Listing 4 — Worked example: maximum torque (exam Q5)
```text
Given:  n = 20 turns
        A = 5 × 10^-3 m²
        I = 2 A
        B = 0.1 T

Maximum torque ⇒ cos θ = 1 ⇒ θ = 0° ⇒ COIL PLANE PARALLEL TO B.

Equation (at maximum):  τ_max = n B I A

Substitute:
        20 × 0.1          = 2
        2 × 2             = 4
        4 × (5 × 10^-3)   = 2 × 10^-2

Answer:  τ_max = 2 × 10^-2 N m = 0.02 N m,
         occurring when the plane of the coil is PARALLEL to the field.
```

### Listing 5 — DC motor components and functions
| Component | Part of | Function (state this, not just the name) |
|-----------|---------|------------------------------------------|
| Rotor coil (armature coil) | Rotor | Carries the DC current; the conductor that feels the motor-effect force and rotates. Wound on the armature (soft-iron core) which concentrates the field. |
| Field magnets | Stator | Stationary permanent magnets or electromagnets; supply the external magnetic field (N→S) the coil sits in. |
| Brushes | Stationary | Graphite/carbon contacts (conduct + self-lubricate) that press on the rotating commutator to keep the spinning coil connected to the supply and stop the wires tangling. |
| Split-ring commutator | Rotor | Ring split into two insulated halves; reverses the coil current every half-turn at the zero-torque position so torque acts one way → continuous rotation. |

### Listing 6 — Key formulas and angle conventions
```text
Force on each active coil side (motor effect):
  F = B I L sin θ        (single conductor)
  F = n B I L sin θ      (n turns)
  θ = angle between the CONDUCTOR and B
  → F MAXIMUM at θ = 90° (conductor ⊥ B); ZERO at θ = 0° (conductor ∥ B)
  Units: F (N), B (T), I (A), L (m)

Torque on the coil:
  τ = n B I A cos θ
  θ = angle between the COIL PLANE and B
  → τ MAXIMUM at θ = 0° (plane ∥ B); ZERO at θ = 90° (plane ⊥ B)
  Units: τ (N m), A (m²)
  Equivalent foundation: τ = F d  (d = perpendicular distance / moment arm)

NOTE on the two angles:
  F uses sin (angle from the conductor);
  τ uses cos (angle from the coil plane).
  Same physics — different reference line. State which θ you mean each time.

Factors that increase torque (read straight off τ = nBIA):
  ↑ n  (more turns)        ↑ B  (stronger magnets / soft-iron core)
  ↑ I  (more current/EMF)  ↑ A  (larger coil area)
  + radial pole pieces (keep sides ⊥ B for longer → smoother torque)
  + multiple coils + multi-segment commutator (no dead-spot → higher average torque)
```

### Listing 7 — DC motor vs AC motor (the most-tested comparison)
| Feature | DC motor | AC motor (simple) |
|---------|----------|-------------------|
| Energy conversion | Electrical → rotational kinetic | Electrical → rotational kinetic |
| Supply current | One-directional (DC) | Alternating (reverses on its own) |
| Connection component | Split-ring commutator (split into 2 insulated halves) | Slip rings (continuous, unsplit) |
| Does it reverse coil current? | Yes — mechanically, every half-turn at the zero-torque point | No — the supply already reverses, so no mechanical reversal needed |
| Why that component | Reversal must be forced because DC flows one way | Slip rings only maintain continuous connection |
