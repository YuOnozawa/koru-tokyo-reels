# Who is the buyer? (first pass 2026-11-29; no personal names here)

## Market facts
Source: Japan Tourism Agency, Inbound Consumption Trend Survey, 2025 annual report (all purposes; food = general visitors, per person per trip).
https://www.mlit.go.jp/kankocho/content/002003329.pdf

| Market | Solo | Couple | Family | Friends | Under 40 | First visit | Nights | Food spend / trip | / night | Self-arranged |
|---|---|---|---|---|---|---|---|---|---|---|
| USA | 33.7% | 24.4% | 20.8% | 18.1% | 71.4% | 63.2% | 12.0 | ¥69,616 | ¥5,800 | 94.4% |
| Australia | 18.8% | 31.4% | 32.7% | 15.3% | 57.6% | 54.2% | 13.5 | ¥84,325 | ¥6,250 | 88.4% |
| UK | 38.6% | 29.7% | 21.0% | 7.4% | 62.6% | 62.1% | 14.4 | ¥82,108 | ¥5,700 | 91.9% |
| Canada | 25.2% | 32.2% | 24.8% | 15.7% | 68.4% | 62.2% | 14.6 | ¥71,924 | ¥4,930 | 95.5% |
| Singapore | 23.5% | 22.7% | 37.6% | 13.4% | 55.9% | 24.7% | 9.1 | ¥64,899 | ¥7,130 | 95.2% |
| Korea (ref.) | 18.0% | 18.8% | 29.9% | 26.7% | 70.1% | 16.3% | 4.0 | ¥28,660 | ¥7,165 | 90.9% |
| Taiwan (ref.) | 16.1% | 15.5% | 44.7% | 18.7% | 57.5% | 12.1% | 6.5 | ¥40,169 | ¥6,180 | 77.5% |

Volume: Oct 2026 arrivals 3.91M total; USA 351,500 (+4.7%), 4th largest (JNTO via Travel Voice, 2026-11-18).
Jul–Sep 2026: food = 22.9% of visitor spending (¥505.8B); average spend per person ¥233,677 (JTA via Travel Voice, 2026-10-21).
Not yet checked: 2025/2026 arrivals for Australia, UK, Canada, Singapore; nights spent in Tokyo by market; income.

## Our own data
- Instagram audience demographics: not available (24 followers).
- Planner app (Koru planner DB): a handful of opens from Instagram in November, no real trips saved. No country data.
- Profiles of 12 people on the warm list, checked 11/29 (bio + recent posts only): 6 are overseas travelers on a Japan trip (1 family, 1 mother–daughter pair on the Tokyo–Fuji–Kyoto route, 1 couple travel account, 1 solo, 2 unclear party); 6 are not buyers (a Tokyo-based photographer, a long-stay resident, an AI-generated artist profile, an events account, 1 unclear, 1 deleted). None state country or age in the bio.
- So: profile reading tells us party and route, not country or age. Country, age band, month and first-time/repeat have to be asked.

## Working target (to test, not proven)
Primary: first-time visitors from the USA, 25–39, couple or solo, ~12 nights in Japan, booking everything themselves, about ¥5,000–6,000 a day per person on food. Largest English-speaking market, mostly first-timers (63%), almost all self-arranged (94%).
Secondary: Australians 35–55 travelling as a couple or family, 13–14 nights, highest food spend per trip, 46% repeat visitors.
Tension with Yu's 11/12 direction ("adults, fairly well-off, want good food over cheap"): US visitors are 71% under 40. Australia fits "older, spends on food" better. Decide by who actually answers and pays.

## How we raise the resolution
1. Self-identify reel: "Going to Tokyo? Comment: month + who with + first time?" (answers go to the Drive list).
2. Ask the warm travelers one question (draft in chat; Yu approves before sending).
3. Order form of the product asks country, month, party, first time.
4. Re-weight the 100 synthetic personas in tools/panel/personas.json to the survey shares above.
5. Follow runs: only log people as prospects when their posts show a trip (day counts, route), not residents.
