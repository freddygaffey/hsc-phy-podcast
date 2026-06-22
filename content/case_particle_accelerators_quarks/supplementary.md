---
title: "Supplementary Materials — Particle Accelerators and the Discovery of Quarks"
kind: case-study
script: script.md
---

# Supplementary Materials

### Listing 1 — Quark content and electric charge of the proton and neutron
```text
Quark electric charges (in units of the elementary charge e):
  up quark      = +2/3
  down quark    = -1/3

Proton = up + up + down
  charge = (+2/3) + (+2/3) + (-1/3)
         = +4/3 - 1/3
         = +3/3
         = +1   (matches the observed proton charge)

Neutron = up + down + down
  charge = (+2/3) + (-1/3) + (-1/3)
         = +2/3 - 2/3
         = 0    (matches the observed neutron charge)

Key point: fractional quark charges combine to give
whole-number charges for every observed particle.
```

### Listing 2 — The de Broglie wavelength: why high energy resolves small structure
```text
de Broglie wavelength of a moving particle (NESA syllabus formula):

  lambda = h / p = h / (m v)

where:
  lambda = wavelength of the probe particle (m)
  h      = Planck's constant = 6.63 × 10^-34 J·s
  p      = momentum of the particle (kg·m/s)
  m      = mass of the particle (kg)
  v      = speed of the particle (m/s)

Accelerated-electron form (from the accelerating voltage V):
  An electron accelerated through voltage V gains kinetic energy
  E_k = q_e V, so its momentum is p = sqrt(2 m_e q_e V), and:

  lambda = h / sqrt(2 m_e q_e V)

  => higher accelerating voltage → higher momentum → shorter lambda.

Rule of probing:
  To resolve a structure of size d, you need lambda <= d (roughly).
  Proton radius d ≈ 1 × 10^-15 m (1 femtometre).
  Smaller lambda  → higher momentum p  → higher energy electrons.

This is why SLAC needed electrons up to 20 GeV:
high energy → short wavelength → resolves sub-proton structure.
(At these energies electrons are ultra-relativistic, so the simple
non-relativistic voltage form is only a guide; use E ≈ p·c instead.)
```

### Listing 3 — The Bjorken scaling variable
```text
In deep inelastic scattering the key dimensionless variable is:

  x = Q^2 / (2 · M · nu)

where:
  Q^2 = squared 4-momentum transfer of the virtual photon
        (large Q^2 = short-wavelength probe = "deep")
  M   = mass of the proton
  nu  = energy lost by the electron in the lab frame
  x   = fraction of the proton's momentum carried by the
        struck quark (parton), ranges from 0 to 1

Bjorken scaling:
  If the proton contains POINT-LIKE constituents, the measured
  structure functions depend only on x — NOT on Q^2 separately.

  Soft diffuse proton  → scattering falls rapidly with Q^2
  Point-like quarks    → scattering depends only on x (scaling)

The SLAC data showed scaling → evidence for point-like quarks.
```

### Listing 4 — Colour confinement and string breaking (energy → matter)
```text
The strong-force flux tube between two quarks stores energy:

  E ≈ kappa · r

where:
  E     = energy stored in the flux tube (J or GeV)
  kappa = string tension ≈ 1 GeV per femtometre (1 GeV/fm)
  r     = separation between the quarks (fm)

Unlike gravity or electromagnetism, the force does NOT fall with r.
The stored energy keeps GROWING as you pull the quarks apart.

String breaking (pair production):
  When stored energy reaches E >= 2·m·c^2 for a new quark pair,
  the vacuum produces a new quark + antiquark at the break point.

  Result: pulling 1 quark away makes 2 new colour-neutral particles
  instead of freeing a single quark.

  => No free quark is ever produced. This is colour confinement.
```

### Listing 5 — Worked example: minimum electron energy to "see" a quark
```text
GOAL:
  Estimate the electron momentum/energy whose de Broglie wavelength
  can resolve structure inside a proton (size ≈ 1 × 10^-15 m).

STEP 1 — set lambda equal to the proton size:
  lambda = 1 × 10^-15 m

STEP 2 — find the required momentum from p = h / lambda:
  p = (6.63 × 10^-34) / (1 × 10^-15)
    = 6.63 × 10^-19 kg·m/s

STEP 3 — convert to energy (ultra-relativistic, E ≈ p·c):
  E = p · c
    = (6.63 × 10^-19) × (3.0 × 10^8)
    = 1.99 × 10^-10 J

STEP 4 — convert joules to electron volts (1 eV = 1.602 × 10^-19 J):
  E = (1.99 × 10^-10) / (1.602 × 10^-19)
    = 1.24 × 10^9 eV
    ≈ 1.2 GeV  (order-of-magnitude minimum)

INTERPRETATION:
  Probing INSIDE the proton (well below its radius) needs energies
  of several GeV and beyond — which is exactly why SLAC ran electrons
  from about 6 GeV up to 20 GeV.
```

### Listing 6 — The Standard Model particle inventory

| Category | Members | Count |
|----------|---------|-------|
| Quarks | up, down, strange, charm, bottom, top | 6 |
| Leptons | electron, muon, tau, + 3 neutrinos | 6 |
| Force-carrying bosons | photon, 8 gluons, W+, W-, Z0 | 4 types |
| Scalar boson | Higgs | 1 |

### Listing 7 — Quark properties

| Quark | Charge (units of e) | Baryon number |
|-------|---------------------|---------------|
| up | +2/3 | 1/3 |
| down | -1/3 | 1/3 |
| strange | -1/3 | 1/3 |
| charm | +2/3 | 1/3 |
| bottom | -1/3 | 1/3 |
| top | +2/3 | 1/3 |

### Listing 8 — Key experimental numbers and dates

| Quantity / Event | Value / Date |
|------------------|--------------|
| SLAC accelerator length | 3.2 km (2 miles) |
| Depth underground | ≈ 9 m (passes under Interstate 280) |
| Maximum electron energy (original) | 20 GeV (later 50 GeV) |
| Scattering angles measured | 6°, 10°, 18°, 26°, 34° (varied by run) |
| Target | liquid hydrogen (protons); later deuterium |
| First SLAC beam | 21 May 1966 |
| Gell-Mann quark paper published | February 1964 |
| Omega-minus event observed (Brookhaven) | 31 January 1964 (paper received 11 February 1964) |
| SLAC deep inelastic results (Vienna) | August/September 1968 |
| J/psi discovery (November Revolution) | 11 November 1974 |
| Top quark discovered (Fermilab) | 2 March 1995 |
| Higgs boson discovered (CERN LHC) | 4 July 2012 |
| String tension (flux tube) | ≈ 1 GeV/fm |
| Top quark mass | ≈ 173 GeV/c² (about as heavy as a tungsten atom) |
| J/psi mass | ≈ 3 GeV/c² |
| Nobel Prize: Friedman, Kendall, Taylor | 1990 |
