---
title: "Supplementary Materials — The Electromagnetic Spectrum and Spectroscopy: Reading Light"
module: M7
lesson: "03"
script: script.md
---

# Supplementary Materials

Key equations, reference data, and worked solutions for this episode. These listings are the read-along reference; the audio is self-contained and never depends on them, though it speaks the key results in words.

### Listing 1 — Electron energy through an accelerating voltage (worked)
```text
RELATIONSHIP
  E_k = qV
    E_k = kinetic energy gained        (joule, J)
    q   = charge                       (coulomb, C);  electron e = 1.6 × 10^-19 C
    V   = accelerating voltage         (volt, V)

PROBLEM
  Calculate the energy of an electron accelerated through 100 kV
  (the order of voltage used in an X-ray tube).

STEP 1 — convert the voltage to base units
  V = 100 kV = 100 × 10^3 V = 1.0 × 10^5 V

STEP 2 — substitute
  E_k = qV
      = (1.6 × 10^-19 C)(1.0 × 10^5 V)

STEP 3 — evaluate
  E_k = 1.6 × 10^-14 J        (= 100 keV)

PHYSICS LINK (why this sits in the spectrum episode)
  These high-energy electrons slam into a metal target and
  decelerate sharply. An accelerating/decelerating charge
  radiates EM waves; this violent deceleration emits at the
  high-frequency, high-energy end of the spectrum → X-rays.
  High V → high-energy electrons → high-frequency radiation.
  (Same idea as Röntgen's discharge tube, 1895.)
```

### Listing 2 — The electromagnetic spectrum in order (low → high frequency)
| Region | Wavelength (longest → shortest) | Frequency / photon energy | Ionising? | Typical source / use |
|---|---|---|---|---|
| Radio | longest | lowest | No | broadcast, comms (Hertz's waves, 1887) |
| Microwave | ↓ | ↓ | No | radar, mobile phones, ovens |
| Infrared | ↓ | ↓ | No | radiant heat (fire, hot road) |
| Visible | ~400–700 nm | middle | No | the band the eye detects |
| Ultraviolet | ↓ | ↑ | **Yes** | sunburn / skin damage |
| X-ray | ↓ | ↑ | **Yes** | medical imaging (Röntgen) |
| Gamma | shortest | highest | **Yes** | nuclear processes |

```text
MNEMONIC (low → high frequency):
  Radio Microwave Infrared Visible Ultraviolet X-ray Gamma
  → "Raging Martians Invaded Venus Using X-ray Guns"

ALONG THE SPECTRUM, radio → gamma:
  frequency      ↑ increases
  photon energy  ↑ increases   (E = hf, previewed; taught in M7-09)
  ionising power ↑ increases
  WAVELENGTH     ↓ decreases   (because c = fλ is fixed)

TRAP: gamma has the SHORTEST wavelength, NOT the longest.
IONISING = top three only: Ultraviolet, X-ray, Gamma ("U-X-G").
"Non-ionising" ≠ "safe": high-intensity IR/microwave still burns.
```

### Listing 3 — The visible spectrum and dispersing devices
```text
VISIBLE LIGHT (long λ → short λ):
  Red Orange Yellow Green Blue Indigo Violet
  → "ROY G BIV"   (Newton, Opticks, 1704)
  Red   ≈ 700 nm  (longest λ, lowest energy)
  Violet ≈ 400 nm (shortest λ, highest energy)
  1 nm = 10^-9 m ;  1 Å = 10^-10 m

WAVE EQUATION (links frequency and wavelength)
  c = f λ
    c = speed of light in vacuum = 3.0 × 10^8 m s^-1
    f = frequency (Hz) ;  λ = wavelength (m)
  Rearranged:  f = c / λ  → shorter λ means higher f means higher
  photon energy.

PHOTON ENERGY (previewed, not derived here — M7-09)
  E = hf
    h = Planck constant = 6.63 × 10^-34 J s
  1 eV = 1.6 × 10^-19 J

DISPERSING DEVICES (both spread white light into a spectrum)
  PRISM    — mechanism: REFRACTION. Different λ bend by different
             amounts. VIOLET bends MOST, red least.
  GRATING  — mechanism: DIFFRACTION (full geometry in M7-06).
             RED diffracts MOST, violet least.
  TRAP: the colour order REVERSES between prism and grating.
```

### Listing 4 — The three spectra: causes, appearance, and the comparison answer
```text
KIRCHHOFF & BUNSEN (1859) — the three types of spectrum

1. CONTINUOUS SPECTRUM
   SOURCE: hot, DENSE glowing solid / liquid / dense gas
           (a black body, e.g. tungsten filament ~3000 K).
   APPEARANCE: unbroken band — ALL wavelengths present.
   CAUSE: electrons are not confined to discrete atomic levels;
          they move relatively freely and emit a continuous
          range of frequencies.

2. EMISSION SPECTRUM
   SOURCE: hot, LOW-DENSITY (rarefied) gas — a discharge tube.
   APPEARANCE: BRIGHT coloured lines on a DARK background.
   CAUSE: discharge excites electrons to higher levels; they
          fall back (de-excite) and emit photons of specific
          energies → specific wavelengths → bright lines.

3. ABSORPTION SPECTRUM
   SOURCE: continuous source seen THROUGH a COOLER gas in front.
   APPEARANCE: DARK lines on a CONTINUOUS (rainbow) background.
   CAUSE: cool gas absorbs photons at its characteristic
          wavelengths (electrons jump up) and re-emits them in
          ALL directions → those λ depleted along line of sight
          → dark gaps. (Sun's = Fraunhofer lines.)

SOURCE → SPECTRUM HOOK
  dense + hot          = CONTINUOUS
  thin + hot           = EMISSION
  cool gas in front of
  a continuous source  = ABSORPTION

THE TOP-BAND LINK (write this for "compare" questions)
  For ONE element, the DARK absorption lines fall at EXACTLY the
  same wavelengths as the BRIGHT emission lines — because BOTH
  arise from the SAME electron energy-level transitions in that
  element's atoms. (Emission = electron falls; absorption =
  electron rises; SAME energy gap → SAME λ.)

MODEL EXTENDED RESPONSE (6–7 marks)
  "Compare the emission and absorption spectra of a given element,
   and explain how spectra are used to identify the elements
   present in a gas."

  • Emission: bright lines on dark; hot low-density gas; excited
    electrons fall to lower levels emitting photons of specific λ.
  • Absorption (in contrast): dark lines on a continuous
    background; continuous source through a cooler gas; gas absorbs
    at characteristic λ and re-emits in all directions, depleting
    those λ.
  • LINK: the dark absorption lines occur at exactly the same
    wavelengths as the bright emission lines — same energy-level
    transitions.
  • IDENTIFY: every element has a UNIQUE set of lines, and every
    atom of an element gives the SAME set; match observed lines to
    known laboratory spectra → identifies the element — even in a
    distant star (helium found in the Sun, 1868, before Earth,
    1895).
```

### Listing 5 — Spectroscopy timeline and key names
| Year | Person | Contribution |
|---|---|---|
| 1704 | Isaac Newton | Disperses sunlight into ROYGBIV with a prism (*Opticks*) |
| 1802 | William Wollaston | Builds early spectroscope; first sees dark solar lines |
| 1814 | Joseph von Fraunhofer | Maps ~576 dark solar lines → **Fraunhofer lines** |
| 1859 | Kirchhoff & Bunsen | State the three laws of spectra; lines = element fingerprints |
| 1868 | Norman Lockyer | Predicts **helium** from an unexplained solar line (*helios* = Sun) |
| 1895 | Wilhelm Röntgen | Discovers X-rays from a discharge tube |
| 1895 | William Ramsay | Isolates helium on Earth, confirming Lockyer (27 years later) |

### Listing 6 — Constants and reference values
| Quantity | Symbol | Value |
|---|---|---|
| Speed of light (vacuum) | c | 3.0 × 10^8 m s^-1 (exactly 299 792 458 m s^-1) |
| Planck constant | h | 6.63 × 10^-34 J s |
| Electron charge | e | 1.6 × 10^-19 C |
| Electron-volt | 1 eV | 1.6 × 10^-19 J |
| Visible range | λ | ~400 nm (violet) to ~700 nm (red) |
| Ångström | 1 Å | 10^-10 m |
| Incandescent tungsten filament | T | ~3000 K (high melting point) |
| Absolute zero | 0 K | −273.15 °C (quote stellar temps in kelvin) |
