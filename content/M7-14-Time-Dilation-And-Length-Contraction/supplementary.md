---
title: "Supplementary Materials — Time Dilation and Length Contraction: The Consequences of Constant c"
module: M7
lesson: "14"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it is the read-along reference. Constants used throughout: speed of light c = 3.0 × 10^8 m s^-1 (exact: 299 792 458 m s^-1). The time dilation and length contraction equations are on the HSC Physics Data Sheet / Formulae Sheet.

### Listing 1 — The Lorentz factor, time dilation and length contraction (the three equations)
```text
Lorentz factor (gamma):
    γ = 1 / √(1 − v²/c²)
        γ = Lorentz factor (dimensionless, no unit; ALWAYS ≥ 1)
        v = relative speed between the two frames  (m s^-1)
        c = speed of light = 3.0 × 10^8 m s^-1
    γ = 1 only when v = 0;  γ → ∞ as v → c.

Time dilation:
    t = t₀ γ          (equivalently  t = t₀ / √(1 − v²/c²))
        t  = dilated (measured) time — events at DIFFERENT places; the LONGER time  (s)
        t₀ = proper time — events at the SAME place (one clock present at both); the SHORTER time  (s)

Length contraction:
    L = L₀ / γ        (equivalently  L = L₀ √(1 − v²/c²))
        L  = contracted (measured) length, from a frame in which the object MOVES; the SHORTER length  (m)
        L₀ = proper length — measured in the object's REST frame; the LONGER length  (m)
        Acts ONLY along the direction of motion. Perpendicular dimensions unchanged.

Getting v back from γ (often needed in muon problems):
    v = c √(1 − 1/γ²)

Sanity checks:   γ ≥ 1,   t ≥ t₀,   L ≤ L₀.  Any violation = algebra error.
```

### Listing 2 — Worked Example: time dilation (James and Mabry, v = 0.5c)
```text
Q: Mabry's clock shows 5 min elapse as she moves past James at 0.5c.
   How much time passes for James?

Step 1 — Identify the proper time:
    The two events (clock reads 12.00, clock reads 12.05) are at the SAME place
    on Mabry's moving clock  →  t₀ = 5 min  (the proper, shorter time).

Step 2 — Compute γ at v = 0.5c:
    v²/c² = (0.5)² = 0.25
    1 − 0.25 = 0.75
    √0.75 = 0.8660
    γ = 1 / 0.8660 = 1.155

Step 3 — Apply t = t₀ γ:
    t = 5 × 1.155 = 5.775 min  (= 5 min 46.5 s)

Answer: 5.775 minutes pass for James — the moving clock runs slow.
```

### Listing 3 — Derivation: length contraction from the tipped light clock
```text
Tip the light clock so its length L lies ALONG the direction of motion (speed v).
Pulse goes back mirror → front mirror → back mirror.

Outbound (front mirror recedes, light must catch up):
    t_AB = L / (c − v)

Return (back mirror advances to meet the light):
    t_BA = L / (c + v)

Total time (external frame):
    t = L/(c−v) + L/(c+v) = 2Lc / (c² − v²)

Set this equal to the time-dilated tick, with rest-frame relation t₀ = 2L₀/c:
    t = t₀ / √(1 − v²/c²) = (2L₀/c) / √(1 − v²/c²)

Equate and solve for the measured length L:
    2Lc/(c² − v²) = (2L₀/c)/√(1 − v²/c²)
    ⇒  L = L₀ √(1 − v²/c²) = L₀ / γ

Result:  L = L₀ / γ   — moving lengths contract along the motion only.
```

### Listing 4 — Worked Example: length contraction (spacecraft at v = 0.5c)
```text
Q: A spacecraft passes Earth at 0.5c. By what percentage is it contracted?

Step 1 — γ at 0.5c = 1.155   (from Listing 2)

Step 2 — Ratio of measured length to proper length:
    L / L₀ = 1 / γ = 1 / 1.155 = 0.866

Step 3 — Interpret:
    Measured length = 86.6% of proper length
    Contraction      = 100% − 86.6% = 13.4%

Answer: contracted to 86.6% of proper length (a 13.4% contraction).
Note: at 0.1c the contraction is < 1% — significant effects only beyond ~0.1c.
```

### Listing 5 — Worked Example: the muon evidence, both frames (Rossi–Hall)
```text
Data: muon proper half-life t₀ = 1.56 μs (measured at rest in the lab).
      Journey takes 6.5 μs by Earth clocks; muons decay as though only 0.7 μs passed.

(a) Proper time for the half-life:
    = the half-life in the muon's own rest frame = 1.56 μs

(b) Lorentz factor from the two journey times:
    γ = t / t₀ = 6.5 / 0.7 = 9.29

(c) Speed of the muons (from γ):
    v = c √(1 − 1/γ²) = c √(1 − 1/9.29²) = c √(1 − 0.0116) = 0.994c

(d) Half-life measured from Earth's frame (dilated):
    t = t₀ γ = (1.56 × 10^-6)(9.29) = 1.45 × 10^-5 s ≈ 14 μs

Both-frames narrative (full-mark answer):
    Earth frame: muon clock is TIME-DILATED → half-life stretched 1.56 μs → ~14 μs,
                 long enough to cross the atmosphere before decaying.
    Muon frame:  half-life is the normal 1.56 μs, but the atmosphere is
                 LENGTH-CONTRACTED → short journey, completed before decay.
    One result: far more muons reach the surface than classical physics predicts.
```

### Listing 6 — Worked Example: spaceship at v = 0.8c (exam Question 2)
```text
Q: Ship passes Earth at 0.8c. One year passes on the ship. Time on Earth?

Step 1 — γ at 0.8c:
    v²/c² = (0.8)² = 0.64
    1 − 0.64 = 0.36
    √0.36 = 0.6
    γ = 1 / 0.6 = 1.67

Step 2 — Identify proper time:
    1 year on the ship; the ship's clock is present at both events → t₀ = 1 yr.

Step 3 — Apply t = t₀ γ:
    t = 1 × 1.67 = 1.67 years on Earth.

Answer: 1.67 years pass on Earth per ship-year.
```

### Listing 7 — Worked Example: contracted rod at v = 0.6c (exam Question 5)
```text
Q: A 1.00 m rod (rest length) moves at 0.6c along its length. Measured length?
   Does its perpendicular width change?

Step 1 — γ at 0.6c:
    v²/c² = (0.6)² = 0.36
    1 − 0.36 = 0.64
    √0.64 = 0.8
    γ = 1 / 0.8 = 1.25

Step 2 — Proper length L₀ = 1.00 m (rest-frame length).

Step 3 — Apply L = L₀ / γ:
    L = 1.00 / 1.25 = 0.80 m

Answer: measured length = 0.80 m.
Perpendicular width: UNCHANGED — contraction acts only along the motion.
```

### Listing 8 — Key values, constants and evidence (reference data)
| Item | Correct value / form |
|------|----------------------|
| Speed of light c | 3.0 × 10^8 m s^-1 (exact: 299 792 458 m s^-1) |
| Lorentz factor γ | 1 / √(1 − v²/c²); dimensionless; always ≥ 1 |
| γ at 0.5c | 1.155 |
| γ at 0.6c | 1.25 |
| γ at 0.8c | 1.67 |
| γ at 0.994c | 9.29 (Rossi–Hall muons) |
| Proper time t₀ | events at the SAME place (clock's rest frame); the shorter time |
| Proper length L₀ | object's REST frame; the longer length |
| Muon proper half-life (Jacaranda) | 1.56 μs = 1.56 × 10^-6 s |
| Muon mean lifetime (alternative model) | 2.2 μs — do NOT mix with the 1.56 μs half-life |
| Rossi–Hall experiment | Bruno Rossi & David Hall, 1941; muon flux drops far less than classical prediction |
| Hafele–Keating experiment | 1971; caesium atomic clocks on airliners (east, west, ground) matched predictions |
| Atomic-clock basis | caesium-133; 1 second = 9 192 631 770 oscillations |
| GPS correction | without relativity, timing drifts > 30 μs/day → km-scale navigation errors |
| Hendrik Lorentz | 1853–1928; "Lorentz factor", "Lorentz contraction" |
| Fitzgerald–Lorentz proposal | Fitzgerald (1889) & Lorentz (1892): a PHYSICAL contraction to save the aether; Einstein needs no force, no aether |
| Einstein's relativity paper | 1905 (special relativity) |
| Metre (modern definition) | distance light travels in vacuum in 1/299 792 458 s |
