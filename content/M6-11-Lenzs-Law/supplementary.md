---
title: "Supplementary Materials — Lenz's Law: Conservation of Energy in Disguise"
module: M6
lesson: "11"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it is the read-along reference.

### Listing 1 — Worked example: induced EMF (Faraday) and direction (Lenz)

```text
GIVEN — flat circular coil in a uniform field
  Number of turns      N  = 50
  Radius               r  = 0.10 m
  Plane ⟂ field        θ  = 0°   →  cos θ = 1   (field along the normal)
  Field falls          B₁ = 0.40 T  →  B₂ = 0 T
  Time interval        Δt = 0.20 s

STEP 1 — AREA OF THE COIL
  A = π r² = π (0.10)² = π (0.01)
  A = 3.14 × 10⁻² m²

STEP 2 — FLUX PER TURN (Φ = B A cos θ, cos θ = 1)
  Φ₁ = B₁ A = 0.40 × 3.14 × 10⁻² = 1.26 × 10⁻² Wb
  Φ₂ = B₂ A = 0 × 3.14 × 10⁻²    = 0 Wb
  ΔΦ = Φ₂ − Φ₁ = 0 − 1.26 × 10⁻² = −1.26 × 10⁻² Wb   (flux DECREASES)

STEP 3 — FARADAY'S LAW (magnitude — drop the minus sign)
  |ε| = N |ΔΦ / Δt|
  |ε| = 50 × (1.26 × 10⁻² / 0.20)
  |ε| = 50 × (6.28 × 10⁻²)
  |ε| = 3.14 V          ≈ 3.1 V

STEP 4 — LENZ'S LAW (direction, part b)
  Flux is decreasing → induced current OPPOSES the decrease
  → induced field points the SAME way as the original field
  → current flows so as to reinforce the original field direction
    (right-hand grip rule: thumb along original field, fingers = current)

ANSWER
  (a) |ε| ≈ 3.1 V
  (b) current reinforces the original field direction (opposing the decrease)

NOTE — the minus sign in ε = −N(ΔΦ/Δt) carries DIRECTION only.
Never substitute it into a magnitude calculation.
```

### Listing 2 — The conservation-of-energy argument (proof by contradiction)

```text
LENZ'S LAW (marker-preferred wording)
  An induced current always flows in the direction that creates a
  magnetic field OPPOSING THE CHANGE in flux that produced it.
  (Opposes the CHANGE — not the flux, not the magnet.)

WHY IT MUST OPPOSE — assume the opposite, then watch energy break:

  1. ASSUME the induced current REINFORCES the change.
     (N-pole approaches coil → coil's near face becomes a S-pole
      that ATTRACTS the magnet, instead of a N-pole that repels it.)

  2. Attractive force  →  magnet ACCELERATES toward the coil.

  3. Faster magnet     →  greater rate of change of flux (ΔΦ/Δt ↑).

  4. Faraday's law     →  larger induced EMF and current.

  5. Larger current    →  stronger coil field → stronger attraction.

  6. Stronger force    →  magnet accelerates MORE → loop runs away.

  7. Both KE (magnet) and electrical energy (coil) grow with
     NO external energy input.

  8. = a PERPETUAL MOTION MACHINE → violates conservation of energy
       → IMPOSSIBLE.

  9. CONCLUSION: the induced current must OPPOSE the change.
     → This is Lenz's law.

WHERE THE ENERGY REALLY COMES FROM (the positive side)
  Coil opposes the magnet's motion (repels on approach, attracts on
  withdrawal), so an external agent must do mechanical WORK to move it.

  Work (mechanical) → electrical energy (induced current) → heat (P = I²R)

  "Work, Watts, Warmth." Every joule of induced electrical energy is
  paid for by mechanical work. Energy is conserved at every stage.

THE THREE "SAME LAW" APPLICATIONS (preview)
  • Magnet falling through a tube/solenoid → opposing force, falls slowly  [M6-12]
  • Conductor plate moving into a field → braking force (EM braking)        [M6-12, M6-15]
  • Spinning motor rotor → back-EMF opposing the supply                     [M6-08]
```

### Listing 3 — Worked example: combined Faraday + Lenz (200-turn coil)

```text
GIVEN
  Number of turns   N  = 200
  Coil area         A  = 2 × 10⁻³ m²
  Plane ⟂ field     θ  = 0°  →  cos θ = 1
  Field falls       B₁ = 0.5 T  →  B₂ = 0.1 T
  Time interval     Δt = 0.10 s

FLUX PER TURN (Φ = B A cos θ)
  Φ₁ = 0.5 × 2 × 10⁻³ = 1.0 × 10⁻³ Wb
  Φ₂ = 0.1 × 2 × 10⁻³ = 0.2 × 10⁻³ Wb
  |ΔΦ| = (1.0 − 0.2) × 10⁻³ = 0.8 × 10⁻³ Wb

FARADAY'S LAW (magnitude)
  |ε| = N |ΔΦ / Δt|
  |ε| = 200 × (0.8 × 10⁻³ / 0.10)
  |ε| = 200 × (8 × 10⁻³)
  |ε| = 1.6 V

LENZ'S LAW (direction)
  Flux is DECREASING → induced current opposes the decrease
  → induced field points the SAME way as the original field
    (it acts to maintain/replace the disappearing flux)

ANSWER
  |ε| = 1.6 V; current flows to reinforce the original field direction.
```

### Listing 4 — Finding the induced-current direction (the 3-step procedure)

```text
"CHANGE, OPPOSE, GRIP"

STEP 1 — CHANGE: how is the flux through the loop changing?
  Increasing or decreasing, and in which direction does it point?

STEP 2 — OPPOSE: which way must the INDUCED field point to oppose
         that change?
  • Flux increasing → induced field points OPPOSITE to the external
    field (fight the increase).
  • Flux decreasing → induced field points the SAME way as the
    original field (replace the lost flux).

STEP 3 — GRIP: right-hand GRIP (curl) rule for a coil.
  Thumb → direction of the required induced field inside the coil.
  Curled fingers → direction of the induced (conventional) current.

WORKED DIRECTION CASES
  N-pole APPROACHING coil:  flux into coil increasing → near face must
    be a N-pole to repel → current ANTICLOCKWISE (viewed from magnet).
  N-pole WITHDRAWING:       flux decreasing → near face becomes a
    S-pole to attract → current reverses to CLOCKWISE.
  Ring pulled OUT of into-page field: into-page flux decreasing →
    induced current CLOCKWISE to maintain into-page flux; current
    STOPS once the ring fully exits the field.

WARNING — use the right-hand GRIP rule (field→current for a coil),
NOT the flat-hand/palm rule (force on a moving charge). Different rule.
```

### Listing 5 — Key terms, symbols and units for this episode

| Quantity / item | Symbol | Unit | Note |
|-----------------|--------|------|------|
| Induced EMF | ε (epsilon) | volt (V) | a voltage, NOT a force |
| Number of turns | N | (dimensionless) | integer |
| Magnetic flux | Φ (phi) | weber (Wb) | 1 Wb = 1 T·m² = 1 V·s |
| Magnetic field strength | B | tesla (T) | flux density |
| Loop area | A | square metre (m²) | |
| Angle in flux | θ (theta) | degrees / radians | between B and the NORMAL, not the plane |
| Time interval | Δt | second (s) | |
| Faraday's law (with Lenz sign) | ε = −N(ΔΦ/Δt) | V | minus sign = Lenz (direction only) |
| Flux | Φ = B A cos θ | Wb | max at θ = 0°, zero at θ = 90° |
| Resistive heating | P = I²R | watt (W) | energy destination |
| Lenz (person) | — | — | H. F. Lenz, 1804–1864, German |
