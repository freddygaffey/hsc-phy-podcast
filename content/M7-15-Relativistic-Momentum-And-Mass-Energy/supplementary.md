---
title: "Supplementary Materials — Relativistic Momentum, E = mc-squared, and the Cosmic Speed Limit"
module: M7
lesson: "15"
script: script.md
---

# Supplementary Materials

Key equations and worked numerical solutions for the relativity capstone. Nothing here is spoken in the audio. Symbols: p = momentum; m₀ = rest mass; m = relativistic mass; v = speed; c = speed of light = 3.0 × 10⁸ m s⁻¹ (c² = 9.0 × 10¹⁶ m² s⁻²); γ = Lorentz factor = 1 / √(1 − v²/c²); E = energy.

### Listing 1 — Relativistic momentum (equation and worked example)
```text
Relativistic momentum:   p = γ m₀ v = m₀ v / √(1 − v²/c²)
  γ = Lorentz factor (≥ 1);  m₀ = rest mass;  v = speed relative to observer
  Low speed (v ≪ c): γ → 1, so p → m₀v  (recovers Newton's p = mv)

WORKED: momentum of a proton at v = 0.6c   (m₀ = 1.67 × 10⁻²⁷ kg)
  √(1 − v²/c²) = √(1 − 0.6²) = √0.64 = 0.8        (so γ = 1.25)
  p = m₀ v / 0.8
    = (1.67 × 10⁻²⁷)(0.6 × 3.0 × 10⁸) / 0.8
    = (1.67 × 10⁻²⁷)(1.8 × 10⁸) / 0.8
    = 3.76 × 10⁻¹⁹ kg m s⁻¹
```

### Listing 2 — Why a mass cannot reach the speed of light
```text
Relativistic mass:   m = γ m₀ = m₀ / √(1 − v²/c²)

As v → c:
    v²/c² → 1   ⇒   √(1 − v²/c²) → 0   ⇒   γ → ∞
  ⇒ m = γ m₀ → ∞      (inertia grows without limit)
  ⇒ p = γ m₀ v → ∞    (momentum grows without limit)

Consequence chain (the band-6 answer):
  γ → ∞  ⇒  mass & momentum → ∞  ⇒  energy to accelerate further → ∞
  ⇒ reaching c needs INFINITE energy  ⇒  impossible for any object with mass.
  Only MASSLESS particles (photons, m₀ = 0) travel at exactly c.

⚠ "Mass increase" = increased inertia/momentum measured from an EXTERNAL frame.
   In its own rest frame nothing changes; the object does not physically swell.
   Conversion factor in E = mc² is c² (NOT c) — never drop the square.
```

### Listing 3 — E = mc²: power output of the Sun
```text
Mass–energy equivalence:   E = mc²   (and ΔE = Δm c²)

The Sun loses mass via fusion at  Δm/Δt = 4.4 × 10⁹ kg per second.
Power = energy per second = (mass lost per second) × c²

  P = (4.4 × 10⁹)(9.0 × 10¹⁶)
    = 4.0 × 10²⁶ W

(Answer is a power directly, in watts, because the mass loss was per second.)
```

### Listing 4 — E = mc²: annihilation and combustion (100% vs negligible)
```text
ELECTRON–POSITRON ANNIHILATION (100% of mass → energy)
  Each mass m = 9.11 × 10⁻³¹ kg; both annihilate.
  Total mass converted = 2 × 9.11 × 10⁻³¹ = 1.82 × 10⁻³⁰ kg
  E = mc² = (1.82 × 10⁻³⁰)(9.0 × 10¹⁶) = 1.64 × 10⁻¹³ J
  (≈ 1.022 MeV total = 2 × 0.511 MeV, the electron rest energy)
  → physics behind the PET scan (M8: case_pet_scans_antimatter)

CHEMICAL COMBUSTION (negligible fraction of mass → energy)
  Burn 1 tonne of coal, release ΔE ≈ 20 × 10⁹ J:
  Δm = ΔE / c² = (20 × 10⁹) / (9.0 × 10¹⁶) ≈ 2.2 × 10⁻⁷ kg
  (~0.2 milligram — far too small to weigh; why mass seemed conserved in chemistry)

Same equation, very different efficiency:
  annihilation 100%  >  nuclear fusion (small but significant)  >  combustion (negligible)
```

### Listing 5 — Particle-accelerator evidence: Newton vs relativity
```text
Give a proton ΔE = 11 GeV of energy   (1 GeV = 10⁹ × 1.6 × 10⁻¹⁹ J)
  ΔE = 11 × 10⁹ × 1.6 × 10⁻¹⁹ = 1.76 × 10⁻⁹ J

RELATIVITY — energy goes mostly into MASS:
  Δm = ΔE / c² = (1.76 × 10⁻⁹) / (9.0 × 10¹⁶) = 1.96 × 10⁻²⁶ kg
  Proton rest mass = 1.67 × 10⁻²⁷ kg
  ⇒ accelerated proton behaves as ~13 × its rest mass; speed stays below c. ✓ observed

NEWTON — if the same 11 GeV were ordinary kinetic energy ½mv²:
  v = √(2E/m) = √[ (2 × 1.76 × 10⁻⁹) / (1.67 × 10⁻²⁷) ]
    = 1.45 × 10⁹ m s⁻¹   (≈ 4.8 × the speed of light — IMPOSSIBLE) ✗

Above ~0.1c Newton fails; particles obey the relativistic equations exactly.
→ M8: case_particle_accelerators_quarks
```
