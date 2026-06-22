---
title: "Supplementary Materials — PET Scans — Antimatter in Medicine"
kind: case-study
script: script.md
---

# Supplementary Materials

### Listing 1 — Energy released in positron-electron annihilation

```text
Mass-energy equivalence:
E = m c^2

rest mass energy of an electron  = 0.511 MeV = 511 keV
rest mass energy of a positron   = 0.511 MeV = 511 keV   (identical mass, by Dirac symmetry)

total energy released in one annihilation:
E_total = 2 x 0.511 MeV = 1.022 MeV

this is shared equally between two photons:
E_per photon = 1.022 MeV / 2 = 0.511 MeV = 511 keV

precise value of each photon energy = 510.99895 keV

In SI units (showing E = mc^2 explicitly):
m = mass of electron + mass of positron
  = 9.109 x 10^-31 kg + 9.109 x 10^-31 kg
  = 1.822 x 10^-30 kg
c = 3.00 x 10^8 m/s

E = (1.822 x 10^-30) x (3.00 x 10^8)^2
E = 1.64 x 10^-13 J
  = 1.022 MeV   (since 1 MeV = 1.602 x 10^-13 J)
```

### Listing 2 — Why two photons, back to back (conservation laws)

```text
Annihilation reaction:
e- (electron)  +  e+ (positron)  ->  gamma  +  gamma

CHARGE conservation:
(-e) + (+e) = 0   before
0   + 0     = 0   after (photons are neutral)        OK

ENERGY conservation:
total energy in  = 0.511 + 0.511 = 1.022 MeV
total energy out = 0.511 + 0.511 = 1.022 MeV         OK
-> each photon must carry 511 keV

MOMENTUM conservation:
before: e- and e+ are (nearly) at rest -> total momentum ~ 0
after:  total momentum must still = 0
        one photon carries momentum p in some direction
        => second photon must carry momentum p in the EXACTLY opposite direction
        so that p + (-p) = 0
-> the two photons are emitted 180 degrees apart (back to back)

Note (non-collinearity):
the electron has a small residual momentum, so in the lab frame the angle
deviates from 180 degrees by ~0.25 degrees. This is a fundamental limit on
PET spatial resolution, NOT an engineering flaw.
```

### Listing 3 — The PET imaging chain (step by step)

```text
1. FDG (fluorodeoxyglucose) injected into bloodstream.
   FDG = glucose with one OH group replaced by fluorine-18.

2. Cells take up FDG like glucose (via GLUT transporters).
   Tumour cells consume glucose fastest (Warburg effect) -> take up most FDG.
   FDG gets phosphorylated then TRAPPED inside the cell -> accumulates.

3. Fluorine-18 decays by beta-plus decay (mediated by the WEAK nuclear force):
        F-18  ->  O-18  +  e+ (positron)  +  neutrino
   (a proton turns into a neutron, emitting a positron)
   Underlying transformation:  p  ->  n  +  e+  +  neutrino

4. Positron travels only ~0.5-2.3 mm in tissue, then meets an electron.

5. Annihilation:  e+ + e-  ->  two 511 keV gamma photons at ~180 degrees.

6. Gamma photons (mean free path ~10 cm in tissue) escape the body.
   NOTE: the scanner detects the GAMMA RAYS, never the positrons.

7. A ring of detector crystals surrounds the patient.
   Two opposite detectors firing within a few nanoseconds = a "coincidence".

8. Each coincidence defines a LINE OF RESPONSE (LOR):
   the annihilation occurred somewhere on the straight line joining the
   two detectors.

9. Millions of LORs are collected. Where many lines intersect = where the
   FDG is concentrated. A computer reconstructs a 3D map of metabolism.
```

### Listing 4 — Fluorine-18 half-life and decay

```text
Beta-plus (positron) decay equation:
   18            18
     F    ->       O   +   e+   +   neutrino
   9             8

In beta-plus decay the WEAK nuclear force converts a proton into a neutron:
   1            1
     p    ->     n   +   e+   +   neutrino
   1            0
=> atomic number Z decreases by 1 (9 -> 8); mass number A unchanged (18).
   Note: beta-PLUS emits a neutrino; beta-MINUS emits an ANTI-neutrino.

half-life of fluorine-18,  t_half = 109.77 min  (~110 min)

decay constant:
   lambda = ln(2) / t_half = 0.693 / 110 min = 0.0063 per min

fraction remaining after n half-lives = (1/2)^n

  half-lives passed     time          fraction remaining
        0               0 min                100%
        1             ~110 min                50%
        2             ~220 min (3.7 h)        25%
        3             ~330 min                12.5%
        6             ~660 min (11 h)         ~1.6%

=> long enough to ship from cyclotron and scan (uptake takes ~60-90 min),
   short enough that the patient is essentially non-radioactive next day.
Compare carbon-11 (t_half ~20 min) -> too short to ship; F-18 chosen instead.
```

### Listing 5 — Key numbers and constants for this episode

| Quantity | Value |
|----------|-------|
| Electron / positron rest mass energy | 0.511 MeV (= 511 keV) each |
| Energy of each annihilation photon | 511 keV (510.99895 keV precisely) |
| Total energy per annihilation | 1.022 MeV |
| Angle between the two photons | 180 degrees (back to back) |
| Fluorine-18 half-life | 109.77 min (~110 min) |
| Positron range in tissue (F-18) | mean ~0.6 mm; max ~2.3 mm in water |
| Mean free path of 511 keV gamma in tissue | ~10 cm |
| Coincidence timing window | ~6-12 nanoseconds |
| PET spatial resolution | ~1-8 mm (scanner dependent) |
| Standard FDG dose | 185-370 MBq (5-10 millicuries) |
| Uptake time before scan | 60-90 min |
| Speed of light, c | 3.00 x 10^8 m/s |
| 1 MeV | 1.602 x 10^-13 J |

### Listing 6 — Timeline of the discovery and the application

| Year | Event |
|------|-------|
| 1928 | Dirac publishes The Quantum Theory of the Electron (Cambridge); negative-energy solutions appear |
| 1930 | Oppenheimer argues the "hole" must have the electron's mass, not be a proton |
| 1931 | Dirac explicitly predicts the "anti-electron" (positron) |
| 1932 | Anderson photographs the positron in a cloud chamber at Caltech (2 Aug); names it the positron |
| 1933 | Dirac shares Nobel Prize (with Schrodinger) |
| 1936 | Anderson shares Nobel Prize for the positron |
| 1953 | Brownell & Sweet (MGH) use positron emitters to locate brain tumours |
| 1974 | First ring PET scanner (Ter-Pogossian, Phelps, Hoffman, Washington Univ. St Louis) |
| 1976 | First human administration of [18F]FDG (Alavi, Univ. of Pennsylvania, Aug) |
| ~1980 | Discovery that tumours accumulate FDG -> PET becomes an oncology tool |
