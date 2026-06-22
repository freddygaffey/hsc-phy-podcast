# Audio Comprehensibility & Speed Listening — Research Report

**Date:** 2026-06-21
**Method:** `deep-research` workflow — 5 search angles → 22 sources fetched → 98 claims extracted → 25 adversarially fact-checked (3-vote, need 2/3 to kill) → 20 confirmed, 5 refuted → synthesized.
**Run ID:** `wf_27150e58-70f`
**Raw data:** `findings.json` (structured), `raw-transcripts/` (211 subagent transcripts), `workflow-script.js` (harness).

**Question:** Best algorithms/techniques to make audio the most comprehensible (time-scale modification like WSOLA/PSOLA, intelligibility enhancement, silence/pause compression, spectral & prosody processing), AND how "speed listening" works at playback speeds greater than 16× — perceptual limits, training/adaptation effects, and the signal-processing that makes extreme speed-ups intelligible.

---

## ⚠️ Headline: "16×" is a category error

The scientific literature does **not** measure playback in "×" multipliers — it measures speech **rate in syllables/second** (or words/minute). There is **no credible evidence for intelligible speech at anything like 16× normal playback.**

| Listener | Comprehension ceiling | vs. normal speaking rate |
|---|---|---|
| Normal speaking rate | ~6–8 syllables/sec | 1× |
| Untrained sighted listener | ~11–16 syll/sec | ~2–3× |
| **Trained late-blind listener** | **~22 syllables/sec** | **~3×** |

The documented human ceiling — even for elite trained blind screen-reader users — is roughly **3× a normal speaking rate**, not 16×. "16 syllables/second" (a real research test point) is ~2–3× normal; at that rate untrained sighted listeners score **below 16%** comprehension (mean ~9%). Forum claims of "16× speed listening" conflate the app's playback multiplier with the underlying speech rate.

---

## Part 1 — Algorithms that make sped-up audio comprehensible

### Foundation: Time-Scale Modification (TSM)
TSM = changing playback speed **without** changing pitch. Naive resampling raises pitch ("chipmunk") and destroys intelligibility. Every podcast app's speed button is TSM under the hood. *(Driedger & Müller, Applied Sciences 2016; Stanford CCRMA / J.O. Smith)*

### The two classical algorithms

**WSOLA (Waveform Similarity Overlap-Add)** — workhorse for speech.
- Allows each analysis frame to shift by up to ±δ_max samples, picking the shift that **maximizes cross-correlation** so periodic (harmonic) structures align across the overlap region — removing the phase-jump artifacts of plain overlap-add.
- Speech is predominantly harmonic → WSOLA gives very high-quality results, pitch/timbre unchanged. *(Verhelst & Roelands, IEEE 1993; Banai & Lavner 2012)*

**PSOLA (Pitch-Synchronous Overlap-Add)** — preferred for uniform time-compression.
- As compression increases, it shifts the speech **modulation spectrum** to higher modulation frequencies while preserving the modulation-spectrum *shape* and spectral/pitch features. Chosen for predictable, uniform behavior. *(Gransier et al., JARO 2022)*

**Phase vocoder (PV-TSM)** — frequency-domain alternative; preserves harmonic signals well.

### Universal caveat: no single method wins
WSOLA and the phase vocoder preserve **harmonic** signals (speech, sustained tones) well but introduce artifacts on **percussive/transient** material. State-of-the-art fix: **harmonic-percussive separation** — split, stretch each part with the suited method, recombine. "There is no single TSM method that can cope with all kinds of audio signals equally well." *(Driedger & Müller 2016)*

### Why pitch-preserving TSM beats naive speed-up
de Haan (1977): the intelligibility threshold for pitch-preserving compressed speech is **significantly higher** than for pitch-raising "speeded" speech — you stay intelligible at a faster rate. Core justification for TSM over plain fast playback.

### Production-ready libraries
- **Rubber Band** — `github.com/breakfastquay/rubberband` — high quality, widely used (Audacity).
- **SoundTouch** — `surina.net/soundtouch` — WSOLA-based, real-time, embeddable.
- **PyTSMod** — `github.com/KAIST-MACLab/PyTSMod` — Python; OLA/WSOLA/PV/PSOLA — ideal for experiments.

---

## Part 2 — How speed listening works (and where the wall is)

### The bottleneck is the memory buffer, not the ears
For normal/sighted listeners, the limit on fast speech is **limited temporary phonological storage (buffer saturation), NOT a hard acoustic speed constraint** (left inferior frontal gyrus, anterior insula, SMA/pre-SMA). The brain *hears* the fast audio fine; it runs out of buffer before processing it. *(Hertrich et al., Frontiers in Psych. 2013; Vagharchakian et al., J. Neurosci. 2012)*

**Practical exploit:** inserting brief **silent gaps** lets the buffer drain and **restores intelligibility** at high compression. Scientific basis for "trim silence + chunked playback." (Optimal gap timing is still open.)

### Comprehension ≠ intelligibility
- **Word intelligibility** — can you identify the word?
- **Discourse comprehension** — can you follow the meaning?

Heiman et al. (1986): words that are perfectly intelligible in isolation become **less intelligible packed into a fast message** — a processing-*time* bottleneck. Comprehension declines around **~275 wpm**. *(Foulke & Sticht 1969)*

### Plasticity: training moves the ceiling (two phases)
1. **Rapid adaptation** — 10–20 sentences measurably improves identification, but stays below ceiling (~40–85% correct).
2. **Slow, deep, training-dependent learning** — months of daily exposure → large, lasting, stimulus-specific gains. *(Banai & Lavner 2012, "More than Rapid Adaptation")*

**Blind power-user evidence:** late-blind people using TTS screen readers ~1hr+/day for ~6 months: **4 of 6 reached ~70% word comprehension at 18 syll/sec** (from <14%). Their brains recruit **visual cortex via cross-modal plasticity** — which is why it does *not* fully generalize to sighted users. *(Dietrich et al. 2013; Moos & Trouvain 2007)*

---

## Reconciliation: a real-world "Audible at 3.5× for 4 months" data point

A trained listener reporting sustained Audible 3.5× **fits** the research — the trap is again the baseline.

Audible's "1×" is the *recorded narration* rate, and audiobook narration is deliberately slow/over-articulated (~150 wpm per ACX guidance). So:

```
3.5 × ~150 wpm  ≈  525 wpm
525 wpm × ~1.5 syllables/word  ≈  ~13 syllables/second
```

**~13 syll/sec sits inside the documented untrained ceiling band of 11–16 syll/sec** — and a *trained* listener (4 months continuous = the deep second-phase learning) comfortably near the top of that range is exactly what the literature predicts. That's ~3–3.5× of a *slow narration* baseline ≈ ~2× a *conversational* baseline — nowhere near 16×. The different denominators are the whole story.

*Caveats: narration baseline (~150 wpm) and syllables/word (~1.5) vary by narrator/book/language; "comprehension" here = following content, not verbatim capture.*

---

## Confirmed findings (20 → synthesized to 10, all `high` confidence, ≥2/3 votes)

See `findings.json` for full evidence quotes, vote tallies, and per-claim sources. Summary:

1. Speed-listening rests on TSM (pitch-preserving). `3-0`
2. WSOLA/PV preserve harmonic signals, artifact on percussive; combine methods. `3-0`
3. WSOLA's edge = ±δ_max frame shifts maximizing cross-correlation. `3-0`
4. PSOLA shifts modulation spectrum up while preserving its shape (uniform compression). `3-0`
5. Pitch-preserving TSM has a higher intelligibility threshold than naive speed-up. `3-0`
6. Words intelligible in isolation degrade inside a fast message; intelligibility ≠ comprehension. `3-0`
7. Bottleneck = phonological buffer saturation, not acoustic speed; silent gaps restore it. `3-0`
8. Untrained ceiling ~11–16 syll/sec; comprehension declines ~275 wpm. `3-0`
9. Trained late-blind reach ~22 syll/sec (~3× sighted ~8 syll/sec ceiling) — plastic limit. `3-0`
10. Adaptation is two-phase; months of daily exposure → large lasting gains (4/6 hit ~70% at 18 syll/sec). `3-0`

## Refuted in adversarial review (5 — read ceilings as ranges, not constants)
- "Untrained ceiling is exactly ~8 syll/sec" `1-2`
- "Intelligibility threshold is exactly 11–16 syll/sec" `1-2`
- "Near-100% identification up to ~8 syll/sec" `0-3`
- "Reduced comprehension is *primarily* reduced word intelligibility" `0-3`
- "Max untrained rate is ~8 syll/sec" `1-2`

## Open questions (candidates for the next research round)
1. Modern intelligibility-enhancement beyond WSOLA/PSOLA — adaptive per-phoneme compression, formant/clarity enhancement, **neural-network TSM** — what most improves comprehension at high speed-up? *(Not covered by this pass.)*
2. Does periodic silent-gap insertion (buffer-drain) translate into a deployable consumer technique, and what gap timing/ratio is optimal?
3. Can blind-listener-style months-long adaptation be replicated in sighted users, and how far past ~11–16 syll/sec can a trained sighted listener reach?
4. Non-uniform (content-aware / variable-rate) compression vs. uniform PSOLA/WSOLA at extreme rates.

## Key sources (all peer-reviewed primary unless noted)
- Driedger & Müller, *Applied Sciences* 2016 — TSM overview (audiolabs-erlangen.de)
- Verhelst & Roelands, IEEE 1993 — original WSOLA
- Gransier et al., *JARO* 2022 — PSOLA, perceptual limits (PMC9085996)
- de Haan, *Perception & Psychophysics* 1977 (10.3758/bf03199702)
- Heiman et al., *Perception & Psychophysics* 1986 (10.3758/BF03208200)
- Foulke & Sticht, *Psychol. Bulletin* 1969 — intelligibility vs comprehension
- Hertrich et al., *Frontiers in Psychology* 2013 (PMC3745084); Vagharchakian et al., *J. Neurosci.* 2012
- Banai & Lavner, *PLoS ONE* 2012 (PMC3467231) — perceptual learning
- Dietrich et al., *Frontiers Hum. Neurosci.* 2013 (PMC3805979); PMC3847124 — trained blind listeners
- Nature *Sci. Reports* s41598-023-29755-x — 11–16 syll/sec
- Libraries: Rubber Band, SoundTouch, PyTSMod

Full source list with quality ratings and per-source claim counts: `findings.json` → `sources[]`.
