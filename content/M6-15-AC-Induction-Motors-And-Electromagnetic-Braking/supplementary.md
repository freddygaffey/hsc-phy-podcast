---
title: "Supplementary Materials — AC Induction Motors and Electromagnetic Braking"
module: M6
lesson: "15"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. These listings are the read-along reference; the audio is self-contained and never depends on them, though it speaks the key results in words.

### Listing 1 — Synchronous speed and slip (worked)
```text
THE ROTATING FIELD'S SPEED (synchronous speed)
  Field rotates at the mains supply frequency.
  Australia:  f = 50 Hz
  Synchronous speed n_s = f = 50 rev s^-1
  In rpm:  n_s = 50 × 60 = 3000 rpm   (single pole-pair)
  (Use 50 Hz — that's Australia. 60 Hz is the US.)

SLIP — worked example
  Synchronous (field) speed   n_s     = 3000 rpm
  Actual rotor speed (loaded) n_rotor = 2880 rpm

  Slip speed = n_s − n_rotor = 3000 − 2880 = 120 rpm
  Fractional slip = (n_s − n_rotor) / n_s
                  = 120 / 3000
                  = 0.04 = 4 %

WHY SLIP IS NECESSARY
  At n_rotor = n_s exactly:
    relative speed = 0
      → ΔΦ/Δt = 0
        → induced EMF = 0
          → induced current = 0
            → force = 0  → torque = 0
  The non-zero 120 rpm of slip is precisely what keeps the flux
  changing and the torque flowing. No slip → no torque.

SELF-REGULATION
  More load → rotor slows → slip ↑ → ΔΦ/Δt ↑ → induced I ↑
            → force F = BIL ↑ → torque ↑  (rises to meet the load)
```

### Listing 2 — Faraday induction in one rotor bar (illustrative)
```text
WHY SLIP PRODUCES AN EMF — the core formula made quantitative

GIVEN (one rotor loop)
  Effective loop area   A  = 0.0030 m^2
  Stator field          B  = 0.40 T
  Field sweep changes flux from full (B·A) to 0
  in time               Δt = 5.0 × 10^-3 s
  Turns                 N  = 1

FLUX
  Φ_initial = B A = 0.40 × 0.0030 = 1.2 × 10^-3 Wb
  Φ_final   = 0 Wb
  ΔΦ        = Φ_final − Φ_initial = −1.2 × 10^-3 Wb
              (magnitude 1.2 × 10^-3 Wb)

INDUCED EMF (Faraday's law)
  ε = −N (ΔΦ / Δt)
    = −(1) × (−1.2 × 10^-3) / (5.0 × 10^-3)
    = 0.24 V

INTERPRETATION
  ~0.24 V is induced in the bar each field sweep. The end rings
  short-circuit the thick, low-resistance bars, so this small EMF
  drives a LARGE current I; that current in field B gives the
  force F = BIL that turns the rotor.
  Slip less (rotor catches up) → Δt longer → ΔΦ/Δt smaller
    → EMF and torque fall.  Faster slip → more torque.
```

### Listing 3 — The torque chain (the examinable cause-and-effect order)
```text
AC INDUCTION MOTOR — how induction makes torque
(write the links IN THIS ORDER for full marks)

  1. Three-phase stator coils (120° apart, currents 120° out of
     phase) → resultant field of CONSTANT magnitude whose
     DIRECTION rotates at supply frequency = ROTATING FIELD.

  2. Rotating field sweeps past stationary squirrel-cage bars
     → RELATIVE MOTION between field and bars.

  3. Relative motion → magnetic flux through the rotor loops
     CHANGES with time.

  4. FARADAY'S LAW:  ε = −N (ΔΦ/Δt)  → changing flux induces an
     EMF; end rings close the loop → large INDUCED (eddy) CURRENT
     in the bars.

  5. MOTOR EFFECT:  F = BIL  → each current-carrying bar in the
     stator field feels a FORCE.

  6. LENZ'S LAW (= conservation of energy): induced current
     opposes the change (the relative motion) → force drags the
     rotor IN THE DIRECTION OF FIELD ROTATION → TORQUE.

  7. SLIP: rotor must run slower than the field. At equal speed,
     no relative motion → no torque. Slip is essential.

MEMORY HOOK: "Rotating Round, Faraday's Force, Lenz Follows"
  + the rotor must SLIP.
  Barer: "Faraday makes it, Lenz aims it."
```

### Listing 4 — Equations used in this episode (symbols and SI units)
```text
MAGNETIC FLUX
  Φ = B A cos θ
    Φ = magnetic flux                       (weber, Wb)
    B = magnetic flux density / field       (tesla, T = Wb m^-2)
    A = area                                (m^2)
    θ = angle between B and the loop NORMAL (area vector)

FARADAY'S LAW OF INDUCTION
  ε = −N (ΔΦ / Δt)
    ε  = induced EMF                        (volt, V)
    N  = number of turns
    ΔΦ = change in flux = Φ_final − Φ_initial (Wb)
    Δt = time interval                      (s)
    The minus sign IS Lenz's law (EMF opposes the change).

MOTOR EFFECT (force on each current-carrying bar)
  F = BIL sin θ        (F = BIL when θ = 90°)
    F = force                               (newton, N)
    I = induced current in the bar          (ampere, A)
    L = length of bar in the field          (metre, m)

ELECTRICAL POWER CONSUMED BY THE MOTOR
  P = VI
    P = power  (watt, W)   V = terminal voltage (V)   I = stator current (A)

RESISTIVE (JOULE) HEATING — where lost KE goes in braking
  P = I^2 R              (W, A, ohm Ω)
```

### Listing 5 — Electromagnetic braking (the cause-and-effect chain)
```text
HOW A FORCE OPPOSING MOTION IS GENERATED

  1. A conductor (disc / plate / rail) moves through a magnetic
     field → RELATIVE MOTION between conductor and field.

  2. Relative motion → magnetic flux through the conductor CHANGES.

  3. FARADAY'S LAW → changing flux induces an EMF → drives
     circulating EDDY CURRENTS in the bulk metal.

  4. LENZ'S LAW (conservation of energy) → eddy currents flow so
     as to OPPOSE the change → they OPPOSE the motion → RETARDING
     (braking) FORCE.

  5. Kinetic energy → HEAT (P = I^2 R) in the conductor → object slows.

KEY MARK-EARNING FEATURE
  Braking force ∝ speed:
    fast → flux changes fast → big eddy currents → big force
    slow → small force
  So the brake is strong at speed, fades as the object slows, and
  approaches rest ASYMPTOTICALLY. It cannot give a sudden complete
  stop on its own — a friction brake finishes the job.

CONTACTLESS, WEAR-FREE, SMOOTH.
  Uses: trains / trams, roller coasters, fairground rides, gym
  and exercise equipment.
```

### Listing 6 — Motor vs generator, and AC induction vs DC motor
```text
ENERGY TRANSFORMATION (learn the exact wording)
  MOTOR:     electrical energy → rotational kinetic (mechanical)
  GENERATOR: mechanical kinetic energy → electrical energy
  Same device, opposite directions; both use the motor effect /
  electromagnetic induction. The exam tests the DIRECTION.

AC INDUCTION MOTOR vs DC MOTOR (use "whereas")
  DC motor: current FED to the rotor via brushes + split-ring
    commutator (commutator reverses current each half-turn).
  AC induction motor: rotor current is INDUCED by the rotating
    field — NO brushes, NO commutator, NO slip rings on the rotor.
  → Nothing rubs the rotor → no wear, no sparking, low maintenance
    → induction motor is more reliable; the most common motor made.

BRUSHLESS DC MOTOR (cross-link)
  Same induction-torque chain: torque from currents in the rotor
  produced WITHOUT brushes carrying rotor current (electronic
  commutation instead of mains three-phase).
```

### Listing 7 — Reference data
| Quantity | Symbol | Value / unit |
|---|---|---|
| Mains (supply) frequency, Australia | f | 50 Hz |
| Synchronous field speed (1 pole-pair) | n_s | 50 rev s^-1 = 3000 rpm |
| Magnetic flux | Φ | weber (Wb) |
| Magnetic flux density | B | tesla (T) = Wb m^-2 |
| Induced emf | ε | volt (V) |
| Induced current (in bars) | I | ampere (A) |
| Force per bar | F | newton (N) |
| Motor energy transform | — | electrical → rotational kinetic (mechanical) |
| Generator energy transform | — | mechanical kinetic → electrical |
