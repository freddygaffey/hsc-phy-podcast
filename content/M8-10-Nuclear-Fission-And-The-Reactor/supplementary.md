---
title: "Supplementary Materials — Nuclear Fission and the Reactor"
module: M8
lesson: "10"
script: script.md
---

# Supplementary Materials

Equations, data, and reference tables for nuclear fission and reactors. Nothing here is spoken in the audio — it is the read-along reference. The energy released in a fission is calculated by the methods in M8-09 (mass-difference or binding-energy); see that episode's Listing 4 for the full U-236 worked example.

### Listing 1 — Fission equations (balanced; conserve A and Z)
```text
A slow neutron is CAPTURED by U-235 → unstable U-236 → splits + 2–3 neutrons + energy.

   ²³⁵₉₂U + ¹₀n → ²³⁶₉₂U* → ¹⁴⁸₅₇La + ⁸⁵₃₅Br + 3 ¹₀n + energy
   ²³⁵₉₂U + ¹₀n → ²³⁶₉₂U* → ¹⁴¹₅₆Ba + ⁹²₃₆Kr + 3 ¹₀n + energy
   ²³⁵₉₂U + ¹₀n → ²³⁶₉₂U* → ¹⁴⁰₅₄Xe + ⁹⁴₃₈Sr + 2 ¹₀n + energy

CONSERVATION CHECK (e.g. La/Br split):
  Mass number A:  235 + 1 = 236  =  148 + 85 + 3(1) = 236   ✓
  Atomic number Z: 92 + 0 = 92   =  57  + 35 + 3(0) = 92    ✓

The fragments vary event-to-event; the number of neutrons (2 or 3) is found by
balancing A. An unbalanced equation is wrong — always check top and bottom.
```

### Listing 2 — Energy per fission (where the ~200 MeV comes from)
```text
Source of the energy: the fission fragments sit HIGHER on the binding-energy-per-
nucleon curve (closer to iron-56) than U-236 → more tightly bound → the increase
in binding energy is released (mass-energy equivalence, M8-09).

Worked value (from M8-09, U-236 → La-148 + Br-85 + 3n):
  Binding-energy method:  ΣBE(products) − BE(U-236)
                        = 1950.416 − 1790.415 ≈ 160 MeV
  Mass-difference method: Δm c² ≈ 160 MeV   (the two agree)

Typical figure quoted for U-235 fission: ~200 MeV per fission, the overwhelming
majority as KINETIC ENERGY of the two fragments (the rest: neutrons + gamma rays).
```

### Listing 3 — Energy density: fission vs chemical vs explosive
| Process | Energy per event/atom | Relative |
|---------|-----------------------|----------|
| Fission of one U-235 nucleus | ~200 MeV (= 2 × 10⁸ eV) | ~20 000 000× |
| Combustion of one carbon atom (coal) | ~10 eV | 1× (baseline) |
| Conventional chemical explosive (per atom) | ~ a few eV | ~ same order as combustion |

```text
Ratio: 200 MeV / 10 eV = 2 × 10⁸ / 10 = 2 × 10⁷  ≈ 20 million times.
WHY: chemical reactions rearrange OUTER ELECTRONS (~eV); fission taps NUCLEAR
BINDING ENERGY (~MeV), about a million times greater per particle. So a few kg of
uranium ≈ thousands of tonnes of coal.
```

### Listing 4 — The four reactor components ("Fast Cars Make Crashes")
| Mnemonic | Component | Typical material | Job (one word) | What it does |
|----------|-----------|------------------|----------------|--------------|
| **Fast** | **Fuel** | Enriched uranium (3–5% U-235) | **Provide** | Supplies the fissile nuclei → fissions, energy, neutrons |
| **Cars** | **Control rods** | Cadmium, boron | **Absorb** | Absorb neutrons; insert → slower, withdraw → faster; hold rate at 1 fission/fission |
| **Make** | **Moderator** | Water, graphite | **Slow** | Slows fast neutrons to thermal speeds so they're captured → sustains the chain |
| **Crashes** | **Coolant** | Water (or gas/liquid metal) | **Cool** | Carries heat out → steam → turbines; prevents the core overheating (meltdown) |

```text
⚠ MOST COMMON TRAP: moderator SLOWS neutrons; control rods ABSORB neutrons.
  Both change the reaction rate, but by OPPOSITE mechanisms. Never swap them.
```

### Listing 5 — Controlled vs uncontrolled chain reaction
```text
Each fission releases 2–3 neutrons. Let k = average number of those neutrons that
go on to cause a FURTHER fission.

  CONTROLLED  (k = 1):  exactly one further fission per fission
                        → steady, self-sustaining, constant power  → REACTOR
  UNCONTROLLED (k > 1): more than one further fission per fission
                        → fissions multiply (1 → 3 → 9 → …) in a fraction of a
                          second → explosive energy release  → BOMB

CRITICAL MASS: the minimum mass of fissile material for a self-sustaining chain.
  Below it, too many neutrons escape the surface before causing fission → chain dies.
  At/above it → chain sustains (reactor: just critical; bomb: supercritical).

Same single-fission physics in both; only the NEUTRON ECONOMY (k) differs.
```
