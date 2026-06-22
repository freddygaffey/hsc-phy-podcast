# Research Archive

Durable archive of `deep-research` workflow runs. Each round is its own dated, self-contained folder so **existing research is never overwritten** — new research = a new folder.

## Why this exists
Deep-research output otherwise lives only in ephemeral (`/private/tmp`) and internal-harness (`~/.claude/...`) locations that get cleared over time. These folders are the permanent copy.

## Layout per round
```
YYYY-MM-DD_<topic-slug>/
  report.md          # human-readable synthesized report (start here)
  findings.json      # full structured result: claims, evidence, votes, sources, refuted, open questions
  workflow-script.js # the exact deep-research harness script used (for reproducibility / resume)
  raw-transcripts/   # every subagent transcript (.jsonl): raw web searches, fetched sources, verification votes
```

## Rounds
| Date | Topic | Folder |
|---|---|---|
| 2026-06-21 | Audio comprehensibility algorithms (WSOLA/PSOLA/TSM) & speed-listening perceptual limits | `2026-06-21_audio-comprehensibility-and-speed-listening/` |
| 2026-06-21 | Speed-listening improvement: training protocols, the realistic sighted ceiling, throughput tricks (7×/10× reality check) | `2026-06-21_speed-listening-improvement-and-sighted-ceiling/` |
| 2026-06-21 | How age affects accelerated-speech comprehension — lifespan curve, mechanisms (hearing vs cognition), peak age, trainability | `2026-06-21_how-age-affects-speed-listening/` |
| 2026-06-21 | Designing/training a voice/TTS model for high-speed comprehensibility — time-compress > native-fast; two-track design; formant synth for extreme track (22/3 verified after a rate-limit-recovery resume) | `2026-06-21_designing-voices-for-high-speed-listening/` |
| 2026-06-21 | Better local/open TTS models vs Kokoro — no candidate independently beats Kokoro; upgrade operationally (mlx-audio re-host + forced-alignment timing map); eSpeak-NG for ultra track | `2026-06-21_better-tts-models-vs-kokoro/` |

## Adding a new round
1. Run a new `deep-research` workflow.
2. After it completes, copy its `findings.json` (task output), `workflow-script.js`, and `raw-transcripts/` into a new `YYYY-MM-DD_<slug>/` folder here.
3. Write a `report.md` and add a row to the table above.

To **extend** the existing round instead of starting fresh, resume its workflow from the saved `workflow-script.js` (edit it, then re-run with `resumeFromRunId` — cached agents return instantly, only new/edited steps re-run).
