# Better Local/Open TTS Models vs. Kokoro

**Date:** 2026-06-21
**Method:** `deep-research` workflow — 6 angles → 27 sources → 133 claims → 25 fact-checked → **23 confirmed, 2 killed.**
**Run ID:** `wf_176a89d4-985`
**Raw data:** `findings.json`, `raw-transcripts/` (111 transcripts), `workflow-script.js`.

**Question:** Best open/local TTS models to replace or augment Kokoro-82M for an English educational-podcast pipeline (Apple Silicon, multi-voice, narrator+question), across quality, alignment output, high-speed comprehensibility, voice control, and local-inference practicality.

---

## Bottom line
**Don't switch synthesizers on quality grounds — no candidate is *independently* shown to beat Kokoro.** The defensible upgrades are **operational, not a model swap**:
1. **Re-host Kokoro on Apple's MLX** (`mlx-audio`) for native Apple-Silicon speed — drop-in, keeps your voices.
2. **Add a forced-alignment stage** to get the word/phoneme timing map Kokoro doesn't emit — this *is* the text↔audio map you asked about, and it unlocks content-aware compression + script-highlighting.
3. **Keep eSpeak-NG "Eloquence"** for the 16× ultra track (already built); avoid DECtalk for redistribution.

## Confirmed findings

### Quality / naturalness
- **Rank naturalness by blind pairwise preference (TTS Arena Elo), not MOS/WER** — the HF blog itself calls WER "unreliable" and MOS "small-scale." `3-0`
- **No verified candidate independently beats Kokoro on naturalness.** The strongest claims (Zonos "on par with or surpassing top providers") are explicit **vendor self-description**, not independent evaluation. Switching on quality alone isn't justified by the evidence. `3-0`

### The Apple-Silicon upgrade
- **`mlx-audio` (MIT) re-hosts Kokoro on MLX** with 54 voice presets *including your existing voices* (af_heart, bm_george…), optimized for M-series. **Lowest-effort, lowest-risk upgrade** — keep voices + two-voice format, gain speed over CPU/MPS, redistribution-safe license. `3-0`

### Alignment / the text↔audio timing map
- **Kokoro (and Chatterbox) emit no word/phoneme timestamps** — a forced-alignment stage is required regardless of synthesizer. `3-0`
- **MFA is the accuracy leader:** Montreal Forced Aligner > WhisperX > MMS for English word alignment — **89.4% / 82.4% / 75.7% at 50 ms** on TIMIT (Interspeech 2024, Rousso et al.). `3-0`
- **`ctc-forced-aligner`** gives a JSON timing map (start/end/text, + SRT/WebVTT) with easy Python integration — trades a little accuracy for simplicity. `3-0`
- **On Mac, `mlx-audio` bundles alignment** via Qwen3-ForcedAligner (word/char timestamps, ~6 ms MAE) and Parakeet — an end-to-end Apple-Silicon synth+align stack, though **MFA still wins on raw accuracy.** `3-0`

### High-speed / ultra track
- **Nonuniform (Mach1) time-compression** stays comprehensible to **~2.5–4.2× real time (390–673 wpm)** and beats *linear* compression by **5–31 pts** (~17 avg), with ~15% faster response — i.e. content-aware compression (enabled by the alignment map) > naive linear speedup. `3-0` *(caveat: 1998, single n=14 study; contested for speech-in-noise.)*
- **eSpeak-NG is the safe formant choice** for the 16× ultra track (crisp at high speed, redistribution-friendly, doubles as a phonemizer). `3-0`
- **DECtalk** builds on macOS and gives the distinctive Klatt/"Hawking" formant sound, **but its proprietary FONIX license is a redistribution red flag** (owners defunct) — prefer eSpeak-NG. `3-0`

### Voice control / licensing (for A/B candidates)
- **Chatterbox (MIT)** runs on MPS, license-clean — but **no alignment** and a known **Apple-Silicon memory leak**; A/B-worthy, doesn't displace the MLX+aligner plan. `3-0`
- **Zonos-v0.1 (Apache-2.0)** — zero-shot cloning + fine prosody/emotion control (rate, pitch, emotions); **the most license-friendly higher-control candidate to A/B**, but README admits artifacts and quality is unbenchmarked. `3-0`
- **XTTS-v2** — fast 6-s voice cloning, **but CPML license terms are unstated and Coqui is defunct → licensing risk** for a redistributed pipeline. `3-0`

## Refuted (2)
- "Phone-level alignment only from MFA" `1-2`
- "XTTS-v2 supports 17 languages + multi-speaker interpolation" `0-3` (don't rely on this)

## Caveats
- **No independent head-to-head naturalness ranking of Kokoro vs candidates exists in this evidence** — "beats Kokoro" is unresolved; needs a blind A/B on your own scripts.
- Concrete **local-inference numbers** (RTF, RAM, latency) were mostly uncaptured — only directional facts (mlx-audio Apple-optimized; Chatterbox MPS leak).
- MFA's edge is scoped to English read/conversational corpora and only scores correctly-recognized words.
- Licensing is time-sensitive: **redistribution-safe = mlx-audio (MIT), Chatterbox (MIT), Zonos (Apache-2.0), eSpeak-NG**; **risky = DECtalk (FONIX), XTTS-v2 (CPML/defunct)**.

## How this plugs into the pipeline (recommended sequence)
1. **Keep Kokoro**, optionally re-hosted via `mlx-audio` for Apple-Silicon speed.
2. **Add a forced-alignment step** after synthesis → emit `<episode>.timing.json` (word/phoneme start/end). MFA for best accuracy; `ctc-forced-aligner` or `mlx-audio`'s Qwen3-ForcedAligner for easiest Mac integration. *This is the text↔audio map* — it powers content-aware speed compression in `speed-engine.js` and script-highlighting.
3. **Eloquence (eSpeak-NG)** stays as the 16× ultra track (already wired).
4. **Optional later:** blind A/B Zonos / Chatterbox vs Kokoro on your own scripts before any switch.

## Open questions → next-round candidates
1. A blind A/B / TTS-Arena test of Kokoro vs Zonos / Chatterbox / XTTS-v2 / StyleTTS2 / F5-TTS on *your* scripts (the latter three produced no surviving verified claims).
2. Concrete Apple-Silicon inference numbers (RTF, RAM, latency) per candidate vs Kokoro-on-MLX.
3. Does MFA's accuracy edge hold on *synthesized* podcast audio specifically?
4. Exact CPML terms for XTTS-v2 now that Coqui is defunct — usable in a published pipeline at all?

## Key sources
HF Arena-TTS blog · Zyphra/Zonos · Blaizzy/mlx-audio · Rousso et al. Interspeech 2024 (arxiv 2406.19363) · MahmoudAshraf97/ctc-forced-aligner · Qwen3-ForcedAligner · Covell/Withgott/Slaney Mach1 (ICASSP 1998) · espeak-ng · dectalk/dectalk · resemble-ai/chatterbox · coqui/XTTS-v2. Full list + per-claim votes in `findings.json`.
