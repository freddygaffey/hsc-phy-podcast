---
title: "Supplementary Materials — Matter Waves: de Broglie, Electron Diffraction, and Standing Waves"
module: M8
lesson: "05"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it is the read-along reference. Constants used throughout: Planck's constant h = 6.63 × 10⁻³⁴ J·s; electron mass mₑ = 9.1 × 10⁻³¹ kg; elementary charge e = 1.6 × 10⁻¹⁹ C; 1 eV = 1.6 × 10⁻¹⁹ J; speed of light c = 3.0 × 10⁸ m·s⁻¹.

### Listing 1 — Why a person never diffracts (de Broglie wavelength of an athlete)
```text
de Broglie wavelength:  λ = h / p = h / (mv)

70 kg athlete sprinting at v = 10 m/s

p = mv = (70)(10) = 700 kg·m·s⁻¹

λ = h / p = (6.63 × 10⁻³⁴) / 700
  = 9.5 × 10⁻³⁷ m

Conclusion: ~10⁻³⁷ m is far smaller than a proton (~10⁻¹⁵ m) and
vastly smaller than any aperture, so diffraction is unobservable.
The wave exists — it is just undetectably small.

(Contrast: a 60 g tennis ball at 30 m/s → λ ≈ 3.7 × 10⁻³⁴ m. Same conclusion.)
```

### Listing 2 — de Broglie wavelength of an electron (≈100 V, direct λ = h/mv)
```text
Electron: m = 9.1 × 10⁻³¹ kg, accelerated through ~100 V → v ≈ 6.0 × 10⁶ m/s

p = mv = (9.1 × 10⁻³¹)(6.0 × 10⁶) = 5.5 × 10⁻²⁴ kg·m·s⁻¹

λ = h / p = (6.63 × 10⁻³⁴) / (5.5 × 10⁻²⁴)
  = 1.2 × 10⁻¹⁰ m

This is the same order of magnitude as the spacing between atoms in a
crystal lattice (~10⁻¹⁰ m = 1 Å), so a crystal acts as a ready-made
diffraction grating for electrons.

Diffraction rule of thumb: noticeable diffraction when λ ≳ (1/10) × aperture width.
```

### Listing 3 — The electron-diffraction evidence (key facts and figures)
| Experiment | Year | Method | Pattern observed | Result |
|------------|------|--------|------------------|--------|
| Davisson & Germer (USA) | 1927 | Beam of electrons reflected off a **single nickel crystal** (sample V = 54 V) in vacuum; intensity measured vs angle | Regular intensity **peaks** at specific angles | Wavelength from the diffraction angles **matched** λ = h/mv exactly |
| G. P. Thomson (England) | 1927 | Higher-energy electrons fired **through a thin polycrystalline metal foil** | Concentric **rings** (bullseye), analysed like X-ray diffraction | Wavelength again **matched** the de Broglie prediction |
| The Nobel irony | — | J. J. Thomson (Nobel **1897**) showed the electron is a **particle** (charge-to-mass ratio); his son G. P. Thomson (Nobel **1937**, with Davisson) showed it is a **wave** | — | "Father particle, son wave, both correct" — wave–particle duality |

### Listing 4 — The standing-wave condition for an allowed orbit
```text
Picture the electron as a wave wrapped around a circular orbit of radius r.

For the wave to join smoothly onto itself (form a standing wave) and persist,
the circumference must hold a WHOLE NUMBER of electron wavelengths:

    n λ = 2 π r          n = 1, 2, 3, …   (positive integer)

Equivalently:   λ = 2 π r / n

If the circumference is NOT a whole number of wavelengths, the wave returns
out of phase, interferes destructively with itself on each lap, and dies out
— so that orbit is forbidden.

Chain to quantisation:
  only discrete λ allowed
    → only discrete p allowed        (p = h / λ)
      → only discrete E allowed      (quantised energy levels = Bohr's stationary states)

Guitar-string analogy:  λ_n = 2 l / n   (only certain harmonics "stand" on a string of length l)
```

### Listing 5 — Structure of the full-mark "de Broglie fixes Bohr" extended response
```text
STRONG ANSWER must contain, in order:

1. The limitation:  Bohr POSTULATED that only certain orbits/energy levels are
   allowed but gave NO MECHANISM for why (Rutherford's criticism: "how does the
   electron know which orbit to occupy?").

2. The de Broglie relation:  the electron has a wavelength λ = h / (mv) and
   behaves as a wave.

3. The standing-wave condition:  for the electron-wave to persist around the
   orbit it must join smoothly onto itself → a standing wave → circumference =
   whole number of wavelengths, n λ = 2 π r.

4. Why other orbits die:  if the condition is not met, the wave interferes
   destructively with itself and dies out → that orbit is forbidden.

5. The payoff:  only standing-wave orbits survive → discrete λ → discrete p →
   discrete (quantised) ENERGY LEVELS = exactly Bohr's stationary states.
   De Broglie SUPPLIED THE MISSING MECHANISM (like harmonics on a string).

WEAK ANSWER (band 4, ~1 mark): "Electrons are waves because de Broglie said so."
   — asserts duality with no reason, never states the standing-wave condition,
     never connects to WHY orbits are quantised. The marks live in steps 3–5.
```

### Listing 6 — Schrödinger, Born, and Heisenberg (the modern model)
```text
Schrödinger (1925–26): a WAVE EQUATION whose solutions are wave functions ψ.
Born: |ψ|² gives the PROBABILITY of finding the electron at a location.

Bohr's definite circular ORBIT  →  3-D probability cloud called an ORBITAL.
  orbit  (with a "t")  = Bohr's definite path
  orbital (with "-al") = Schrödinger's fuzzy probability cloud   ← marking trap

Schrödinger's model is FULLY quantum (no classical orbit bolted on):
  ✔ handles multi-electron atoms
  ✔ predicts relative line intensities   (both of which Bohr could not)

Heisenberg uncertainty principle (late 1926):
    Δx · Δp ≥ h / (4π)

  CONSTANT TRAP: uncertainty uses h / (4π).
  Bohr's angular-momentum quantisation used h / (2π) — DIFFERENT result, do not swap.

Meaning: you cannot know position and momentum together, so a definite "orbit"
must give way to "probability." (Schrödinger later showed his wave mechanics and
Heisenberg's matrix mechanics are the same theory.)
```

### Listing 7 — Worked example: de Broglie wavelength of an electron accelerated through 600 V
```text
Q: An electron is accelerated through a potential difference of 600 V.
   Find its de Broglie wavelength.  (m = 9.1 × 10⁻³¹ kg, e = 1.6 × 10⁻¹⁹ C)

Step 1 — Kinetic energy gained = work done by the field:
    E_k = qV = (1.6 × 10⁻¹⁹)(600) = 9.6 × 10⁻¹⁷ J

Step 2 — Momentum from kinetic energy  (E_k = p²/2m  →  p = √(2 m E_k)):
    p = √(2 × 9.1 × 10⁻³¹ × 9.6 × 10⁻¹⁷)
      = √(1.747 × 10⁻⁴⁶)
      = 1.32 × 10⁻²³ kg·m·s⁻¹

Step 3 — de Broglie wavelength:
    λ = h / p = (6.63 × 10⁻³⁴) / (1.32 × 10⁻²³)
      = 5.0 × 10⁻¹¹ m

Answer: λ ≈ 5.0 × 10⁻¹¹ m — comparable to the X-ray wavelength
(7.1 × 10⁻¹¹ m) used in foil experiments, which is why these electrons
diffract off crystals just as X-rays do.

Combined form:  λ = h / √(2 m q V)

⚠ TYPO WARNING: some textbooks print the electron mass as 9.1 × 10⁻³⁴ kg here.
   That is wrong — use 9.1 × 10⁻³¹ kg. Only 10⁻³¹ gives 5.0 × 10⁻¹¹ m.
```

### Listing 8 — Reference data and key dates
| Quantity / fact | Value / detail |
|-----------------|----------------|
| Planck's constant h | 6.63 × 10⁻³⁴ J·s (= 4.15 × 10⁻¹⁵ eV·s) |
| Electron mass mₑ | 9.1 × 10⁻³¹ kg (data sheet 9.109 × 10⁻³¹ kg) |
| Electron charge e | 1.6 × 10⁻¹⁹ C |
| 1 eV | 1.6 × 10⁻¹⁹ J |
| Proton/neutron mass | ≈ 1.67 × 10⁻²⁷ kg (≈ 1800 × electron mass) |
| Crystal atomic spacing | ~10⁻¹⁰ m (= 1 Å) |
| Davisson–Germer voltage | V = 54 V (nickel crystal) |
| Louis de Broglie | matter-wave hypothesis 1923 (PhD thesis); atom standing-wave picture 1924 |
| Davisson & Germer | electron diffraction off nickel, 1927 |
| G. P. Thomson | electron diffraction through foil, 1927; Nobel 1937 |
| J. J. Thomson | electron as particle (q/m); Nobel 1897 |
| Erwin Schrödinger | wave equation / wave mechanics, 1925–26 |
| Max Born | probability interpretation of \|ψ\|² |
| Werner Heisenberg | uncertainty principle, late 1926 |
| Atomic-model order | Dalton → Thomson → Rutherford → Bohr → Schrödinger ("Dotty Tom Ran Bohr's Schedule") |
</content>
</invoke>
