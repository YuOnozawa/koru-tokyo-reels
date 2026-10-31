"""Shared site navigation + "phrase you'll need here" helper, used by the page builders and patch scripts.
Keep in sync with the copies inside site/planner/planner.js (phraseFor) if you change PHRASE_RULES."""

NAV_CSS = (
    '.kn{max-width:640px;margin:0 auto 14px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px;'
    'background:#17110c;border-radius:12px;padding:6px;box-shadow:inset 0 0 0 3px #000}'
    '.kn a{display:grid;place-items:center;padding:8px 4px;border-radius:8px;text-decoration:none;color:#ffa22b;'
    'font:16px/1.15 "DotGothic16",ui-monospace,monospace;text-shadow:0 0 6px rgba(255,150,40,.6)}'
    '.kn a span{font:12px/1.3 "DotGothic16",ui-monospace,monospace;opacity:.85}'
    '.kn a[aria-current]{background:#ffa22b;color:#17110c;text-shadow:none}'
    '.kn a:focus-visible{outline:3px solid #ffd84a;outline-offset:2px}'
)
ITEMS = [('planner', '券売機', 'Plan meals'), ('phrases', '日本語', 'Phrases'), ('shops', 'お店', 'All shops')]


def nav(prefix, current):
    """prefix = path back to the site root ('../', '../../', or '')."""
    return '<nav class="kn" aria-label="Site">%s</nav>' % ''.join(
        '<a href="%s%s/"%s>%s<span>%s</span></a>' % (prefix, k, ' aria-current="page"' if k == current else '', ja, en)
        for k, ja, en in ITEMS)


# (match words in genre / what_to_order / tip, phrase ja, romaji, english, phrases-page anchor)
PHRASE_RULES = [
    (['ticket machine', 'meal ticket'], '食券', 'shokken', 'meal ticket: buy it at the machine first', 'ramen'),
    (['tsukemen', 'ramen', 'dandan', 'chuka soba'], '麺かためで', 'men katame de', 'firm noodles, please', 'ramen'),
    (['izakaya', 'bar', 'beer', 'senbero', 'yakitori', 'hoppy'], '生ビールください', 'nama bīru kudasai', 'a draft beer, please', 'table'),
    (['takeout', 'dorayaki', 'wagashi', 'taiyaki', 'senbei', 'melon pan'], '持ち帰りで', 'mochikaeri de', 'to go, please', 'pay'),
    (['sushi', 'kaisen', 'sashimi'], 'おすすめは何ですか？', 'osusume wa nan desu ka?', 'what do you recommend?', 'order'),
    (['curry', 'tonkatsu', 'katsu', 'gyudon'], '大盛りで', 'ōmori de', 'large portion, please', 'order'),
]


def phrase_for(s):
    hay = ' '.join(str(s.get(k, '')) for k in ('genre', 'what_to_order', 'tourist_tip')).lower()
    for words, ja, ro, en, anchor in PHRASE_RULES:
        if any(w in hay for w in words):
            return ja, ro, en, anchor
    return 'ごちそうさまでした', 'gochisōsama deshita', 'thank you for the meal (when leaving)', 'pay'
