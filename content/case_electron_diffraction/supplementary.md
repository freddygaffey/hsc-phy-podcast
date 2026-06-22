---
title: "Supplementary Materials — Electron Diffraction: The Wave Inside the Particle"
kind: case-study
script: script.md
---

# Supplementary Materials

### Listing 1 — The de Broglie equation (the central relationship)
```text
lambda = h / p          (wavelength = Planck's constant / momentum)

since   p = m * v        (momentum = mass * velocity)

lambda = h / (m * v)

where
  lambda = de Broglie wavelength (m)
  h      = Planck's constant = 6.626 x 10^-34 J s
  p      = momentum (kg m/s)
  m      = mass of the particle (kg)
  v      = speed of the particle (m/s)

Key idea: wavelength is INVERSELY proportional to momentum.
  - light, slow objects  -> long wavelength -> wave effects observable
  - heavy, fast objects  -> short wavelength -> wave effects undetectable
```

### Listing 2 — Constants and key experimental values
| Quantity | Symbol | Value |
|----------|--------|-------|
| Planck's constant (NESA data sheet) | h | 6.626 x 10^-34 J s |
| Electron mass | m_e | 9.109 x 10^-31 kg |
| Elementary charge | e | 1.602 x 10^-19 C |
| Speed of light | c | 3.00 x 10^8 m/s |
| Davisson–Germer accelerating voltage | V | 54 V |
| Davisson–Germer scattering-peak angle | theta | 50 degrees (from incident beam) |
| Nickel atomic-row (surface) spacing | d | 0.215 nm = 2.15 x 10^-10 m |
| de Broglie wavelength predicted (theory) | lambda | 0.167 nm = 1.67 x 10^-10 m |
| Wavelength measured from diffraction | lambda | 0.165 nm = 1.65 x 10^-10 m |
| Agreement between theory and experiment | — | better than 1.2% |
| G.P. Thomson film thickness | — | approx 3 x 10^-8 m (30 nm) |
| G.P. Thomson agreement with prediction | — | within about 5% |
| Typical atomic spacing in crystals | — | ~1 x 10^-10 m (order 0.1 nm) |
| Condition for observable diffraction | lambda / w | greater than ~1/10 (textbook rule) |

Context: Max von Laue (1912) showed a crystal's regularly spaced atoms act as a
diffraction grating for X-rays (X-ray wavelength ~1 x 10^-10 m, comparable to atomic
spacing). The Braggs turned this into X-ray crystallography. De Broglie's predicted
electron wavelength falls in the same ~0.1 nm range, which is why the same crystals
diffract electrons.

### Listing 3 — Worked example: de Broglie wavelength of a 54 V electron
```text
GOAL: find the wavelength predicted by theory for the Davisson-Germer electrons.

Step 1 — energy gained from the accelerating voltage:
  E_k = e * V
      = (1.602 x 10^-19) * 54
      = 8.65 x 10^-18 J

Step 2 — relate kinetic energy to momentum (non-relativistic):
  E_k = p^2 / (2 m_e)     =>     p = sqrt(2 * m_e * E_k)

  p = sqrt( 2 * (9.109 x 10^-31) * (8.65 x 10^-18) )
    = sqrt( 1.576 x 10^-47 )
    = 3.97 x 10^-24 kg m/s

  (equivalently:  p = sqrt(2 * m_e * e * V) )

Step 3 — apply de Broglie:
  lambda = h / p
         = (6.626 x 10^-34) / (3.97 x 10^-24)
         = 1.67 x 10^-10 m
         = 0.167 nm

USEFUL SHORTCUT (combine steps 1-3 into one accelerating-voltage formula):
  lambda = h / sqrt(2 * m_e * e * V)      (when accelerated through voltage V)
  lambda = h / sqrt(2 * m_e * E_k)        (when kinetic energy E_k is known)
  (derived from  E_k = e*V = p^2 / 2m_e , so  p = sqrt(2 * m_e * e * V) )

RESULT: ~0.167 nm — comparable to the spacing of nickel atoms (~0.1-0.2 nm),
which is exactly why the crystal can diffract the electrons.
The diffraction GEOMETRY (angle 50 deg + known nickel spacing) independently
yields ~0.165 nm. The two numbers agree to better than 1.2%.

EXPERIMENTAL HALF (the second, independent road):
  Surface-grating condition:  n * lambda = d * sin(theta)
  n = 1,  d = 0.215 nm,  theta = 50 deg
  lambda = (0.215 x 10^-9) * sin(50 deg)
         = 1.65 x 10^-10 m
         = 0.165 nm
  This uses only the measured angle and the known nickel spacing (from X-ray
  crystallography) — it knows NOTHING about de Broglie, yet lands on the same value.
```

### Listing 4 — Why Bohr's orbits are de Broglie standing waves
```text
Stable-orbit (standing-wave) condition:
  the circumference must hold a whole number of de Broglie wavelengths

  2 * pi * r = n * lambda           (n = 1, 2, 3, ...)

Substitute the de Broglie wavelength  lambda = h / (m * v):

  2 * pi * r = n * h / (m * v)

Rearrange:

  m * v * r = n * h / (2 * pi)

The left-hand side (m * v * r) is the electron's angular momentum, L.
So:

  L = n * h / (2 * pi)

This is EXACTLY Bohr's quantisation postulate — but now DERIVED from a wave
picture instead of simply assumed. Only orbits whose circumference fits a whole
number of wavelengths form a stable standing wave; all others self-destruct by
destructive interference. The quantised energy levels are the resonances of the
confined electron-wave.
```

### Listing 5 — Why matter waves are invisible for everyday objects
```text
Compare the de Broglie wavelength of an electron with that of a person.

Slow electron (accelerated through ~100 V), v approx 6.0 x 10^6 m/s:
  lambda = h / (m_e * v)
         = (6.626 x 10^-34) / ((9.109 x 10^-31) * (6.0 x 10^6))
         approx 1.2 x 10^-10 m   (about one atomic spacing -> diffraction visible)

A 70 kg person walking at 1 m/s:
  lambda = h / (m * v)
         = (6.626 x 10^-34) / (70 * 1)
         approx 9.5 x 10^-36 m   (about 10^25 times smaller than an atom)

CONCLUSION: diffraction is only observable when the wavelength is comparable to
the size of the opening or atomic spacing (roughly lambda/width > 1/10). For
macroscopic objects lambda is so absurdly small that no opening could ever reveal
it — which is why we never see people diffract through doorways.
```

### Listing 6 — Comparison of the two confirming experiments
| Feature | Davisson & Germer (1927) | G.P. Thomson & Reid (1927) |
|---------|--------------------------|----------------------------|
| Location | Bell Labs, New York | University of Aberdeen, Scotland |
| Electron energy | slow (~54 eV) | fast (~thousands of eV) |
| Geometry | reflection off a single crystal surface | transmission through a thin film |
| Target | large single-crystal nickel | thin polycrystalline foils (gold, Al, Pt) |
| Pattern observed | intensity peaks at set angles | concentric rings on a photographic plate |
| Analogy | crystal-surface diffraction | X-ray powder (Debye–Scherrer) diffraction |
| Result | lambda matched de Broglie to ~1.2% | lambda matched de Broglie to ~5% |
| Nobel Prize | 1937 (Davisson; Germer omitted) | 1937 (shared with Davisson) |

### Listing 7 — NESA syllabus dot-points covered by this episode
Focus area: Matter, energy and the cosmos — Modelling the atom (PY-12-04).

| NESA dot-point (exact wording) | Where the episode addresses it |
|--------------------------------|--------------------------------|
| Explain how standing waves can be used to represent electrons in stationary energy levels using qualitative data | The standing-wave electron / harmonics-of-a-string argument; Listing 4 |
| Use lambda = h/mv to relate wave and particle properties of matter | de Broglie equation throughout; Listings 1 and 3 |
| Explain why the production of electron diffraction patterns provides evidence for electrons behaving as waves | Davisson–Germer peaks and G.P. Thomson rings; two independent confirmations |
| Explain how the proposal of electrons as waves in atoms addresses a limitation of the stationary energy level model | Standing-wave orbits derive Bohr's quantisation that the stationary energy level model merely assumed |
| Identify the limitations of the stationary energy level model of the atom | Bohr's rule was unjustified, mixed classical + quantum, only worked for one-electron atoms; Schrödinger replaces it |
| Explain how the stationary energy level model uses a mixture of classical physics and quantum physics | Bohr's planetary orbits (classical) plus quantised angular momentum (quantum) |

Note on terminology: NESA (2025 syllabus, implemented 2027) calls the Bohr-type model
the "stationary energy level model of the atom." Use that exact phrase in exam answers.
The de Broglie relationship lambda = h/mv is on the NESA Physics data sheet.
