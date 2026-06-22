---
title: "Supplementary Materials — Chadwick and the Discovery of the Neutron"
kind: case-study
script: script.md
---

# Supplementary Materials

Key equations, derivations, worked solutions and data tables for this episode. Nothing
here is spoken in the audio — it is the read-along reference. Each listing is referenced
by label in the narration.

### Listing 1 — Chadwick's mass calculation from conservation of momentum and energy

```text
SETUP: a neutral particle of unknown mass m_n and unknown speed v_n
strikes a STATIONARY target nucleus head-on in an ELASTIC collision.
The target recoils with speed v_target. Mass of the target = m_target.

Two conservation laws apply to the head-on elastic collision:

  Conservation of momentum:
      m_n · v_n  =  m_n · v_n'  +  m_target · v_target

  Conservation of kinetic energy (elastic):
      ½ · m_n · v_n²  =  ½ · m_n · v_n'²  +  ½ · m_target · v_target²

Standard result for a 1-D elastic collision (max recoil, head-on),
the target recoil speed is:

      v_target = ( 2 · m_n / (m_n + m_target) ) · v_n

DO THIS FOR TWO DIFFERENT, KNOWN TARGETS:

  Target 1 — hydrogen (a proton), mass m_H, measured recoil speed v_H:
      v_H = ( 2 · m_n / (m_n + m_H) ) · v_n

  Target 2 — nitrogen nucleus, mass m_N, measured recoil speed v_N:
      v_N = ( 2 · m_n / (m_n + m_N) ) · v_n

DIVIDE the two equations — the unknown incoming speed v_n CANCELS:

      v_H / v_N  =  (m_n + m_N) / (m_n + m_H)

REARRANGE to isolate the neutron mass m_n (everything else is measured):

      m_n = ( v_N · m_N  −  v_H · m_H ) / ( v_H  −  v_N )

RESULT: Chadwick obtained  m_n ≈ 1.15 × m_proton.
Crucially: the particle has mass ≈ a proton AND no charge → the NEUTRON.
```

### Listing 2 — Key masses and energies in the discovery

| Quantity | Value | Note |
|----------|-------|------|
| Proton mass | 1.67 × 10⁻²⁷ kg | hydrogen nucleus |
| Neutron mass (Chadwick, 1932) | ≈ 1.15 × proton mass | his measured figure |
| Neutron mass (modern value) | ≈ 1.0014 × proton mass | neutron just heavier than proton |
| Ejected proton speed (from wax) | 3.3 × 10⁷ m s⁻¹ | about 0.1 × speed of light |
| Energy required IF radiation were gamma | ≈ 50 MeV per photon | to eject protons at that speed |
| Energy actually available (incident alphas) | ≈ 5 MeV | ~10× less than 50 MeV → impossible |
| Bothe & Becker estimate (1930) | ≈ 10 MeV "gamma" | the original mislabelling |

### Listing 3 — The beryllium reaction that produces neutrons

```text
Chadwick's neutron source: alpha particles from a polonium source
strike beryllium-9. The nuclear equation is:

      beryllium-9  +  alpha  →  carbon-12  +  neutron

In symbol form (mass number on top, atomic number below):

      9-Be(4)  +  4-He(2)  →  12-C(6)  +  1-n(0)

CHECK conservation of nucleon number (top):   9 + 4  = 12 + 1   ✓
CHECK conservation of charge / proton number (bottom): 4 + 2 = 6 + 0  ✓

This was the first practical way to make a beam of free neutrons:
a high-energy alpha source (polonium) plus beryllium.
```

### Listing 4 — Why gamma rays fail but a massive neutral particle works

```text
THE CONTRADICTION (gamma-ray hypothesis):

  A photon's momentum is small for its energy:   p = E / c
  (c = 3 × 10⁸ m s⁻¹ is huge, so p is small).

  To shove a heavy proton to 3.3 × 10⁷ m s⁻¹ by a photon "kick"
  (Compton-style) would need a photon of about 50 MeV.

  But the incident alpha particles supply only about 5 MeV.
      50 MeV needed  vs  ~5 MeV available  =  ~10× shortfall
      →  violates conservation of energy.
  CONCLUSION: the radiation cannot be gamma rays.

THE RESOLUTION (neutral particle of mass ≈ proton):

  Equal-mass head-on elastic collision transfers nearly ALL the
  speed from projectile to target (like billiard balls).

      v_target ≈ v_projectile   when   m_projectile ≈ m_target

  So a neutral particle of ≈ proton mass, moving at the modest speed
  expected from a few-MeV reaction, ejects the proton at the observed
  speed WITHOUT any energy violation.
  CONCLUSION: the radiation is a stream of NEUTRONS.
```

### Listing 5 — Comparison of penetrating ability and charge

| Particle / radiation | Charge | Rest mass | Penetrating ability | Detectable by charge? |
|----------------------|--------|-----------|---------------------|-----------------------|
| Alpha (helium nucleus) | +2 | ≈ 4 proton masses | low — stopped by paper | yes (ionises strongly) |
| Proton | +1 | 1 proton mass | low–moderate | yes |
| Gamma ray (photon) | 0 | 0 | very high | no (but few interactions) |
| Neutron | 0 | ≈ 1 proton mass | very high | no — leaves no track |

### Listing 6 — Timeline of the discovery

```text
1919   Rutherford identifies the proton (bombarding nitrogen with alphas).
1920   Rutherford's Bakerian Lecture predicts a neutral particle ≈ proton
       mass, and names it the "neutron".
1930   Bothe & Becker (Germany): alpha + beryllium → penetrating radiation,
       ≈ 10 MeV, mislabelled as gamma rays.
1932   Joliot-Curies (Paris): that radiation ejects fast protons from
       paraffin wax — still called gamma rays.
1932   Chadwick (Cambridge) reads the paper; in barely a fortnight applies
       conservation of energy + momentum, measures neutron mass ≈ 1.15
       proton masses. Paper "Possible Existence of a Neutron" submitted to
       Nature on 17 February 1932.
1935   Chadwick awarded the Nobel Prize in Physics.
1938   Neutron-induced nuclear fission of uranium discovered (Hahn,
       Meitner, Strassmann) — opening the nuclear age.
```
