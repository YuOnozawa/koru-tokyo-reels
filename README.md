# koru-tokyo-reels

Auto-posting for Instagram @koru.tokyo_guide (Tokyo food tips for travelers, by Yu & Koru).

- `queue.json` : reels to publish (id, file, publish_at JST, caption)
- `videos/` : finished MP4s (hosted on GitHub Pages so Instagram can fetch them)
- `state/` : what was posted + daily insights (written by the bot)
- Workflows: publish 21:03 JST daily (one reel per run), insights 09:17 JST daily, token check/refresh on the 1st & 15th.

Secret needed: `IG_TOKEN` (Instagram API with Instagram Login, long-lived user token with
instagram_business_basic, instagram_business_content_publish, instagram_business_manage_insights).
