---
title: "Supplementary Materials — H-R Diagrams, Stellar Lives, and the Origin of the Elements"
module: M8
lesson: "14"
script: script.md
---

# Supplementary Materials

Key equations, reaction sets, worked numerical solutions, and reference data for this episode. Nothing here is spoken in the audio — it is the read-along reference.

### Listing 1 — Reading the H-R diagram (axes, regions, size logic)
```text
AXES
  Vertical axis   = luminosity (power radiated), BRIGHT at TOP, dim at bottom
                    (sometimes drawn as absolute magnitude)
  Horizontal axis = surface temperature OR spectral class (O B A F G K M)
  TRAP: temperature INCREASES TO THE LEFT
        → hot, blue O stars on the LEFT ; cool, red M stars on the RIGHT
        Hook: "Hot is on the left, like the start of a page."

THREE REGIONS  (Hook: "My Giant White dog runs Left when it's Hot")
  Main sequence       = diagonal band, top-left (hot, bright) → bottom-right (cool, dim)
                        ALL fusing hydrogen → helium in cores; ~90% of stars, ~90% of a star's life
  Giants/Supergiants  = ABOVE main sequence (upper right): COOL but BRIGHT → because HUGE (large area)
  White dwarfs        = BELOW main sequence (lower left): HOT but DIM → because TINY (~Earth-sized)

READING SIZE OFF THE DIAGRAM (the mark-earning reasoning)
  Luminosity depends on BOTH temperature AND surface area (radius).
  Stefan-Boltzmann (qualitative at HSC):   L ∝ R² T⁴
  → Two stars at SAME temperature (same vertical line) but different luminosity
    MUST differ in SIZE; the more luminous one is the larger.
```

### Listing 2 — Worked example: mass lost in one pp-chain fusion step
```text
Q: Step 1 of the pp chain releases E = 1.44 MeV. How much mass is lost?

Step 1 — convert energy to joules
  E = 1.44 MeV = 1.44 × 10^6 eV × (1.6 × 10^-19 J eV^-1)
    = 2.3 × 10^-13 J

Step 2 — rearrange E = mc²  for mass
  m = E / c²

Step 3 — substitute  (c = 3.0 × 10^8 m s^-1,  c² = 9.0 × 10^16)
  m = (2.3 × 10^-13 J) / (9.0 × 10^16 m² s^-2)
    = 2.56 × 10^-30 kg

ANSWER:  m ≈ 2.6 × 10^-30 kg per reaction.
  Tiny per step — but the Sun holds ~10^57 protons, powering it ~10 billion years.
  Mark-earning step: convert eV → J FIRST, then rearrange E = mc².
```

### Listing 3 — Main-sequence nucleosynthesis: pp chain and CNO cycle
```text
PROTON-PROTON (pp) CHAIN  — dominant in Sun-mass and smaller stars; needs only protons
  Hook for the 3 steps: "Pair, Pickup, Pair-up"
  1 (Pair):    ¹₁H + ¹₁H  →  ²₁H + e⁺ + ν        (+1.44 MeV)   [proton → neutron, beta-plus]
  2 (Pickup):  ²₁H + ¹₁H  →  ³₂He + γ            (+5.49 MeV)
  3 (Pair-up): ³₂He + ³₂He →  ⁴₂He + 2 ¹₁H       (+12.9 MeV)
  NET:  4 ¹₁H → ⁴₂He + 2e⁺ + 2ν + γ              (≈ +26.7 MeV)

CNO CYCLE  — dominant in stars hotter / more massive than the Sun (> ~1.3 M_sun)
  C, N, O act as CATALYSTS: consumed then REGENERATED — NOT used up, NOT fuel.
  ¹²₆C + ¹₁H → ¹³₇N + γ
  ¹³₇N      → ¹³₆C + e⁺ + ν
  ¹³₆C + ¹₁H → ¹⁴₇N + γ
  ¹⁴₇N + ¹₁H → ¹⁵₈O + γ
  ¹⁵₈O      → ¹⁵₇N + e⁺ + ν
  ¹⁵₇N + ¹₁H → ¹²₆C + ⁴₂He      (carbon-12 regenerated)
  NET:  4 ¹₁H → ⁴₂He + 2e⁺ + 2ν + γ   — IDENTICAL net products to the pp chain

DIFFERENCE (exam): pathway, core temperature required, and CNO's need for pre-existing
  carbon — NOT the products. Both balance A and Z across every arrow.

TRIPLE-ALPHA (helium → carbon, in red giants):
  ⁴₂He + ⁴₂He ⇌ ⁸₄Be + γ ;  ⁸₄Be + ⁴₂He → ¹²₆C + γ   (Be-8 unstable; needs 3 alphas)
```

### Listing 4 — Why iron: model extended-response answer (binding-energy curve)
```text
Q: Use the binding-energy-per-nucleon curve to explain why iron is the heaviest
   element produced by fusion in a star.

MODEL ANSWER (mark-earning chain):
  • Fusion releases energy only when the product has a HIGHER binding energy per
    nucleon than the reactants — i.e. while moving UP the curve toward its peak.
  • The peak is at iron-56 (≈ 8.8 MeV per nucleon), the most stable nucleus.
  • Up to iron, each fusion step climbs the curve and RELEASES energy, sustaining
    the star against gravity.
  • Fusing iron into a heavier nucleus means moving DOWN the right side of the curve
    to a LOWER binding energy per nucleon → requires a NET INPUT of energy.
  • A star cannot power itself this way, so fusion HALTS at iron.
  • With no fusion to supply radiation pressure, the iron core collapses under gravity
    → the star explodes as a supernova.
  • Elements HEAVIER than iron are made in the supernova by rapid neutron capture.

WEAK ANSWER (avoid): "Big stars explode and small stars don't; iron is stable."
  — never invokes the curve, asserts stability without a mechanism. Band 4.
```

### Listing 5 — Stellar death: the two mass-set paths
```text
Hook: "Light goes quiet, heavy goes bang."

~1 SOLAR MASS  (e.g. the Sun)  — ends QUIET
  core H exhausted → core contracts & heats → H fuses in a SHELL around inert He core
  → outer layers expand & cool → RED GIANT  (up-and-right on H-R diagram)
  → He ignites (helium flash, ~3.5 × 10^8 °C) → triple-alpha: 3 ⁴He → ¹²C
  → outer layers shed as a PLANETARY NEBULA
  → bare carbon core left = WHITE DWARF (Earth-sized, no fusion; lower-left on H-R)
  → slowly cools toward a black dwarf
  H-R track: main sequence → giant region (up/right) → white-dwarf region (down/left)

> ~8 SOLAR MASSES  — ends with a BANG
  fuses successively heavier elements in concentric SHELLS ("onion"): H→He→C→O→Si→Fe
  → builds an IRON core
  → iron is at the binding-energy peak: fusing it would ABSORB energy → fusion HALTS
  → no radiation pressure → core collapses catastrophically
  → infalling layers rebound → SUPERNOVA (Type II, hydrogen lines present)
  → remnant core < ~3 M_sun → NEUTRON STAR ;  > ~3 M_sun → BLACK HOLE
```

### Listing 6 — Origin of the elements: the three tiers
```text
Hook: "Bang, Burn, Boom."

  BANG  — Big Bang nucleosynthesis: hydrogen (~75%), helium (~25%), trace lithium. NOTHING heavier.
  BURN  — stellar FUSION in cores: all elements from carbon UP TO IRON-56.
          (Only up to iron — past iron, fusion absorbs energy: binding-energy peak.)
  BOOM  — SUPERNOVAE: all elements HEAVIER than iron, via rapid neutron capture,
          then scattered into space to seed new stars, planets and life.

TRAP: "Iron is the heaviest element in the universe" is FALSE.
  Iron is the heaviest element made by FUSION. Heavier elements (gold, uranium…)
  are made in supernovae by neutron capture. Always keep the qualifier "by fusion."
```

### Listing 7 — Spectral classes: temperature, colour, key feature
| Class | Surface temp (K) | Colour      | Key spectral feature             |
|-------|------------------|-------------|----------------------------------|
| O     | 28 000–50 000    | Blue        | Ionised helium lines, strong UV  |
| B     | 10 000–28 000    | Blue        | Neutral helium lines             |
| A     | 7 500–10 000     | Blue-white  | Strong hydrogen lines            |
| F     | 6 000–7 500      | White       | Strong metal lines, weak H       |
| G     | 5 000–6 000      | Yellow      | Ionised calcium lines (the Sun)  |
| K     | 3 500–5 000      | Orange      | Neutral metals dominate          |
| M     | 2 500–3 500      | Red         | Molecular lines dominate         |

Mnemonic for the order O B A F G K M: "Oh Be A Fine Guy, Kiss Me." (Hottest/blue → coolest/red.)

### Listing 8 — Constants and key stellar values
| Quantity                                   | Value                                      |
|--------------------------------------------|--------------------------------------------|
| Speed of light, c                          | 3.0 × 10⁸ m s⁻¹                            |
| Elementary charge / 1 eV                   | 1.6 × 10⁻¹⁹ C  /  1 eV = 1.6 × 10⁻¹⁹ J     |
| Mass-energy of 1 atomic mass unit (u)      | 931.5 MeV  (1 u = 1.661 × 10⁻²⁷ kg)        |
| Binding-energy peak (iron-56)              | ≈ 8.8 MeV per nucleon                      |
| Binding energy per nucleon, helium-4       | ≈ 7.08 MeV per nucleon                     |
| pp-chain step energies                     | 1.44, 5.49, 12.9 MeV (net ≈ 26.7 MeV)      |
| Sun: spectral class / surface temperature  | G2 / ~5 800 K                              |
| Sun: main-sequence lifetime / proton count | ~10 billion yr / ~10⁵⁷ protons             |
| White-dwarf / supernova mass threshold     | < ~8 M_sun → white dwarf ; > ~8 → supernova |
| Remnant-core threshold                     | < ~3 M_sun → neutron star ; > ~3 → black hole |
| H-R diagram authors / dates                | Hertzsprung (~1911), Russell (~1913)       |
