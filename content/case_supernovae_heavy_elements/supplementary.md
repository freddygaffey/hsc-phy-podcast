---
title: "Supplementary Materials — Supernovae: Making Everything Heavier than Iron"
kind: case-study
script: script.md
---

# Supplementary Materials

These materials are NOT spoken in the episode. They collect the key equations, numbers, and a worked example that the narration refers to in plain English.

### Listing 1 — Binding energy per nucleon (the master concept)

```text
binding_energy_per_nucleon = total_binding_energy / number_of_nucleons

total_binding_energy = mass_defect * c^2
mass_defect = (sum of masses of separate protons and neutrons) - (mass of nucleus)

Exam shortcut (from teacher slides / NESA data sheet):
  1 u = 931.5 MeV/c^2
  so   binding_energy (MeV) = mass_defect (in u) * 931.5
  (do NOT also divide by c^2 in SI - the 931.5 already carries the /c^2 unit)

Key feature of the curve B/A versus mass number A:
  rises steeply for light nuclei
  PEAKS near iron-56 / nickel-62
  falls slowly for heavy nuclei

Iron-56  : B/A = 8.791 MeV per nucleon  (conventional "peak")
Nickel-62: B/A = 8.795 MeV per nucleon  (true maximum, technicality)

Consequence:
  fusion of nuclei LIGHTER than iron -> product higher on curve -> EXOTHERMIC (releases energy)
  fusion of nuclei HEAVIER than iron -> product lower on curve  -> ENDOTHERMIC (absorbs energy)

This is why stellar fusion stops at iron and why a catastrophe
is required to build everything heavier.
```

### Listing 2 — The Chandrasekhar limit and degeneracy pressure

```text
Electron degeneracy pressure arises from the Pauli exclusion principle
(no two electrons in the same quantum state).

Non-relativistic electrons:  P  proportional to  density^(5/3)
Relativistic electrons:      P  proportional to  density^(4/3)   <- softer, cannot resist gravity

Chandrasekhar limit (maximum mass supportable by electron degeneracy pressure):
  M_Ch  ~  1.44  solar masses   (commonly quoted as ~1.4)

Above M_Ch the core cannot be held up and MUST collapse.

Derived by S. Chandrasekhar, 1930-1935.
Nobel Prize in Physics 1983.
```

### Listing 3 — The core-collapse sequence (timeline and numbers)

```text
1. Silicon shell burning dumps iron onto the core (final ~1 day of silicon burning).
2. Iron core mass crosses ~1.44 solar masses (Chandrasekhar limit).
3. Electron capture (neutronisation):  e- + p -> n + neutrino
   - removes the electrons providing degeneracy pressure
4. Photodisintegration:  gamma + Fe-56 -> 13 He-4 + 4 n   (absorbs ~124 MeV per iron nucleus)
   - removes thermal support; both effects accelerate collapse
5. Collapse speed of outer core: up to 70,000 km/s  (~23% of c)
6. Core shrinks: ~8,000 km diameter -> ~19 km diameter in < 1 second
7. Reaches nuclear saturation density ~2.4 x 10^14 g/cm^3; temperature ~10^11 K
8. Strong force turns repulsive; equation of state stiffens; core BOUNCES
9. Shock wave launched outward, then STALLS at ~100-200 km
10. Neutrino heating (~1% of neutrino flux absorbed) REVIVES the shock -> explosion

Energy budget:
  Total released (gravitational):  ~10^46 J   (more than the Sun's whole-life output)
  Carried by neutrinos:            ~99%
  Kinetic energy of ejecta:        ~10^44 J   (~1%)
  Radiated as visible light:       ~10^43 J   (~0.01%)

Remnant: neutron star (core < ~3 solar masses) or black hole (core > ~3 solar masses).
NOTE: the iron core IMPLODES; the visible supernova is the outer envelope being blasted off.

Progenitor mass range (Jacaranda Ch12): stars of ~8 to 50 solar masses end as
core-collapse (Type II) supernovae. Lifetimes of millions of years (vs billions
for a Sun-like star). A neutron star has the density of an atomic nucleus and a
diameter of little more than ~20 km, with a mass greater than the Sun's.

Type II vs Type I (spectral distinction, Jacaranda Ch12):
  Type II: hydrogen lines PRESENT  -> core collapse of a massive star (this episode)
  Type I : hydrogen lines ABSENT   -> e.g. white dwarf exceeding ~1.4 solar masses
           in a binary (accretion of hydrogen, runaway fusion)
```

### Listing 4 — The r-process (rapid neutron capture)

```text
Required conditions:
  free neutron density:  ~10^24 neutrons/cm^3  (~1 gram of free neutrons per cm^3)
  temperature:           ~10^9 K (1 gigakelvin)
  timescale:             seconds (free neutrons decay in ~10 minutes)

Mechanism (two competing clocks):
  neutron capture:   (Z, A) + n -> (Z, A+1)      [no Coulomb barrier: neutron is neutral]
  beta decay:        n -> p + e- + antineutrino   [raises Z by 1: climbs the periodic table]

RAPID process: capture is much faster than beta decay, so nuclei become extremely
neutron-rich before decaying, then cascade up to thorium and uranium.

SLOW process (s-process, for contrast): capture much slower than beta decay; stays
near the valley of stability; tops out near lead/bismuth; occurs in aging AGB stars.

Outcomes:
  r-process makes ~half of all nuclei heavier than iron, and essentially ALL of the
  heaviest (thorium, uranium, and beyond).
  Abundance peaks at mass numbers A ~ 80, 130, 195 (nuclei stalling at the neutron
  magic numbers N = 50, 82, 126).

Confirmed sites: neutron star mergers (dominant for heaviest elements) and rare supernovae.
```

### Listing 5 — Key observational events

| Event | Date | What it measured | Headline result |
|-------|------|------------------|-----------------|
| B2FH paper | 1957 | theory | Named r-process and s-process; map of stellar nucleosynthesis |
| Supernova 1987A | 23 Feb 1987 | neutrino burst + light | ~24 neutrinos over ~13 s, ~2-3 h before light; confirmed core collapse |
| GW170817 | 17 Aug 2017 | gravitational waves + light | Neutron star merger; kilonova AT2017gfo; r-process site confirmed |
| Strontium in kilonova | Oct 2019 (Watson et al.) | spectrum at ~810 nm | First single r-process element identified in a merger |

### Listing 6 — Worked example: energy released forming a helium-4 nucleus

```text
Question: How much energy is released when two protons and two neutrons
fuse into one helium-4 nucleus? (Illustrates WHY fusion below iron is exothermic.)

Data (atomic mass unit u = 1.6605 x 10^-27 kg ; c = 3.0 x 10^8 m/s):
  mass of proton  = 1.00728 u
  mass of neutron = 1.00867 u
  mass of He-4 nucleus = 4.00151 u

Step 1 - mass of separate nucleons:
  2 protons  = 2 x 1.00728 = 2.01456 u
  2 neutrons = 2 x 1.00867 = 2.01734 u
  total      = 4.03190 u

Step 2 - mass defect:
  mass_defect = 4.03190 - 4.00151 = 0.03039 u

Step 3 - convert to kilograms:
  0.03039 u x 1.6605 x 10^-27 kg/u = 5.046 x 10^-29 kg

Step 4 - energy released (E = mc^2):
  E = (5.046 x 10^-29) x (3.0 x 10^8)^2
  E = 4.54 x 10^-12 J
  E = 28.3 MeV  (about 7.1 MeV per nucleon)

Faster route using the 931.5 MeV/c^2 shortcut (matches teacher slides exactly):
  E = mass_defect (u) x 931.5 = 0.030376 x 931.5 = 28.30 MeV total
  28.30 / 4 nucleons = 7.07 MeV per nucleon
  (Compare with iron-56 at 8.79 MeV per nucleon: He-4 is still climbing toward
   the iron peak, which is exactly why further fusion below iron keeps releasing
   energy.)

Interpretation:
  Energy is RELEASED because He-4 sits higher on the binding-energy-per-nucleon
  curve than free nucleons. The same logic, run in reverse, shows that fusing
  iron into heavier nuclei would REQUIRE energy input - which is why no star can
  fuse past iron, and why the heavy elements need a supernova or neutron star merger.
```
