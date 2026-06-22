---
title: "Supplementary Materials — The Hertz Experiment — Proving Maxwell Right"
kind: case-study
script: script.md
---

# Supplementary Materials

### Listing 1 — Maxwell's speed of an electromagnetic wave

```text
v = 1 / sqrt( mu_0 * epsilon_0 )

where (values and units as given in Jacaranda Physics 12):
  mu_0      = permeability of free space = 4*pi x 10^-7   m kg C^-2
  epsilon_0 = permittivity of free space = 8.854 x 10^-12 C^2 s^2 kg^-1 m^-3

substitute:
  v = 1 / sqrt( (4*pi x 10^-7) * (8.854 x 10^-12) )
  v = 1 / sqrt( 1.1126 x 10^-17 )
  v = 1 / (3.3356 x 10^-9)
  v = 2.998 x 10^8  m/s   (rounded to 3.0 x 10^8 m/s)
  exact accepted value of c = 299 792 458 m/s

This matched the measured speed of light, leading Maxwell to
conclude that light IS an electromagnetic wave, and that other
(invisible) frequencies of EM wave must also exist.

With the less precise constants available in the 1860s, Maxwell's
own figure came out near ~3.1 x 10^8 m/s, within ~1-3% of the best
measured speed of light of the day (~3.0 x 10^8 m/s) - close enough
that he judged it could not be a coincidence.
```

### Listing 2 — The universal wave equation (how Hertz got the speed)

```text
v = f * lambda

where:
  v      = wave speed (m/s)
  f      = frequency (Hz)
  lambda = wavelength (m)

Hertz's method:
  lambda  -> measured directly from standing-wave node spacing
  f       -> calculated from the oscillator's L-C resonant frequency
  v       -> f * lambda  ->  approx 3 x 10^8 m/s  (the speed of light)
```

### Listing 3 — Standing wave from a reflector (node spacing)

```text
A transmitted wave + its reflection off a metal sheet
superimpose to form a STANDING wave.

  distance between adjacent NODES      = lambda / 2
  distance between adjacent ANTINODES  = lambda / 2

Hertz measured node-to-node spacing of about 2 m:
  lambda / 2 = 2 m
  lambda     = 4 m

Detector loop:
  at a NODE      -> fields cancel -> spark vanishes
  at an ANTINODE -> fields add    -> spark is brightest
```

### Listing 4 — Resonant frequency of the spark-gap oscillator

```text
f = 1 / ( 2*pi * sqrt(L * C) )

where:
  L = inductance of the 2 m copper dipole (set by its geometry)
  C = capacitance of the rods + zinc end-spheres

Hertz could NOT measure f directly with any instrument of the day.
He CALCULATED it from L and C, getting roughly 50-100 MHz
(VHF band - similar to modern television frequencies).

Check:  lambda = c / f
  if f ~ 75 MHz:  lambda = (3 x 10^8) / (75 x 10^6) = 4 m
  consistent with the measured standing-wave value.
```

### Listing 5 — Hertz's apparatus: key numbers

| Component | Specification |
|-----------|---------------|
| Transmitter rods | two copper rods, ~1 m each (2 m total dipole) |
| Spark gap (transmitter) | ~7.5 mm |
| End spheres (capacitive load) | zinc, ~30 cm diameter |
| Power source | Ruhmkorff induction coil, ~30 kV |
| Oscillation frequency | ~50-100 MHz (calculated, not measured) |
| Receiver | copper wire loop with adjustable micrometer gap |
| Receiver spark size | "scarcely a hundredth of a millimetre", ~10^-6 s |
| Reflector plate | zinc sheet, ~12 m from transmitter |
| Measured wavelength | ~4 m |
| Measured speed | ~3 x 10^8 m/s (the speed of light) |

### Listing 6 — Worked example: speed of an EM wave from standing waves

```text
PROBLEM:
A spark-gap oscillator radiates waves at frequency f = 75 MHz.
A reflector produces standing waves; a detector loop finds the
distance between adjacent nodes is 2.0 m.
Find the wavelength and the wave speed.

STEP 1 - wavelength from node spacing:
  node spacing = lambda / 2
  2.0 = lambda / 2
  lambda = 4.0 m

STEP 2 - wave speed from v = f * lambda:
  f = 75 MHz = 75 x 10^6 Hz
  v = f * lambda
  v = (75 x 10^6) * (4.0)
  v = 3.0 x 10^8 m/s

RESULT:
  v = 3.0 x 10^8 m/s  -> the speed of light.
  This is how Hertz confirmed Maxwell's predicted speed.
```

### Listing 7 — The electromagnetic spectrum Maxwell's theory predicted

```text
Maxwell's equations allow EM waves of ANY frequency.
ALL travel at the same speed c = 3.0 x 10^8 m/s in a vacuum;
they differ only in frequency f and wavelength lambda (c = f * lambda).

Order from SHORTEST wavelength (highest f, highest energy)
        to LONGEST wavelength (lowest f, lowest energy):

  gamma rays  ->  X-rays  ->  ultraviolet  ->  visible light
              ->  infrared  ->  microwaves  ->  radio waves

In Maxwell's day (1860s) only VISIBLE LIGHT and INFRARED had been
observed. The rest were predicted by the theory, then found later -
Hertz's radio waves (1887) being the first deliberately produced.
```

| Property | Across the spectrum |
|----------|---------------------|
| Speed in vacuum | constant, c = 3.0 x 10^8 m/s (same for all) |
| Distinguishing quantities | frequency f and wavelength lambda |
| Relation | c = f * lambda (so higher f means shorter lambda) |
| Energy trend | shorter wavelength carries more energy per wave |
| Nature | transverse; E field perpendicular to B field, both perpendicular to direction of travel |

### Listing 8 — Syllabus checklist: where each dot-point is addressed (M7, Nature of light)

| NESA dot-point (Electromagnetic waves) | Covered in episode |
|----------------------------------------|--------------------|
| All EM radiation has constant speed c in a vacuum | Named EM spectrum; "the one speed, c, in a vacuum" |
| Explain how EM waves are produced and propagated | Accelerating/oscillating charge radiates; self-sustaining E and B fields regenerate each other |
| Maxwell: unification of electricity and magnetism | Maxwell's four equations unify the phenomena |
| Maxwell: prediction of electromagnetic waves | Displacement current term -> self-propagating wave |
| Maxwell: prediction of velocity | v = 1 / sqrt(mu_0 * epsilon_0) -> matches speed of light |
| Historical prediction of c from permittivity and permeability | Listing 1; constants measured in "jars and coils" |
| Spark-gap oscillator and loop antenna verified the speed (Hertz) | Transmitter, receiver, standing-wave method, v = f * lambda |
| Reflection, refraction, diffraction, polarisation = same as light | Hertz reproduced every property of light |
