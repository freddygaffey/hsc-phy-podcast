---
title: "Supplementary Materials — Eddy Currents: Lenz's Law in Bulk Conductors"
module: M6
lesson: "12"
script: script.md
---

# Supplementary Materials

Key equations, the worked braking example, the model extended-response answer, and the help-versus-harm reference table for this episode. Nothing here is spoken in the audio — it is the read-along reference.

### Listing 1 — Electromagnetic braking, worked numerical example
```text
PROBLEM
Roller-coaster car:  m = 600 kg
Enters braking section at  v_i = 25 m s^-1
Leaves at                  v_f = 5.0 m s^-1
Braking distance           d   = 30 m
Find: (a) KE removed   (b) where it goes   (c) average braking force

(a) KINETIC ENERGY REMOVED        K = ½ m v²
    K_i = ½ × 600 × (25)²  = ½ × 600 × 625 = 187 500 J
    K_f = ½ × 600 × (5.0)² = ½ × 600 × 25  =   7 500 J
    ΔK  = K_i − K_f = 187 500 − 7 500 = 180 000 J
    ΔK  = 1.8 × 10^5 J  (180 kJ)

(b) ENERGY PATHWAY (irreversible)
    kinetic energy → electrical energy of eddy currents → thermal energy
    Dissipated by resistive (Joule) heating in the conductor:  P = I² R
    ⇒ ~180 kJ of heat is generated in the rail / fin.

(c) AVERAGE BRAKING FORCE          W = F d = ΔK
    F = ΔK / d = 180 000 / 30 = 6 000 N
    F = 6.0 × 10^3 N, directed OPPOSITE to the car's motion.

NOTE: 6000 N is an AVERAGE. The instantaneous force is largest at 25 m s^-1
(largest ΔΦ/Δt → largest eddy current → largest F) and falls as v falls.
Because F → 0 as v → 0, eddy brakes cannot deliver the final stop alone.
```

### Listing 2 — Model extended-response answer (6 marks): "Explain how electromagnetic braking works, with reference to eddy currents and Lenz's law."
```text
When a solid metal conductor (train wheel, disc or fin) moves through an external
magnetic field, the magnetic flux through the region of metal inside the field
changes. By Faraday's law of electromagnetic induction, this changing flux induces
an EMF in the metal:  emf = −N (ΔΦ / Δt).

Because the conductor is a solid bulk material rather than a wire, the induced EMF
drives circulating closed loops of current within the body of the metal. These are
EDDY CURRENTS.

By Lenz's law, the eddy currents flow in the direction that creates a magnetic field
opposing the change in flux that produced them. As a consequence, the side of each
eddy-current loop lying inside the external field is a current-carrying conductor in
a magnetic field and therefore experiences a force (F = BIL). The right-hand push
rule shows this force always acts OPPOSITE to the direction of motion — a braking
(retarding) force.

This opposing direction is required by conservation of energy: if the induced force
aided the motion, the conductor would gain kinetic energy while also generating
electrical energy — creating energy from nothing. Instead, the braking force does
negative work, removing kinetic energy, which is transferred to the eddy currents and
then dissipated as thermal energy through resistive heating (P = I²R) as the electrons
collide with the metal lattice. The process is irreversible and always heats the metal.

Because the induced EMF — and hence the eddy current and braking force — all increase
with the rate of change of flux, the braking force INCREASES WITH SPEED. Electromagnetic
braking is therefore strongest at high speed and weakens as the object slows, giving
smooth, wear-free, contactless braking — but the force falls to zero as the object
stops, so it cannot by itself bring the object fully to rest.

MARKING TARGETS HIT: defines eddy currents in a bulk conductor; Faraday's law as the
origin; Lenz's law for direction; motor-effect force opposing motion; conservation-of-
energy justification; KE → heat dissipation; speed-dependence.
```

### Listing 3 — Where eddy currents help vs harm
| Context | Eddy currents are… | Mechanism / outcome | Engineering response |
|---|---|---|---|
| Train / tram / coaster brakes | Useful | Force opposes motion; smooth, contactless, wear-free; stronger at high speed | Exploit — switch the electromagnet on |
| Induction cooktop | Useful | AC field induces eddy currents in the pot → I²R heats the pot directly (~80% eff. vs ~43% gas) | Exploit; ceramic surface stays comparatively cool |
| Induction furnace | Useful | Eddy currents melt and stir the metal charge | Exploit |
| Metal detector / induction switch | Useful | Eddy currents load the coil, shift the oscillator frequency (up to ~22 MHz) → relay trips | Exploit |
| Moving-disc electricity meter | Useful | Disc braked in proportion to power drawn → measures energy use | Exploit |
| Transformer iron core | Harmful | Alternating flux induces eddy currents → heat loss, lower efficiency | Laminate the core (thin insulated sheets along flux); or use a ferrite |
| Motor / generator core | Harmful | Same eddy-current heating in rotor / stator cores | Laminate the core |

### Listing 4 — Core equations for this episode (words, symbols, SI units)
```text
FARADAY'S LAW (origin of the eddy current)
  "Induced EMF = −(number of turns) × (rate of change of magnetic flux)"
  emf = −N (ΔΦ / Δt)
  emf  induced EMF, volts (V)
  N    number of turns (dimensionless; N = 1 for a single bulk loop)
  ΔΦ   change in magnetic flux, webers (Wb)
  Δt   change in time, seconds (s)
  The minus sign is Lenz's law: the induced effect opposes the change.

MAGNETIC FLUX
  "Flux = field strength × area × cosine of angle to the normal"
  Φ = B A cos θ
  Φ  magnetic flux, webers (Wb)
  B  magnetic flux density / field strength, teslas (T)
  A  area, square metres (m²)
  θ  angle between B and the normal (area vector) to the loop

MOTOR-EFFECT FORCE on the eddy current (why it brakes)
  "Force = field × current × length in field × sine of angle"
  F = B I L sin θ      (= B I L when current ⟂ field)
  F  force, newtons (N)
  B  field strength, teslas (T)
  I  current, amperes (A)
  L  length of conductor in the field, metres (m)

RESISTIVE (JOULE) HEATING — where the energy ends up
  "Power dissipated = current squared × resistance"
  P = I² R
  P  power dissipated, watts (W)
  I  current, amperes (A)
  R  resistance, ohms (Ω)

ENERGY BOOKKEEPING (braking)
  Work by braking force = loss in kinetic energy = heat generated
  W = F d ;   ΔKE = ½ m v_i² − ½ m v_f²
  W  work, joules (J);  F  force, N;  d  distance, m;  m  mass, kg;  v  speed, m s^-1
```
