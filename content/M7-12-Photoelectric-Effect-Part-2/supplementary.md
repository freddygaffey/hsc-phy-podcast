---
title: "Supplementary Materials — The Photoelectric Effect, Part 2: Einstein, K_max = hf - phi, and Real Applications"
module: M7
lesson: "12"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it is the read-along reference. Symbols: K_max = maximum kinetic energy of a photoelectron; h = Planck's constant; f = frequency; φ (or W) = work function; f₀ = threshold frequency; V₀ = stopping voltage; e = electron charge; c = speed of light; λ = wavelength.

### Listing 1 — Full worked example: 425 nm light, stopping voltage 1.25 V (parts a–e)
```text
Einstein equation:   K_max = hf − φ
Data sheet:          h = 6.63 × 10^-34 J s,  c = 3.0 × 10^8 m s^-1,  e = 1.6 × 10^-19 C
                     1 eV = 1.6 × 10^-19 J
Given:               λ = 425 nm = 4.25 × 10^-7 m,   V₀ = 1.25 V

(a) Frequency        f = c / λ
                       = (3.0 × 10^8) / (4.25 × 10^-7)
                       = 7.06 × 10^14 Hz

(b) Photon energy    E = hf = (6.63 × 10^-34)(7.06 × 10^14)
                       = 4.68 × 10^-19 J
                     In eV: 4.68 × 10^-19 ÷ 1.6 × 10^-19 = 2.92 eV  (≈ 2.9 eV)

(c) K_max            Stopping voltage gives K_max directly: K_max = eV₀
                     V₀ = 1.25 V  ⇒  K_max = 1.25 eV
                     In joules: 1.25 × 1.6 × 10^-19 = 2.00 × 10^-19 J

(d) Work function    K_max = hf − φ  ⇒  φ = hf − K_max
                     φ = 2.92 − 1.25 = 1.67 eV
                     In joules: 1.67 × 1.6 × 10^-19 = 2.67 × 10^-19 J

(e) Threshold f₀     At threshold K_max = 0  ⇒  φ = h f₀  ⇒  f₀ = φ / h
                     f₀ = (2.67 × 10^-19) / (6.63 × 10^-34)
                       = 4.03 × 10^14 Hz
                     Threshold wavelength: λ₀ = c / f₀
                       = (3.0 × 10^8) / (4.03 × 10^14)
                       = 7.4 × 10^-7 m = 740 nm
```

### Listing 2 — Reading the graph: lithium photocell, two data points
```text
K_max vs f is a straight line:  K_max = hf − φ   (compare y = mx + c)
  Gradient m = h            (Planck's constant — same for ALL metals → parallel lines)
  x-intercept = f₀          (threshold frequency)
  y-intercept = −φ          (NEGATIVE work function; |y-intercept| = φ)

Two points on the line:
  Point 1:  f = 4.52 × 10^14 Hz,  K_max = 0.45 eV = 7.20 × 10^-20 J
  Point 2:  f = 6.14 × 10^14 Hz,  K_max = 1.15 eV = 1.84 × 10^-19 J

Planck's constant = gradient = rise / run
  rise = 1.84 × 10^-19 − 7.20 × 10^-20 = 1.12 × 10^-19 J
  run  = (6.14 − 4.52) × 10^14         = 1.62 × 10^14 Hz
  h = 1.12 × 10^-19 / 1.62 × 10^14 = 6.9 × 10^-34 J s   (≈ accepted value)

Work function (use Point 1):  φ = hf − K_max
  φ = (6.9 × 10^-34)(4.52 × 10^14) − 7.20 × 10^-20
    = 3.12 × 10^-19 − 0.72 × 10^-19 ≈ 2.4 × 10^-19 J  (≈ 1.5 eV)

Threshold frequency:  f₀ = φ / h
  f₀ = 2.4 × 10^-19 / 6.9 × 10^-34 ≈ 3.5 × 10^14 Hz   (= x-intercept)

A metal with a LARGER work function → parallel line (same gradient h), shifted RIGHT
(higher f₀, more negative y-intercept). Lines never converge.
```

### Listing 3 — Exam Question 3 worked solution: 390 nm light, φ = 1.67 eV
```text
K_max = hc/λ − φ
Given:  λ = 390 nm = 3.90 × 10^-7 m,   φ = 1.67 eV
Use h in eV·s:  h = 4.15 × 10^-15 eV s,   c = 3.0 × 10^8 m s^-1

Photon energy:
  E = hc / λ = (4.15 × 10^-15 × 3.0 × 10^8) / (3.90 × 10^-7)
    = (1.245 × 10^-6) / (3.90 × 10^-7)
    = 3.19 eV

Maximum kinetic energy:
  K_max = E − φ = 3.19 − 1.67 = 1.52 eV   (≈ 1.5 eV)

Stopping voltage:
  K_max = eV₀  ⇒  in eV, V₀ (volts) = K_max (eV) numerically
  V₀ = 1.5 V
```

### Listing 4 — The four observations explained by Einstein's photon model (DENF)
| Observation | Wave-model prediction (wrong unless noted) | Einstein's photon explanation |
|-------------|---------------------------------------------|-------------------------------|
| **D** — No time **D**elay | Faint light needs time to accumulate energy → delay | One photon delivers all its energy (hf) in one collision → instant emission |
| **E** — **E**nergy from frequency | Energy comes from amplitude/intensity | K_max = hf − φ; higher f → more hf left after paying φ → higher K_max |
| **N** — **N**umber from intensity | Brighter → more electrons (✓ correct, wrong reason) | Intensity = photons per second → more 1-to-1 hits → more electrons (bigger photocurrent) |
| **F** — Threshold **F**requency f₀ | No threshold; any f works given time | If hf < φ a single photon can't free an electron, regardless of intensity → cut-off at f₀ = φ/h |

### Listing 5 — Key constants and values (NSW HSC data sheet)
| Quantity | Symbol | Value |
|----------|--------|-------|
| Planck's constant | h | 6.63 × 10⁻³⁴ J s  (= 4.14 × 10⁻¹⁵ eV s) |
| Speed of light | c | 3.0 × 10⁸ m s⁻¹ |
| Electron charge (magnitude) | e | 1.6 × 10⁻¹⁹ C |
| Electron-volt | 1 eV | 1.6 × 10⁻¹⁹ J |
| Electron rest mass | mₑ | 9.1 × 10⁻³¹ kg |
| Worked example work function (≈ calcium) | φ | 1.67 eV = 2.67 × 10⁻¹⁹ J |
| Worked example threshold frequency | f₀ | 4.03 × 10¹⁴ Hz (λ₀ ≈ 740 nm) |

### Listing 6 — Photoelectric vs thermionic emission; key people
```text
PHOTOELECTRIC EMISSION   electrons freed by LIGHT (single photon, one collision)
THERMIONIC EMISSION      electrons freed by HEAT (thermal energy in the metal)
  → SAME barrier to overcome: the work function φ
  → DIFFERENT energy source: photon vs thermal
  → BOTH analysed with the same work-function / energy-conservation logic

People & dates (get these right):
  Hertz 1887        first observed the effect at a spark gap
  J.J. Thomson 1899 showed UV ejects electrons (= cathode-ray particles)
  Lenard 1902       quantified: higher f → higher electron energy; intensity → number
  Planck 1900       introduced E = hf (quantisation) for black-body radiation; thought it a "trick"
  Einstein 1905     photon ("light quantum") explanation → Nobel Prize 1921 (for THIS, not relativity)
  Millikan 1915–16  measured V₀ vs f, gradient = h; confirmed Einstein "reluctantly"
  "Photon"          term coined 1926 (Gilbert Lewis)
```

### Listing 7 — Applications of the photoelectric effect (secondary-source investigation)
| Application | How the photoelectric effect is used |
|-------------|--------------------------------------|
| **Photovoltaic (solar) cell** (named in syllabus) | Photons above threshold free electrons inside a semiconductor (internal photoelectric effect, across a band gap); freed electrons drive a current → sunlight to electricity. *Caveat: electrons are freed inside the material, not ejected into the air.* |
| **Photomultiplier tube** (strong "one other") | A faint photon ejects one electron from a photocathode (photoelectric effect); cascaded plates amplify it ~10⁶× → single-photon detection (astronomy, medical scintillation detectors, radiation counters) |
| Light meters / camera exposure | Incident light frees electrons → current proportional to brightness |
| Digital image sensors (CCD/CMOS) | Photons free electrons per pixel → charge read out as an image |
| Automatic doors / light switches | Light beam frees electrons; breaking the beam changes the current → triggers the switch |
| Night-vision devices | Photocathode releases electrons that are amplified to brighten a dim image |
