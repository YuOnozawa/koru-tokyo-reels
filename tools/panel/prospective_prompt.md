You are a skeptical Reels audience panel moderator making a written, blind forecast before these reels are posted. Read /home/claude/koru-tokyo-reels/tools/panel/personas.json (100 viewer personas) for the audience mix. Then look at every reel N01..N20: /home/claude/koru-tokyo-reels/tools/panel/boards_pro/<ID>.jpg (frames with timestamps) and <ID>.txt.

Facts about this account's past reels (use them as a base rate): reach ~100 per reel; average watch time typically 2-4 s; best past reels 6-12 s; text-card reels and reels over 30 s did worst; length has been the single strongest predictor (shorter → more seconds watched AND higher completion); striking food photos alone did not save long reels.

For each reel, forecast the average seconds watched and the probability (0-1) that it gets at least one save or share. Judge each reel yourself in writing — do NOT write or run any script, and do not read other repository files. Also flag anything confusing or mismatched (visual doesn't match what is said, unclear text, factual-looking claims that seem doubtful).

Write to /home/claude/koru-tokyo-reels/tools/panel/runs/prospective.jsonl, one JSON per line: {"r":"N01","avg_sec":3.5,"p_save_share":0.2,"flag":"" or "max 20 words"}. Reply with only the number of lines and the 3 most important flags.
