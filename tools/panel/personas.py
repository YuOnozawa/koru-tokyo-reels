"""100 synthetic viewer personas for pre-testing reels. Weights are ASSUMPTIONS (English-language IG viewers who see
Tokyo food reels), loosely shaped by JNTO arrivals (US, AU, SG/MY/PH, UK, CA, Europe strong in 2025-26). Not data."""
import json, random
R = random.Random(20261106)
ORIGIN = [('USA', 20), ('Australia', 9), ('UK', 7), ('Canada', 5), ('Singapore', 6), ('Philippines', 5), ('Malaysia', 4),
          ('India', 5), ('Germany', 4), ('France', 3), ('Netherlands', 2), ('Nordics', 2), ('Italy/Spain', 3),
          ('Mexico/Brazil', 4), ('Indonesia/Thailand', 5), ('Hong Kong/Taiwan', 4), ('New Zealand', 2), ('Other', 10)]
STAGE = [('dreaming, no dates', 25), ('trip booked 1-6 months out', 30), ('trip in the next 4 weeks', 15),
         ('in Tokyo right now', 7), ('been before, nostalgic', 15), ('lives in Japan (expat)', 8)]
AGE = [('18-24', 22), ('25-34', 38), ('35-44', 22), ('45-59', 14), ('60+', 4)]
PARTY = [('solo', 30), ('couple', 35), ('friends', 20), ('family with kids', 15)]
BUDGET = [('tight backpacker', 25), ('mid-range', 55), ('splurge-happy', 20)]
DIET = [('eats anything', 70), ('vegetarian', 8), ('halal', 5), ('no raw fish', 7), ('allergy (shellfish/peanut)', 5), ('picky eater', 5)]
HABIT = [('fast scroller, skips anything slow', 35), ('watches food content to the end if it looks tasty', 25),
         ('saves practical tips into a Japan folder', 20), ('sends reels to partner/friends planning the trip', 15), ('comments and asks questions', 5)]
INTEREST = ['ramen & cheap eats', 'anime/Akihabara', 'temples & history', 'cafes & sweets', 'nightlife & izakaya', 'shopping', 'onsen/sauna & wellness', 'photography']
def pick(opts): return R.choices([o for o, _ in opts], [w for _, w in opts])[0]
P = []
for i in range(100):
    P.append({'id': 'P%03d' % (i + 1), 'from': pick(ORIGIN), 'age': pick(AGE), 'stage': pick(STAGE), 'party': pick(PARTY),
              'budget': pick(BUDGET), 'diet': pick(DIET), 'habit': pick(HABIT), 'interests': R.sample(INTEREST, 2),
              'japan_familiarity': R.choice(['first-timer', 'first-timer', 'been once', 'been 3+ times'])})
json.dump(P, open('personas.json', 'w'), indent=0)
print(len(P), sum(p['stage'].startswith('trip in') or p['stage'].startswith('in Tokyo') for p in P), 'near-term travelers')
