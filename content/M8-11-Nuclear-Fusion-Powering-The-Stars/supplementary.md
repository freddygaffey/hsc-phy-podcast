---
title: "Supplementary Materials — Nuclear Fusion: Powering the Stars"
module: M8
lesson: "11"
script: script.md
---

# Supplementary Materials

Key equations, derivations, worked numerical solutions, and reference data for this episode. Nothing here is spoken in the audio — it's the read-along reference for working you don't have time to write out at 4–5× speed.

### Listing 1 — Deuterium–tritium fusion: energy released (full working)
```text
Reaction (conserve mass number A on top, atomic number Z on bottom):
  ²₁H + ³₁H  →  ⁴₂He + ¹₀n + energy

Check conservation:
  A (top):    2 + 3 = 5   and   4 + 1 = 5   ✓
  Z (bottom): 1 + 1 = 2   and   2 + 0 = 2   ✓

STEP 1 — Mass defect  Δm = (Σ reactant masses) − (Σ product masses)
  reactants: m(²H) + m(³H) = 2.014102 + 3.016050 = 5.030152 u
  products:  m(⁴He) + m(n) = 4.002603 + 1.008665 = 5.011268 u
  Δm = 5.030152 − 5.011268 = 0.018884 u   (≈ 0.0188 u)

STEP 2 — Energy via the data-sheet shortcut  E (MeV) = Δm (u) × 931.5
  E = 0.018884 × 931.5 ≈ 17.6 MeV
  (textbook value ≈ 17.69 MeV using more precise intermediate masses)

  ⚠ TRAP: 931.5 already carries units MeV/c² — the c² is built in.
          Multiply by 931.5 and STOP. Do NOT also divide by c².

STEP 3 — Cross-check via E = Δm c² (the long route, in SI units)
  Δm = 0.018884 u × 1.6605 × 10⁻²⁷ kg/u ≈ 3.136 × 10⁻²⁹ kg
  E  = Δm c² = (3.136 × 10⁻²⁹)(3.0 × 10⁸)² ≈ 2.9 × 10⁻¹² J
  Convert: 2.9 × 10⁻¹² J ÷ 1.602 × 10⁻¹³ J/MeV ≈ 17.6 MeV   ✓

ANSWER: ≈ 17.6 MeV (≈ 2.9 × 10⁻¹² J) released per D–T fusion event.
The free neutron carries away most of this energy.
```

### Listing 2 — Masses and constants used
| Quantity | Value |
|----------|-------|
| Deuterium ²₁H | 2.014102 u |
| Tritium ³₁H | 3.016050 u |
| Helium-4 ⁴₂He | 4.002603 u |
| Neutron ¹₀n | 1.008665 u |
| Proton ¹₁H | 1.007276 u |
| Electron | 0.000549 u |
| Mass–energy conversion | 1 u ≡ 931.5 MeV/c² = 1.661 × 10⁻²⁷ kg |
| Speed of light | c = 3.0 × 10⁸ m s⁻¹ (c² ≈ 9.0 × 10¹⁶ m² s⁻²) |
| 1 MeV | 1.602 × 10⁻¹³ J |
| Iron-56 (curve peak) | ≈ 8.8 MeV/nucleon — most stable nucleus |

### Listing 3 — The proton–proton chain (stellar prototype, previewed; full treatment in M8-14)
```text
Net result: 4(¹₁H) → ⁴₂He + 2e⁺ + 2ν + energy   (≈ 26.7 MeV per He-4)

Step 1:  ¹₁H + ¹₁H → ²₁H + e⁺ + ν        (a proton → neutron, β⁺; ≈ 1.44 MeV)
Step 2:  ²₁H + ¹₁H → ³₂He + γ            (≈ 5.49 MeV)
Step 3:  ³₂He + ³₂He → ⁴₂He + 2(¹₁H)     (≈ 12.9 MeV)

Each step conserves mass number A and atomic number Z.
The positron (e⁺) is antimatter — it later annihilates with an electron (M8-12).
```

### Listing 4 — Why helium-4 is so tightly bound (the "why H→He is so energetic" number)
```text
Δm = [2 m(¹H) + 2 m(n)] − m(⁴He)   (atomic masses; electron masses cancel)
   = [2(1.007276) + 2(1.008665)] − 4.002603
   = 4.032882 − 4.002603 = 0.030379 u

Total binding energy:
  E_B = 0.030379 × 931.5 ≈ 28.3 MeV

Binding energy per nucleon:
  E_B / A = 28.3 ÷ 4 ≈ 7.07 MeV/nucleon
  (unusually high for such a light nucleus — close to the iron peak,
   which is why hydrogen → helium fusion releases so much energy)
```

### Listing 5 — Energy per unit mass: the comparison (fusion > fission ≫ chemical)
| Process | Typical energy per event | Basis of "more energy per unit mass" |
|---------|--------------------------|--------------------------------------|
| Chemical (burn 1 C atom) | ≈ 10 eV | Rearranges electrons only — the floor |
| Fission (one U-235 split) | ≈ 200 MeV | ~20 million × a chemical event per atom |
| Fusion (one D–T event) | ≈ 17.6 MeV | Fewer nucleons, steepest part of the curve → most energy *per nucleon* |

```text
Order PER UNIT MASS:  fusion  >  fission  ≫  chemical
Mnemonic: "Fusion Feeds the Cosmos"  (Fusion → Fission → Chemical, descending)

Note the basis: per single EVENT, fission (200 MeV) > fusion (17.6 MeV);
but per UNIT MASS / per nucleon, fusion wins. Always state the basis.
```

### Listing 6 — Key terms, names and dates
| Item | What to know |
|------|--------------|
| Coulomb barrier | Long-range electrostatic repulsion between the two positive nuclei — the obstacle to fusion |
| Strong nuclear force | Short-range (~10⁻¹⁵ m) attraction that binds nucleons once close; overcomes Coulomb repulsion |
| Temperature requirement | High KE to beat the Coulomb barrier; Sun's core ≈ 15 million K; Earth reactors need 100s of millions K |
| Pressure/density requirement | Frequent enough collisions to sustain the reaction; in a star, supplied by gravity |
| Iron limit | Fusion releases energy only up to iron-56; beyond iron it consumes energy → iron is heaviest fusion product |
| Arthur Eddington (~1926) | Proposed fusion of hydrogen as the Sun's energy source |
| Mark Oliphant (1932) | Australian; first observed fusion in the lab (with Rutherford); discovered tritium and helium-3 |
| Hans Bethe (1938) | Worked out the proton–proton chain and CNO cycle; Nobel Prize |
| ITER | Magnetic-confinement tokamak; leading Earth-based fusion candidate; not yet net-positive sustained |
