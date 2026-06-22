---
title: "Supplementary Materials — Module Review: The Nature of Light, End to End"
module: M7
lesson: "99"
script: script.md
---

# Supplementary Materials

Key equations, full worked solutions, the extended-response skeletons, and the trap-reference tables for the Module 7 review. Nothing here is spoken in the audio — it is the read-along reference. Constants used throughout: speed of light c = 3.0 × 10^8 m s^-1; Planck constant h = 6.63 × 10^-34 J s; electron charge e = 1.6 × 10^-19 C (1 eV = 1.6 × 10^-19 J); Wien's constant b = 2.9 × 10^-3 m K.

### Listing 1 — Double-slit interference, worked example
```text
d sin θ = mλ   (maxima),   sin θ = mλ/d,   x = L sin θ

Given:
  λ = 589 nm = 5.89 × 10^-7 m   (sodium light)
  d = 0.100 mm = 1.00 × 10^-4 m
  L = 1.50 m

First-order maximum (m = 1):
  sin θ = (1)(5.89 × 10^-7) / (1.00 × 10^-4) = 5.89 × 10^-3
  θ = sin^-1(5.89 × 10^-3) = 0.337°

  x₁ = L sin θ = 1.50 × 5.89 × 10^-3 = 8.8 × 10^-3 m = 8.8 mm

Third-order maximum (fringes evenly spaced):
  x₃ = 3 × x₁ = 3 × 8.8 mm = 26.4 mm
```

### Listing 2 — Polarisation (Malus's law), worked example with the unpolarised-step trap
```text
First (unpolarised) filter:  I = ½I₀      ← use ½, NOT Malus
Polariser → analyser:        I = I_max cos²θ   (θ = angle between axes)

Light: unpolarised, intensity I₀.
Polariser → analyser at 60° → second analyser a further 30° (90° total).

Step 1 — after polariser (unpolarised in):
  I_a = ½I₀ = 0.500 I₀            (50%)

Step 2 — after analyser at 60°:
  I_b = I_a cos²(60°) = 0.500 × (0.5)² = 0.500 × 0.25
  I_b = 0.125 I₀                  (12.5%)

Step 3 — after 2nd analyser, a further 30°:
  I_c = I_b cos²(30°) = 0.125 × (0.866)² = 0.125 × 0.75
  I_c = 0.094 I₀                  (≈ 9.4%)

Crossed polarisers (polariser + analyser at 90°, nothing between):
  I = I_a cos²(90°) = I_a × 0 = 0   (no light transmitted)
```

### Listing 3 — Photon energy, worked example
```text
E = hf = hc/λ

UV photon, λ = 3.00 × 10^-7 m:
  E = (6.63 × 10^-34 × 3.00 × 10^8) / (3.00 × 10^-7)
  E = (1.989 × 10^-25) / (3.00 × 10^-7)
  E = 6.63 × 10^-19 J

Convert to electron-volts:
  E = (6.63 × 10^-19) / (1.6 × 10^-19) = 4.14 eV
```

### Listing 4 — Wien's law, worked example
```text
λ_max = b/T   →   T = b / λ_max     (b = 2.9 × 10^-3 m K)

Dark-red hotplate, λ_max = 4.0 μm = 4.0 × 10^-6 m:
  T = (2.9 × 10^-3) / (4.0 × 10^-6)
  T = 725 K

Direction check: longer λ_max  →  cooler body.   Hotter = bluer (shorter λ_max).
```

### Listing 5 — Photoelectric stopping voltage, worked example
```text
E_k,max = qV₀   →   V₀ = E_k,max / q     (q = e = 1.6 × 10^-19 C)

Photoelectrons emitted with E_k,max = 2.6 × 10^-19 J:
  V₀ = (2.6 × 10^-19) / (1.6 × 10^-19)
  V₀ = 1.6 V

The stopping voltage is just the maximum kinetic energy expressed in volts.
```

### Listing 6 — Time dilation, worked example
```text
γ = 1 / √(1 − v²/c²),     t = γ t₀

Clock moving at v = 0.5c shows t₀ = 5 min (proper time, on the moving clock):
  γ = 1 / √(1 − 0.5²) = 1 / √(0.75) = 1.155

  t = γ t₀ = 1.155 × 5 = 5.775 min
  t ≈ 5 min 46.5 s   (stationary observer's elapsed time)

t₀ (proper time) is the smaller value; the moving clock runs slow, so the
observed interval t is larger.
```

### Listing 7 — Muon evidence (time dilation), worked example
```text
γ = t / t₀,     v = c√(1 − 1/γ²),     half-life in Earth frame = γ t₀

Muon proper half-life t₀ = 1.56 μs.
Earth frame: journey takes t = 6.5 μs while muons "age" t₀-equiv = 0.7 μs.

Lorentz factor:
  γ = 6.5 / 0.7 = 9.29

Speed from γ:
  v = c√(1 − 1/9.29²) = c√(1 − 0.0116) = 0.994c

Muon half-life as measured from Earth:
  t = γ t₀ = 9.29 × 1.56 × 10^-6 = 1.4 × 10^-5 s = 14 μs

The stretched half-life is why far more muons reach the ground than their
1.56 μs proper half-life would allow.
```

### Listing 8 — Extended-response skeleton: "justify that light is both wave and particle"
```text
Q: Light shows both wave and particle behaviour. Using specific evidence, justify.

WAVE evidence:
  • Diffraction — light spreads through gaps ≈ wavelength; particles cannot bend
    around corners.
  • Interference (Young's double slit): d sin θ = mλ.
      - bright: path difference = mλ (constructive)
      - dark:   path difference = (m − ½)λ (destructive)
      - a particle stream cannot cancel to darkness → wave evidence.
  • Polarisation (Malus: I = I_max cos²θ) only occurs for TRANSVERSE waves
      → proves light is a transverse wave.

PARTICLE (photon) evidence — photoelectric effect:
  • no time delay
  • threshold frequency f₀ exists
  • E_k,max depends on FREQUENCY, not intensity:  E_k,max = hf − W
  • wave model explains only intensity→number; photon model (1 photon → 1 electron)
    explains all four.

CONCLUSION: same light is BOTH wave and particle → wave–particle duality.

Weak (band-4): "It diffracts so it's a wave, and the photoelectric effect makes it
a particle." — no specific evidence, no equations, no reasoning → almost no marks.
```

### Listing 9 — Reading the photoelectric graph (E_k,max vs frequency)
```text
Plot:  E_k,max (y-axis)  against  f (x-axis)   from   E_k,max = hf − W

  gradient    = h            (Planck's constant — SAME for every metal,
                              so all metals' lines are PARALLEL)
  x-intercept = f₀           (threshold frequency, where E_k,max = 0)
  y-intercept = −W           (NEGATIVE of the work function)

At threshold:  W = h f₀

Common errors:
  • reading the gradient as W (it is h)
  • reading the y-intercept as +W or as f₀ (it is −W)
  • confusing f₀ (a frequency, Hz) with W (an energy, J or eV)
```

### Listing 10 — The "proper" distinctions, directions, and module traps
| Pair / rule | Get it right |
|-------------|--------------|
| Malus's law | I = I_max cos²θ (cosine **squared**); θ = angle **between the two filter axes** |
| First filter on unpolarised light | I = ½I₀ (use one half, **not** Malus) |
| Threshold frequency vs work function | f₀ is a frequency (Hz); W is an energy (J/eV); linked by W = hf₀ |
| Intensity vs frequency | intensity = number of photons (more electrons); only frequency raises E_k,max |
| Photoelectric graph | gradient = h; x-intercept = f₀; y-intercept = −W (negative) |
| Black body vs discharge tube | black body = **continuous** spectrum; discharge tube = **emission lines** |
| Wien direction | hotter → shorter λ_max (bluer); cooler → longer λ_max |
| Stellar lines: shift vs broadening | Doppler **shift** = radial velocity; **broadening** = rotation/density |
| Proper time t₀ | measured where the two events occur at the **same place** (clock's own frame); time **dilates** (t = γt₀, larger) |
| Proper length l₀ | measured in the object's **rest frame**; length **contracts** (l = l₀/γ, smaller), only **along the direction of motion** |
| Lorentz factor | γ ≥ 1 **always**; if you get γ < 1 the working is wrong |
| Mass cannot reach c | as v → c, γ → ∞ so required energy → ∞; never "infinitely fast", say "needs infinite energy" |
| EM waves & medium | EM waves need **no medium**; aether never detected (Michelson–Morley null result) |
| Source of EM waves | **accelerating/oscillating** charges radiate; steady DC current does **not** |

### Listing 11 — Diffraction grating, first-order angle, worked example
```text
d = 1 / (lines per metre),     d sin θ = mλ

Grating: 600 lines per mm.
  600 lines/mm = 6.00 × 10^5 lines/m
  d = 1 / (6.00 × 10^5) = 1.67 × 10^-6 m

Light: λ = 650 nm = 6.50 × 10^-7 m,  first order (m = 1):
  sin θ = mλ / d = (6.50 × 10^-7) / (1.67 × 10^-6) = 0.389
  θ = sin^-1(0.389) = 22.9°

Mark-earning steps: convert lines/mm → spacing in metres; substitute; take sin^-1.
```

### Listing 12 — Length contraction (spacecraft), worked example
```text
γ = 1 / √(1 − v²/c²),     l = l₀ / γ = l₀√(1 − v²/c²)

Spacecraft: v = 0.80c,  proper length l₀ = 100 m.

Lorentz factor:
  γ = 1 / √(1 − 0.8²) = 1 / √(0.36) = 1 / 0.6 = 1.667

Contracted length (Earth observer):
  l = l₀ / γ = 100 / 1.667 = 60 m

Proper length = 100 m (measured in the spacecraft's own rest frame).
Earth observer measures the contracted 60 m.
```

### Listing 13 — Module 7 reference data and mnemonics
| Quantity / list | Value or hook |
|-----------------|---------------|
| Speed of light c | 3.0 × 10^8 m s^-1 (exact 299 792 458 m s^-1) |
| Planck constant h | 6.63 × 10^-34 J s |
| Electron charge e | 1.6 × 10^-19 C (= 1 eV in joules) |
| Wien's constant b | 2.9 × 10^-3 m K |
| Permittivity ε₀ | 8.854 × 10^-12 F m^-1 |
| Permeability μ₀ | 4π × 10^-7 ≈ 1.257 × 10^-6 T m A^-1 |
| Electron rest mass | 9.11 × 10^-31 kg |
| Proton rest mass | 1.67 × 10^-27 kg |
| EM spectrum (rising frequency) | Radio, Microwave, Infrared, Visible, Ultraviolet, X-ray, Gamma → "Raging Martians Invaded Venus Using X-ray Guns" |
| Three spectrum types | Continuous, Emission, Absorption → "CEA": hot Coal, Excited gas, cool Atmosphere |
| Four stellar properties | Temperature, Composition, Velocity, Rotation → "The Cosmos Verifies Relativity" |
| Three wave-model pillars | Diffraction, Interference, Polarisation → "Don't Ignore Photons" |
| Four photoelectric observations | Number, Threshold, Energy, No-delay → "Newton's Theory Explodes Now" |
| Evidence → model map | diffraction/interference/polarisation → wave; black-body curve + photoelectric → quantum (photon); Michelson–Morley null + muons + atomic clocks → relativity |
