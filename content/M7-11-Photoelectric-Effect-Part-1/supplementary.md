---
title: "Supplementary Materials — The Photoelectric Effect, Part 1: The Observations That Broke the Wave Model"
module: M7
lesson: "11"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it is the read-along reference. Symbols: K_max = maximum kinetic energy of a photoelectron; V₀ = stopping voltage; e = electron charge; f = frequency; f₀ = threshold frequency. Note: this is Part 1 — the resolving equation K_max = hf − φ is developed in M7-12.

### Listing 1 — The photoelectric apparatus and the stopping voltage
```text
SETUP (evacuated glass tube):
  • Cathode / emitter  — clean metal surface; light enters a window and strikes it
  • Collector          — second electrode facing the emitter across the tube
  • Ejected electrons (PHOTOELECTRONS) cross the gap → small PHOTOCURRENT (ammeter)
  • Vacuum so electrons travel freely (no collisions with air)

MEASURING ENERGY — the stopping voltage V₀:
  • Apply a REVERSE (retarding) voltage: collector made negative to repel electrons
  • Increase it until even the FASTEST electron is turned back → photocurrent = 0
  • That voltage is the STOPPING VOLTAGE V₀

Energy bookkeeping (cash-in of M6-01, charged particle through a potential difference):
  K_max = e V₀
    K_max = maximum kinetic energy of the photoelectrons (J)
    e     = electron charge = 1.6 × 10^-19 C
    V₀    = stopping voltage (V)
  → measure V₀, and you have measured K_max.
```

### Listing 2 — The four observations: DENF
| Hook | Observation | What is seen |
|------|-------------|--------------|
| **D** | No time **D**elay | Electrons emitted essentially instantly, even for very faint light |
| **E** | **E**nergy from frequency | Max kinetic energy depends on the **frequency** (colour) only — not on brightness |
| **N** | **N**umber from intensity | Brighter light (same colour) → **more electrons per second** (bigger photocurrent), same energy each |
| **F** | Threshold **F**requency f₀ | Below a metal-specific cut-off frequency, **no** electrons emitted — at any intensity, any duration |

```text
Mnemonic: DENF — no Delay, Energy from frequency, Number from intensity, threshold Frequency.
Carry it into M7-12, the module review, and the exam.
```

### Listing 3 — Why the wave model fails: prediction vs observation
| Observation | Wave-model prediction | Actually observed | Verdict |
|-------------|-----------------------|-------------------|---------|
| No time delay (**D**) | Faint light → energy accumulates slowly → a time **delay** (longer when dimmer) | Instant emission even for very faint light | ✗ FAILS |
| Threshold frequency (**F**) | Energy depends on intensity → **any** frequency works if bright/long enough → no threshold | Hard threshold f₀; below it nothing, at any intensity | ✗ FAILS |
| Energy from frequency (**E**) | Electron energy rises with **intensity** (amplitude); independent of frequency | Energy rises with **frequency**; independent of intensity (the exact reverse) | ✗ FAILS (backwards) |
| Number from intensity (**N**) | Brighter → more energy → more electrons | Brighter → more electrons per second | ✓ correct (shaky reason) |

```text
SCOREBOARD: wave model gets 3 of 4 WRONG (D, F, E) and only N right.
Exam technique: pair EACH observation with the wave prediction it contradicts —
"the wave model predicts X, but we observe Y." Listing the observations alone ≈ half marks.
```

### Listing 4 — Worked example: stopping voltage from maximum kinetic energy
```text
Relationship:  K_max = e V₀   ⇒   V₀ = K_max / e
Data sheet:    e = 1.6 × 10^-19 C

Example (Exam Q3):  K_max = 2.6 × 10^-19 J. Find V₀.
  V₀ = K_max / e
     = (2.6 × 10^-19) / (1.6 × 10^-19)
     = 1.6 V   (2 sig figs)
  Units check: joules / coulombs = volts ✓

Reverse example:  V₀ = 4.2 V. What energy electrons does it stop?
  K_max = e V₀ = (1.6 × 10^-19)(4.2) = 6.7 × 10^-19 J
```

### Listing 5 — The photocurrent-vs-voltage graph (and how it shifts)
```text
  Photocurrent
      |          ________ saturation (all emitted electrons collected)
      |        /
      |      /
      |    /
  ____|__ /________________________  Voltage
   −V₀  0           +  (accelerating)
   ↑
 stopping voltage (current = 0)

CHANGE THE LIGHT:
  • Increase INTENSITY (same frequency):
        saturation photocurrent RISES (more electrons/sec),
        stopping voltage V₀ UNCHANGED (same K_max).            [N of DENF]
  • Increase FREQUENCY (same intensity):
        stopping voltage V₀ becomes MORE NEGATIVE (higher K_max),
        saturation current roughly unchanged.                  [E of DENF]
  • Below the threshold frequency f₀:
        NO photocurrent at any voltage or intensity.           [F of DENF]
```

### Listing 6 — Timeline of key people and dates
```text
1887  Heinrich Hertz   — first OBSERVES the effect at his spark gap (UV → stronger sparks),
                          while confirming EM waves exist. Does not pursue it. (irony: the man
                          who proved light is a wave first saw the evidence it's a particle.)
~1888 Wilhelm Hallwachs — simple demo: UV discharges a NEGATIVELY charged zinc plate fast;
                          a positively charged plate is unaffected.
1899  J.J. Thomson     — shows the ejected particles ARE electrons (same as cathode-ray particles).
                          → cross-link: case_jj_thomson_cathode_rays (M8).
1900  Max Planck       — quantises energy (E = hf) to fix black-body radiation (M7-10).
1902  Philipp Lenard   — quantifies it: energy depends on frequency, number on intensity,
                          and there is a threshold frequency. These are the four observations.
1905  Albert Einstein  — explains it with the photon (NEXT EPISODE, M7-12).
```
