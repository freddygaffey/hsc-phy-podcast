---
title: "Supplementary Materials — Rutherford's Gold Foil Experiment"
kind: case-study
script: script.md
---

# Supplementary Materials

### Listing 1 — The Rutherford scattering formula
```text
dσ/dΩ = ( Z1 · Z2 · e^2 / (4 · E_k) )^2 · csc^4(θ / 2)

where:
  dσ/dΩ = differential scattering cross-section (scattering probability per solid angle)
  Z1    = charge number of the alpha particle = 2
  Z2    = charge number of the target nucleus (gold ≈ 79)
  e     = elementary charge = 1.602 × 10^-19 C
  E_k   = kinetic energy of the incoming alpha particle
  θ     = scattering angle (0° = straight through, 180° = straight back)

Key behaviour:
  csc^4(θ/2) is very large for small θ  → most particles barely deflect
  csc^4(θ/2) is small but NON-ZERO at large θ → rare large-angle backscatter
```

### Listing 2 — The four predictions confirmed by Geiger & Marsden (1912–1913)
```text
Number of particles scattered at angle θ is:
  1. proportional to csc^4(θ / 2)        (the angular dependence)
  2. proportional to foil thickness      (linear in thickness)
  3. proportional to (nuclear charge)^2  (proportional to Z2^2)
  4. inversely proportional to v^4       (1 / particle velocity, fourth power)

All four were verified experimentally → strong confirmation of the nuclear model.
```

### Listing 3 — Coulomb repulsion and the head-on "distance of closest approach"
```text
At a head-on collision the alpha particle is momentarily stopped.
All its kinetic energy has converted to electric potential energy:

  E_k = k · (Z1 · e) · (Z2 · e) / r_min

Rearranged for the distance of closest approach:

  r_min = k · Z1 · Z2 · e^2 / E_k

where:
  k     = Coulomb constant = 8.99 × 10^9 N·m^2·C^-2
  Z1    = 2 (alpha)
  Z2    = 79 (gold)
  E_k   = alpha kinetic energy ≈ 7.7 MeV = 7.7 × 10^6 × 1.602 × 10^-19 J

This r_min sets an UPPER LIMIT on the nuclear radius (≈ 3 × 10^-14 m for gold,
i.e. ~30 fm; see the worked calculation in Listing 4),
because the alpha clearly never penetrates inside the nucleus.
```

### Listing 4 — Worked example: distance of closest approach for an alpha on gold
```text
GIVEN:
  Z1 = 2, Z2 = 79
  e  = 1.602 × 10^-19 C
  k  = 8.99 × 10^9 N·m^2·C^-2
  E_k = 7.7 MeV = 7.7 × 10^6 × 1.602 × 10^-19 J = 1.233 × 10^-12 J

STEP 1 — numerator k · Z1 · Z2 · e^2:
  e^2 = (1.602 × 10^-19)^2 = 2.566 × 10^-38 C^2
  Z1 · Z2 = 2 × 79 = 158
  k · Z1 · Z2 · e^2 = 8.99 × 10^9 × 158 × 2.566 × 10^-38
                    = 3.645 × 10^-26 N·m^2

STEP 2 — divide by E_k:
  r_min = 3.645 × 10^-26 / 1.233 × 10^-12
        = 2.96 × 10^-14 m
        ≈ 3 × 10^-14 m  (≈ 30 femtometres)

INTERPRETATION:
  The gold nucleus must be SMALLER than ~3 × 10^-14 m (this r_min is an UPPER LIMIT,
  not the true nuclear radius — the alpha never quite reaches the nuclear surface).
  Compare to the atomic radius ~1.44 × 10^-10 m.
  Even using the upper-limit r_min, the atom is ~5000× larger than the nucleus;
  using the true nuclear radius the ratio is at least 10,000:1 → atom is mostly empty space.
```

### Listing 5 — Key numbers from the experiment

| Quantity | Value |
|----------|-------|
| Gold foil thickness | ≈ 100 nm (≈ 0.000004 cm, ~1000 atoms thick) |
| Alpha particle charge | +2e |
| Alpha particle mass | ≈ 4 atomic mass units |
| Alpha particle energy (radium C) | ≈ 7.7 MeV |
| Alpha particle speed | ≈ 1.6 × 10^7 m/s (~5% of c) |
| Deflected > 90° (gold foil, Geiger–Marsden) | ≈ 1 in 8,000 |
| Fraction passing nearly straight through | > 99.9% |
| Nucleus holds fraction of atom's mass | ≈ 99.9% |
| Atomic radius (order of magnitude) | ≈ 1.44 × 10^-10 m |
| Nuclear radius (upper limit, Rutherford) | ≈ 10^-14 m (10 fm) |
| Gold nuclear charge (modern, Z) | 79 (Rutherford estimated ~100) |
| Atom : nucleus size ratio | ≥ 10,000 : 1 |

### Listing 6 — Plum pudding model vs nuclear model

| Feature | Thomson plum pudding (1904) | Rutherford nuclear (1911) |
|---------|-----------------------------|----------------------------|
| Positive charge | spread evenly through whole atom | concentrated in tiny central nucleus |
| Mass distribution | spread evenly through whole atom | almost all in the nucleus |
| Electrons | embedded throughout positive sphere | out in surrounding (mostly empty) space |
| Predicted large-angle scattering | effectively impossible | rare but expected (single close encounter) |
| Explains backscatter? | No | Yes |
| Known weakness | wrong charge distribution | orbiting electrons should radiate and collapse (fixed by Bohr, 1913) |
