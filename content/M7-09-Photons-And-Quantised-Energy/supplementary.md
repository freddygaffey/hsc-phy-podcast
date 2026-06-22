---
title: "Supplementary Materials — Photons: Light as a Particle with Quantised Energy"
module: M7
lesson: "09"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it is the read-along reference. Constants used throughout: Planck's constant h = 6.63 × 10^-34 J s, speed of light c = 3.0 × 10^8 m s^-1, and 1 eV = 1.6 × 10^-19 J (all on the HSC Physics Data Sheet / Formulae Sheet except the eV conversion).

### Listing 1 — Photon energy: the three forms (E = hf, c = fλ, E = hc/λ)
```text
Photon energy (Planck relation):
    E = h f
        E = energy of ONE photon  (J)
        h = Planck's constant = 6.63 × 10^-34  (J s)
        f = frequency  (Hz = s^-1)

Wave relation (vacuum):
    c = f λ      →      f = c / λ
        c = 3.0 × 10^8 m s^-1
        λ = wavelength  (m)

Combined form (substitute f = c/λ into E = hf):
    E = h c / λ
        units:  (J s × m s^-1) / m  =  J  ✓

Proportionalities to memorise:
    E ∝ f          (higher frequency → higher-energy photon)
    E ∝ 1/λ        (shorter wavelength → higher-energy photon)
    "short wave, big punch"

Convert nm → m before substituting:  1 nm = 1 × 10^-9 m
```

### Listing 2 — The electron-volt (energy unit at this scale)
```text
Definition:
    1 eV = energy an electron gains across a potential difference of 1 V
         = e × V = (1.6 × 10^-19 C)(1 V)
    1 eV = 1.6 × 10^-19 J

Converting:
    joules → eV :  divide by 1.6 × 10^-19
    eV → joules :  multiply by 1.6 × 10^-19

Why use it: photon energies are ~10^-19 J — awkward in joules,
tidy in eV. Work functions (later episodes) are also quoted in eV.
```

### Listing 3 — Worked Example A: energy of a UV photon (λ = 3.00 × 10^-7 m)
```text
Want E, given λ  →  use  E = hc/λ

E = (6.63 × 10^-34 × 3.0 × 10^8) / (3.00 × 10^-7)

Numerator:  6.63 × 10^-34 × 3.0 × 10^8 = 1.989 × 10^-25

E = 1.989 × 10^-25 / 3.00 × 10^-7
E = 6.63 × 10^-19 J

In eV:  6.63 × 10^-19 / 1.6 × 10^-19 ≈ 4.1 eV

Method (mark-earning structure):
    1. write equation   2. substitute with units
    3. evaluate         4. convert to eV
```

### Listing 4 — Worked Example B: λ = 425 nm → frequency and energy (J and eV)
```text
Convert wavelength:
    425 nm = 4.25 × 10^-7 m

Frequency:
    f = c / λ = (3.0 × 10^8) / (4.25 × 10^-7)
    f = 7.06 × 10^14 Hz   (≈ 7.1 × 10^14 Hz)

Energy:
    E = h f = (6.63 × 10^-34)(7.06 × 10^14)
    E = 4.68 × 10^-19 J

In eV:
    E = 4.68 × 10^-19 / 1.6 × 10^-19
    E = 2.92 eV   (≈ 2.9 eV, a blue-violet photon)

Note: E = hf (via f) and E = hc/λ (direct) give the same answer.
```

### Listing 5 — Worked Example C: how many photons? (eye detection)
```text
Q: eye detects E_total = 2.00 × 10^-17 J of light at λ = 5.50 × 10^-7 m.
   How many photons is that?

Step 1 — energy of ONE photon:
    E_photon = hc/λ = (6.63 × 10^-34 × 3.0 × 10^8) / (5.50 × 10^-7)
             = 1.989 × 10^-25 / 5.50 × 10^-7
    E_photon = 3.62 × 10^-19 J

Step 2 — number of photons:
    n = E_total / E_photon
      = 2.00 × 10^-17 / 3.62 × 10^-19
    n ≈ 55 photons

Keep distinct:
    E_total (J)  ÷  E_photon (J)  →  n  (pure number)
    P (W = J s^-1) ÷ E_photon (J) →  N  (photons per second)
```

### Listing 6 — Worked Example D: equal-power lasers, different colour
```text
Q: red laser λ_red = 600 nm, blue laser λ_blue = 450 nm, SAME power P.
   Compare their rate of emitting photons.

Energy per photon ∝ 1/λ, so:
    E_blue / E_red = λ_red / λ_blue = 600 / 450 = 4/3
    (each blue photon carries 4/3 the energy of a red photon)

Photons per second at fixed power:
    N = P / E_photon      →      N ∝ λ
    N_red / N_blue = λ_red / λ_blue = 600 / 450 = 4/3 ≈ 1.33

Conclusion:
    The RED laser emits photons at the higher rate
    (≈ 1.33× as many per second) because each red photon
    carries less energy, so more are needed to deliver the same power.
    Equal power → redder light → more photons per second.
```

### Listing 7 — Reference values and key terms
| Quantity / item | Value / detail |
|---|---|
| Planck's constant, h | 6.63 × 10^-34 J s |
| Speed of light, c | 3.0 × 10^8 m s^-1 |
| Electron charge, e | 1.6 × 10^-19 C |
| 1 electron-volt | 1 eV = 1.6 × 10^-19 J |
| Photon | discrete, indivisible quantum (packet) of light energy = hf |
| Quantisation | energy exchanged only in whole multiples of hf (all-or-nothing) |
| Frequency → | sets the ENERGY of each photon (E = hf) |
| Intensity → | sets the NUMBER of photons per second (not photon energy) |
| Power relation | P = N × hf  (power = photons per second × energy per photon) |
| Max Planck | 1900: introduced E = hf for black-body radiation; called it a "mathematical trick" |
| Albert Einstein | 1905: treated quanta as real photons; photoelectric effect; Nobel Prize 1921 |
| 1 nm | 1 × 10^-9 m (convert before using c = fλ) |
