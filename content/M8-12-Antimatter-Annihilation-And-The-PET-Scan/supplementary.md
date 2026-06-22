---
title: "Supplementary Materials — Antimatter, Annihilation, and the PET Scan"
module: M8
lesson: "12"
script: script.md
---

# Supplementary Materials

Key equations, decay equations, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it is the read-along reference. The narration refers to each listing by label only.

### Listing 1 — Energy of an annihilation photon (worked example)
```text
Find: energy of EACH gamma photon when an electron and positron annihilate at rest.

Reaction:   e⁻ + e⁺ → γ + γ   (two photons, opposite directions, ≈180° apart)

Data:   m_e = 9.11 × 10⁻³¹ kg
        c   = 3.0 × 10⁸ m s⁻¹
        1 MeV = 1.602 × 10⁻¹³ J

Step 1 — Total energy released = rest energy of BOTH particles:
        E_total = 2 m_e c²
        E_total = 2 × (9.11 × 10⁻³¹) × (3.0 × 10⁸)²
        E_total = 2 × (9.11 × 10⁻³¹) × (9.0 × 10¹⁶)
        E_total = 1.64 × 10⁻¹³ J

Step 2 — Two photons share it equally → each photon:
        E_photon = ½ × (1.64 × 10⁻¹³)
        E_photon = 8.2 × 10⁻¹⁴ J

Step 3 — Convert one photon to MeV:
        E_photon = (8.2 × 10⁻¹⁴) ÷ (1.602 × 10⁻¹³)
        E_photon = 0.511 MeV

Answer:  each photon = 8.2 × 10⁻¹⁴ J = 0.511 MeV
         total released = 1.64 × 10⁻¹³ J = 1.022 MeV = 2 m_e c²
```

### Listing 2 — Energy released in C-11 beta-plus decay (worked example)
```text
Reaction:   ¹¹₆C → ¹¹₅B + ⁰₊₁e + ν    (positron + neutrino emitted)

Atomic masses (u):   ¹¹₆C = 11.011 43
                     ¹¹₅B = 11.009 31
                     electron / positron = 0.000 55 each
Conversion:          1 u ≡ 931.5 MeV/c²   (multiply by 931.5 and STOP)

These are ATOMIC masses (include orbital electrons), so the electrons
must be tracked explicitly. Neutrino mass is neglected.

Mass before (C-11 nucleus) = atomic mass − 6 electrons:
        = 11.011 43 − (6 × 0.000 55)
        = 11.008 13 u

Mass after (B-11 nucleus + emitted positron), via electron bookkeeping:
        = [11.009 31 − (4 × 0.000 55)]
        = 11.007 11 u

Mass lost (Δm):
        Δm = 11.008 13 − 11.007 11
        Δm = 0.001 02 u

Energy released (multiply by 931.5; do NOT divide by c² as well):
        E = 0.001 02 × 931.5
        E ≈ 0.95 MeV

Answer:  ≈ 0.95 MeV, shared as kinetic energy of the positron and neutrino.
         (The emitted positron then annihilates → two 0.511 MeV photons: Listing 1.)
```

### Listing 3 — Key equations for this episode
```text
Beta-plus decay (general):   ¹₁p → ¹₀n + ⁰₊₁e + ν
   • mass number A unchanged; atomic number Z falls by 1

Pair production:             γ → e⁻ + e⁺
   • energy → mass, near a nucleus
   • two PARTICLES made to conserve CHARGE
   • threshold E_γ ≥ 1.022 MeV = 2 m_e c²

Annihilation:                e⁻ + e⁺ → γ + γ
   • mass → energy
   • two PHOTONS made to conserve MOMENTUM (pair at rest, total p ≈ 0)
   • E_total = 2 m_e c² = 1.022 MeV ; each photon = m_e c² = 0.511 MeV

Mass–energy equivalence:     E = mc²
Mass→energy shortcut:        1 u ≡ 931.5 MeV/c²
```

### Listing 4 — Particle properties and key constants
| Quantity | Symbol | Value |
|----------|--------|-------|
| Electron / positron rest mass | m_e | 9.11 × 10⁻³¹ kg (= 0.000 55 u) |
| Electron rest energy | m_e c² | 0.511 MeV |
| Annihilation photon energy (each) | E_photon | 0.511 MeV |
| Total annihilation energy | 2 m_e c² | 1.022 MeV |
| Pair-production threshold | 2 m_e c² | 1.022 MeV |
| Electron charge | −e | −1.6 × 10⁻¹⁹ C |
| Positron charge | +e | +1.6 × 10⁻¹⁹ C |
| Speed of light | c | 3.0 × 10⁸ m s⁻¹ |
| Atomic mass unit | u | 1.661 × 10⁻²⁷ kg ≡ 931.5 MeV/c² |
| 1 MeV in joules | — | 1.602 × 10⁻¹³ J |

### Listing 5 — The PET imaging chain (the "TRACER" memory hook)
| Step | TRACER | What happens |
|------|--------|--------------|
| 1 | **T**racer injected | Short-lived β⁺ emitter (e.g. F-18 in FDG, a glucose analogue) injected into the patient |
| 2 | **R**eaches active tissue | FDG concentrates in metabolically active tissue (tumours, active brain) because it behaves like glucose |
| 3 | **A**nnihilation | Each positron travels a few mm, meets an electron, and annihilates → two 0.511 MeV γ photons, ≈180° apart |
| 4 | **C**oincidence detection | A surrounding ring of detectors registers the two photons simultaneously, on opposite sides |
| 5 | **E**stablish the line | The line joining the two detectors — the "line of response" — passes through the annihilation point |
| 6 | **R**econstruct | A computer combines millions of lines of response into a 3-D image of tracer concentration = metabolic map |

### Listing 6 — Production routes and named scientists
| Item | Detail |
|------|--------|
| Production route 1 — Beta-plus decay | Proton-rich nucleus: p → n + e⁺ + ν; e.g. ¹¹₆C → ¹¹₅B + e⁺ + ν, or ²²₁₁Na → ²²₁₀Ne + e⁺ + ν |
| Production route 2 — Pair production | High-energy γ near a nucleus: γ → e⁻ + e⁺ (threshold 1.022 MeV) |
| Predicted by | Paul Dirac (1928–1931), from negative-energy solutions of his relativistic quantum equation |
| Discovered by | Carl Anderson (1932–1933), cosmic-ray track curving opposite to an electron in a cloud chamber |
| Real PET isotopes | Fluorine-18 (≈110 min half-life), Carbon-11, Nitrogen-13, Oxygen-15 |
