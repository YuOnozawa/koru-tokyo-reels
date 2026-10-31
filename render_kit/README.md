# Render kit (reel production)

Snapshot of the scripts that produce the @koru.tokyo_guide reels (1080x1920, 30fps). Copied from the working sandbox on 2026-10-31.

- `scripts.py`: all reel scripts (SCRIPTS dict). Each scene: `say` (narration; `{display|IPA}` spans set pronunciation), `bg` (photo name, focus x, focus y), `tag` (photo label such as "Photo: similar dish, not this shop"), `card` (kicker / big / jp / roman / sub), `hook`, `end`. `style: 'wa'` = washi/noren template.
- `tts.py`: narration with Kokoro-82M (`kokoro_onnx`, voice `am_michael`, speed 1.05). Writes `audio/<id>.mp3` and `audio/<id>_timing.json`. Run `python3 tts.py <id> ...`.
- `render.py`: PIL + FFmpeg renderer. Run `python3 render.py <id> ...` after tts.py. Output: `out/<id>.mp4`; copy to `../videos/` and add an entry to `../queue.json` to schedule.

Requirements: Python 3, Pillow, numpy, ffmpeg, kokoro_onnx + espeak-ng phonemizer, model files `kokoro-v1.0.onnx` and `voices-v1.0.bin` (github.com/thewh1teagle/kokoro-onnx releases), fonts Poppins (Google Fonts) and Noto Sans/Serif CJK.
Paths are hard-coded for the original sandbox (`/home/claude/...`); edit the constants at the top of render.py and tts.py.

Photos: stock photos are in `../stock/` (CC0/PDM, credits in stock/credits.json). Koru photos (`koru_*.jpg`) and AI images (`ai_*.jpg`) are NOT in this public repo; originals are in Yu's Google Drive (TokyoGuide_動画プロジェクト/02_素材 and 03_AI画像).
