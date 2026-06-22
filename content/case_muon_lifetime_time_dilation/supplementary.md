---
title: "Supplementary Materials — Muon Lifetime — Time Dilation Made Real"
kind: case-study
script: script.md
---

# Supplementary Materials

### Listing 1 — The classical (wrong) prediction: how far a muon should travel

```text
proper lifetime of muon, t0 = 2.2 us = 2.2 x 10^-6 s
maximum speed = c = 3 x 10^8 m/s   (absolute best case)

classical max distance:
d = v x t0
d = (3 x 10^8 m/s) x (2.2 x 10^-6 s)
d = 660 m

a realistic muon at v = 0.98c:
d = (0.98 x 3 x 10^8) x (2.2 x 10^-6)
d = approx 647 m

journey actually required = 15,000 m
verdict: classical physics is short by a factor of ~22
```

### Listing 2 — Time dilation: the muon survives in OUR frame

```text
Lorentz factor:
gamma = 1 / sqrt(1 - v^2/c^2)

standard HSC narrative value: gamma = 15   (corresponds to v = 0.9978c)

time dilation formula:
t = gamma x t0
t = 15 x (2.2 x 10^-6 s)
t = 33 x 10^-6 s = 33 us

distance now possible in Earth's frame:
d = v x t
d = (0.9978 x 3 x 10^8 m/s) x (33 x 10^-6 s)
d ~ 9,880 m ~ 10 km

enough to cross the atmosphere -> muons reach the ground
```

### Listing 3 — Length contraction: the muon survives in ITS OWN frame

```text
In the muon's frame, its clock is NORMAL: it lives only t0 = 2.2 us.
Instead, the atmosphere is contracted along the direction of motion.

length contraction formula:
L = L0 / gamma      (equivalently L = L0 x sqrt(1 - v^2/c^2))

L0 = 15,000 m  (proper length of atmosphere, Earth's frame)
gamma = 15

L = 15,000 / 15 = 1,000 m

time to cross, in muon's frame:
t = L / v = 1000 / (0.9978 x 3 x 10^8) ~ 3.3 x 10^-6 s = 3.3 us

This is only ~1.5 proper lifetimes, so a sizeable fraction of muons survive.
Both frames agree on the outcome: the muon reaches the ground.
```

### Listing 4 — The Frisch-Smith experiment (Mount Washington, 1962-63)

| Quantity | Value |
|----------|-------|
| Summit altitude (Mount Washington) | 1,917 m |
| Muon speed selected | ~0.995c |
| Lorentz factor gamma at this speed | ~10 |
| Transit time, summit to Cambridge (Earth frame) | 6.34 us (~3 lifetimes) |
| Count rate at summit | 565 +/- 10 per hour |
| Predicted survivors WITHOUT time dilation | ~27 per hour |
| Predicted survivors WITH time dilation | ~400 per hour |
| Measured count at sea level | 409 +/- 9 per hour |
| Time dilation factor measured | 8.8 +/- 0.8 |
| Time dilation factor predicted | ~8.4 |

```text
survival count follows exponential decay:
N = N0 x e^(-t / (gamma x t0))

WITH time dilation (gamma x t0 = 8.8 x 2.2 us = 19.4 us):
N = 565 x e^(-6.34/19.4) = 565 x e^(-0.327) ~ 407 per hour  (matches 409 measured)

WITHOUT time dilation (gamma = 1, gamma x t0 = 2.2 us):
N = 565 x e^(-6.34/2.2) = 565 x e^(-2.88) ~ 32 per hour  (matches ~27 predicted)
```

### Listing 5 — The Hafele-Keating experiment (1971): two effects, both real

| Effect | Eastward (ns) | Westward (ns) |
|--------|---------------|---------------|
| Gravitational, general relativity (altitude) | +144 | +179 |
| Kinematic, special relativity (motion) | -184 | +96 |
| Total predicted | -40 +/- 23 | +275 +/- 21 |
| Total measured | -59 +/- 10 | +273 +/- 7 |

```text
Sign convention: positive = flying clock GAINS time vs ground clock.

Eastward: plane speed ADDS to Earth's rotation -> faster vs Earth's centre
          -> SR slowing dominates -> clock loses time (net -59 ns).
Westward: plane speed OPPOSES Earth's rotation -> slower vs Earth's centre
          -> less SR slowing, GR speed-up wins -> clock gains time (net +273 ns).

Westward result agreed with prediction to within ~0.1 standard deviations.
```

### Listing 6 — GPS: relativity built into daily technology

```text
satellite orbital altitude ~ 20,200 km
satellite speed ~ 3.87 km/s

special relativity (motion):   clocks run SLOW by  -7.2 us/day
general relativity (gravity):  clocks run FAST by +45.8 us/day
-----------------------------------------------------------------
net effect:                    clocks run FAST by ~+38.4 us/day

position error if uncorrected:
38.4 us = 38,400 ns
light travels ~0.30 m per ns
error ~ 38,400 x 0.30 m ~ 11,500 m ~ 10 km per day (and growing)

engineering fix (pre-compensation before launch):
target clock frequency        = 10.23 MHz
pre-set ground frequency      = 10.22999999543 MHz
(set slightly slow so it ticks correctly once sped up in orbit)
```

### Listing 7 — Key constants and quick-reference values

| Quantity | Symbol | Value |
|----------|--------|-------|
| Speed of light | c | 3.00 x 10^8 m/s (exactly 299 792 458 m/s) |
| Muon proper MEAN lifetime | t0 | 2.197 us (~2.2 us) |
| Muon proper HALF-LIFE | t_half | ~1.56 us (value used in Jacaranda textbook) |
| Muon rest mass | — | 105.7 MeV/c^2 (~207 x electron mass) |
| Muon production altitude | — | ~15 km (range 10-20 km) |
| Muon flux at sea level | — | ~10,000 per square metre per minute |
| Time dilation formula | t = t0 / sqrt(1 - v^2/c^2) | t = gamma x t0 |
| Length contraction formula | L = L0 x sqrt(1 - v^2/c^2) | L = L0 / gamma |
| Lorentz factor | gamma | 1 / sqrt(1 - v^2/c^2) |

```text
NOTE on lifetime vs half-life (exam-relevant):
- Mean (average) lifetime of the muon  = 2.197 us (~2.2 us). This script uses this value.
- Half-life of the muon                = mean lifetime x ln(2)
                                       = 2.197 us x 0.693 = 1.52 us (~1.56 us)
The Jacaranda textbook quotes the half-life of 1.56 us in the Rossi-Hall worked example.
Both are correct; they describe the same exponential decay measured two ways.

Syllabus formulas (NESA, Nature of light):
time dilation:        t = t0 / sqrt(1 - v^2/c^2)
length contraction:   l = l0 x sqrt(1 - v^2/c^2)
relativistic momentum: p = m0 v / sqrt(1 - v^2/c^2)
mass-energy:           E = mc^2
```

### Listing 8 — The Rossi-Hall experiment (Colorado, 1940-41): textbook worked figures

| Quantity | Value |
|----------|-------|
| Muon proper half-life (rest frame) | 1.56 us |
| Transit time between detectors (Earth frame) | ~6.5 us |
| Decay time experienced by muons (muon frame) | ~0.7 us |
| Lorentz factor from gamma = t / t0 | 6.5 / 0.7 ~ 9.3 |
| Muon speed from gamma | v = c x sqrt(1 - 1/gamma^2) ~ 0.994c |
| Half-life measured in Earth frame | t = gamma x t0 = 1.56 us x 9.3 ~ 14.5 us |

```text
Two-frame interpretation (same outcome, both frames agree muons survive):

EARTH frame:  the muons' clocks run slow, so their half-life dilates
              from 1.56 us out to ~14.5 us -> many survive the ~6.5 us trip.

MUON frame:   the muons' clocks are normal (only ~0.7 us elapses), but the
              mountain/atmosphere is LENGTH-CONTRACTED to a small hill,
              so the contracted distance is crossed within a normal lifetime.

This is the syllabus' quantitative muon-lifetime example, and it shows time
dilation (Earth frame) and length contraction (muon frame) are two descriptions
of one physical result.
```
