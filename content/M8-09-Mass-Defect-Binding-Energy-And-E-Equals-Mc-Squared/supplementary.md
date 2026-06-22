---
title: "Supplementary Materials — Mass Defect, Binding Energy, and E = mc^2"
module: M8
lesson: "09"
script: script.md
---

# Supplementary Materials

Worked nuclear-energy calculations for this episode. Nothing here is spoken in the audio — it is the read-along reference. Symbols: u = atomic mass unit; Δm = mass defect; E_b = binding energy; A = mass number (number of nucleons); c = speed of light. Key conversion: 1 u ↔ 931.5 MeV (the data sheet writes it as 931.5 MeV/c² — the c² is already built into the factor, so multiply by 931.5 and STOP).

### Listing 1 — Binding energy of helium-4 (the canonical worked example)
```text
Goal: total binding energy and binding energy per nucleon of helium-4 (2 p, 2 n).

STEP 1 — mass of the separate constituents (atomic-mass bookkeeping)
  Use atomic masses and include 2 electrons; these cancel against the 2 electrons
  already inside the helium-4 ATOMIC mass, so the nuclear result is unaffected.
    2 × (proton + neutron + electron)
      = 2 × (1.007276 + 1.008665 + 0.000549)
      = 2 × 2.016490
      = 4.032980 u
  (Equivalently: 2 × H-1 atom + 2 × neutron = 2(1.007825) + 2(1.008665) = 4.032980 u.)

STEP 2 — mass defect
  helium-4 atomic mass = 4.002603 u
  Δm = 4.032980 − 4.002603 = 0.030377 u   (≈ 0.0304 u; ~0.75% of the nucleus)

STEP 3 — total binding energy (fast way, via 931.5)
  E_b = Δm × 931.5 = 0.030377 × 931.5 = 28.30 MeV
  ⚠ DO NOT also divide by c²: the "per c²" is already in the 931.5 factor.

  Cross-check (long way, via kilograms and E = mc²):
    Δm = 0.030377 × 1.661 × 10^-27 = 5.046 × 10^-29 kg
    E_b = Δm c² = (5.046 × 10^-29)(3.0 × 10^8)² = 4.54 × 10^-12 J
    In MeV: 4.54 × 10^-12 ÷ 1.602 × 10^-13 = 28.3 MeV   ✓ (agrees)

STEP 4 — binding energy per nucleon
  E_b / A = 28.30 / 4 = 7.07 MeV per nucleon
  (Landmark value: helium-4 is unusually tightly bound for so light a nucleus.)
```

### Listing 2 — Masses and constants (data sheet / atomic-mass tables)
| Quantity | Symbol | Value |
|----------|--------|-------|
| Atomic mass unit | 1 u | 1.661 × 10⁻²⁷ kg ↔ 931.5 MeV/c² |
| Proton mass | m_p | 1.007276 u |
| Neutron mass | m_n | 1.008665 u |
| Electron mass | m_e | 0.000549 u |
| Hydrogen-1 (atom) | ¹H | 1.007825 u |
| Deuterium, H-2 (atom) | ²H | 2.014102 u |
| Tritium, H-3 (atom) | ³H | 3.016049 u |
| Helium-4 (atom) | ⁴He | 4.002603 u |
| Speed of light | c | 3.0 × 10⁸ m s⁻¹ (c² ≈ 9.0 × 10¹⁶) |
| MeV → joules | 1 MeV | 1.602 × 10⁻¹³ J |
| Iron-56 peak | — | ≈ 8.8 MeV per nucleon (most stable nucleus) |

### Listing 3 — Deuterium–tritium fusion (≈ 17.6 MeV)
```text
Reaction:   ²H (deuterium) + ³H (tritium) → ⁴He + n   + energy
(Electrons balance: 1 + 1 on the left, 2 + 0 on the right — atomic masses work directly.)

Mass of reactants:
  ²H + ³H = 2.014102 + 3.016049 = 5.030151 u

Mass of products:
  ⁴He + n = 4.002603 + 1.008665 = 5.011268 u

Mass lost:
  Δm = 5.030151 − 5.011268 = 0.018883 u   (≈ 0.0189 u)

Energy released:
  E = Δm × 931.5 = 0.018883 × 931.5 ≈ 17.6 MeV   per reaction

Consistent with the curve: ⁴He sits high on the binding-energy-per-nucleon curve,
so forming it from lighter nuclei releases energy. (Per unit mass, fusion beats fission.)
```

### Listing 4 — Uranium-236 fission, two methods agree (≈ 160 MeV)
```text
Reaction:   ²³⁶U → ¹⁴⁸La + ⁸⁵Br + 3n   + energy
(Check: A = 148 + 85 + 3 = 236 ✓;  Z = 57 + 35 = 92 ✓)

METHOD A — binding-energy method  (E_released = ΣBE(products) − BE(reactant))
  BE(U-236)  = 1790.415 MeV
  BE(La-148) = 1213.125 MeV
  BE(Br-85)  =  737.291 MeV
  Σ BE(fragments) = 1213.125 + 737.291 = 1950.416 MeV
  E_released = 1950.416 − 1790.415 = 160.0 MeV

METHOD B — mass-difference method  (E_released = Δm c²)
  Mass(U-236)  = 3.919629 × 10⁻²⁵ kg
  Mass(La-148) = 2.456472 × 10⁻²⁵ kg
  Mass(Br-85)  = 1.410057 × 10⁻²⁵ kg
  Mass(n)      = 1.674924 × 10⁻²⁷ kg
  Σ mass(products) = 2.456472e-25 + 1.410057e-25 + 3(1.674924e-27)
                   = 3.916777 × 10⁻²⁵ kg
  Δm = 3.919629e-25 − 3.916777e-25 = 2.852 × 10⁻²⁸ kg
  E = Δm c² = (2.852e-28)(2.998e8)² = 2.563 × 10⁻¹¹ J
            = 2.563e-11 ÷ 1.602e-13 = 160.0 MeV

BOTH METHODS ≈ 160 MeV (agree to within rounding) — more binding energy in the
products is the same physics as less mass in the products. A uranium fission releases
~10× the energy of one D-T fusion (far more nucleons), but far less per unit mass.
```
