---
title: "Supplementary Materials — Diffraction Gratings and d sin theta = m lambda: Solving Interference Problems"
module: M7
lesson: "06"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. These listings are the read-along reference; the audio is self-contained and never depends on them, though it speaks every key result in words.

### Listing 0 — The interference equations (reference)
```text
Maximum (bright fringe), condition for constructive interference:
    d sin θ = m λ            m = 0, 1, 2, 3 ...   (on the HSC data sheet)

Minimum (dark fringe), condition for destructive interference:
    d sin θ = (m − ½) λ      m = 1, 2, 3 ...      (not on data sheet)

Symbols and SI units:
    d  = slit / grating-line separation        metres (m)
    θ  = angle from central (straight-through) direction   degrees or radians
    m  = order of the maximum (integer)        no unit
    λ  = wavelength of the light               metres (m)

Small-angle screen geometry (small θ only, a few degrees):
    sin θ ≈ tan θ = x / L   →   m λ / d = x / L
    x = distance on screen from central maximum to the fringe (m)
    L = perpendicular distance from slits/grating to screen (m)

Large angle (θ more than a few degrees): use d sin θ = m λ directly,
    then  x = L tan θ   (NOT x = L sin θ)

Grating line-spacing from line density:
    d = 1 / N            N = number of lines per METRE
    lines per metre = (lines per cm) × 100      →   d = 1 / (100 × lines-per-cm)
```

### Listing 1 — Double slit, worked example (sodium lamp)
```text
Given:
    λ = 589 nm = 589 × 10^-9 m
    d = 0.100 mm = 1.0 × 10^-4 m
    L = 1.50 m

(a) First-order maximum, m = 1:
    sin θ = mλ / d
          = (1 × 589 × 10^-9) / (1.0 × 10^-4)
          = 5.89 × 10^-3
    θ = sin⁻¹(5.89 × 10^-3) = 0.337°            (small angle — approximation valid)

    Distance on screen:
    x = L sin θ = 1.50 × 5.89 × 10^-3
              = 8.8 × 10^-3 m = 8.8 mm

(b) Third-order maximum, m = 3:
    Small angles → maxima evenly spaced
    x₃ = 3 × x₁ = 3 × 8.8 mm = 26.4 mm ≈ 26 mm
```

### Listing 2 — Diffraction grating, white-light dispersion (10 μm line spacing)
```text
Given:
    d = 10 μm = 10 × 10^-6 m,   m = 1

Red, λ = 700 nm = 700 × 10^-9 m:
    sin θ = mλ / d = (700 × 10^-9) / (10 × 10^-6) = 0.070
    θ_red = sin⁻¹(0.070) = 4.0°

Blue, λ = 450 nm = 450 × 10^-9 m:
    sin θ = mλ / d = (450 × 10^-9) / (10 × 10^-6) = 0.045
    θ_blue = sin⁻¹(0.045) = 2.6°

Conclusion: red (4.0°) is deflected MORE than blue (2.6°), so each order
fans into a spectrum — blue/violet nearest the centre, red furthest out.
This is the OPPOSITE order to a glass prism (where blue/violet bends most).
"Grating Red Greatest."
```

### Listing 3 — Diffraction grating, find the spot spacing (the reciprocal + small-angle traps)
```text
Given:
    3000 lines per cm,   λ = 530 nm = 530 × 10^-9 m,   L = 1.25 m

(a) Line spacing d — convert to lines per metre FIRST, then reciprocate:
    3000 lines/cm × 100 = 300 000 lines/m
    d = 1 / 300 000 = 3.33 × 10^-6 m   (3.33 μm)
    Trap: forgetting ×100 → 100× error;  using 3000 directly → wrong.

(b) First-order angle, m = 1:
    sin θ = mλ / d = (530 × 10^-9) / (3.33 × 10^-6) = 0.159
    θ = sin⁻¹(0.159) = 9.15°            ← NOT a small angle

(c) Distance on screen — angle is large, so use x = L tan θ:
    x = L tan θ = 1.25 × tan(9.15°) = 1.25 × 0.1611 = 0.201 m ≈ 20 cm

    Compare small-angle (invalid here): x = L sin θ = 1.25 × 0.159 = 0.199 m
    The two already differ at 9° and diverge further as θ grows — flag it.
```

### Listing 4 — Grating line-spacing quick reference (d = 1/N)
| Lines per cm | Lines per metre (× 100) | d = 1 / N (m)        |
|--------------|-------------------------|----------------------|
| 3 000        | 300 000                 | 3.33 × 10⁻⁶ (3.33 μm)|
| 4 000        | 400 000                 | 2.50 × 10⁻⁶ (2.50 μm)|
| 5 000        | 500 000                 | 2.00 × 10⁻⁶ (2.00 μm)|
| 10 000       | 1 000 000               | 1.00 × 10⁻⁶ (1.00 μm)|

### Listing 5 — Exam-question worked answers (Q2 and Q3 from the script)
```text
Q2 — Double slit, second-order angle:
    λ = 600 nm = 600 × 10^-9 m,   d = 2 × 10^-5 m,   m = 2
    sin θ = mλ / d = (2 × 600 × 10^-9) / (2 × 10^-5)
          = (1.2 × 10^-6) / (2 × 10^-5) = 0.06
    θ = sin⁻¹(0.06) = 3.4°

Q3 — Grating, 4000 lines/cm, red 650 nm, first order:
    4000 lines/cm × 100 = 400 000 lines/m
    d = 1 / 400 000 = 2.5 × 10^-6 m
    sin θ = mλ / d = (650 × 10^-9) / (2.5 × 10^-6) = 0.26
    θ = sin⁻¹(0.26) = 15.1°
    Judgement: 15° is NOT small → small-angle approximation invalid;
    use d sin θ = mλ directly and x = L tan θ for any screen distance.
```

### Listing 6 — Reference data and visible-spectrum values
| Quantity                         | Value / range                          |
|----------------------------------|----------------------------------------|
| Speed of light, c                | 3.0 × 10⁸ m s⁻¹ (data sheet)           |
| Visible spectrum                 | ≈ 400 nm (violet) to 700 nm (red)      |
| 1 nanometre (nm)                 | 1 × 10⁻⁹ m                             |
| 1 micrometre (μm)                | 1 × 10⁻⁶ m                             |
| 1 millimetre (mm)                | 1 × 10⁻³ m                             |
| Central maximum                  | m = 0 (white in white light)           |
| Dispersion order (grating)       | blue/violet nearest centre → red furthest |
| Dispersion order (prism, contrast)| red least deviated → blue/violet most |
