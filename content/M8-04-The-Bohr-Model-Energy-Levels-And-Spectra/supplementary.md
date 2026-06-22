---
title: "Supplementary Materials — The Bohr Model: Energy Levels, Spectra, and the Photon"
module: M8
lesson: "04"
script: script.md
---

# Supplementary Materials

Key equations, derivations, worked numerical solutions, and reference data for this episode. Nothing here is spoken in the audio — it is the read-along reference.

### Listing 1 — Worked Example A: the H-alpha (red Balmer) line, longest visible wavelength
```text
Rydberg equation:   1/λ = R_H (1/n_f² − 1/n_i²)

R_H = 1.097 × 10^7 m^-1

Longest λ ⇒ smallest energy gap ⇒ smallest transition.
Visible (Balmer) series lands on n_f = 2, so smallest gap is n_i = 3 → n_f = 2.

1/λ = 1.097 × 10^7 × (1/2² − 1/3²)
    = 1.097 × 10^7 × (1/4 − 1/9)
    = 1.097 × 10^7 × (0.2500 − 0.1111)
    = 1.097 × 10^7 × 0.1389
    = 1.524 × 10^6 m^-1

λ = 1 / (1.524 × 10^6) = 6.56 × 10^-7 m = 656 nm   (red H-alpha line)

Trap: R_H is in m^-1, so the equation returns 1/λ. Always take the reciprocal
to get λ. An answer ~10^6 is 1/λ, NOT a wavelength.
```

### Listing 2 — Worked Example B: the n = 4 → n = 1 photon (energy, frequency, wavelength)
```text
Level energies:   E_n = E_1 / n²     with E_1 = −13.6 eV

(a) E_4 = −13.6 / 4² = −13.6 / 16 = −0.85 eV

(b) Photon energy = |E_i − E_f| = |(−0.85) − (−13.6)| = 12.75 eV
    (Take the MAGNITUDE — subtracting the wrong way gives a meaningless
     negative frequency.)

    Convert to joules:  12.75 × 1.602 × 10^-19 = 2.04 × 10^-18 J

(c) Frequency, from E = hf:
    f = E / h = (2.04 × 10^-18) / (6.63 × 10^-34) = 3.08 × 10^15 Hz

(d) Wavelength, from c = fλ:
    λ = c / f = (3.0 × 10^8) / (3.08 × 10^15) = 9.7 × 10^-8 m ≈ 97 nm

    Lands on n = 1 ⇒ Lyman series ⇒ ultraviolet. Self-check agrees: 97 nm is UV.
```

### Listing 3 — Hydrogen energy levels (electron volts)
| Level n | Energy E_n (eV) | Notes                          |
|---------|-----------------|--------------------------------|
| 1       | −13.6           | ground state (most bound)      |
| 2       | −3.4            | first excited state            |
| 3       | −1.51           |                                |
| 4       | −0.85           |                                |
| 5       | −0.54           |                                |
| 6       | −0.38           |                                |
| ∞       | 0               | ionisation (electron free)     |

### Listing 4 — Exam Question 4 worked: n = 2 → n = 1 photon
```text
Given:  E_2 = −3.4 eV,  E_1 = −13.6 eV

Photon energy = |E_i − E_f| = |(−3.4) − (−13.6)| = 10.2 eV
Convert:  10.2 × 1.602 × 10^-19 = 1.63 × 10^-18 J

Use E = hc/λ  →  λ = hc / E
λ = (6.63 × 10^-34 × 3.0 × 10^8) / (1.63 × 10^-18)
  = (1.989 × 10^-25) / (1.63 × 10^-18)
  = 1.22 × 10^-7 m  ≈ 122 nm

Lands on n = 1 ⇒ Lyman series ⇒ ultraviolet.
```

### Listing 5 — Model extended-response answer (line emission spectrum of hydrogen)
```text
"In the Bohr model the electron in a hydrogen atom can occupy only certain
discrete stationary states, each with a fixed, quantised energy. When the atom
is excited, the electron is raised to a higher stationary state. It then
transitions back to a lower state, and in doing so the atom emits a single
photon. By the law of conservation of energy, the photon's energy is exactly
equal to the difference in energy between the two states — Planck's constant
times the photon's frequency equals the higher energy minus the lower energy.
Because the energy levels are discrete and unique to hydrogen, only photons of
specific frequencies, and therefore specific wavelengths, can be emitted. These
appear as a discrete set of bright lines — a line emission spectrum — rather
than a continuous spectrum."

Weak (band-4) answer for contrast: "Electrons jump down and give off light."
— states an observation with no mechanism, no quantisation, no conservation
of energy: almost no marks.
```

### Listing 6 — Key equations and constants for transitions
```text
E = hf                     photon energy = Planck's constant × frequency
c = fλ                     wave speed = frequency × wavelength
E = hc/λ                   photon energy = hc / wavelength
hf = E_i − E_f             photon energy = magnitude of level difference
1/λ = R_H(1/n_f² − 1/n_i²) Rydberg equation (emission: n_f < n_i)
E_n = E_1/n²               hydrogen level energy, E_1 = −13.6 eV

Constants (HSC data sheet):
h   = 6.63 × 10^-34 J·s     Planck's constant
c   = 3.0 × 10^8 m s^-1     speed of light
e   = 1.602 × 10^-19 C      elementary charge ( = 1 eV in joules)
1 eV = 1.602 × 10^-19 J     electron-volt to joule conversion
R_H = 1.097 × 10^7 m^-1     Rydberg constant
```

### Listing 7 — Hydrogen spectral series ("Little Birds Pause")
| Series  | Falls to level | Region        | Mnemonic letter |
|---------|----------------|---------------|-----------------|
| Lyman   | n = 1          | ultraviolet   | Little (L)      |
| Balmer  | n = 2          | visible       | Birds (B)       |
| Paschen | n = 3          | infrared      | Pause (P)       |

### Listing 8 — Bohr model limitations ("Hydrogen Is My Sole Why")
| Letter | Limitation                                                              |
|--------|-------------------------------------------------------------------------|
| H      | Works for **H**ydrogen / one-electron systems only                      |
| I      | Cannot explain relative **I**ntensities of spectral lines               |
| M      | Cannot explain line splitting — fine structure and the **M**agnetic (Zeeman) effect |
| S      | Is a **S**ticky mixture of classical and quantum physics (inelegant)    |
| W      | Never explains **W**hy orbits are stable / non-radiating — only asserts it |
