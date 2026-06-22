---
title: "Supplementary Materials — Transformers: Why AC and How They Work"
module: M6
lesson: "14"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it is the read-along reference.

### Listing 1 — Why AC, not DC: the Faraday chain
```text
Faraday's law (magnitude):   emf = N × (Δϕ / Δt)
  emf  = induced EMF, volts (V)
  N    = number of turns (dimensionless)
  Δϕ   = change in magnetic flux, weber (Wb)
  Δt   = time interval, seconds (s)
  (full law: emf = −N (Δϕ/Δt); minus sign = Lenz's law, opposition)

Magnetic flux:   ϕ = B A cos θ
  B = flux density, tesla (T) = Wb m^-2 ;  A = area (m^2) ;  θ = angle to normal

DC input  →  steady current  →  constant flux  →  Δϕ/Δt = 0
          →  no induced emf  →  NO sustained output
          (only a brief pulse at switch-on / switch-off, when ϕ momentarily changes)

AC input  →  reversing current  →  continuously changing flux  →  Δϕ/Δt ≠ 0
          →  continuous induced emf  →  AC output, at the SAME frequency

Conclusion: a transformer needs the continuously changing flux that ONLY AC supplies.
Mark-earning step: state explicitly that constant flux gives Δϕ/Δt = 0, so NO emf.
```

### Listing 2 — Worked example: electric-piano transformer (ideal)
```text
GIVEN
  Vp = 240 V        (primary voltage)
  Vs = 12.0 V       (secondary voltage)
  Ns = 30 turns     (secondary turns)
  Is = 500 mA = 0.500 A   (convert mA → A first)
  Treat as ideal.

(a) PRIMARY TURNS  — turns-ratio equation
  Vp / Vs = Np / Ns
  Np = Ns × (Vp / Vs) = 30 × (240 / 12.0) = 30 × 20
  Np = 600 turns        (Np > Ns ⇒ step-DOWN, consistent with 240 V → 12 V)

(b) PRIMARY CURRENT  — conservation of energy
  Vp Ip = Vs Is        →     Ip = Is × (Ns / Np)
  Ip = 0.500 × (30 / 600) = 0.500 × (1/20) = 0.025 A = 25 mA
  Check (inverse trade-off): V down ×20 (240→12); I up ×20 (25 mA→500 mA) ✓

(c) POWER OUTPUT
  Ps = Vs Is = 12.0 × 0.500 = 6.0 W
  Check power conserved: Pp = Vp Ip = 240 × 0.025 = 6.0 W = Ps ✓
```

### Listing 3 — Worked example: turns ratio from power (ideal)
```text
GIVEN
  Pp = 10 kW = 10 000 W      (power supplied to transformer)
  Vp = 1.0 kV = 1000 V       (primary voltage)
  Is = 0.50 A                (secondary current)
  Ideal ⇒ Ps = Pp = 10 000 W

PRIMARY CURRENT
  Ip = Pp / Vp = 10 000 / 1000 = 10 A

SECONDARY VOLTAGE
  Vs = Ps / Is = 10 000 / 0.50 = 20 000 V = 20 kV

TURNS RATIO  = voltage ratio
  Np : Ns = Vp : Vs = 1.0 kV : 20 kV = 1 : 20
  Vs > Vp ⇒ Ns > Np ⇒ step-UP transformer
```

### Listing 4 — Worked example: step-down, find Vs and Ip (exam Q3)
```text
GIVEN
  Np = 8000 turns ,  Ns = 200 turns
  Vp = 240 V (AC) ,  Is = 3 A ,  ideal

SECONDARY VOLTAGE  — turns ratio
  Vp / Vs = Np / Ns
  Vs = Vp × (Ns / Np) = 240 × (200 / 8000) = 240 × (1/40)
  Vs = 6 V                  (step-down: 240 V → 6 V)

PRIMARY CURRENT  — conservation of energy
  Vp Ip = Vs Is
  Ip = (Vs Is) / Vp = (6 × 3) / 240 = 18 / 240
  Ip = 0.075 A = 75 mA
  Check: V down ×40 (240→6); I up ×40 (75 mA→3 A) ✓
```

### Listing 5 — The transformer equations and quantities
| Relationship | Equation (words) | Holds for |
|---|---|---|
| Faraday's law | emf = N × (Δϕ/Δt) — induced emf = turns × rate of change of flux | always (the working principle) |
| Turns / voltage ratio | Vp / Vs = Np / Ns — voltage ratio = turns ratio | always (ideal core assumed) |
| Current ratio (inverse) | Is / Ip = Np / Ns — current goes the opposite way to voltage | ideal transformer |
| Power conservation | Vp Ip = Vs Is — power out = power in | IDEAL only (real: Vp Ip > Vs Is) |
| Power | P = V I, watts | always |
| Line loss (grid context) | P_loss = I² R — step V up → I down → loss falls as I² | transmission lines |

### Listing 6 — Step-up vs step-down at a glance
| Feature | Step-up | Step-down |
|---|---|---|
| Secondary turns Ns vs Np | Ns > Np (more on secondary) | Ns < Np (fewer on secondary) |
| Output voltage Vs vs Vp | Vs > Vp (voltage raised) | Vs < Vp (voltage lowered) |
| Output current Is vs Ip | Is < Ip (current lowered) | Is > Ip (current raised) |
| Frequency | unchanged (= input) | unchanged (= input) |
| Grid use | generator → transmission line | transmission line → homes |

### Listing 7 — Real-transformer losses: "real transformers FRET"
| Loss (FRET) | Mechanism | Reduced by |
|---|---|---|
| **F** — incomplete Flux linkage | Some primary flux leaks through the air instead of threading the secondary, so the secondary links less flux. | Wind coils tightly together on a closed/continuous (toroidal or rectangular) soft-iron core. |
| **R** — Resistive heating (copper / I²R loss) | Copper windings have resistance; current dissipates power as heat at rate I²R. | Use thicker, lower-resistance (high-conductivity) wire. |
| **E** — Eddy currents (in the IRON CORE) | Changing flux induces circulating currents in the conducting core (Faraday + Lenz); they heat the core via I²R. | Laminate the core (thin insulated iron layers cutting the loops); or use ferrites (poor electrical conductors). |

### Listing 8 — Trap table: pair each loss with the RIGHT fix
```text
CORRECT pairings (do not scramble these):
  incomplete flux linkage  →  closed, tightly-wound core
  eddy currents (in core)  →  laminated core / ferrites
  resistive coil heating   →  thicker, lower-resistance wire

COMMON ERRORS to avoid:
  ✗ "lamination reduces resistive heating in the coils"  (no — lamination = core, eddy currents)
  ✗ "thicker wire reduces eddy currents"                 (no — thicker wire = coil resistance)
  ✗ "eddy currents flow in the copper coils"             (no — they are induced in the IRON core)
  ✗ "a transformer changes the frequency"               (no — only voltage/current change)
  ✗ "Vp Ip = Vs Is for a real transformer"              (no — that is the IDEAL model; real: Vp Ip > Vs Is)
  ✗ "DC gives literally zero output ever"               (imprecise — no SUSTAINED output; brief pulse at switch-on/off)
```
