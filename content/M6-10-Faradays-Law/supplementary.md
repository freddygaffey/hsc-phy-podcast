---
title: "Supplementary Materials — Faraday's Law: Why Change Is Everything"
module: M6
lesson: "10"
script: script.md
---

# Supplementary Materials

Key equations, derivations, and worked numerical solutions for this episode. Nothing here is spoken in the audio — it is the read-along reference.

### Listing 1 — Worked example: rectangular loop entering a field

```text
GIVEN
  Loop dimensions   0.25 m × 0.30 m
  Field strength    B  = 0.66 T   (perpendicular to plane of loop)
  Time to enter     Δt = 2.0 s
  Number of turns   N  = 1

STEP 1 — AREA OF THE LOOP
  A = 0.25 × 0.30 = 0.075 m^2

STEP 2 — CHANGE IN FLUX  (Φ = B A cos θ)
  Field ⟂ plane → θ = 0 → cos θ = 1 → Φ = B A
  Φ_initial = 0            (loop outside the field, no flux through it)
  Φ_final   = B A = 0.66 × 0.075 = 0.0495 Wb  ≈ 0.05 Wb
  ΔΦ = Φ_final − Φ_initial = 0.0495 − 0 = 0.0495 Wb  ≈ 0.05 Wb

STEP 3 — FARADAY'S LAW   ε = −N (ΔΦ / Δt)
  ε = −(1)(0.0495 / 2.0)
  ε = −0.0248 V
  |ε| ≈ 0.025 V = 25 mV

  The minus sign = direction (opposes the increasing flux) = Lenz's law (M6-11).
  For a "magnitude" question, report the positive value: 0.025 V.

NUMBER-OF-TURNS VARIANT  (same flux change, N = 200)
  ε = 200 × 0.0248 ≈ 5.0 V
  Same ΔΦ/Δt, 200× the EMF — purely from more turns in series.
```

### Listing 2 — Worked example: squashed loop (changing the AREA, not the field)

```text
GIVEN
  Initial radius   r_i = 15.0 cm = 0.150 m   ← convert cm → m BEFORE squaring
  Final radius     r_f =  7.0 cm = 0.070 m
  Field strength   B   = 0.30 T  (constant, ⟂ to loop)
  Time             Δt  = 0.13 s
  Number of turns  N   = 1

AREAS  (A = π r^2)
  A_i = π (0.150)^2 = 0.07069 m^2
  A_f = π (0.070)^2 = 0.01539 m^2

FLUX  (Φ = B A, since θ = 0)
  Φ_i = 0.30 × 0.07069 = 0.02121 Wb
  Φ_f = 0.30 × 0.01539 = 0.004618 Wb

CHANGE IN FLUX
  ΔΦ = Φ_f − Φ_i = 0.004618 − 0.02121 = −0.01659 Wb
  (negative: flux decreased because the loop shrank)

FARADAY'S LAW   ε = −N (ΔΦ / Δt)
  ε = −(1)(−0.01659 / 0.13) = +0.1276 V
  |ε| ≈ 0.13 V

KEY POINT
  B never changed — only A did. Same Faraday machinery still gives an EMF.
  Constant field does NOT mean constant flux. (This is "lever A" of the BAT.)
```

### Listing 3 — Faraday's law: the relationships, terms and units

```text
FARADAY'S LAW OF ELECTROMAGNETIC INDUCTION
  ε = −N (ΔΦ / Δt)
    ε  = induced EMF (electromotive force)      (volt, V)
    N  = number of turns in the coil            (a pure count, no units)
    ΔΦ = change in magnetic flux = Φ_final − Φ_initial  (weber, Wb)
    Δt = time interval over which flux changes  (second, s)
    minus sign = direction; the EMF opposes the change (Lenz's law, M6-11)

  → EMF depends on the RATE OF CHANGE of flux, not the flux itself.
  → ΔΦ/Δt = 0  ⇒  ε = 0   (steady flux, however strong, induces nothing).

MAGNETIC FLUX (the quantity that changes)
  Φ = B A cos θ
    Φ = magnetic flux                 (weber, Wb;  1 Wb = 1 T·m^2 = 1 V·s)
    B = magnetic field strength       (tesla, T;   1 T = 1 Wb·m^-2)
    A = area of the loop              (m^2)
    θ = angle between B and the area vector (normal) of the loop
        θ = 0°  → cos θ = 1 → maximum flux (field straight through)
        θ = 90° → cos θ = 0 → zero flux   (field lies in the plane)

THREE WAYS TO CHANGE THE FLUX — "swing the BAT"
  B : change the field strength   (move a magnet; switch an electromagnet)
  A : change the area in the field (slide a rod on rails; loop enters field)
  θ : change the angle            (rotate the coil — this is a generator)
  All three change Φ, so all three induce an EMF by the same law.

MOTIONAL EMF — straight conductor moving ⟂ to a field
  ε = B L v   (derivable from Faraday: ΔΦ/Δt = B·(L·v·Δt)/Δt = B L v)
    B = field strength (T), L = length in field (m), v = speed (m·s^-1)
  Microscopic origin: each free charge feels force F = q v B,
  which separates charge to the ends of the rod → potential difference (EMF).
  (F = q v B is the same moving-charge force from M6-02.)

WORKED EXAM ITEM — square loop, rising field (script Q4)
  Side 0.20 m → A = 0.20^2 = 0.04 m^2
  Field ⟂ plane: 0 → 0.50 T in 0.10 s
  Φ_i = 0,  Φ_f = 0.50 × 0.04 = 0.02 Wb,  ΔΦ = 0.02 Wb
  ε = N (ΔΦ/Δt) = 1 × (0.02 / 0.10) = 0.2 V
```

### Listing 4 — Induction in the three named systems (the mechanism, in order)

```text
SOLENOID + MOVING MAGNET   (lever B: change field strength)
  Magnet approaches → field through coil ↑ → flux Φ ↑
    → Faraday: EMF induced in each turn → series → total = N × (EMF/turn)
      → current flows IF the coil is a closed circuit
  Magnet held still → Φ constant → ΔΦ/Δt = 0 → EMF = 0  (key exam point)

STRAIGHT CONDUCTOR MOVING THROUGH A FIELD   (lever A: change area)
  Rod cuts field lines → area of its circuit inside the field changes → ΔΦ
    Macroscopic: rate of cutting field lines sets the EMF (ε = B L v)
    Microscopic: F = q v B pushes + and − charges to opposite ends
      → charge separation → potential difference (EMF) across the rod
        → the rod acts as a source of EMF

METAL PLATE MOVING THROUGH A FIELD   (eddy currents — preview M6-12)
  No wire loops, but changing flux through the bulk still induces an EMF
    → drives circulating currents (EDDY CURRENTS) through the solid metal
      → by Lenz's law they oppose the motion (braking force)
  TRAP: "no loop, so no induction" is WRONG — bulk metal induces too.

WHY MORE TURNS → MORE EMF
  Every turn encloses the same changing flux → same EMF per turn.
  Turns are in series → EMFs add → N turns give N × the single-turn EMF.
```

### Listing 5 — Extended response: weak vs strong answer

```text
QUESTION: "Explain why an EMF is induced when a magnet is moved into a solenoid."

WEAK ANSWER (Band 4 — loses marks)
  "Moving the magnet into the coil causes a current to flow."
  Faults: collapses the chain; treats the magnet as directly making current;
          conflates EMF with current; names no law.

STRONG ANSWER (full marks) — the THREE-STEP CHAIN
  1. As the magnet moves in, the field through the coil increases,
     so the magnetic flux through the coil increases.
  2. By Faraday's law, this change in flux induces an EMF equal to the
     number of turns times the rate of change of flux (faster magnet or
     more turns → larger EMF).
  3. This induced EMF drives an induced current around the coil — but
     ONLY if the coil forms a complete circuit. (Open circuit: EMF still
     present, no current flows.)

  MEMORY HOOK:  "Flux, EMF, Current, if Closed."
  Flux changes → EMF appears → current flows (only with a closed loop).

  KEEP DISTINCT:  EMF (a voltage; exists with or without a circuit)
                  CURRENT (needs a complete conducting loop).
```

### Listing 6 — Reference data and common traps

| Item | Value / statement |
|------|-------------------|
| EMF (electromotive force) | symbol ε; unit volt (V); it is a voltage, NOT a force — the name is a misnomer |
| Magnetic flux | symbol Φ; unit weber (Wb); 1 Wb = 1 T·m² = 1 V·s |
| Magnetic field strength (flux density) | symbol B; unit tesla (T) = Wb·m⁻²; "flux density" means B, NOT flux Φ |
| Number of turns | symbol N (or n); a pure count, dimensionless |
| Δ (delta) | "change in" = final value − initial value |
| Electron charge magnitude | 1.6 × 10⁻¹⁹ C (for the q v B mechanism, if needed) |
| Michael Faraday | discovered electromagnetic induction, August 1831 (iron-ring + moving-magnet experiments) |
| Trap 1 | A strong but CONSTANT field induces nothing — only changing flux induces |
| Trap 2 | "Magnet makes current" collapses the chain — state flux → EMF → current (if closed) |
| Trap 3 | EMF ≠ current — open circuit still has an EMF, just no current |
| Trap 4 | Flux Φ ≠ field strength B — different symbols and units (Wb vs T) |
| Trap 5 | θ is measured from the NORMAL; max flux at θ = 0, zero flux at θ = 90° (use cos θ) |
| Trap 6 | Don't drop N — number of turns is itself an examinable factor |
| Trap 7 | Convert cm → m BEFORE squaring for area; mixing units gives errors of 10ⁿ |
| Trap 8 | The minus sign is direction only (Lenz) — for magnitude, report the positive value |
| Trap 9 | A metal plate with no wires can still be induced in (eddy currents) |
