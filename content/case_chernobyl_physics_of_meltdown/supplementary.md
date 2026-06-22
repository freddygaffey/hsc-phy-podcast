---
title: "Supplementary Materials — Chernobyl — The Physics of a Meltdown"
kind: case-study
script: script.md
---

# Supplementary Materials

### Listing 1 — Fission of uranium-235 and the chain reaction

```text
A typical fission of U-235 after absorbing a slow (thermal) neutron:

  235        1        236                                  1
   92 U  +    0 n  ->   92 U*  ->  fission fragments  +  k  0 n  +  energy

Example reaction:

  235        1        141           92           1
   92 U  +    0 n  ->   56 Ba   +    36 Kr   +  3  0 n  +  ~200 MeV

Energy per fission  ~ 200 MeV  =  200 x 10^6 x 1.602 x 10^-19 J
                              ~ 3.2 x 10^-11 J

Neutrons released per fission, k:  typically 2 to 3 (average ~2.4)

WHY ENERGY IS RELEASED (binding energy per nucleon):
  The two medium-mass fragments have a HIGHER binding energy per
  nucleon (are more tightly bound / more stable) than U-235.
  That gain in stability is released, mostly as kinetic energy of
  the fragments. Fission of heavy nuclei and fusion of light nuclei
  both move products TOWARD the iron-56 peak of the curve.

Chain reaction condition (multiplication factor k_eff):
  k_eff < 1   subcritical   (chain dies out)
  k_eff = 1   critical      (steady power — a CONTROLLED reactor)
  k_eff > 1   supercritical (power rises — UNCONTROLLED if sustained)

CONTROLLED vs UNCONTROLLED (syllabus comparison):
  Controlled   -> on average EXACTLY 1 neutron per fission causes
                  the next fission -> steady power (reactor).
  Uncontrolled -> MORE THAN 1 neutron per fission causes further
                  fissions -> fissions multiply (2->4->8...) ->
                  power rises without limit (bomb / runaway).
```

```text
ENERGY COMPARISON (syllabus: vs fossil fuels and explosives):
  1 fission of U-235        ~ 200 MeV
  1 carbon atom burned      ~ 10 eV
  => fission yields ~ 2 x 10^7 (20 million) times more energy
     per atom than burning coal.
  Chernobyl 2nd blast       ~ 225 tonnes TNT equivalent
  => still thousands of times SMALLER than a nuclear weapon.
```

### Listing 2 — The four reactor components and their physics roles

| Component | Material at Chernobyl (RBMK) | Physics role |
|-----------|------------------------------|--------------|
| Fuel | Uranium oxide, ~2.0% U-235 enriched | Site of fission; releases energy + fast neutrons |
| Moderator | Graphite (1700 t, solid) | SLOWS fast neutrons to thermal speed (raises fission rate) |
| Control rods | Boron carbide (170 rods) | ABSORBS neutrons (lowers fission rate) — throttle/brake |
| Coolant | Light (ordinary) water | Carries heat away; boils to steam to drive turbine |

```text
KEY DISTINCTION (common exam error):
  Moderator  -> SLOWS neutrons  (so they CAN cause fission)
  Control rod -> ABSORBS neutrons (so they CANNOT cause fission)
These are different jobs done by different materials.
```

### Listing 3 — The positive void coefficient (the core fault)

```text
A "void" = a bubble of steam in the coolant water.
Void coefficient = sign of (change in reactivity) per (steam fraction).

WESTERN water-moderated reactor (water = moderator AND coolant):
  water boils -> lose MODERATOR -> fewer neutrons slowed
              -> fewer fissions -> power FALLS
  => NEGATIVE void coefficient  (self-correcting, SAFE)

RBMK reactor (graphite = moderator, water = coolant only):
  water boils -> moderator (graphite) UNCHANGED
              -> but lose a neutron ABSORBER (the water)
              -> more free neutrons -> more fissions -> power RISES
              -> more heat -> more boiling -> ... (runaway loop)
  => POSITIVE void coefficient  (self-reinforcing, DANGEROUS)

RBMK value at time of accident:  +4.5 beta  (largest of any
   commercial reactor ever built; worst at LOW power)
Post-accident target after modifications:  +0.7 beta
```

### Listing 4 — Xenon-135 poisoning

```text
Production path of the neutron poison:

  fission -> I-135  --(beta decay, t-half ~6.6 h)-->  Xe-135

Xe-135 has the largest thermal neutron absorption cross-section
of any known nuclide (millions of barns).

At FULL power:  Xe-135 burned away by neutrons as fast as it forms
                -> low, steady xenon level.

After a POWER DROP:
  - neutron flux falls -> Xe-135 no longer burned away
  - but stored I-135 keeps decaying -> Xe-135 keeps being made
  -> xenon SURGES (the "xenon pit")
  -> chain reaction smothered; reactor hard to restart

Chernobyl: the 9-hour hold + power crash to ~30 MW created a huge
xenon load. Operators withdrew control rods to fight it, leaving
almost no reactivity margin.
```

### Listing 5 — Key numbers of the accident

| Quantity | Value |
|----------|-------|
| Reactor | RBMK-1000, Unit 4 |
| Rated thermal power | 3200 MW (1000 MW electrical) |
| Core size | 11.8 m diameter x 7.0 m high |
| Required reactivity margin | 26–30 equivalent rods |
| Actual margin ~01:22 | ~8 equivalent rods |
| Power at test start (01:23:04) | ~200 MW |
| AZ-5 button pressed | 01:23:40, 26 April 1986 |
| Peak power reached | ~30 000 MW (~10x rated) in ~3 s |
| 2nd explosion energy | ~225 tonnes TNT equivalent |
| Reactor-floor radiation | ~5.6 R/s (~20 000 R/hr) |
| Lethal dose (LD50) | ~400–500 R |
| Graphite displacer tip length | 4.5 m |
| Direct deaths | 2 (blast) + 28 (acute radiation) = 30 |
| Exclusion zone radius | 30 km |

### Listing 6 — Half-life: equations and the caesium-137 worked example

```text
Exponential decay law (HSC Module 8):
  N_t = N_0 * e^(-lambda * t)

Decay constant from half-life:
  lambda = ln(2) / t_half = 0.6931 / t_half

Simple half-life rule (whole numbers of half-lives):
  fraction remaining after n half-lives = (1/2)^n

Key Chernobyl isotopes:
  Iodine-131    t_half = 8.02 days   (short-lived; thyroid hazard)
  Caesium-137   t_half = 30.04 years (long-lived; defines zone)
  Strontium-90  t_half = 28.8 years  (bone-seeking)

Cs-137 decay:  Cs-137 --(beta)--> Ba-137m --(gamma 0.662 MeV)--> Ba-137 (stable)
```

```text
WORKED EXAMPLE — how long until Cs-137 falls to 0.1% of its level?

Want fraction remaining = 0.001 = (1/2)^n
  Take logs:  n = ln(0.001) / ln(0.5)
              n = (-6.908) / (-0.6931)
              n ~ 9.97  ->  about 10 half-lives

Time = n x t_half = 10 x 30.04 years
     ~ 300 years

So ~300 years are needed for Cs-137 contamination to fall to ~0.1%
of its 1986 level — the physical reason the most contaminated land
stays restricted into the 23rd century.

Check after a single 30-year half-life (1986 -> 2016):
  fraction remaining = (1/2)^1 = 0.5
  i.e. half the original Cs-137 had decayed by 2016.
```

### Listing 7 — Scientists who discovered fission, and the first controlled reactor

| Scientist(s) | Year | Contribution |
|--------------|------|--------------|
| Enrico Fermi | 1934 | Fired neutrons at uranium; produced new half-lives (misread as new elements) |
| Otto Hahn & Fritz Strassmann | 1938 | Chemically detected barium after bombarding uranium — evidence the nucleus had split |
| Lise Meitner & Otto Frisch | 1938–39 | Explained the result, named it "fission", estimated ~200 MeV per event from binding energies |
| Frederic Joliot (and team) | 1939 | Confirmed 2–3 neutrons released per fission — making a chain reaction possible |
| Enrico Fermi (and team) | 1942 | Built the first controlled chain reaction (Chicago Pile-1): graphite-moderated, uranium fuel, cadmium control rods |

```text
NUCLEAR EQUATION FOR FISSION (syllabus: use equations to describe
fission of large nuclei). One representative U-235 fission:

  235        1        236                                   1
   92 U  +    0 n  ->   92 U   ->  141 Ba  +  92 Kr  +  3   0 n  +  ~200 MeV
                                    56         36

Mass numbers balance: 235 + 1 = 141 + 92 + 3(1) = 236
Atomic numbers balance: 92 + 0 = 56 + 36 + 0     = 92
(Many fragment pairs are possible — e.g. La-148 + Br-85 + 3n.)
```
