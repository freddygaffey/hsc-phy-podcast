---
title: "Supplementary Materials — Back-EMF: The Motor That Fights Itself"
module: M6
lesson: "08"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it is the read-along reference.

### Listing 1 — The load-bearing relationships of this episode

```text
WHERE BACK-EMF COMES FROM (production)

Magnetic flux through the coil:   Φ = B A cos θ
  Φ = magnetic flux            (weber, Wb)
  B = magnetic field strength  (tesla, T)
  A = coil area                (m^2)
  θ = angle between B and the coil's normal (area vector)

Rotating the coil sweeps θ → flux Φ changes continuously.

Faraday's law of induction:       ε = −N (ΔΦ / Δt)
  ε  = induced EMF, here the back-EMF (volt, V)
  N  = number of turns in the coil
  ΔΦ = change in flux            (Wb)
  Δt = time interval             (s)
  The minus sign IS Lenz's law: the EMF opposes the change.

Faster spin → larger ΔΦ/Δt → larger back-EMF.
Zero spin (start-up or stall) → ΔΦ/Δt = 0 → back-EMF = 0.


WHAT BACK-EMF DOES (effect on current) — the key equation

Net (effective) voltage driving current:
  V_net = V_supply − ε_back

Ohm's law on the armature (resistance R):
  I = V_net / R  =  (V_supply − ε_back) / R

  I        = current through the motor (ampere, A)
  V_supply = supply voltage            (volt, V)
  ε_back   = back-EMF                   (volt, V)
  R        = armature resistance        (ohm, Ω)

So: speed ↑  →  ε_back ↑  →  V_net ↓  →  I ↓


SUPPORTING RELATIONS
  Motor-effect force (why current → torque):  F = B I L sin θ
  Resistive (Joule) heating (why stall burns out):  P = I^2 R
```

### Listing 2 — Worked example: motor current at start-up vs normal running

```text
GIVEN
  Armature resistance   R        = 10 Ω
  Supply voltage        V_supply = 240 V
  Back-EMF (normal load) ε_back  = 232 V

(a) CURRENT AT START-UP
  Coil stationary → ε_back = 0
  V_net = V_supply − ε_back = 240 − 0 = 240 V
  I = V_net / R = 240 / 10
  I = 24 A          ← the start-up surge

(b) CURRENT AT NORMAL RUNNING SPEED
  ε_back = 232 V
  V_net = V_supply − ε_back = 240 − 232 = 8 V
  I = V_net / R = 8 / 10
  I = 0.8 A         ← small, efficient running current

INTERPRETATION
  Start-up current / running current = 24 / 0.8 = 30×
  The motor draws 30 times its running current at switch-on,
  because no back-EMF exists until the coil moves.
```

### Listing 3 — Worked example (other way round): find the back-EMF

```text
GIVEN — electric drill
  Armature resistance   R        = 10 Ω
  Supply voltage        V_supply = 240 V
  Running current       I        = 2.0 A

FIND THE BACK-EMF
  Net voltage when running = I × R = 2.0 × 10 = 20 V
  This V_net is V_supply − ε_back, so:
  ε_back = V_supply − V_net = 240 − 20
  ε_back = 220 V

BONUS — start-up current (ε_back = 0)
  I = V_supply / R = 240 / 10 = 24 A

WATCH THE TRAP
  I × R gives the NET voltage (20 V), not the supply.
  Subtract it FROM the supply to get the back-EMF.
```

### Listing 4 — Why a stalled motor burns out (the cause-and-effect chain)

```text
STALL = rotor held stationary by an excessive load

  speed = 0
    → ΔΦ/Δt = 0
      → back-EMF ε_back = 0
        → V_net = V_supply − 0 = full supply
          → I = V_supply / R = MAXIMUM (the start-up value)
            → and it is CONTINUOUS (the coil never speeds up)

Heating:  P = I^2 R
  Current is ~30× the running value → heating is ~30^2 = 900×
  Sustained heat cannot escape → insulation fails → motor burns out.

START-UP vs STALL — same physics, different duration
  Start-up: max current for a split second, then back-EMF chokes it.
  Stall:    max current forever, because the coil never moves.

MITIGATION at start-up: a SERIES STARTING RESISTOR limits the
surge, then is switched out once back-EMF builds.
```

### Listing 5 — Exam question worked solution: 5 Ω motor

```text
GIVEN
  R        = 5.0 Ω
  V_supply = 240 V
  ε_back (normal speed) = 237 V

START-UP (ε_back = 0)
  V_net = 240 V
  I = 240 / 5.0 = 48 A

NORMAL OPERATING SPEED
  V_net = V_supply − ε_back = 240 − 237 = 3 V
  I = 3 / 5.0 = 0.6 A

COMMENT
  48 A / 0.6 A = 80× larger at start-up.
  The surge exists because there is no back-EMF until the
  coil moves; it falls sharply once the motor speeds up and
  back-EMF builds, reducing the net voltage and the current.
```
