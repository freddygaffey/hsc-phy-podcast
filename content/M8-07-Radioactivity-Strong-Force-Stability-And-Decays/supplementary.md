---
title: "Supplementary Materials — Radioactivity: The Strong Force, Nuclear Stability, and the Three Decays"
module: M8
lesson: "07"
script: script.md
---

# Supplementary Materials

Key equations, decay bookkeeping, worked numerical solutions, and reference data for this episode. Nothing here is spoken in the audio — it is the read-along reference.

### Listing 1 — Alpha decay of uranium-238: balanced equation and energy released
```text
Equation:
    238/92 U  →  234/90 Th  +  4/2 He  +  energy

Conservation check:
    mass number A:   238 = 234 + 4      ✓
    atomic number Z:  92 = 90 + 2       ✓   (Z = 90 is thorium)

Masses (atomic mass units, u):
    m(238/92 U)   = 238.05079 u
    m(234/90 Th)  = 234.04363 u
    m(4/2 He)     =   4.00260 u

Mass of products:
    234.04363 + 4.00260 = 238.04623 u

Mass defect (mass lost):
    Δm = 238.05079 − 238.04623 = 0.00456 u

Energy released (using 1 u ↔ 931.5 MeV):
    E = Δm × 931.5
      = 0.00456 × 931.5
      ≈ 4.25 MeV
    (released as kinetic energy of the alpha particle and the recoiling Th nucleus)

Note: the quoted masses are ATOMIC masses (electrons included).
In alpha decay the electron counts cancel, so no correction is needed.
```

### Listing 2 — Beta-minus decay energy: lead-210 → bismuth-210 (electron masses must be tracked)
```text
Equation:
    210/82 Pb  →  210/83 Bi  +  0/−1 e  +  ν̄  +  energy

Atomic masses (u):
    m(Pb-210, atomic) = 209.98419 u
    m(Bi-210, atomic) = 209.98412 u
    m(electron)       =   0.00055 u

Because these are ATOMIC masses, in beta decay the electron counts do NOT
fully cancel (Z changes by 1), so track them:

    Initial nuclear mass = 209.98419 − 82(0.00055) = 209.93909 u

    Final mass = [Bi-210 nuclear mass] + emitted electron
               = (209.98412 − 83×0.00055) + 0.00055
               = 209.98412 − 82×0.00055
               = 209.93902 u

Mass lost:
    Δm = 209.93909 − 209.93902 = 0.00007 u

Energy released:
    E = 0.00007 × 931.5 ≈ 0.065 MeV
    (antineutrino mass is negligible; energy is shared between the β⁻ and the ν̄,
     which is why β particles emerge with a CONTINUOUS range of energies)
```

### Listing 3 — Exam Q2: alpha decay of radium-226
```text
Radium-226 undergoes alpha decay.

Alpha decay rule:  A decreases by 4,  Z decreases by 2

    226/88 Ra  →  222/86 Rn  +  4/2 He

Conservation check:
    mass number:  226 = 222 + 4   ✓
    charge (Z):    88 = 86 + 2     ✓   (Z = 86 is radon)

Daughter nucleus: radon-222.
```

### Listing 4 — Exam Q5: beta-minus decay of carbon-14
```text
Carbon-14 undergoes beta-minus decay.

Beta-minus rule:  A unchanged,  Z increases by 1

    14/6 C  →  14/7 N  +  0/−1 e  +  ν̄

Underlying nucleon change:
    1/0 n  →  1/1 p  +  0/−1 e  +  ν̄   (a down quark → up quark, via the weak force / W boson)

Conservation check:
    mass number:  14 = 14 + 0          ✓
    charge (Z):    6 = 7 + (−1)         ✓   (Z = 7 is nitrogen)
    lepton number: 0 = 0 + (+1) + (−1)  ✓   (electron +1, antineutrino −1 → this forces the ν̄)
    mass-energy:   small Δm released as kinetic energy of the β⁻ and ν̄

Daughter nucleus: nitrogen-14.   (This is the decay used in radiocarbon dating.)
```

### Listing 5 — The four decay-bookkeeping rules ("alpha eats four and two, beta swaps a charge, gamma changes nothing")
| Decay | Change in A | Change in Z | What is emitted | Underlying nucleon change |
|-------|-------------|-------------|-----------------|---------------------------|
| Alpha (α) | −4 | −2 | helium-4 nucleus (⁴₂He) | — |
| Beta-minus (β⁻) | 0 | +1 | electron + antineutrino | neutron → proton (down→up quark) |
| Beta-plus (β⁺) | 0 | −1 | positron + neutrino | proton → neutron (up→down quark) |
| Gamma (γ) | 0 | 0 | high-energy photon | excited nucleus de-excites (no transmutation) |

### Listing 6 — Comparing the three radiations ("bouncer, punter, ghost")
| Property | Alpha (α) | Beta-minus (β⁻) | Gamma (γ) |
|----------|-----------|-----------------|-----------|
| Composition | helium-4 nucleus (2 p + 2 n) | fast electron (from nucleus) | high-energy photon (EM radiation) |
| Symbol | ⁴₂He | ⁰₋₁e | γ |
| Charge | +2 | −1 | 0 |
| Relative mass | ~4 u (massive) | ~1/1836 u (tiny) | 0 (massless) |
| Ionising power | very high | moderate | very low |
| Penetration | very low (paper / few cm air / dead skin) | moderate (~1 cm aluminium / ~1 m air) | very high (cm of lead / m of concrete) |
| Speed | ~5–7% of c (≈2×10⁷ m/s) | range, up to ~99% of c | c (it is light) |
| Deflection in B-field | curves (positive) | curves opposite, more sharply (negative) | not deflected (neutral) |

Inverse relationship: ionising power α > β > γ; penetration γ > β > α.

### Listing 7 — Key values, constants, names and dates
| Quantity / fact | Value or detail |
|-----------------|-----------------|
| Strong nuclear force range | ~10⁻¹⁵ m (≈1 femtometre); nearest-neighbour; repulsive at very short range |
| Mass–energy conversion | 1 u ↔ 931.5 MeV/c² |
| Atomic mass unit | 1 u = 1.6605 × 10⁻²⁷ kg |
| Speed of light | c = 3.0 × 10⁸ m/s |
| Mass–energy equivalence | E = Δm·c² ; mass number A = Z + N |
| Proton / neutron / electron mass | 1.007276 u / 1.008665 u / 0.00055 u |
| Stability cutoff | beyond Z ≈ 83 (bismuth) no neutron excess gives stability |
| Quark content | proton = uud, neutron = udd; β⁻: down→up, β⁺: up→down |
| Weak-force carriers | W boson (and Z boson) |
| Neutrino predicted | Wolfgang Pauli, 1930; named by Enrico Fermi; detected 1956 |
| U-238 α decay energy | ≈ 4.25 MeV |
