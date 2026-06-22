---
title: "Supplementary Materials — LEO and Geostationary Satellites — Newton's Orbits in Practice"
kind: case-study
script: script.md
---

# Supplementary Materials

### Listing 1 — Deriving orbital velocity (gravity = centripetal force)
```text
Set gravitational force equal to centripetal force:
  G*M*m / r^2  =  m*v^2 / r

Cancel the satellite mass m from both sides:
  G*M / r^2  =  v^2 / r

Multiply both sides by r:
  G*M / r  =  v^2

Take the square root:
  v = sqrt( G*M / r )

where:
  v = orbital speed (m/s)
  G = 6.674e-11 N m^2 kg^-2  (universal gravitational constant)
  M = 5.972e24 kg            (mass of the Earth)
  r = orbital radius from Earth's CENTRE (m) = R_earth + altitude

Key results:
  - satellite mass m cancels: orbital speed is independent of satellite mass
  - larger r  ->  smaller v  (higher orbits are slower)
```

### Listing 2 — Deriving Kepler's Law of Periods from Newton
```text
Start again from gravity = centripetal force:
  G*M*m / r^2  =  m*v^2 / r

Orbital speed in terms of period T (one lap = circumference / time):
  v = 2*pi*r / T

Substitute and simplify:
  G*M / r^2  =  (2*pi*r / T)^2 / r
  G*M / r^2  =  4*pi^2*r / T^2

Rearrange:
  r^3 / T^2  =  G*M / (4*pi^2)   =  constant

This is Kepler's Third Law: T^2 is proportional to r^3,
with the constant fixed by the mass of the central body only.
```

### Listing 3 — Worked example: solving for geostationary altitude
```text
Goal: find the altitude where orbital period = 1 sidereal day.

Given:
  T = 86,164 s            (one sidereal day, NOT the 86,400 s solar day)
  G = 6.674e-11 N m^2 kg^-2
  M = 5.972e24 kg
  R_earth = 6.378e6 m

Rearrange Kepler's law for r:
  r^3 = G*M*T^2 / (4*pi^2)

Step 1 - numerator G*M*T^2:
  G*M     = 6.674e-11 * 5.972e24 = 3.986e14
  T^2     = (86,164)^2           = 7.424e9
  G*M*T^2 = 3.986e14 * 7.424e9   = 2.959e24

Step 2 - divide by 4*pi^2 (= 39.48):
  r^3 = 2.959e24 / 39.48 = 7.495e22  (m^3)

Step 3 - cube root:
  r = (7.495e22)^(1/3) = 4.216e7 m = 42,164 km   (from Earth's centre)

Step 4 - subtract Earth's radius for altitude:
  altitude = 42,164 - 6,378 = 35,786 km

Orbital speed at this radius (from Listing 1):
  v = sqrt(3.986e14 / 4.216e7) = 3,075 m/s  (about 3.07 km/s)
```

### Listing 4 — Orbit comparison table
| Orbit type | Altitude | Radius from centre | Orbital speed | Period | Example uses |
|------------|----------|--------------------|---------------|--------|--------------|
| Low Earth Orbit (LEO) | 200–2,000 km | ~6,600–8,400 km | ~7.7 km/s | ~90–127 min | ISS, imaging, weather |
| Medium Earth Orbit (MEO) | ~20,200 km | ~26,560 km | ~3.87 km/s | ~11 h 58 min | GPS / GNSS navigation |
| Geostationary (GEO) | 35,786 km | 42,164 km | ~3.07 km/s | 23 h 56 min 4 s | TV broadcast, weather, comms |
| ISS (specific LEO) | ~408–420 km | ~6,790 km | ~7.66 km/s | ~92.7 min | crewed station |

Note: ISS inclination 51.6 degrees; GEO inclination must be 0 degrees (equatorial) and eccentricity 0.

### Listing 5 — GPS relativistic clock correction
```text
Two relativistic effects act on a GPS satellite clock vs a ground clock.

SPECIAL RELATIVITY (satellite moves fast -> its clock runs SLOW):
  fractional rate ~ -v^2 / (2*c^2)
  v = 3,870 m/s ,  c = 3.00e8 m/s
  = -(3870)^2 / (2 * (3.00e8)^2)
  = -8.32e-11 per second
  -> about -7.2 microseconds per day

GENERAL RELATIVITY (weaker gravity at altitude -> clock runs FAST):
  fractional rate ~ +5.31e-10 per second
  -> about +45.9 microseconds per day

NET EFFECT (gravity term dominates):
  +45.9 - 7.2 = +38.4 microseconds per day  (satellite clock runs FAST)

Why it matters (convert timing error to position error):
  distance error = (38.4e-6 s) * (3.00e8 m/s) = 11,520 m ~ 11.5 km PER DAY

Engineering fix:
  Pre-set clocks to 10.22999999543 MHz on the ground instead of 10.23 MHz,
  so they tick at exactly 10.23 MHz once in orbit.
```

### Listing 6 — Gravitational field strength and why orbits are not "zero gravity"
```text
Gravitational field strength (inverse square law):
  g = G*M / r^2          where r = R_earth + altitude

At Earth's surface (r = 6.378e6 m):
  g = (6.674e-11 * 5.972e24) / (6.378e6)^2 = 9.80 N/kg  (= 9.8 m/s^2)

At ISS altitude (~400 km, r = 6.778e6 m):
  g = 3.986e14 / (6.778e6)^2 = 8.68 N/kg  (~89% of surface value)

Key teaching point:
  Orbit is NOT a zero-gravity region. At LEO altitudes g still exceeds 9 N/kg
  for most satellites. Weightlessness = experiencing ONLY gravity, in free fall,
  with no supporting (normal) force from below. It is not the absence of gravity.

  g  = GM/r^2   is the SAME quantity as centripetal acceleration  a = v^2/r
  for a satellite, because gravity alone supplies the centripetal force.
```

### Listing 7 — Energy of a satellite in orbit (and changing orbits)
```text
Convention: gravitational potential energy U = 0 at r = infinity,
so U is NEGATIVE everywhere closer in.

Gravitational potential energy:
  U = -G*M*m / r

Kinetic energy (from orbital speed v = sqrt(GM/r)):
  K = (1/2) m v^2 = G*M*m / (2r)        (note: K = -U/2)

Total mechanical energy of a circular orbit:
  E = U + K = -G*M*m / (2r)             (note: E = -K)

Consequences:
  - E is negative -> the satellite is gravitationally bound.
  - Larger r (higher orbit) -> LESS negative E -> MORE total energy.
  - To raise an orbit you must ADD energy, yet the higher orbit is SLOWER
    (v decreases), because added energy goes mostly into potential energy.

Work to move between orbits:
  W = E_final - E_initial = (G*M*m/2)(1/r_initial - 1/r_final)

Worked example (m = 1000 kg satellite at 400 km altitude, r = 6.778e6 m):
  U = -G*M*m/r        = -5.88e10 J
  K = +G*M*m/(2r)     = +2.94e10 J
  E = -G*M*m/(2r)     = -2.94e10 J
```

### Listing 8 — Escape velocity
```text
Escape velocity is the minimum launch speed for an object to leave a body's
gravitational field entirely (total energy = 0). Derived from K + U = 0:

  (1/2) m v_esc^2  -  G*M*m / r  =  0
  v_esc = sqrt( 2*G*M / r )

Depends only on G and the mass M and radius r of the body — NOT on the
mass of the escaping object.

For Earth (r = R_earth = 6.378e6 m):
  v_esc = sqrt( 2 * 3.986e14 / 6.378e6 ) = 1.12e4 m/s
        ~ 11.2 km/s  (~40,000 km/h)

Compare: at any altitude, orbital speed v_orbit = sqrt(GM/r),
so v_esc = sqrt(2) * v_orbit. Below v_esc you orbit; at or above it you leave.
```
