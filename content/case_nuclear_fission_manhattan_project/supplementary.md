---
title: "Supplementary Materials — Nuclear Fission and the Manhattan Project"
kind: case-study
script: script.md
---

# Supplementary Materials

### Listing 1 — Core equations of nuclear fission energetics

```text
Mass-energy equivalence (Einstein):
E = m c^2

Energy conversion factor used on the HSC data sheet:
1 u = 931.5 MeV / c^2
so a mass defect of 1 u releases 931.5 MeV of energy

Mass defect of a reaction:
delta_m = (total mass of reactants) - (total mass of products)

Energy released:
E = delta_m * 931.5    (delta_m in u, E in MeV)
or
E = delta_m * c^2      (delta_m in kg, c = 2.998e8 m/s, E in joules)

Multiplication factor k = average neutrons per fission that cause a further fission:
k < 1  -> subcritical (chain dies out)
k = 1  -> critical    (steady power, a controlled reactor)
k > 1  -> supercritical (exponential growth, an uncontrolled reaction / bomb)
```

### Listing 2 — A canonical U-235 fission reaction

```text
U-235 + n  ->  U-236*  ->  Ba-141 + Kr-92 + 3 n + energy

Written with mass and atomic numbers:
(235,92)U + (1,0)n -> (141,56)Ba + (92,36)Kr + 3 (1,0)n + energy

Check conservation:
Mass numbers:   235 + 1 = 141 + 92 + 3(1) = 236   OK
Atomic numbers: 92 + 0  = 56 + 36 + 3(0)  = 92    OK
```

### Listing 3 — Worked example: energy released per fission

```text
GOAL: find the energy released in U-235 + n -> Ba-141 + Kr-92 + 3 n

Step 1 — total mass of reactants (in u):
mass U-235  = 235.043930
mass n      =   1.008665
reactants   = 236.052595 u

Step 2 — total mass of products (in u):
mass Ba-141 = 140.914411
mass Kr-92  =  91.926156
mass 3 n    =   3.025995   (= 3 * 1.008665)
products    = 235.866562 u

Step 3 — mass defect:
delta_m = 236.052595 - 235.866562
delta_m = 0.186033 u

Step 4 — convert to energy:
E = 0.186033 * 931.5
E = 173.3 MeV   (kinetic energy of fragments; ~200 MeV total
                 once gamma rays and fragment decay are included)

Step 5 — express in joules (per single fission):
E ~ 200 MeV = 200e6 * 1.602e-19 J = 3.2e-11 J
```

### Listing 4 — Key numbers and constants

| Quantity | Value |
|----------|-------|
| Energy per fission (total) | ~200 MeV = 3.2 x 10^-11 J |
| Energy conversion factor | 1 u = 931.5 MeV/c^2 |
| 1 atomic mass unit (u) | 1.661 x 10^-27 kg |
| Speed of light, c | 2.998 x 10^8 m/s |
| Neutron mass | 1.008665 u |
| Carbon atom burned (chemical) | ~10 eV (about 20 million times less than fission) |
| Energy from 1 kg U-235 (full fission) | ~8.2 x 10^13 J (~20,000 tonnes TNT) |
| Natural abundance of U-235 | 0.72% (rest is U-238) |
| Reactor fuel enrichment | ~3-5% U-235 |
| Weapons-grade enrichment | >90% U-235 |
| Neutrons released per fission (average) | ~2.4 |
| Critical mass, U-235 bare sphere | ~52 kg |
| Critical mass, U-235 with reflector | ~15 kg |

### Listing 5 — Binding energy per nucleon (why fission releases energy)

```text
Binding energy per nucleon measures how tightly bound each nucleon is.
The curve peaks near iron-56 (the most stable nucleus).

Approximate binding energy per nucleon (from Jacaranda Table 15.3 totals):
U-236  ~ 7.59 MeV/nucleon   (1790.4 MeV / 236, less tightly bound)
Ba-141 ~ 8.33 MeV/nucleon   (1174.0 MeV / 141, more tightly bound)
Kr-92  ~ 8.51 MeV/nucleon   (783.2 MeV / 92,  more tightly bound)

U-235 itself sits at ~7.6 MeV/nucleon, far down the right-hand slope.

The curve of binding energy per nucleon rises steeply from light nuclei,
peaks near iron-56 (~8.8 MeV/nucleon, the most stable nucleus), then
falls slowly toward the heavy nuclei such as uranium.

Splitting U-235 produces fragments that lie closer to the iron peak,
i.e. with HIGHER binding energy per nucleon. The products are more
tightly bound, so energy is released as the system moves toward the
peak of the curve. (Equivalently: the total binding energy of the two
fragments exceeds that of U-236, and the surplus appears as kinetic
energy of the fragments and neutrons.)

Fusion (light nuclei joining) and fission (heavy nuclei splitting)
both release energy by moving nuclei TOWARD the iron-56 peak. Iron-56
is the heaviest nucleus that can be made by fusion releasing energy,
and the lightest practical target for energy-releasing fission lies
well above it.
```

### Listing 6 — Fission reactor components and their physics role

| Component | Material (example) | Physics role |
|-----------|--------------------|--------------|
| Fuel | Enriched uranium (~3-5% U-235) | Fissile material; releases energy and fast neutrons |
| Moderator | Graphite, light water, heavy water | Slows fast neutrons to thermal speeds (raises fission cross-section) |
| Control rods | Cadmium, boron, hafnium | Absorb excess neutrons to hold k = 1 (the throttle/brake) |
| Coolant | Water (often same as moderator) | Removes heat to drive a turbine |
| Reflector | Graphite, beryllium | Bounces escaping neutrons back into the core |
| Shielding | Concrete, lead | Absorbs gamma rays and stray neutrons |
