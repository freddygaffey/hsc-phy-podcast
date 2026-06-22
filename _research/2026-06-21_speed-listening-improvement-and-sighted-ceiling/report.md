# Speed-Listening: Improvement Methods & the Realistic Sighted Ceiling

**Date:** 2026-06-21
**Method:** `deep-research` workflow — 5 angles → 23 sources → 99 claims → 25 fact-checked (20 confirmed, 5 killed).
**Run ID:** `wf_9125bf95-2c8`
**Raw data:** `findings.json`, `raw-transcripts/`, `workflow-script.js`.

**Question:** Best evidence-based training to improve a *sighted* person's speed listening; the realistic sighted ceiling; throughput tricks that don't raise syllable rate; tools beyond Audible 3.5×; practitioner knowledge. Context: user at Audible 3.5× (~13 syll/sec) for 4 months, wants "10×" ideal / "7×" acceptable.

---

## Headline: 7× and 10× are not physically reachable

**No** — 7× and especially 10× are not achievable as raw syllable-rate increases for *any* human, sighted or blind.

- Your **3.5× of slow Audible narration (~150 wpm) ≈ ~13 syllables/sec** — already at the **top of the documented untrained-sighted band** (~9–16 syll/sec). Untrained intelligibility collapses from **99.8% at 6.6 sps → 41.9% at 15.6 sps** (PMC9938863, 2023).
- The **absolute human ceiling is ~22 syll/sec**, reached **only by trained late-blind listeners using formant-synth TTS** (not compressed audiobooks), after ~6 months daily training + visual-cortex plasticity.
- Mapping your targets against the slow baseline: **7× ≈ ~26 syll/sec, 10× ≈ ~37 syll/sec** — both beyond *all* documented human comprehension. Even the 22 syll/sec record is only **~6×** of the slow baseline.

| Rate | syll/sec (approx) | Status |
|---|---|---|
| Audible 1× (slow narration ~150 wpm) | ~3.7 | baseline |
| **Your 3.5× now** | **~13** | top of untrained-sighted band |
| Untrained-sighted comprehension edge | ~15–16 | comprehension ~42% |
| Realistic *trained* sighted target (natural speech) | ~15–18 | degraded comprehension |
| Absolute record (trained blind, formant TTS) | ~22 (~6×) | not reachable with natural audio |
| **Your "7×" goal** | **~26** | beyond any human |
| **Your "10×" goal** | **~37** | far beyond any human |

**Key nuance:** the 22 syll/sec ceiling is a **formant-synthesized-TTS + trained-blind** result. For **natural compressed speech** (which is what re-encoded Audible is), the blind advantage **nearly vanishes** — sighted listeners perform comparably or better (Moos & Trouvain 2007; J. Speech Sciences 2018). So natural audiobooks have a *lower* effective ceiling than the synthetic-TTS record.

---

## So what *can* actually move the needle

Two levers, both real and evidence-backed:

### Lever A — Training (push from ~13 toward ~15–18 syll/sec)
- **Progressive easy-to-hard ramp beats starting hard.** Adaptive-incremental staircase reached **91%** word accuracy at 30% compression vs **76%** for a constant-high group — which performed *worst* of all trained groups. *Never jump straight to max speed.* (Gabay/Karni/Banai, PLoS One 2017, PMC5436740)
- **Timeline:** measurable gains in a single ~1-hr session (5 blocks × 60 trials), but durable, *transferable* gains need **multiple sessions**. Two-phase learning (fast initial → slow stimulus-specific); most gain between sessions 1–2; documented protocol = **5 sessions / 10 days / 300 sentences, two-down-one-up staircase**, large effect (d=1.37). (Banai & Lavner 2012, PMC3467231)
- **Brief practice doesn't generalize** — only sustained multi-session training transfers to new material. This matches your 4-month adaptation arc. (Banai & Lavner, JASA 2014, PMID 25324090)
- **The one documented sighted data point:** in the Dietrich 2013 study, the **sighted control subject** trained to **~67% comprehension at 18 syll/sec** with formant TTS over ~6 months — proof a sighted person *can* reach ~18 syll/sec, but only with synthetic speech and intense daily training. (PMC3805979)

### Lever B — Throughput tricks (more content/hour *without* raising syllable rate)
- **★ Boundary-pause "time-restoration" (highest leverage):** insert silent pauses at **clause and sentence boundaries** (not uniformly). This restored normal-hearing recall to **~95% of normal-rate baseline (p=.874, statistically indistinguishable)** while words stayed fast — and *reduced* listening effort (pupillometry). Optimal: silence only at linguistic boundaries; **sentence-boundary pauses = 2× clause-boundary pauses**; total added silence ≈ restores original uncompressed duration. (O'Leary et al., Trends in Hearing 2023, PMC10637151)
- **Theta-band "repackaging":** 3× compression drops below 50% words-correct, but inserting **periodic ~80 ms gaps** restores intelligibility (U-shaped curve, 20–120 ms window); periodic beats aperiodic; re-establishes a ~9 Hz syllabic packaging rate that re-syncs the buffer. *Caveat:* the 80 ms optimum is paradigm-specific, not universal. (Ghitza & Greenberg, Phonetica 2009, PMID 19390234)
- **⚠ Don't over-fragment:** aggressive insertion (166 ms every 333 ms) *reduced* intelligibility; neural-tracking increases don't prove comprehension gains. Tune conservatively. (Deoisres et al., PLOS ONE 2023)
- **Content-aware variable-rate** (normalize every passage to a constant target syllable rate — speed slow speakers more, fast speakers less) is the *right strategy* over a blind multiplier, but deployed tools cap at ~5× because higher exceeds human comprehension regardless of player. (speech-speed Chrome extension, target 9 syll/sec, max 5×)

---

## Tools (coverage was thin — treat as leads, mostly unverified)
- **Sonic** (`github.com/waywardgeek/sonic) — the open-source library behind Android/Audible-style speed-up; designed for high-factor speech.
- **ffmpeg `atempo`** + silence-trimming filters — DIY re-encode pipeline beyond app caps.
- **Rubber Band / SoundTouch** — high-quality TSM for re-encoding (from round 1).
- **speech-speed** Chrome extension — content-aware normalization, max 5×.
- Overcast/Pocket Casts — "Smart Speed"/trim-silence (pause removal, the easy win).

*The research did not verify a single workflow that combines >3.5× + auto silence-trim + boundary-pause re-insertion. That's an open build opportunity.*

---

## Bottom line for you
1. **Drop the "×" framing** — you're already at the top of the normal human band. There is no 7×/10× to reach.
2. **Biggest realistic win = boundary-pause time-restoration + silence-trimming**, not a higher multiplier. You keep ~13 syll/sec but comprehension/recall climbs toward baseline, and trimmed dead air means more book per hour anyway.
3. **If you train for raw rate**, use a *gradual ramp*, multiple short sessions, and accept that ~15–18 syll/sec (with synthetic/clear speech) is the realistic frontier — not 26–37.
4. **Natural audiobook narration caps lower** than synthetic TTS. If you want the absolute frontier, the medium itself (formant TTS) matters — which is exactly what round 3 investigates.

## Refuted in review (5) — read ceilings as ranges
"Sighted control hit a hard un-improvable ceiling" `0-3`; "sighted ceiling is exactly 8 syll/sec" `0-3`; "100 ms inter-syllable gaps help across all conditions" `1-2`; "3 sessions strictly required for any transfer" `1-2`; "untrained sighted ceiling is exactly 9–14 syll/sec" `1-2`.

## Open questions → candidates for a follow-up round
1. A concrete pipeline (ffmpeg/Sonic/Rubber Band) combining >3.5× + auto silence-trim + boundary-pause re-insertion in one workflow.
2. Does time-restoration's recall benefit hold over multi-hour listening, and net-positive on throughput once re-inserted silence is counted?
3. Any sighted listener exceeding ~18 syll/sec with *natural* (non-synthetic) compressed speech?
4. Practitioner/community knowledge (blind power users, r/speedlistening) — under-captured here.

## Key sources
Dietrich et al. *Front. Hum. Neurosci.* 2013 (PMC3805979) · Moos & Trouvain 2007 · PMC9938863 (2023 intelligibility collapse) · Gabay/Karni/Banai *PLoS One* 2017 (PMC5436740) · Banai & Lavner 2012 (PMC3467231) / 2014 (PMID 25324090) · O'Leary et al. *Trends in Hearing* 2023 (PMC10637151) · Ghitza & Greenberg *Phonetica* 2009 (PMID 19390234) · Deoisres et al. *PLOS ONE* 2023 · speech-speed extension · Sonic. Full list + quality ratings in `findings.json`.
