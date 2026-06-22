# Designing/Training a Voice (TTS) for High-Speed Comprehensibility

**Date:** 2026-06-21
**Method:** `deep-research` workflow — 6 angles → 25 sources → 119 claims → 25 fact-checked → **22 confirmed, 3 killed.**
**Run ID:** `wf_099544df-d63` (launched 16:18; died on laptop reboot mid-run; resumed from cache; a first resume's verification was degraded by an API rate-limit; a **second resume re-ran the failed verifiers cleanly** → this report reflects the recovered, fully-verified run, task `woe6pzpm8`).
**Raw data:** `findings.json`, `raw-transcripts/` (252 transcripts), `workflow-script.js`.

> **Provenance note:** an earlier copy of this report carried a degradation banner because a post-reboot resume hit an API rate-limit that killed ~40 verifier agents (claims came back `0-0 abstain`, i.e. unverified, not refuted). A second resume — reusing all cached search/fetch work — re-verified them. Final tally **22/3**; the 3 killed are now genuine 1-2 vote refutations. Angles 2 (formant-vs-neural) and 5 (engines) are now answered, not unresolved.

---

## Bottom line (well-supported)
**Generate at a normal rate, then time-compress + DSP. Do NOT fine-tune on clear-speech/fast-speech corpora to "natively" produce fast speech** — across multiple peer-reviewed studies, linear time-compression of a normal voice is *more* intelligible than both naturally-fast speech and time-compressed hyperarticulated "clear" speech at aggressive rates. The expensive tiers (fine-tune, train-from-scratch) are not justified; the value is in cheap, engine-agnostic DSP. **Two-track design is validated:** keep the natural Kokoro voice for students; ship an optional crisp/robotic (formant-synth) speed track for power listeners.

## Effort-tier recommendation
| Tier | Action | Evidence | Worth it? |
|---|---|---|---|
| **1 — Configure** (cheap) | Natural Kokoro default for students. For speed track: **generate at normal rate → linear/PSOLA time-compress**; tune pause length; consider an **eSpeak-NG/Eloquence-class formant synth** for the extreme >18 syll/s track | strong | ✅ **big win, ~zero cost** |
| **2 — DSP** (moderate) | Engine-agnostic: **SSDRC/Lombard-style spectral shaping + dynamic-range compression + consonant/HF boost**, and/or **repackaging** (insert silent gaps → ~4–5 packets/s) | strong | ✅ **best ROI above voice choice** |
| **3 — Fine-tune** (expensive) | Fine-tune Kokoro on clear-/fast-speech corpora | predicts **low/negative** gain | ❌ not worth it (one unproven hedge — see below) |
| **4 — Train from scratch** | Custom model | none | ❌ unjustified |

Gate any fine-tune behind a measured "significant gain" bar (STOI/STMI + modulation-spectrum + an A/B/MUSHRA panel at the **actual target rate and listener population**).

---

## Confirmed findings (all verified, mostly 3-0)

1. **Time-compression of a normal voice is the most intelligible route to fast speech.** Ranking best→worst: normal > 40% time-compressed > natural-fast (pairwise p≤.006). "Compressed normal speech is more intelligible than compressed clear speech even when overall duration is kept the same." Linear TC is processed faster than natural-fast even when both are intelligible (phoneme detection **572 ms vs 624 ms, +52 ms**). For synthetic voices: "generating at a normal rate then applying linear compression resulted in the most intelligible speech at all tested rates." *Mechanism:* natural fast speech deletes/distorts stops & affricates via coarticulation/lenition; TC preserves spectral fine structure + formant transitions. *(arXiv:1901.07239; Gordon-Salant PMC6377055; Janse 2004 S0167639303001092; S0167639315000977)*

2. **What carries intelligibility (and what DSP must protect):** dynamic **formant movement/transitions** (β=0.576, p<0.0001 — not static targets), **high-frequency consonant/fricative energy** (clear-speech fricative gains 7–38 pts, driven by spectral energy shifting higher), and an **expanded vowel space** (F2 +14%, F1 +9%) with **~1.5× longer vowels** (290 vs 204 ms) for processing time. *(Ferguson & Quené/Neel JASA 2014 PMC4048446; Maniwa/Jongman/Wade 2007/2008)*

3. **The intelligibility "core" = low-frequency spectro-temporal modulation:** temporal **~1–8 Hz**, spectral **<4 cycles/kHz** (bandpass in time, low-pass in frequency). Comprehension drops when these are removed. → defines DSP targets and the right metrics (**modulation-spectrum, STOI, STMI**). *(Elliott & Theunissen, PLoS Comp Biol 2009, PMC2639724)*

4. **Repackaging restores intelligibility (key cheap DSP lever):** inserting silent gaps so speech arrives in packets at **~5 packets/s (young) / 4 (older)** markedly beats continuous compression. **Rhythm, not raw rate, governs comprehensibility.** Engine-agnostic. *(JASA 2018, PMC6181647. The "theta hard neural ceiling" framing was refuted 1-2 — it's a validated technique, not proof of a fixed ceiling.)*

5. **★ Angle 2 — Blind power listeners & formant synths (now confirmed 3-0):** trained vision-impaired listeners comprehend ultra-fast speech **up to ~22 syll/s (~2.75× the ~8 syll/s sighted max)**; at 16 syll/s they averaged **59.7% vs 9.0%** for sighted controls. Those experiments used the **Eloquence formant synthesizer (via JAWS)** — the same class power users favor. → points to a **formant-synth engine for the extreme track.** *(Dietrich/Hertrich/Ackermann PMC3805979, PMC3847124; PMC3955012. Caveat: some lit puts the sighted max at 11–16 syll/s, shrinking the multiplier toward ~1.5×.)*

6. **★ Naturalness vs. intelligibility diverge at speed (now confirmed 3-0):** novices prioritize voice naturalness; **expert screen-reader users care little about TTS quality and prioritize reliability/responsiveness/predictability** (application-support χ²=23.77, p<.001). Experts speed up output, *accepting* the robotic timbre novices dislike. → **validates the two-track design** rather than one compromise voice. *(Sorscher et al., "The voice has it," PMC3955012; n=146 survey + 20 interviews.)*

7. **DSP enhancement gives large objective gains, engine-agnostic:** Lombard + SSDRC spectral shaping/dynamic-range compression → **110–130% SIIB-Gauss improvement** in speech-shaped noise, 47–140% in competing-speaker noise. Works locally on Kokoro/Piper output. *Scope caveat:* these are intelligibility-**in-noise** gains vs a weak baseline, not directly high-**speed** gains — used as mechanism evidence. *(Paul et al., Interspeech 2020, arXiv:2008.05809)*

8–9. **Measurement & tiering (medium confidence, synthesized):** gate decisions with objective modulation/intelligibility metrics **plus** subjective A/B at the real target rate; remember **TC recognition over-estimates natural-fast recognition**, and student vs. power-listener capacity differs ~2.5–3×.

## Genuinely refuted (3, voted 1-2)
- "Theta band sets a hard neural ceiling TC can't overcome" — correlational/contested mechanism.
- "Hyperarticulation easier across *all* listeners and *all* conditions (η²=0.82)."
- "Mimicking non-linear human fast-timing (compress unstressed more) helps" — it *hurts*; **so prosody-mimicking rate-aware generation is wasted effort.**

## Open questions → next-round candidates
1. **The one unrefuted fine-tune bet:** does clear-speech-fine-tuned TTS *then aggressively time-compressed* beat compressing a normal voice? Krause & Braida's rate-*independent* clear-speech gains were never tested under aggressive compression — the only Tier-3 option with theoretical upside.
2. Controlled local **engine bake-off** (Kokoro vs Piper vs RHVoice vs eSpeak-NG/Eloquence) at 14–22 syll/s with matched STOI/STMI + A/B.
3. How much does **content-aware per-phoneme variable-rate** (compress steady-state vowels more, preserve transitions/stops) add over uniform TC at speed?
4. Optimal **repackaging params** (gap duration, 4–5 packets/s) combined with DSP on real podcast audio — and whether gaps help/hurt untrained students vs. trained power listeners.

## Key sources
arXiv:1901.07239 · Gordon-Salant PMC6377055 · Janse 2004 (S0167639303001092) · S0167639315000977 · Ferguson & Quené JASA 2014 (PMC4048446) · Maniwa/Jongman/Wade 2007/2008 · Elliott & Theunissen PLoS Comp Biol 2009 (PMC2639724) · JASA 2018 repackaging (PMC6181647) · Dietrich PMC3805979 / PMC3847124 · Sorscher PMC3955012 · Paul et al. arXiv:2008.05809. Full list + per-claim votes in `findings.json`.
