# Week 2 (Oct 13-17, 2026) scripts for @koru.tokyo_guide
# bg: (photo_name, focus_x, focus_y)  or  None -> solid brand colour
# card keys: kicker, big, jp, roman, sub   (all optional)

SCRIPTS = {
 'w2_01_taxfree': {
  'title': 'Tax-free changed Nov 1',
  'scenes': [
   {'say': "Shopping in Japan after November first? Tax-free just changed.",
    'bg': ('ai_street1', .5, .5), 'ai': True, 'hook': True,
    'card': {'kicker': 'FROM NOV 1, 2026', 'big': 'Tax-free\nchanged.'}},
   {'say': "Now you pay the full price, tax included, at the store.",
    'bg': ('ai_street2', .45, .5), 'ai': True,
    'card': {'kicker': 'STEP 1', 'big': 'Pay full price', 'sub': 'tax included, at the register'}},
   {'say': "You get the tax back after you leave, once customs checks your items at the airport.",
    'bg': ('ai_airport_exit', .5, .45), 'ai': True,
    'card': {'kicker': 'STEP 2', 'big': 'Refund after customs', 'sub': 'at departure, before check-in'}},
   {'say': "So don't put them in your checked bag before that check.",
    'bg': ('ai_airport1', .5, .5), 'ai': True,
    'card': {'kicker': 'STEP 3', 'big': 'Keep items with you', 'sub': 'customs may want to see them'}},
   {'say': "Minimum: five thousand yen before tax, per store, per day.",
    'bg': None,
    'card': {'kicker': 'MINIMUM', 'big': '¥5,000+', 'sub': 'per store · per day · before tax'}},
   {'say': "And don't open the snacks. Anything used in Japan, no refund.",
    'bg': ('koru_nose', .5, .45),
    'card': {'kicker': 'WARNING', 'big': "Don't open\nthe snacks"}},
   {'say': "Save this for your trip. Follow for real Tokyo food tips.",
    'bg': ('koru_blep', .45, .5), 'end': True,
    'card': {'big': 'Save for your trip', 'sub': 'Follow @koru.tokyo_guide'}},
  ]},

 'w2_02_iekei': {
  'title': 'Iekei ramen: what to say',
  'scenes': [
   {'say': "At this kind of ramen shop, they'll ask you three questions. Here's what to say.",
    'bg': ('ai_street3', .5, .5), 'ai': True, 'hook': True,
    'card': {'kicker': 'IEKEI RAMEN', 'big': "They'll ask you\n3 questions."}},
   {'say': "First, the noodles. {Katame|kɑtˈɑmɛ} means firm.",
    'bg': None,
    'card': {'kicker': '1 · NOODLES', 'jp': '硬め', 'roman': 'KATAME', 'sub': '= firm noodles'}},
   {'say': "Then the flavor. {Koime|koʊˈimɛ} is strong, {usume|uːsˈuːmɛ} is light.",
    'bg': None,
    'card': {'kicker': '2 · FLAVOR', 'jp': '濃いめ / 薄め', 'roman': 'KOIME / USUME', 'sub': '= strong / light'}},
   {'say': "Then the oil. {Ōme|ˈoːmɛ} for more, {sukuname|skˌuːnˈɑːmɛ} for less.",
    'bg': None,
    'card': {'kicker': '3 · OIL', 'jp': '多め / 少なめ', 'roman': 'ŌME / SUKUNAME', 'sub': '= more / less'}},
   {'say': "First time? Just say: {futsū de|fuːtsˈuː dɛ}. Everything normal.",
    'bg': None,
    'card': {'kicker': 'FIRST TIME?', 'jp': '普通で', 'roman': 'FUTSŪ DE', 'sub': '= everything normal'}},
   {'say': "Save this before your first bowl. Follow for a real Tokyo lunch every week.",
    'bg': ('koru_smile', .5, .45), 'end': True,
    'card': {'big': 'Save before your\nfirst bowl', 'sub': 'Follow @koru.tokyo_guide'}},
  ]},

 'w2_03_otoshi': {
  'title': "The charge you didn't order",
  'scenes': [
   {'say': "Got a charge on your izakaya bill for food you never ordered? It's not a scam.",
    'bg': ('ai_street4', .5, .55), 'ai': True, 'hook': True,
    'card': {'kicker': 'IZAKAYA BILL', 'big': "It's not\na scam."}},
   {'say': "It's called {otōshi|oʊtˈoʊʃi}. A small starter they bring when you sit down.",
    'bg': None,
    'card': {'kicker': 'WHAT IS IT', 'jp': 'お通し', 'roman': 'OTŌSHI', 'sub': 'small starter, served automatically'}},
   {'say': "Think of it as a seat charge. Usually a few hundred yen per person.",
    'bg': None,
    'card': {'kicker': 'HOW MUCH', 'big': '~¥300–500', 'sub': 'per person · a seat charge'}},
   {'say': "You can't really send it back. And there's no tipping on top.",
    'bg': None,
    'card': {'kicker': 'GOOD TO KNOW', 'big': 'No tipping\nin Japan'}},
   {'say': "Want to check first? Ask: {otōshi-dai, arimasu ka?|oʊtˈoʊʃi dˈaɪ, ɑɾimˈɑs kɑ?}",
    'bg': None,
    'card': {'kicker': 'ASK BEFORE YOU SIT', 'jp': 'お通し代\nありますか？', 'roman': 'OTŌSHI-DAI, ARIMASU KA?', 'sub': '= is there a seat charge?'}},
   {'say': "Then just enjoy it. Follow for more real Tokyo food tips.",
    'bg': ('koru_autumn', .5, .5), 'end': True,
    'card': {'big': 'Then enjoy it', 'sub': 'Follow @koru.tokyo_guide'}},
  ]},

 'w2_04_lunchrules': {
  'title': 'Lunch like a Tokyo office worker',
  'scenes': [
   {'say': "I'm a Japanese office worker in {Akihabara|ɑkihɑbˈɑɾɑ}. These are my three lunch rules.",
    'bg': ('ai_street1', .55, .5), 'ai': True, 'hook': True,
    'card': {'kicker': 'TOKYO OFFICE WORKER', 'big': 'My 3 lunch\nrules.'}},
   {'say': "One. Skip noon. All of Tokyo eats at twelve. Go at eleven thirty, or after one.",
    'bg': None,
    'card': {'kicker': 'RULE 1', 'big': 'Skip 12:00', 'sub': 'go at 11:30 or after 13:00'}},
   {'say': "Two. A ticket machine at the door means fast, cheap, and no Japanese needed.",
    'bg': None,
    'card': {'kicker': 'RULE 2', 'jp': '券売機', 'roman': 'TICKET MACHINE', 'sub': '= fast, cheap, no Japanese needed'}},
   {'say': "Three. Order the {teishoku|tˈeɪʃoʊku}. Rice, miso soup and pickles come with it.",
    'bg': None,
    'card': {'kicker': 'RULE 3', 'jp': '定食', 'roman': 'TEISHOKU', 'sub': '= set meal: rice + miso + pickles'}},
   {'say': "On the way out, say: {gochisōsama deshita|ɡoʊtʃisˈoʊsɑmɑ dˈɛʃtɑ}. Thanks for the meal.",
    'bg': None,
    'card': {'kicker': 'ON THE WAY OUT', 'jp': 'ごちそうさま\nでした', 'roman': 'GOCHISŌSAMA DESHITA', 'sub': '= thanks for the meal'}},
   {'say': "Follow for a real Tokyo lunch every week.",
    'bg': ('koru_autumn2', .45, .5), 'end': True,
    'card': {'big': 'Real Tokyo lunch,\nevery week', 'sub': 'Follow @koru.tokyo_guide'}},
  ]},

 'w2_05_sendlist': {
  'title': 'Send me your Tokyo food list',
  'scenes': [
   {'say': "Going to Tokyo? Send me your restaurant list, and I'll tell you what to skip.",
    'bg': ('ai_street2', .5, .5), 'ai': True, 'hook': True,
    'card': {'kicker': 'GOING TO TOKYO?', 'big': 'Send me your\nfood list.'}},
   {'say': "I'm a Japanese office worker in {Akihabara|ɑkihɑbˈɑɾɑ}, and I eat out almost every day.",
    'bg': ('ai_street3', .5, .5), 'ai': True,
    'card': {'kicker': 'WHO AM I', 'big': 'A local who\neats out daily'}},
   {'say': "I'll tell you which places are worth the line, which ones are tourist traps, and what to order.",
    'bg': None,
    'card': {'kicker': "WHAT YOU GET", 'big': 'Worth the line?\nTourist trap?\nWhat to order?'}},
   {'say': "The first three lists this month are free.",
    'bg': None,
    'card': {'kicker': 'THIS MONTH', 'big': 'First 3 lists:\nFREE'}},
   {'say': "Just send me a message with the word: list.",
    'bg': ('koru_flowers', .5, .45), 'end': True,
    'card': {'big': 'DM me: LIST', 'sub': '@koru.tokyo_guide'}},
  ]},
}

# ---------------- Week 3 (Oct 20-24, 2026) ----------------
SCRIPTS.update({
 'w3_01_kaitenzushi': {
  'title': 'Conveyor sushi like a local',
  'scenes': [
   {'say': "Most tourists miss these three things at conveyor sushi.",
    'bg': ('ai_street3', .5, .5), 'ai': True, 'hook': True,
    'card': {'kicker': 'KAITEN-ZUSHI', 'big': 'You missed\nthese 3.'}},
   {'say': "One. The green powder by your seat is tea. Add hot water from the tap at the counter.",
    'bg': None,
    'card': {'kicker': '1 · FREE TEA', 'jp': 'お茶', 'roman': 'GREEN POWDER = TEA', 'sub': '+ hot water tap at your seat'}},
   {'say': "Two. The pink ginger is free. Eat it between pieces, not on top of the sushi.",
    'bg': None,
    'card': {'kicker': '2 · GINGER', 'jp': 'ガリ', 'roman': 'GARI', 'sub': '= free, eat between pieces'}},
   {'say': "Three. Don't wait for the belt. Order fresh from the touch screen. Most have English.",
    'bg': None,
    'card': {'kicker': '3 · ORDER FRESH', 'big': 'Use the\ntouch screen', 'sub': 'most have an English option'}},
   {'say': "Save this for your first sushi night.",
    'bg': ('koru_sofa', .55, .5), 'end': True,
    'card': {'big': 'Save for sushi night', 'sub': 'Follow @koru.tokyo_guide'}},
  ]},

 'w3_02_tachigui': {
  'title': 'Standing soba in 5 minutes',
  'scenes': [
   {'say': "Tokyo's real fast food is not a burger. It's standing soba.",
    'bg': ('ai_street4', .5, .5), 'ai': True, 'hook': True,
    'card': {'kicker': 'TACHIGUI SOBA', 'big': 'Tokyo fast food\nisn’t a burger.'}},
   {'say': "Buy a ticket at the machine by the door.",
    'bg': None,
    'card': {'kicker': 'STEP 1', 'jp': '食券', 'roman': 'SHOKKEN', 'sub': '= meal ticket from the machine'}},
   {'say': "Hand it over. If they ask, just say {soba|sˈoʊbɑ} or {udon|ˈuːdɔn}.",
    'bg': None,
    'card': {'kicker': 'STEP 2', 'jp': 'そば / うどん', 'roman': 'SOBA / UDON', 'sub': 'buckwheat / thick wheat noodles'}},
   {'say': "Eat standing up. It takes about five minutes.",
    'bg': None,
    'card': {'kicker': 'STEP 3', 'big': 'Eat standing.\n~5 minutes.'}},
   {'say': "Then put your bowl back on the counter. That's it.",
    'bg': None,
    'card': {'kicker': 'STEP 4', 'big': 'Bowl back\non the counter'}},
   {'say': "Follow for a real Tokyo lunch every week.",
    'bg': ('koru_chair', .5, .5), 'end': True,
    'card': {'big': 'Real Tokyo lunch,\nevery week', 'sub': 'Follow @koru.tokyo_guide'}},
  ]},

 'w3_03_izakaya_words': {
  'title': 'Izakaya: 3 words you need',
  'scenes': [
   {'say': "Walking into an izakaya? You only need three phrases.",
    'bg': ('ai_street1', .5, .5), 'ai': True, 'hook': True,
    'card': {'kicker': 'IZAKAYA', 'big': 'Only 3 phrases.'}},
   {'say': "First drink? Say {toriaezu nama|toʊɾiˈɑɛzu nˈɑmɑ}. Draft beer for now.",
    'bg': None,
    'card': {'kicker': '1 · FIRST DRINK', 'jp': 'とりあえず生', 'roman': 'TORIAEZU NAMA', 'sub': '= a draft beer for now'}},
   {'say': "To call staff, raise your hand and say {sumimasen|sumimɑsˈɛn}.",
    'bg': None,
    'card': {'kicker': '2 · CALL STAFF', 'jp': 'すみません', 'roman': 'SUMIMASEN', 'sub': '= excuse me! (hand up)'}},
   {'say': "When you're done, say {okaikei onegaishimasu|oʊkˈaɪkeɪ oʊnɛɡˈaɪʃimɑs}. Check, please.",
    'bg': None,
    'card': {'kicker': '3 · THE BILL', 'jp': 'お会計\nお願いします', 'roman': 'OKAIKEI ONEGAISHIMASU', 'sub': '= check, please'}},
   {'say': "Save this. You'll need it on your first night.",
    'bg': ('koru_autumn2', .45, .5), 'end': True,
    'card': {'big': 'Save for night one', 'sub': 'Follow @koru.tokyo_guide'}},
  ]},

 'w3_04_sake': {
  'title': 'How to order sake',
  'scenes': [
   {'say': "I love sake. Here's how to order it without the menu panic.",
    'bg': ('ai_street2', .5, .5), 'ai': True, 'hook': True,
    'card': {'kicker': 'SAKE', 'big': 'Order sake\nwithout panic.'}},
   {'say': "Sake comes in {ichigō|itʃiɡˈoʊ}. That's one hundred eighty milliliters. Enough for one or two people.",
    'bg': None,
    'card': {'kicker': 'SIZE', 'jp': '一合', 'roman': 'ICHIGŌ = 180 ml', 'sub': 'good for 1–2 people'}},
   {'say': "Pick a temperature. {Reishu|ɾˈeɪʃu} is chilled. {Atsukan|ɑtsˈukɑn} is hot.",
    'bg': None,
    'card': {'kicker': 'TEMPERATURE', 'jp': '冷酒 / 熱燗', 'roman': 'REISHU / ATSUKAN', 'sub': '= chilled / hot'}},
   {'say': "Pick a taste. {Karakuchi|kɑɾɑkˈutʃi} is dry. {Amakuchi|ɑmɑkˈutʃi} is sweet.",
    'bg': None,
    'card': {'kicker': 'TASTE', 'jp': '辛口 / 甘口', 'roman': 'KARAKUCHI / AMAKUCHI', 'sub': '= dry / sweet'}},
   {'say': "Still lost? Ask: {osusume wa?|oʊsusˈumɛ wɑ} What do you recommend?",
    'bg': None,
    'card': {'kicker': 'STILL LOST?', 'jp': 'おすすめは？', 'roman': 'OSUSUME WA?', 'sub': '= what do you recommend?'}},
   {'say': "Kanpai. Follow for more real Tokyo food tips.",
    'bg': ('koru_blep', .45, .5), 'end': True,
    'card': {'big': 'Kanpai!', 'sub': 'Follow @koru.tokyo_guide'}},
  ]},

 'w3_05_closed_sunday': {
  'title': 'Why that restaurant was closed',
  'scenes': [
   {'say': "Planning lunch in Akihabara on a Sunday? Check this first.",
    'bg': ('ai_street3', .45, .5), 'ai': True, 'hook': True,
    'card': {'kicker': 'BEFORE YOU GO', 'big': 'Sunday lunch?\nCheck this.'}},
   {'say': "Many small lunch spots in office areas close on Sundays and holidays. Their customers are office workers.",
    'bg': None,
    'card': {'kicker': 'WHY', 'big': 'Office areas\nclose on Sundays', 'sub': 'no office workers, no lunch rush'}},
   {'say': "Look for this word on the door or the website: {teikyūbi|tˈeɪkjuːbi}. Regular day off.",
    'bg': None,
    'card': {'kicker': 'LOOK FOR', 'jp': '定休日', 'roman': 'TEIKYŪBI', 'sub': '= regular day off'}},
   {'say': "And check Google Maps hours the same morning. Small places change them often.",
    'bg': None,
    'card': {'kicker': 'TIP', 'big': 'Check hours\nthat morning'}},
   {'say': "Want me to check your list? Send me a message with the word: list.",
    'bg': ('koru_flowers', .5, .45), 'end': True,
    'card': {'big': 'DM me: LIST', 'sub': 'free list check · @koru.tokyo_guide'}},
  ]},
})

# ---------------- Batch 4 ----------------
SCRIPTS.update({
 'w4_01_onigiri': {
  'title': 'Open an onigiri right',
  'scenes': [
   {'say': "Everyone rips the seaweed on their first onigiri. Here's the trick.",
    'bg': ('ai_street2', .5, .5), 'ai': True, 'hook': True,
    'card': {'kicker': 'KONBINI ONIGIRI', 'big': 'Stop ripping\nthe seaweed.'}},
   {'say': "Pull tab number one, straight down the middle.",
    'bg': None, 'card': {'kicker': 'STEP 1', 'big': 'Tab 1:\ndown the middle'}},
   {'say': "Then pull corner two, and corner three, out to the sides.",
    'bg': None, 'card': {'kicker': 'STEP 2', 'big': 'Corners 2 and 3:\nout to the sides'}},
   {'say': "The seaweed stays crispy and wraps itself around the rice.",
    'bg': None, 'card': {'kicker': 'RESULT', 'big': 'Crispy seaweed.\nNo mess.'}},
   {'say': "Save this for your first convenience store run.",
    'bg': ('koru_smile', .5, .45), 'end': True,
    'card': {'big': 'Save for konbini day', 'sub': 'Follow @koru.tokyo_guide'}},
  ]},
 'w4_02_ticketmachine': {
  'title': 'Ramen ticket machine hack',
  'scenes': [
   {'say': "Can't read the ramen ticket machine? Look at the top left.",
    'bg': ('ai_street4', .5, .5), 'ai': True, 'hook': True,
    'card': {'kicker': 'RAMEN SHOPS', 'big': 'Look top left.'}},
   {'say': "The top left button is usually the shop's signature bowl.",
    'bg': None, 'card': {'kicker': 'THE HACK', 'big': 'Top left =\nhouse special', 'sub': '(usually)'}},
   {'say': "Put your money in first. Then press the button. Your change comes out below.",
    'bg': None, 'card': {'kicker': 'HOW', 'big': 'Money first,\nthen the button'}},
   {'say': "Many machines also have an English button. Look for E N.",
    'bg': None, 'card': {'kicker': 'TIP', 'big': 'Look for "EN"'}},
   {'say': "Then hand the ticket to the staff and sit down. Follow for a real Tokyo lunch every week.",
    'bg': ('koru_autumn', .5, .5), 'end': True,
    'card': {'big': 'Ticket to staff,\nthen sit', 'sub': 'Follow @koru.tokyo_guide'}},
  ]},
 'w4_03_konbini_hotsnack': {
  'title': 'Konbini hot snacks',
  'scenes': [
   {'say': "The best fried chicken in Japan might be next to the register at the convenience store.",
    'bg': ('ai_street1', .5, .5), 'ai': True, 'hook': True,
    'card': {'kicker': 'KONBINI', 'big': 'Look next to\nthe register.'}},
   {'say': "That warm glass case has fried chicken, croquettes and more. Made to eat right away.",
    'bg': None, 'card': {'kicker': 'HOT SNACKS', 'big': 'Warm case\nby the register'}},
   {'say': "You can't grab it yourself. Just point and say {kore kudasai|kˈoʊɾɛ kudˈɑsaɪ}.",
    'bg': None, 'card': {'kicker': 'HOW TO ORDER', 'jp': 'これください', 'roman': 'KORE KUDASAI', 'sub': '= this one, please (and point)'}},
   {'say': "In winter, look for the pot of {oden|oʊdˈɛn} too.",
    'bg': None, 'card': {'kicker': 'WINTER', 'jp': 'おでん', 'roman': 'ODEN', 'sub': '= simmered winter comfort food'}},
   {'say': "Save this for a late night snack.",
    'bg': ('koru_nose', .5, .45), 'end': True,
    'card': {'big': 'Save for a late snack', 'sub': 'Follow @koru.tokyo_guide'}},
  ]},
 'w4_04_depachika': {
  'title': 'Depachika before closing',
  'scenes': [
   {'say': "Want great Japanese food for less? Go to a department store basement before closing.",
    'bg': ('ai_street3', .5, .5), 'ai': True, 'hook': True,
    'card': {'kicker': 'DEPACHIKA', 'big': 'Go before\nclosing time.'}},
   {'say': "The basement food hall is called {depachika|dɛpɑtʃˈikɑ}. Bento, sushi, sweets, all made fresh.",
    'bg': None, 'card': {'kicker': 'WHAT', 'jp': 'デパ地下', 'roman': 'DEPACHIKA', 'sub': '= department store food hall'}},
   {'say': "In the last hour or so, many counters put discount stickers on what's left.",
    'bg': None, 'card': {'kicker': 'WHEN', 'big': 'Last hour\nbefore closing'}},
   {'say': "Look for these characters: {waribiki|wɑɾibˈiki}. Discount.",
    'bg': None, 'card': {'kicker': 'LOOK FOR', 'jp': '割引', 'roman': 'WARIBIKI', 'sub': '= discount'}},
   {'say': "Take it back to your hotel. Best cheap dinner in Tokyo.",
    'bg': ('koru_sofa', .55, .5), 'end': True,
    'card': {'big': 'Hotel dinner, sorted', 'sub': 'Follow @koru.tokyo_guide'}},
  ]},
 'w4_05_cash': {
  'title': 'Card or cash?',
  'scenes': [
   {'say': "Some small restaurants in Tokyo still don't take cards. Ask before you order.",
    'bg': ('ai_street4', .45, .5), 'ai': True, 'hook': True,
    'card': {'kicker': 'BEFORE YOU ORDER', 'big': 'Card or cash?'}},
   {'say': "Just ask: {kādo tsukaemasu ka?|kˈɑːdo tsukɑɛmˈɑs kɑ} Can I use a card?",
    'bg': None, 'card': {'kicker': 'ASK', 'jp': 'カード\n使えますか？', 'roman': 'KĀDO TSUKAEMASU KA?', 'sub': '= can I use a card?'}},
   {'say': "If you hear {genkin dake|ɡɛnkˈin dˈɑkɛ}, it means cash only.",
    'bg': None, 'card': {'kicker': 'IF THEY SAY', 'jp': '現金だけ', 'roman': 'GENKIN DAKE', 'sub': '= cash only'}},
   {'say': "Keep a few thousand yen on you. Convenience store ATMs work with most foreign cards.",
    'bg': None, 'card': {'kicker': 'TIP', 'big': 'Carry some yen', 'sub': 'konbini ATMs take most foreign cards'}},
   {'say': "Follow for more real Tokyo food tips.",
    'bg': ('koru_autumn2', .45, .5), 'end': True,
    'card': {'big': 'Real Tokyo tips', 'sub': 'Follow @koru.tokyo_guide'}},
  ]},
 'w4_06_gyudon_breakfast': {
  'title': 'Cheap early breakfast',
  'scenes': [
   {'say': "Jet lag woke you up at five? Here's where Tokyo office workers eat breakfast.",
    'bg': ('ai_street1', .45, .5), 'ai': True, 'hook': True,
    'card': {'kicker': 'JET LAG?', 'big': 'Breakfast\nat 5 a.m.'}},
   {'say': "Beef bowl chains. Many are open early or all night.",
    'bg': None, 'card': {'kicker': 'WHERE', 'jp': '牛丼チェーン', 'roman': 'GYŪDON CHAINS', 'sub': 'many open early or 24 hours'}},
   {'say': "In the morning they serve breakfast sets. Rice, miso soup, grilled fish or egg.",
    'bg': None, 'card': {'kicker': 'WHAT', 'jp': '朝定食', 'roman': 'ASA-TEISHOKU', 'sub': '= breakfast set meal'}},
   {'say': "Order on a touch screen or ticket machine. Most have English.",
    'bg': None, 'card': {'kicker': 'HOW', 'big': 'Touch screen\nor ticket machine'}},
   {'say': "Cheap, fast, and very Japanese. Follow for a real Tokyo lunch every week.",
    'bg': ('koru_chair', .5, .5), 'end': True,
    'card': {'big': 'Very Japanese\nbreakfast', 'sub': 'Follow @koru.tokyo_guide'}},
  ]},
})

# ---------------- Batch 5: photo backgrounds in every scene, shorter, no sales hooks ----------------
NS = 'Photo: similar dish, not this shop'
FOLLOW = {'big': 'Real Tokyo food tips', 'sub': 'Follow @koru.tokyo_guide'}
LIST = {'big': 'Going to Tokyo?', 'sub': 'Link in bio: free food list check'}
SCRIPTS.update({
 'b5_01_shinpuku': {'title': 'Black ramen, ¥880', 'scenes': [
   {'say': "This black ramen costs eight hundred eighty yen, right by {Akihabara|ɑkihɑbˈɑɾɑ}.",
    'bg': ('ramen_bowl_0', .5, .5), 'tag': NS, 'hook': True, 'card': {'kicker': 'AKIHABARA', 'big': 'Black ramen.\n¥880.'}},
   {'say': "It's Kyoto style. The soup looks like coffee, but it's soy sauce.",
    'bg': ('ramen_bowl_0', .4, .45), 'tag': NS, 'card': {'kicker': 'KYOTO STYLE', 'big': 'Looks like coffee.\nIt’s soy sauce.'}},
   {'say': "Small is eight eighty. Regular is nine eighty.",
    'bg': ('tokyo_alley_restaurant_2', .5, .5), 'card': {'kicker': 'PRICE (SEP 2026)', 'big': 'Small ¥880\nRegular ¥980'}},
   {'say': "The shop is {Shinpuku Saikan|ʃˈinpuku sˈaɪkɑn}. One of my regular lunch spots.",
    'bg': ('tokyo_alley_restaurant_1', .5, .5), 'card': {'kicker': "YU'S PICK", 'jp': '新福菜館', 'roman': 'SHINPUKU SAIKAN', 'sub': 'Akihabara'}},
   {'say': "Follow for a real Tokyo lunch every week.", 'bg': ('koru_smile', .5, .45), 'end': True, 'card': FOLLOW},
 ]},
 'b5_02_tsukemen': {'title': 'How to eat tsukemen', 'scenes': [
   {'say': "Don't drink the tsukemen soup yet. Here's the order.",
    'bg': ('ramen_bowl_1', .5, .5), 'hook': True, 'card': {'kicker': 'TSUKEMEN', 'big': "Don't drink\nthe soup yet."}},
   {'say': "Dip the cold noodles into the thick soup, and eat.",
    'bg': ('ramen_bowl_1', .35, .5), 'card': {'kicker': 'STEP 1', 'big': 'Dip, then eat'}},
   {'say': "When the noodles are gone, ask for {sūpu wari|sˈuːpu wˈɑɾi}. They add hot broth.",
    'bg': ('ramen_bowl_1', .65, .5), 'card': {'kicker': 'STEP 2', 'jp': 'スープ割り', 'roman': 'SŪPU-WARI', 'sub': '= hot broth to thin the soup'}},
   {'say': "Now drink it. My pick is {Tsujita|tsudʒˈitɑ}, near {Suehirochō|sueɪhiɾoʊtʃˈoʊ}.",
    'bg': ('tokyo_alley_restaurant_3', .5, .5), 'card': {'kicker': "YU'S PICK", 'jp': 'つじ田', 'roman': 'TSUJITA', 'sub': 'near Suehirocho, by Akihabara'}},
   {'say': "Save this before your first bowl.", 'bg': ('koru_autumn', .5, .5), 'end': True, 'card': FOLLOW},
 ]},
 'b5_03_dandan': {'title': 'Soupless dandan noodles', 'scenes': [
   {'say': "My favorite spicy noodles in Tokyo have no soup at all.",
    'bg': ('ramen_bowl_0', .5, .55), 'tag': NS, 'hook': True, 'card': {'kicker': 'YUSHIMA', 'big': 'Spicy noodles.\nNo soup.'}},
   {'say': "It's called {tsuyu nashi tantanmen|tsˈujuː nˈɑʃi tɑntˈɑnmɛn}. Soupless dandan noodles.",
    'bg': ('ramen_bowl_0', .4, .5), 'tag': NS, 'card': {'kicker': 'ORDER', 'jp': '汁なし担担麺', 'roman': 'SOUPLESS DANDAN', 'sub': 'Sichuan pepper, sesame, chili oil'}},
   {'say': "Mix it well from the bottom before your first bite.",
    'bg': ('ramen_bowl_0', .6, .5), 'tag': NS, 'card': {'kicker': 'HOW', 'big': 'Mix from\nthe bottom'}},
   {'say': "My pick is {A-un|ˈɑuːn} in {Yushima|juːʃˈimɑ}. About ten minutes' walk from {Akihabara|ɑkihɑbˈɑɾɑ}.",
    'bg': ('tokyo_street_night_3', .5, .5), 'card': {'kicker': "YU'S PICK", 'jp': '阿吽 湯島', 'roman': 'A-UN, YUSHIMA', 'sub': '~10 min walk from Akihabara'}},
   {'say': "Follow for a real Tokyo lunch every week.", 'bg': ('koru_blep', .45, .5), 'end': True, 'card': FOLLOW},
 ]},
 'b5_04_allergy': {'title': 'Food allergy in Japan', 'scenes': [
   {'say': "Food allergy? Learn this one sentence before you fly to Japan.",
    'bg': ('tempura_0', .5, .5), 'hook': True, 'card': {'kicker': 'ALLERGIES', 'big': 'Learn this\none sentence.'}},
   {'say': "Say the food, then {ga taberaremasen|ɡɑ tɑbɛɾɑɾɛmɑsˈɛn}. I can't eat it.",
    'bg': ('tempura_1', .5, .5), 'card': {'kicker': 'SAY', 'jp': '〇〇が\n食べられません', 'roman': '___ GA TABERAREMASEN', 'sub': "= I can't eat ___"}},
   {'say': "Shrimp is {ebi|ˈɛbi}. Crab is {kani|kˈɑni}. Pork is {butaniku|butˈɑniku}.",
    'bg': ('tempura_0', .4, .5), 'card': {'kicker': 'COMMON WORDS', 'jp': 'えび · かに · 豚肉', 'roman': 'EBI · KANI · BUTANIKU', 'sub': 'shrimp · crab · pork'}},
   {'say': "For serious allergies, carry it written in Japanese and show the staff.",
    'bg': ('izakaya_0', .5, .5), 'card': {'kicker': 'SERIOUS ALLERGY?', 'big': 'Carry it\nwritten down'}},
   {'say': "Save this. Share it with your travel buddy.", 'bg': ('koru_flowers', .5, .45), 'end': True, 'card': FOLLOW},
 ]},
 'b5_05_dashi': {'title': 'Vegetarian? Read this', 'scenes': [
   {'say': "Vegetarian in Japan? That miso soup probably has fish in it.",
    'bg': ('japanese_breakfast_0', .5, .5), 'hook': True, 'card': {'kicker': 'VEGETARIAN?', 'big': 'Miso soup\nhas fish.'}},
   {'say': "Most soups and noodle broths use {dashi|dˈɑʃi}. A stock usually made from bonito fish.",
    'bg': ('japanese_breakfast_0', .35, .55), 'card': {'kicker': 'WHY', 'jp': 'だし', 'roman': 'DASHI', 'sub': '= stock, often from bonito fish'}},
   {'say': "That includes udon, soba and many sauces.",
    'bg': ('soba_noodles_0', .5, .5), 'card': {'kicker': 'ALSO IN', 'big': 'Udon · soba ·\nsauces'}},
   {'say': "Ask: {dashi ni sakana wa haitte imasu ka?|dˈɑʃi ni sɑkˈɑnɑ wɑ hˈaɪttɛ imˈɑs kɑ} Is there fish in the stock?",
    'bg': ('japanese_breakfast_0', .65, .5), 'card': {'kicker': 'ASK', 'jp': 'だしに魚は\n入っていますか？', 'roman': 'DASHI NI SAKANA WA…?', 'sub': '= is there fish in the stock?'}},
   {'say': "Planning a trip? Link in my bio. I'll check your food list.", 'bg': ('koru_sofa', .55, .5), 'end': True, 'card': LIST},
 ]},
 'b5_06_nanmei': {'title': 'The first question you hear', 'scenes': [
   {'say': "Every restaurant in Tokyo will ask you this first.",
    'bg': ('tokyo_alley_restaurant_2', .5, .5), 'hook': True, 'card': {'kicker': 'AT THE DOOR', 'big': 'The first\nquestion.'}},
   {'say': "{Nan-mei sama desu ka?|nɑnmˈeɪ sɑmɑ dɛs kɑ} How many people?",
    'bg': ('tokyo_alley_restaurant_0', .5, .5), 'card': {'kicker': 'THEY SAY', 'jp': '何名様ですか？', 'roman': 'NAN-MEI SAMA DESU KA?', 'sub': '= how many people?'}},
   {'say': "Just hold up your fingers. Or say {hitori|hitˈoɾi}, {futari|futˈɑɾi}, {sannin|sɑnnˈin}.",
    'bg': ('tokyo_alley_restaurant_3', .5, .5), 'card': {'kicker': 'YOU SAY', 'jp': '一人 · 二人 · 三人', 'roman': 'HITORI · FUTARI · SANNIN', 'sub': '1 · 2 · 3 people'}},
   {'say': "Then wait to be seated. Don't just pick a table.",
    'bg': ('izakaya_0', .5, .5), 'card': {'kicker': 'THEN', 'big': 'Wait to\nbe seated'}},
   {'say': "Follow for more real Tokyo food tips.", 'bg': ('koru_park', .5, .55), 'end': True, 'card': FOLLOW},
 ]},
 'b5_07_lastorder': {'title': 'What "L.O." means', 'scenes': [
   {'say': "Restaurant says open till ten? You might need to order by nine thirty.",
    'bg': ('tokyo_alley_restaurant_0', .5, .5), 'hook': True, 'card': {'kicker': 'OPENING HOURS', 'big': 'Open till 22:00?\nOrder by 21:30.'}},
   {'say': "Look for L O on the door or on Google Maps. It means last order.",
    'bg': ('tokyo_alley_restaurant_1', .5, .5), 'card': {'kicker': 'LOOK FOR', 'big': 'L.O.', 'sub': '= last order'}},
   {'say': "It's often thirty to sixty minutes before closing.",
    'bg': ('tokyo_street_night_2', .5, .5), 'card': {'kicker': 'USUALLY', 'big': '30–60 min\nbefore closing'}},
   {'say': "Late dinner? Check it before you walk there.",
    'bg': ('tokyo_street_night_3', .5, .5), 'card': {'kicker': 'TIP', 'big': 'Check before\nyou walk'}},
   {'say': "Follow for more real Tokyo food tips.", 'bg': ('koru_chair', .5, .5), 'end': True, 'card': FOLLOW},
 ]},
 'b5_08_oshibori': {'title': 'Free at every table', 'scenes': [
   {'say': "In Tokyo restaurants, three things are free. Don't pay extra for them.",
    'bg': ('izakaya_0', .5, .5), 'hook': True, 'card': {'kicker': 'TOKYO RESTAURANTS', 'big': '3 things\nare free.'}},
   {'say': "Water or tea. Just ask for {mizu|mˈizu} if it doesn't come.",
    'bg': ('matcha_1', .5, .5), 'card': {'kicker': '1', 'jp': 'お水', 'roman': 'MIZU', 'sub': '= water (usually free)'}},
   {'say': "A wet towel, {oshibori|oʊʃibˈoɾi}. It's for your hands.",
    'bg': ('japanese_breakfast_0', .5, .5), 'card': {'kicker': '2', 'jp': 'おしぼり', 'roman': 'OSHIBORI', 'sub': '= wet towel, for your hands'}},
   {'say': "And the service. There's no tipping in Japan.",
    'bg': ('tonkatsu_0', .5, .5), 'card': {'kicker': '3', 'big': 'No tipping'}},
   {'say': "Save this for your first meal.", 'bg': ('koru_autumn2', .45, .5), 'end': True, 'card': FOLLOW},
 ]},
 'b5_09_register': {'title': 'Where to pay', 'scenes': [
   {'say': "Don't wait for the bill at your table in Japan. Do this instead.",
    'bg': ('tokyo_alley_restaurant_3', .5, .5), 'hook': True, 'card': {'kicker': 'PAYING', 'big': "Don't wait\nfor the bill."}},
   {'say': "In most casual places, the bill is already on your table, or they bring it with the food.",
    'bg': ('tonkatsu_0', .5, .5), 'card': {'kicker': 'LOOK', 'big': 'Bill is often\nalready there'}},
   {'say': "Take it to the register by the door and pay there.",
    'bg': ('tokyo_alley_restaurant_2', .5, .5), 'card': {'kicker': 'THEN', 'jp': 'レジ', 'roman': 'REJI', 'sub': '= register, by the door'}},
   {'say': "Don't leave cash on the table. They'll chase you to return it.",
    'bg': ('izakaya_0', .5, .5), 'card': {'kicker': 'DON’T', 'big': 'Leave cash\non the table'}},
   {'say': "Follow for more real Tokyo food tips.", 'bg': ('koru_nose', .5, .45), 'end': True, 'card': FOLLOW},
 ]},
 'b5_10_ekibiru': {'title': 'Station building dinner', 'scenes': [
   {'say': "When I travel for work, this is how I pick dinner in a new city.",
    'bg': ('tokyo_station_1', .5, .5), 'hook': True, 'card': {'kicker': 'BUSINESS TRIP', 'big': 'How I pick\ndinner.'}},
   {'say': "Go to the station building. The top floors are a restaurant floor.",
    'bg': ('tokyo_station_1', .35, .5), 'card': {'kicker': 'WHERE', 'jp': 'レストラン街', 'roman': 'RESUTORAN-GAI', 'sub': '= restaurant floor, usually upstairs'}},
   {'say': "Many places have the local specialty, plastic food samples, and picture menus.",
    'bg': ('tempura_1', .5, .5), 'card': {'kicker': 'WHY', 'big': 'Local food,\npicture menus'}},
   {'say': "It's not the hidden gem. But you'll eat well, and you won't get lost.",
    'bg': ('bento_box_0', .5, .5), 'card': {'kicker': 'HONESTLY', 'big': 'Not a hidden gem.\nStill good.'}},
   {'say': "Planning a trip? Link in my bio. I'll check your food list.", 'bg': ('koru_smile', .5, .45), 'end': True, 'card': LIST},
 ]},
 'b5_11_ameyoko': {'title': 'Ameyoko street food rule', 'scenes': [
   {'say': "At {Ameyoko|ɑmɛjˈoʊkoʊ} market in {Ueno|uˈɛnoʊ}, there's one rule for street food.",
    'bg': ('tokyo_street_night_1', .5, .5), 'hook': True, 'card': {'kicker': 'UENO · AMEYOKO', 'big': 'One street\nfood rule.'}},
   {'say': "Eat it at the stall. Many shops ask you not to eat while walking.",
    'bg': ('tokyo_street_night_1', .4, .6), 'card': {'kicker': 'THE RULE', 'big': 'Eat at\nthe stall'}},
   {'say': "Not sure? Ask: {koko de tabete ii desu ka?|kˈoʊkoʊ dɛ tɑbˈɛtɛ ˈiː dɛs kɑ} Can I eat here?",
    'bg': ('takoyaki_0', .5, .5), 'card': {'kicker': 'ASK', 'jp': 'ここで食べて\nいいですか？', 'roman': 'KOKO DE TABETE II DESU KA?', 'sub': '= can I eat here?'}},
   {'say': "And take your trash back to the shop. There are almost no bins.",
    'bg': ('tokyo_street_night_1', .6, .4), 'card': {'kicker': 'TRASH', 'big': 'Give it back\nto the shop'}},
   {'say': "Follow for more real Tokyo food tips.", 'bg': ('koru_park', .5, .55), 'end': True, 'card': FOLLOW},
 ]},
 'b5_12_okawari': {'title': 'Free refills?', 'scenes': [
   {'say': "At some tonkatsu shops in Tokyo, the rice and cabbage refills are free.",
    'bg': ('tonkatsu_0', .5, .5), 'hook': True, 'card': {'kicker': 'TONKATSU', 'big': 'Free refills?\nSometimes.'}},
   {'say': "Not every shop. But if you see staff walking around with cabbage, that's the sign.",
    'bg': ('tonkatsu_0', .35, .4), 'card': {'kicker': 'THE SIGN', 'big': 'Staff carrying\ncabbage'}},
   {'say': "Just say {okawari|oʊkɑwˈɑɾi}. Another one, please.",
    'bg': ('tonkatsu_0', .6, .6), 'card': {'kicker': 'SAY', 'jp': 'おかわり', 'roman': 'OKAWARI', 'sub': '= another one, please'}},
   {'say': "Follow for a real Tokyo lunch every week.", 'bg': ('koru_chair', .5, .5), 'end': True, 'card': FOLLOW},
 ]},
 'b5_13_platecolors': {'title': 'Sushi plate colors', 'scenes': [
   {'say': "At conveyor sushi, the plate color is the price.",
    'bg': ('sushi_conveyor_belt_0', .5, .5), 'hook': True, 'card': {'kicker': 'KAITEN-ZUSHI', 'big': 'Color = price.'}},
   {'say': "Find the price chart on the wall or the menu. Each color has a price.",
    'bg': ('sushi_plate_1', .5, .5), 'card': {'kicker': 'LOOK FOR', 'big': 'The color chart'}},
   {'say': "Stack your plates. Staff count them at the end.",
    'bg': ('sushi_conveyor_belt_0', .4, .6), 'card': {'kicker': 'THEN', 'big': 'Stack your plates'}},
   {'say': "Gold and black plates are usually the expensive ones.",
    'bg': ('sushi_plate_1', .6, .4), 'card': {'kicker': 'WATCH OUT', 'big': 'Gold & black\n= pricey'}},
   {'say': "Save this for sushi night.", 'bg': ('koru_sofa', .55, .5), 'end': True, 'card': FOLLOW},
 ]},
 'b5_14_takoyaki': {'title': 'Takoyaki warning', 'scenes': [
   {'say': "Fresh takoyaki is lava inside. Don't eat it in one bite.",
    'bg': ('takoyaki_0', .5, .5), 'hook': True, 'card': {'kicker': 'TAKOYAKI', 'big': 'Lava inside.'}},
   {'say': "Bite a small hole first, and let the steam out.",
    'bg': ('takoyaki_0', .4, .6), 'card': {'kicker': 'HOW', 'big': 'Small bite first.\nLet it breathe.'}},
   {'say': "It's octopus in a soft batter, with sauce, mayo and bonito flakes.",
    'bg': ('takoyaki_0', .6, .5), 'card': {'kicker': 'WHAT', 'jp': 'たこ焼き', 'roman': 'TAKOYAKI', 'sub': '= octopus balls'}},
   {'say': "Follow for more real Tokyo food tips.", 'bg': ('koru_blep', .45, .5), 'end': True, 'card': FOLLOW},
 ]},
})

# ---- Retention fix (data 10/15: dark text-only cards lost viewers at 2-4s) ----
# Give every remaining text-only scene a real photo background.
BG_FILL = {
 'w3_04_sake': ['sake_bottle_0', 'sake_cup_4', 'sake_bottle_2', 'izakaya_0'],
 'w3_05_closed_sunday': ['tokyo_alley_restaurant_1', 'soba_noodles_0', 'tokyo_alley_restaurant_3'],
 'w4_01_onigiri': ['convenience_store_japan_0', 'bento_box_0', 'convenience_store_japan_0'],
 'w4_02_ticketmachine': ['ramen_0', 'tokyo_alley_restaurant_2', 'ramen_bowl_0'],
 'w4_03_konbini_hotsnack': ['convenience_store_japan_0', 'tempura_1', 'takoyaki_0'],
 'w4_04_depachika': ['bento_box_0', 'sushi_plate_1', 'tempura_0'],
 'w4_05_cash': ['tokyo_alley_restaurant_0', 'takoyaki_0', 'tokyo_street_night_1'],
 'w4_06_gyudon_breakfast': ['tokyo_street_night_2', 'japanese_breakfast_0', 'tonkatsu_0'],
}
for _vid, _bgs in BG_FILL.items():
    _it = iter(_bgs)
    for _sc in SCRIPTS[_vid]['scenes']:
        if not _sc.get('bg'):
            _sc['bg'] = (next(_it), .5, .5)
HOOK_BG = {'w3_04_sake': 'sake_bottle_0', 'w3_05_closed_sunday': 'tokyo_alley_restaurant_1',
           'w4_01_onigiri': 'convenience_store_japan_0', 'w4_02_ticketmachine': 'ramen_0',
           'w4_03_konbini_hotsnack': 'convenience_store_japan_0', 'w4_04_depachika': 'bento_box_0',
           'w4_05_cash': 'tokyo_alley_restaurant_0', 'w4_06_gyudon_breakfast': 'japanese_breakfast_0'}
for _vid, _bg in HOOK_BG.items():
    _h = SCRIPTS[_vid]['scenes'][0]; _h['bg'] = (_bg, .5, .5); _h.pop('ai', None)
# Named-shop scenes use generic street photos: label them so nobody thinks it's the shop.
for _vid in ('b5_01_shinpuku', 'b5_02_tsukemen', 'b5_03_dandan'):
    for _sc in SCRIPTS[_vid]['scenes']:
        if _sc.get('card', {}).get('kicker') == "YU'S PICK":
            _sc['tag'] = 'Photo: not this shop'

# ---------------- Batch 6 (from Oct 31): 1/day, first-person "my pick" + timely ----------------
SCRIPTS.update({
 'c6_01_taxfree_now': {'title': 'Tax-free: new rules now', 'scenes': [
   {'say': "From November first, tax-free shopping in Japan works differently. Don't get caught out.",
    'bg': ('ai_airport_exit', .5, .45), 'ai': True, 'hook': True, 'card': {'kicker': 'FROM NOV 1', 'big': 'Tax-free\njust changed.'}},
   {'say': "You pay the full price with tax at the store.",
    'bg': ('ai_street2', .45, .5), 'ai': True, 'card': {'kicker': 'AT THE STORE', 'big': 'Pay full price'}},
   {'say': "You get the tax back only after customs checks your items at the airport, before check-in.",
    'bg': ('ai_airport1', .5, .5), 'ai': True, 'card': {'kicker': 'AT THE AIRPORT', 'big': 'Customs check,\nthen refund'}},
   {'say': "So keep your items with you, not in your checked bag, until then.",
    'bg': ('ai_airport2', .5, .5), 'ai': True, 'card': {'kicker': 'UNTIL CUSTOMS', 'big': 'Keep them with you,\nnot checked in'}},
   {'say': "Save this. Send it to whoever you're traveling with.", 'bg': ('koru_nose', .5, .45), 'end': True,
    'card': {'big': 'Save & share', 'sub': 'Follow @koru.tokyo_guide'}},
 ]},
 'c6_02_ippekoppe': {'title': 'My favorite katsu curry', 'scenes': [
   {'say': "My favorite katsu curry near {Akihabara|ɑkihɑbˈɑɾɑ} comes from a famous tonkatsu shop.",
    'bg': ('japanese_curry_rice_1', .5, .5), 'tag': NS, 'hook': True, 'card': {'kicker': "YU'S PICK", 'big': 'Katsu curry\nfrom a tonkatsu pro.'}},
   {'say': "It's the curry shop of Tonkatsu {Aoki|ɑˈoʊki}. So the cutlet is the star. Thick and juicy.",
    'bg': ('tonkatsu_0', .5, .4), 'tag': NS, 'card': {'kicker': 'WHY', 'jp': 'とんかつ檍', 'roman': 'TONKATSU AOKI', 'sub': 'the curry is their side project'}},
   {'say': "The shop is called {Ippekoppe|ippɛkˈoppɛ}.",
    'bg': ('tokyo_alley_restaurant_3', .5, .5), 'tag': 'Photo: not this shop', 'card': {'kicker': 'THE SHOP', 'jp': 'いっぺこっぺ', 'roman': 'IPPEKOPPE', 'sub': 'Suehirocho side of Akihabara'}},
   {'say': "Follow for a real Tokyo lunch every week.", 'bg': ('koru_autumn', .5, .5), 'end': True, 'card': FOLLOW},
 ]},
 'c6_03_yamabe': {'title': 'Rosu or hire?', 'scenes': [
   {'say': "Ordering tonkatsu in Japan? You'll have to choose: {rōsu|ɾˈoʊsu} or {hire|hˈiɾɛ}.",
    'bg': ('tonkatsu_0', .5, .5), 'hook': True, 'card': {'kicker': 'TONKATSU', 'big': 'Rōsu or hire?'}},
   {'say': "{Rōsu|ɾˈoʊsu} is pork loin, with a juicy strip of fat.",
    'bg': ('tonkatsu_0', .35, .45), 'card': {'kicker': 'ROSU', 'jp': 'ロース', 'roman': 'RŌSU', 'sub': '= loin, juicy, with fat'}},
   {'say': "{Hire|hˈiɾɛ} is the fillet. Lean and soft.",
    'bg': ('tonkatsu_0', .65, .55), 'card': {'kicker': 'HIRE', 'jp': 'ヒレ', 'roman': 'HIRE', 'sub': '= fillet, lean and tender'}},
   {'say': "My go-to in {Ueno|uˈɛnoʊ} is {Yamabe|jɑmɑbˈɛ}. I get the {rōsu|ɾˈoʊsu} set.",
    'bg': ('tokyo_alley_restaurant_0', .5, .5), 'tag': 'Photo: not this shop', 'card': {'kicker': "YU'S PICK", 'jp': 'とんかつ山家', 'roman': 'YAMABE, UENO', 'sub': 'I order the rōsu set'}},
   {'say': "Follow for a real Tokyo lunch every week.", 'bg': ('koru_chair', .5, .5), 'end': True, 'card': FOLLOW},
 ]},
 'c6_04_oyama': {'title': 'Menchi-katsu and a beer', 'scenes': [
   {'say': "My favorite cheap snack in {Ueno|uˈɛnoʊ}: a menchi-katsu and a beer, standing up.",
    'bg': ('tokyo_street_night_1', .5, .5), 'hook': True, 'card': {'kicker': 'UENO', 'big': 'Menchi-katsu\n+ a beer.'}},
   {'say': "Menchi-katsu is minced meat, breaded and deep fried. Crispy outside, juicy inside.",
    'bg': ('tonkatsu_0', .5, .5), 'tag': 'Photo: similar fried food', 'card': {'kicker': 'WHAT', 'jp': 'メンチカツ', 'roman': 'MENCHI-KATSU', 'sub': '= deep-fried minced meat cutlet'}},
   {'say': "I get mine at {Niku no Ōyama|nˈiku noʊ ˈoʊjɑmɑ}, a butcher shop with a standing bar.",
    'bg': ('tokyo_street_night_1', .4, .6), 'card': {'kicker': "YU'S PICK", 'jp': '肉の大山', 'roman': 'NIKU NO ŌYAMA', 'sub': 'Ueno, near Ameyoko'}},
   {'say': "Follow for more real Tokyo food tips.", 'bg': ('koru_autumn2', .45, .5), 'end': True, 'card': FOLLOW},
 ]},
 'c6_05_suehirocho': {'title': 'Akihabara lunch secret', 'scenes': [
   {'say': "Lunch in {Akihabara|ɑkihɑbˈɑɾɑ}? Walk five minutes away from the main street.",
    'bg': ('tokyo_alley_restaurant_1', .5, .5), 'hook': True, 'card': {'kicker': 'AKIHABARA', 'big': 'Walk 5 minutes.'}},
   {'say': "Head toward {Suehirochō|sueɪhiɾoʊtʃˈoʊ}. That's where the office workers eat.",
    'bg': ('tokyo_alley_restaurant_2', .5, .5), 'card': {'kicker': 'GO TOWARD', 'jp': '末広町', 'roman': 'SUEHIROCHŌ', 'sub': 'north of Akihabara, Ginza Line'}},
   {'say': "Tsukemen, katsu curry, ramen. Most of my regular lunch spots are there.",
    'bg': ('ramen_bowl_1', .5, .5), 'card': {'kicker': 'WHAT YOU’LL FIND', 'big': 'Tsukemen · curry\n· ramen'}},
   {'say': "Planning a trip? Link in my bio. I'll check your food list.", 'bg': ('koru_smile', .5, .45), 'end': True, 'card': LIST},
 ]},
})

# A1 sample of the Japanese (wa) template
import copy as _copy
SCRIPTS['wa_sample'] = _copy.deepcopy(SCRIPTS['c6_02_ippekoppe']); SCRIPTS['wa_sample']['style'] = 'wa'

# ---------------- Batch 7: wa style, facts from data/shops.json (checked 2026-10-31) ----------------
SIM = 'Photo: similar dish, not this shop'
NOT = 'Photo: not this shop'
PLAN = {'big': 'Free Tokyo food plan', 'sub': 'Link in bio · @koru.tokyo_guide'}
def _wa(title, scenes):
    return {'title': title, 'style': 'wa', 'scenes': scenes}
SCRIPTS.update({
 'd7_01_ramenkai': _wa('Clam ramen, 7 awards', [
   {'say': "This ramen shop in {Kuramae|kuɾɑmˈɛ} made Tabelog's top one hundred list seven times.",
    'bg': ('ramen_0', .5, .5), 'tag': SIM, 'hook': True, 'card': {'kicker': 'KURAMAE', 'big': '7 times\nin the top 100.'}},
   {'say': "The broth is made from clams.", 'bg': ('ramen_0', .4, .45), 'tag': SIM,
    'card': {'kicker': 'THE BOWL', 'jp': '貝だし', 'roman': 'CLAM BROTH RAMEN', 'sub': 'Ramen Kai, らーめん 改'}},
   {'say': "Cash only, no reservations, and it closes when the soup runs out.", 'bg': ('tokyo_alley_restaurant_2', .5, .5), 'tag': NOT,
    'card': {'kicker': 'BEFORE YOU GO', 'big': 'Cash only.\nGo early.'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_smile', .5, .45), 'end': True, 'card': PLAN},
 ]),
 'd7_02_marugo': _wa('Tonkatsu, 7 awards', [
   {'say': "This tonkatsu shop in {Akihabara|ɑkihɑbˈɑɾɑ} has been on Tabelog's top one hundred list seven times.",
    'bg': ('tonkatsu_0', .5, .5), 'tag': SIM, 'hook': True, 'card': {'kicker': 'AKIHABARA', 'big': 'Top 100 tonkatsu.\n7 times.'}},
   {'say': "It's called {Marugo|mɑɾˈuɡoʊ}. Order the premium loin set.", 'bg': ('tonkatsu_0', .4, .45), 'tag': SIM,
    'card': {'kicker': 'ORDER', 'jp': '特ロース', 'roman': 'TOKU-RŌSU', 'sub': 'premium loin cutlet set · Marugo 丸五'}},
   {'say': "Cash only, no reservations. Closed Mondays and most Tuesdays.", 'bg': ('tokyo_alley_restaurant_0', .5, .5), 'tag': NOT,
    'card': {'kicker': 'BEFORE YOU GO', 'big': 'Cash only.\nClosed Mon, most Tue.'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_autumn', .5, .5), 'end': True, 'card': PLAN},
 ]),
 'd7_03_karigari': _wa('Curry grand prix winner', [
   {'say': "My favorite curry in {Akihabara|ɑkihɑbˈɑɾɑ} won the {Kanda|kˈɑndɑ} Curry Grand Prix.",
    'bg': ('tokyo_alley_restaurant_1', .5, .5), 'tag': NOT, 'hook': True, 'card': {'kicker': "YU'S PICK", 'big': 'Curry Grand Prix\nwinner.'}},
   {'say': "It's {Karigari|kɑɾiɡˈɑɾi}. Order the {Akiba-mori|ɑkibɑmˈoɾi}, a plate with several curries.", 'bg': ('tokyo_alley_restaurant_1', .4, .6), 'tag': NOT,
    'card': {'kicker': 'ORDER', 'jp': 'アキバ盛り', 'roman': 'AKIBA-MORI', 'sub': 'several curries on one plate'}},
   {'say': "Open every day except New Year. Near {Suehirochō|sueɪhiɾoʊtʃˈoʊ} station.", 'bg': ('tokyo_alley_restaurant_3', .5, .5), 'tag': NOT,
    'card': {'kicker': 'GOOD TO KNOW', 'big': 'Open daily', 'sub': 'Suehirocho, 2 min walk'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_flowers', .5, .45), 'end': True, 'card': PLAN},
 ]),
 'd7_04_sugita': _wa('Michelin tonkatsu', [
   {'say': "This tonkatsu in {Kuramae|kuɾɑmˈɛ} is in the Michelin Guide. Lunch is about three thousand yen.",
    'bg': ('tonkatsu_0', .5, .5), 'tag': SIM, 'hook': True, 'card': {'kicker': 'KURAMAE', 'big': 'Michelin tonkatsu.\n~¥3,000.'}},
   {'say': "It's {Sugita|suɡˈitɑ}. Bib Gourmand, twenty twenty six. Order the loin.", 'bg': ('tonkatsu_0', .4, .4), 'tag': SIM,
    'card': {'kicker': 'ORDER', 'jp': 'ロースかつ', 'roman': 'RŌSU KATSU', 'sub': 'Tonkatsu Sugita, とんかつ すぎ田'}},
   {'say': "Closed on Thursdays. One stop from {Asakusa|ɑsɑkˈusɑ}.", 'bg': ('tokyo_alley_restaurant_0', .5, .5), 'tag': NOT,
    'card': {'kicker': 'BEFORE YOU GO', 'big': 'Closed Thursdays'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_autumn2', .45, .5), 'end': True, 'card': PLAN},
 ]),
 'd7_05_matsuya': _wa('Soba since 1884', [
   {'say': "This soba shop has been open since eighteen eighty four. People line up before it opens.",
    'bg': ('soba_noodles_0', .5, .5), 'tag': NOT, 'hook': True, 'card': {'kicker': 'KANDA', 'big': 'Soba since 1884.'}},
   {'say': "It's {Kanda Matsuya|kˈɑndɑ mɑtsˈujɑ}. Order cold {mori|mˈoɾi} soba.", 'bg': ('soba_noodles_0', .4, .6), 'tag': NOT,
    'card': {'kicker': 'ORDER', 'jp': 'もりそば', 'roman': 'MORI SOBA', 'sub': 'cold soba · Kanda Matsuya 神田まつや'}},
   {'say': "Cash only. Closed Sundays. Check Mondays before you go.", 'bg': ('tokyo_alley_restaurant_2', .5, .5), 'tag': NOT,
    'card': {'kicker': 'BEFORE YOU GO', 'big': 'Cash only.\nClosed Sundays.'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_park', .5, .55), 'end': True, 'card': PLAN},
 ]),
 'd7_06_under1000': _wa('3 lunches under ¥1,000', [
   {'say': "Three lunches under one thousand yen near {Akihabara|ɑkihɑbˈɑɾɑ}. The ones I actually eat.",
    'bg': ('tokyo_street_night_0', .5, .5), 'hook': True, 'card': {'kicker': "YU'S PICKS", 'big': '3 lunches\nunder ¥1,000.'}},
   {'say': "One. {Minogasa|minoʊɡˈɑsɑ}. Standing soba with fresh noodles. Opens at six a.m.", 'bg': ('soba_noodles_0', .5, .5), 'tag': NOT,
    'card': {'kicker': '1', 'jp': 'みのがさ', 'roman': 'MINOGASA', 'sub': 'standing soba · from ¥460'}},
   {'say': "Two. {Shinpuku Saikan|ʃˈinpuku sˈaɪkɑn}. Black soy sauce ramen, small for eight eighty.", 'bg': ('ramen_bowl_0', .5, .5), 'tag': SIM,
    'card': {'kicker': '2', 'jp': '新福菜館', 'roman': 'SHINPUKU SAIKAN', 'sub': 'ramen · small ¥880'}},
   {'say': "Three. Beef bowl at {Sanbo|sˈɑnboʊ}, near {Suehirochō|sueɪhiɾoʊtʃˈoʊ}.", 'bg': ('tokyo_alley_restaurant_3', .5, .5), 'tag': NOT,
    'card': {'kicker': '3', 'jp': '牛丼専門 サンボ', 'roman': 'SANBO', 'sub': 'gyudon · under ¥1,000'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_sofa', .55, .5), 'end': True, 'card': PLAN},
 ]),
 'd7_07_asakusa_snacks': _wa('Asakusa snacks under ¥500', [
   {'say': "Three {Asakusa|ɑsɑkˈusɑ} snacks, each under five hundred yen.",
    'bg': ('japanese_lantern_street_0', .5, .5), 'hook': True, 'card': {'kicker': 'ASAKUSA', 'big': '3 snacks\nunder ¥500.'}},
   {'say': "{Kibi dango|kˈibi dˈɑŋɡoʊ} at {Azuma|ɑzˈumɑ}. Five skewers, rolled in soybean flour.", 'bg': ('japanese_lantern_street_0', .4, .6),
    'card': {'kicker': '1', 'jp': 'きびだんご', 'roman': 'KIBI DANGO', 'sub': 'Azuma あづま · 5 skewers'}},
   {'say': "Fried buns at {Kokonoe|kokonˈoʊɛ}. From one hundred sixty yen.", 'bg': ('tempura_1', .5, .5), 'tag': 'Photo: similar fried food',
    'card': {'kicker': '2', 'jp': '揚げまんじゅう', 'roman': 'AGE-MANJŪ', 'sub': 'Kokonoe 九重 · from ¥160'}},
   {'say': "{Ningyo-yaki|niŋɡjˈoʊjɑki} at {Kimuraya|kimuɾˈɑjɑ}, open since eighteen sixty eight.", 'bg': ('japanese_lantern_street_0', .6, .4),
    'card': {'kicker': '3', 'jp': '人形焼', 'roman': 'NINGYO-YAKI', 'sub': 'Kimuraya 木村家本店 · since 1868'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_blep', .45, .5), 'end': True, 'card': PLAN},
 ]),
 'd7_08_tsujita': _wa('Tsujita: this branch only', [
   {'say': "This tsukemen bowl is only sold at one shop. Near {Akihabara|ɑkihɑbˈɑɾɑ}.",
    'bg': ('ramen_bowl_1', .5, .5), 'tag': SIM, 'hook': True, 'card': {'kicker': "YU'S PICK", 'big': 'Only sold\nat this shop.'}},
   {'say': "{Tsujita|tsudʒˈitɑ}, {Kanda Suehirochō|kˈɑndɑ sueɪhiɾoʊtʃˈoʊ}. The special chashu tsukemen.", 'bg': ('ramen_bowl_1', .4, .5), 'tag': SIM,
    'card': {'kicker': 'ORDER', 'jp': '特製チャーシューつけ麺', 'roman': 'SPECIAL CHASHU', 'sub': '¥1,640 · this branch only (May 2025)'}},
   {'say': "Or the regular rich tsukemen, eleven ten. One minute from {Suehirochō|sueɪhiɾoʊtʃˈoʊ} exit four.", 'bg': ('tokyo_alley_restaurant_1', .5, .5), 'tag': NOT,
    'card': {'kicker': 'OR', 'big': 'Rich tsukemen\n¥1,110', 'sub': 'Suehirocho Exit 4, 1 min'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_autumn', .5, .5), 'end': True, 'card': PLAN},
 ]),
 'd7_09_senbero': _wa('Senbero in Ueno', [
   {'say': "In {Ueno|uˈɛnoʊ}, thirteen hundred yen gets you tempura and up to four drinks.",
    'bg': ('tempura_0', .5, .5), 'tag': SIM, 'hook': True, 'card': {'kicker': 'UENO', 'big': 'Tempura + up to\n4 drinks: ¥1,300.'}},
   {'say': "It's called {senbero|sɛnbˈɛɾoʊ}. Drunk for about a thousand yen.", 'bg': ('izakaya_0', .5, .5),
    'card': {'kicker': 'THE WORD', 'jp': 'せんべろ', 'roman': 'SENBERO', 'sub': '= drunk for about ¥1,000'}},
   {'say': "At {Kacchan|kˈɑttʃɑn}, the set is only in the standing area on the ground floor.", 'bg': ('tokyo_street_night_1', .5, .5), 'tag': NOT,
    'card': {'kicker': 'WHERE', 'jp': 'かっちゃん', 'roman': 'KACCHAN', 'sub': 'ground-floor standing area only'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_chair', .5, .5), 'end': True, 'card': PLAN},
 ]),
})

# ---- e8: wa batch for 11/6 21:00 - 11/9 ----
SCRIPTS.update({
 'e8_01_kamiya': _wa('Bar since 1880', [
   {'say': "This bar in {Asakusa|ɑsɑkˈusɑ} opened in eighteen eighty. The building is a registered cultural property.",
    'bg': ('izakaya_0', .5, .5), 'tag': NOT, 'hook': True, 'card': {'kicker': 'ASAKUSA', 'big': 'A bar\nsince 1880.'}},
   {'say': "It's {Kamiya|kɑmˈijɑ} Bar. Order the house drink, {Denki|dˈɛŋki} Bran. Four hundred yen.", 'bg': ('izakaya_0', .4, .5), 'tag': NOT,
    'card': {'kicker': 'ORDER', 'jp': '電気ブラン', 'roman': 'DENKI BRAN', 'sub': '¥400 · Kamiya Bar 神谷バー'}},
   {'say': "Buy tickets at the register first. Cash only. Closed Tuesdays.", 'bg': ('tokyo_street_night_2', .5, .5), 'tag': NOT,
    'card': {'kicker': 'BEFORE YOU GO', 'big': 'Tickets first.\nCash only.', 'sub': 'Closed Tue + 2 Mondays a month'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_sofa', .55, .5), 'end': True, 'card': PLAN},
 ]),
 'e8_02_usagiya': _wa('Dorayaki since 1913', [
   {'say': "This dorayaki shop in {Ueno|uˈɛnoʊ} has been open since nineteen thirteen. One costs two hundred seventy yen.",
    'bg': ('dorayaki_1', .5, .5), 'tag': SIM, 'hook': True, 'card': {'kicker': 'UENO', 'big': 'Dorayaki.\n¥270.'}},
   {'say': "It's {Usagiya|usˈɑɡijɑ}. Pancakes with sweet red bean paste. Takeout only.", 'bg': ('dorayaki_0', .4, .45), 'tag': SIM,
    'card': {'kicker': 'ORDER', 'jp': 'どらやき', 'roman': 'DORAYAKI', 'sub': 'Usagiya うさぎや · takeout only'}},
   {'say': "No cards. Closed Wednesdays. After four p.m., you need to reserve.", 'bg': ('tokyo_alley_restaurant_3', .5, .5), 'tag': NOT,
    'card': {'kicker': 'BEFORE YOU GO', 'big': 'Cash only.\nClosed Wed.', 'sub': 'after 16:00: reservation needed'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_smile', .5, .45), 'end': True, 'card': PLAN},
 ]),
 'e8_03_onihei': _wa('Sashimi lunch ¥880', [
   {'say': "One of my lunch picks near {Akihabara|ɑkihɑbˈɑɾɑ}. A sashimi set for eight hundred eighty yen.",
    'bg': ('sashimi_0', .5, .5), 'tag': SIM, 'hook': True, 'card': {'kicker': "YU'S PICK", 'big': 'Sashimi lunch.\n¥880.'}},
   {'say': "It's {Onihei|onihˈeɪ}, near {Suehirochō|sueɪhiɾoʊtʃˈoʊ} station. Order the sashimi or tuna set.", 'bg': ('sashimi_3', .4, .5), 'tag': SIM,
    'card': {'kicker': 'ORDER', 'jp': '刺身定食', 'roman': 'SASHIMI TEISHOKU', 'sub': 'Uogashi Onihei 魚河岸 おに平'}},
   {'say': "Lunch Monday to Saturday. Cards are OK. Closed Sundays.", 'bg': ('tokyo_alley_restaurant_1', .5, .5), 'tag': NOT,
    'card': {'kicker': 'GOOD TO KNOW', 'big': 'Cards OK.\nClosed Sundays.', 'sub': 'lunch 11:30-14:30 Mon-Sat'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_autumn', .5, .5), 'end': True, 'card': PLAN},
 ]),
 'e8_04_yonekyu': _wa('Beef hotpot since 1886', [
   {'say': "This beef hotpot shop in {Asakusa|ɑsɑkˈusɑ} opened in eighteen eighty six.",
    'bg': ('hot_pot_1', .5, .5), 'tag': SIM, 'hook': True, 'card': {'kicker': 'ASAKUSA', 'big': 'Beef hotpot\nsince 1886.'}},
   {'say': "It's {Yonekyu|joʊnˈɛkju}. On Tabelog's top one hundred list. Order {gyunabe|ɡjˈunɑbɛ}.", 'bg': ('hot_pot_1', .4, .45), 'tag': SIM,
    'card': {'kicker': 'ORDER', 'jp': '牛鍋', 'roman': 'GYUNABE', 'sub': 'Yonekyu 米久本店 · Top 100 2026'}},
   {'say': "Closed Wednesdays. Reservations only for groups of ten or more.", 'bg': ('japanese_lantern_street_0', .5, .5), 'tag': NOT,
    'card': {'kicker': 'BEFORE YOU GO', 'big': 'Closed Wednesdays.', 'sub': 'no reservations for small groups'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_autumn2', .45, .5), 'end': True, 'card': PLAN},
 ]),
 'e8_05_tengoku': _wa('Heaven hotcakes', [
   {'say': "These hotcakes in {Asakusa|ɑsɑkˈusɑ} are stamped with the word heaven.",
    'bg': ('pancakes_3', .5, .5), 'tag': SIM, 'hook': True, 'card': {'kicker': 'ASAKUSA', 'big': 'Hotcakes\nstamped "heaven".'}},
   {'say': "It's Coffee {Tengoku|tˈɛŋɡoku}, an old style cafe on Tabelog's top cafe list.", 'bg': ('pancakes_4', .4, .45), 'tag': SIM,
    'card': {'kicker': 'ORDER', 'jp': '天国', 'roman': 'TENGOKU = HEAVEN', 'sub': 'Coffee Tengoku 珈琲 天国 · hotcakes'}},
   {'say': "Open from noon to six. Closed Tuesdays. No reservations.", 'bg': ('tokyo_alley_restaurant_0', .5, .5), 'tag': NOT,
    'card': {'kicker': 'BEFORE YOU GO', 'big': '12:00-18:00.\nClosed Tuesdays.'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_flowers', .5, .45), 'end': True, 'card': PLAN},
 ]),
 'e8_06_bondy': _wa('Curry + free potato', [
   {'say': "My favorite curry in {Jinbōchō|dʒinboʊtʃˈoʊ} comes with a free baked potato.",
    'bg': ('curry_rice_1', .5, .5), 'tag': SIM, 'hook': True, 'card': {'kicker': "YU'S PICK", 'big': 'Curry with a\nfree potato.'}},
   {'say': "It's {Bondy|bˈɑndi}. It won the {Kanda|kˈɑndɑ} Curry Grand Prix. Order the beef curry.", 'bg': ('curry_rice_1', .4, .45), 'tag': SIM,
    'card': {'kicker': 'ORDER', 'jp': 'ビーフカレー', 'roman': 'BEEF CURRY', 'sub': 'Bondy ボンディ · about ¥1,700-2,000'}},
   {'say': "It's on the second floor. Enter from the back of the building. Cash only.", 'bg': ('tokyo_alley_restaurant_2', .5, .5), 'tag': NOT,
    'card': {'kicker': 'BEFORE YOU GO', 'big': '2F, enter at\nthe back.', 'sub': 'Cash only'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_park', .5, .55), 'end': True, 'card': PLAN},
 ]),
 'e8_07_isegen': _wa('Monkfish hotpot since 1830', [
   {'say': "This monkfish hotpot shop opened in eighteen thirty. From November, it opens on weekends again.",
    'bg': ('hot_pot_2', .5, .5), 'tag': SIM, 'hook': True, 'card': {'kicker': 'KANDA', 'big': 'Since 1830.\nHotpot season.'}},
   {'say': "It's {Isegen|isˈɛɡɛn}. Order {ankō|ɑŋkˈoʊ} {nabe|nˈɑbɛ}, monkfish hotpot.", 'bg': ('hot_pot_2', .4, .45), 'tag': SIM,
    'card': {'kicker': 'ORDER', 'jp': 'あんこう鍋', 'roman': 'ANKŌ NABE', 'sub': 'Isegen いせ源 · monkfish hotpot'}},
   {'say': "Dinner is ten thousand yen or more. Lunch is cheaper.", 'bg': ('tokyo_street_night_3', .5, .5), 'tag': NOT,
    'card': {'kicker': 'BUDGET', 'big': 'Dinner ¥10,000+', 'sub': 'Apr-Oct: closed weekends'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_chair', .5, .5), 'end': True, 'card': PLAN},
 ]),
 'e8_08_rokurinsha': _wa('Tsukemen in Ueno Station', [
   {'say': "You can eat famous {tsukemen|tsukˈɛmɛn} without leaving {Ueno|uˈɛnoʊ} station.",
    'bg': ('ramen_bowl_1', .5, .5), 'tag': SIM, 'hook': True, 'card': {'kicker': 'UENO STATION', 'big': 'Tsukemen,\ninside the station.'}},
   {'say': "It's {Rokurinsha|ɾoʊkuɾˈinʃɑ}, on the first floor of {atre|ˈɑtɾeɪ} {Ueno|uˈɛnoʊ}. Dip thick noodles in rich soup.", 'bg': ('ramen_bowl_1', .4, .45), 'tag': SIM,
    'card': {'kicker': 'ORDER', 'jp': 'つけめん', 'roman': 'TSUKEMEN', 'sub': 'Rokurinsha 六厘舎 · about ¥1,000'}},
   {'say': "Open every day, ten a.m. to eleven p.m. Easy before a train.", 'bg': ('tokyo_station_2', .5, .5), 'tag': NOT,
    'card': {'kicker': 'GOOD TO KNOW', 'big': 'Daily\n10:00-23:00'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_nose', .5, .5), 'end': True, 'card': PLAN},
 ]),
 'e8_09_daikokuya': _wa('Tendon, 4 big prawns', [
   {'say': "Four big prawns on one bowl of rice. This is a famous {tendon|tˈɛndɑn} in {Asakusa|ɑsɑkˈusɑ}.",
    'bg': ('tempura_1', .5, .5), 'tag': SIM, 'hook': True, 'card': {'kicker': 'ASAKUSA', 'big': '4 big prawns.\nOne bowl.'}},
   {'say': "It's {Daikokuya|dɑɪkˈoʊkujɑ}. Order the {ebi|ˈɛbi} {tendon|tˈɛndɑn}. From about two thousand three hundred yen.", 'bg': ('tempura_0', .4, .45), 'tag': SIM,
    'card': {'kicker': 'ORDER', 'jp': '海老天丼', 'roman': 'EBI TENDON', 'sub': 'Daikokuya 大黒家 · from ¥2,300'}},
   {'say': "No credit cards. Dinner lines can be about an hour, so go at lunch.", 'bg': ('japanese_lantern_street_0', .5, .5), 'tag': NOT,
    'card': {'kicker': 'BEFORE YOU GO', 'big': 'No cards.\nGo at lunch.'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_blep', .5, .5), 'end': True, 'card': PLAN},
 ]),
 'e8_10_kikanbo': _wa('Hot + numbing ramen', [
   {'say': "This ramen in {Kanda|kˈɑndɑ} is spicy hot and numbing at the same time.",
    'bg': ('ramen_bowl_0', .5, .5), 'tag': SIM, 'hook': True, 'card': {'kicker': 'KANDA', 'big': 'Spicy.\nAnd numbing.'}},
   {'say': "It's {Kikanbo|kikˈɑnboʊ}. Order the {karashibi|kɑɾɑʃˈibi} miso ramen. Under one thousand yen.", 'bg': ('ramen_bowl_0', .4, .45), 'tag': SIM,
    'card': {'kicker': 'ORDER', 'jp': 'カラシビ味噌らー麺', 'roman': 'KARASHIBI MISO', 'sub': 'Kikanbo 鬼金棒 · chili + sansho'}},
   {'say': "Cash only. On Sundays it closes at four p.m.", 'bg': ('tokyo_street_night_0', .5, .5), 'tag': NOT,
    'card': {'kicker': 'BEFORE YOU GO', 'big': 'Cash only.\nSun until 16:00.'}},
   {'say': "Get a free Tokyo food plan. Link in my bio.", 'bg': ('koru_sleep', .5, .5), 'end': True, 'card': PLAN},
 ]),
})

# ---- launch reel: screen recording of the planner (composed by compose_screen.py) ----
SCRIPTS['lr_01_planner'] = {'title': 'Free Tokyo food planner', 'style': 'wa', 'scenes': [
  {'say': "I made a free Tokyo food planner.", 'title': 'I made a free\nTokyo food planner'},
  {'say': "Pick your areas and budget, then press print.", 'title': 'Pick areas + budget.\nPress print.'},
  {'say': "You get lunch, a sweet stop, and dinner for every day.", 'title': 'Lunch, sweets, dinner.\nEvery day.'},
  {'say': "Don't like one? Swap just that ticket, or pick your own.", 'title': "Don't like one?\nSwap just that ticket."},
  {'say': "Share it with your friends. It's free. Link in my bio.", 'title': "It's free.\nLink in bio."},
]}

SCRIPTS['lr_02_phrases'] = {'title': 'Restaurant Japanese', 'style': 'wa', 'scenes': [
  {'say': "Learn these before you eat out in Tokyo.", 'title': 'Learn these before\nyou eat in Tokyo'},
  {'say': "Say {itadakimasu|itɑdɑkimɑsu} before you eat.", 'title': 'いただきます\nitadakimasu'},
  {'say': "At ramen shops, say {men katame de|mɛn kɑtɑmɛ dɛ} for firm noodles.", 'title': '麺かためで\n= firm noodles'},
  {'say': "There's a one minute quiz, and a card to show staff your allergies.", 'title': 'Quiz + allergy card\nfor the staff'},
  {'say': "Say {gochisōsama deshita|ɡoʊtʃisoʊsɑmɑ dɛʃitɑ} when you leave. Thirty phrases, free. Link in my bio.", 'title': 'ごちそうさまでした\n30 phrases · link in bio'},
]}

SCRIPTS['lr_03_app'] = {'title': 'Free Tokyo food app', 'style': 'wa', 'scenes': [
  {'say': "Going to Tokyo? This free planner shows you where locals actually eat.", 'title': 'Where locals eat in Tokyo.\nPlanned for you. Free.'},
  {'say': "No more closed doors, cash-only surprises, or not knowing what to say.", 'title': 'Closed? Cash only?\nWhat do I say?'},
  {'say': "Pick your days, areas and budget. You get lunch, a sweet stop and dinner for every day. Don't like one? Swap it.", 'title': 'Days + areas + budget\n= your food plan'},
  {'say': "Every place is checked by a local. Hours, closed days, and what to order.", 'title': 'Checked by a local:\nhours · closed days · what to order'},
  {'say': "Tap to hear what to say, and show this card if you have allergies.", 'title': 'Hear it. Say it.\nAllergy card for staff.'},
  {'say': "I'm {Yu|juː}, an office worker in Akihabara. And this is {Koru|kˈoʊɾu}.", 'title': 'Made by Yu & Koru'},
  {'say': "It's free, no sign-up. Link in my bio. Send this to the friend you're going with.", 'title': 'Free · no sign-up\nLink in bio'},
]}

# v2 shop format prototype: photo + ticket caption + Koru host bubble + app-proof ending
SCRIPTS['v2_01_indira'] = {'title': 'Indira v2', 'style': 'v2', 'led': "YU'S PICK · KANDA 神田", 'scenes': [
  {'say': "My favorite cheap lunch in {Kanda|kˈɑndɑ} is down a staircase. Curry, for about eight hundred yen.",
   'v2': {'kind': 'photo', 'bg': None, 'pic': ('curry_rice_1', (0.3, 0.45, 1.0, 1.0)), 'kicker': "YU'S PICK", 'big': 'About ¥800 curry,\ndown a staircase', 'sub': 'Indira インデラ · since 1970'}},
  {'say': "Order the curry with an egg on top. Pick regular, or hard, which is a little spicier.",
   'v2': {'kind': 'photo', 'bg': None, 'pic': ('curry_rice_1', (0.35, 0.5, 0.95, 1.0)), 'kicker': 'ORDER', 'big': 'Curry + egg', 'sub': "Regular or 'hard' (a bit spicier)"}},
  {'say': "Then help yourself to the free pickles. There are more than ten.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'FREE', 'big': '10+ pickles &\ncondiments', 'sub': 'Fukujinzuke, rakkyo... help yourself', 'koru': 'Free toppings!'}},
  {'say': "But it's weekdays only, and it closes at six.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'BEFORE YOU GO', 'big': 'Weekdays only', 'sub': 'Closed Sat, Sun & holidays', 'koru': 'Closes at 6pm!', 'stamp': 'NO WEEKENDS'}},
  {'say': "Want more rice? Say {ōmori de|oʊmˈoɾi dɛ}.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAY THIS', 'big': '大盛りで', 'sub': 'oomori de · large rice, please', 'koru': 'Tap it in my app\nto hear it!'}},
  {'say': "Hours, closed days, and what to say are in my free app. Link in bio. Send this to your curry friend.",
   'v2': {'kind': 'screen', 'clip': 'shop_indira', 'title': 'Hours · closed days · what to say\nFree app, link in bio'}},
]}

SCRIPTS['v2_02_mochizuki'] = {'title': 'Mochizuki v2', 'style': 'v2', 'led': "YU'S PICK · SUEHIROCHO 末広町", 'scenes': [
  {'say': "My go-to curry near {Akihabara|ɑkihɑbɑɾɑ} has just sixteen seats, one minute from {Suehirocho|suɛhiɾoʊtʃoʊ} Station.",
   'v2': {'kind': 'photo', 'bg': None, 'pic': ('curry_rice_1', (0.3, 0.45, 1.0, 1.0)), 'kicker': "YU'S PICK", 'big': '16 seats.\nCurry under ¥1,000', 'sub': 'Mochizuki Curry モチヅキカレー'}},
  {'say': "Order the chicken curry. Lunch is under a thousand yen.",
   'v2': {'kind': 'photo', 'bg': None, 'pic': ('curry_rice_1', (0.35, 0.5, 0.95, 1.0)), 'kicker': 'ORDER', 'big': 'Chicken curry', 'sub': 'Lunch under ¥1,000'}},
  {'say': "Bring cash. Card payment isn't listed.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'BEFORE YOU GO', 'big': 'Bring cash', 'sub': 'Cards not listed · 16 seats, no booking needed', 'koru': 'Cash is safest!', 'stamp': 'CASH'}},
  {'say': "It's closed on Sundays and public holidays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'CLOSED', 'big': 'Sundays &\nholidays', 'sub': '9 min walk from JR Akihabara', 'koru': 'Plan a weekday\nor Saturday!', 'stamp': 'NO SUNDAYS'}},
  {'say': "Want a bigger plate? Say {ōmori de|oʊmˈoɾi dɛ}.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAY THIS', 'big': '大盛りで', 'sub': 'oomori de · large portion, please', 'koru': 'Tap it in my app\nto hear it!'}},
  {'say': "Hours, closed days, and what to say are in my free app. Link in bio. Send this to your curry friend.",
   'v2': {'kind': 'screen', 'clip': 'shop_mochizuki-curry', 'title': 'Hours · closed days · what to say\nFree app, link in bio'}},
]}

SCRIPTS['v2_03_ethiopia'] = {'title': 'Ethiopia v2', 'style': 'v2', 'led': "JIMBOCHO CURRY · 神保町", 'scenes': [
  {'say': "This {Jinbōchō|dʒinboʊtʃˈoʊ} curry lets you pick your spice level, from zero all the way up to seventy times.",
   'v2': {'kind': 'photo', 'bg': None, 'pic': ('curry_rice_1', (0.3, 0.45, 1.0, 1.0)), 'kicker': 'SPICE LEVEL', 'big': 'Spice level\n0 to 70x', 'sub': 'Ethiopia エチオピア · Jimbocho'}},
  {'say': "Order the chicken or beef curry. The roux uses twelve spices, and lunch is under a thousand yen.",
   'v2': {'kind': 'photo', 'bg': None, 'pic': ('curry_rice_1', (0.35, 0.5, 0.95, 1.0)), 'kicker': 'ORDER', 'big': 'Chicken or beef', 'sub': '12-spice roux · lunch under ¥1,000'}},
  {'say': "It's open every day, even Sundays. But it's cash only.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'BEFORE YOU GO', 'big': 'Open every day', 'sub': 'Cash only · 3 min from Jimbocho Exit A5', 'koru': 'Bring cash!', 'stamp': 'CASH ONLY'}},
  {'say': "Not sure how hot to go? Ask, {osusume wa nan desu ka|oʊsusumɛ wɑ nɑn dɛs kɑ}. What do you recommend?",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAY THIS', 'big': 'おすすめは\n何ですか？', 'sub': 'osusume wa nan desu ka · what do you recommend?', 'koru': 'Start low.\nTrust me!'}},
  {'say': "Hours, closed days, and what to say are in my free app. Link in bio. Send this to your spicy food friend.",
   'v2': {'kind': 'screen', 'clip': 'shop_curry-rice-specialty-shop-ethiopia', 'title': 'Hours · closed days · what to say\nFree app, link in bio'}},
]}

SCRIPTS['v2_04_jimbo4'] = {'title': 'Jimbocho 4 under 1000', 'style': 'v2', 'led': "SAVE THIS · 神保町カレー", 'scenes': [
  {'say': "Four curries in {Jinbōchō|dʒinboʊtʃˈoʊ} for under a thousand yen. Save this for your Tokyo trip.",
   'v2': {'kind': 'photo', 'bg': None, 'pic': ('curry_rice_1', (0.0, 0.0, 1.0, 1.0)), 'kicker': 'SAVE THIS', 'big': '4 curries\nunder ¥1,000', 'sub': 'Jimbocho, the curry town of Tokyo'}},
  {'say': "One. Ethiopia. Pick your spice level, from zero to seventy times. Open every day.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '1 / 4', 'big': 'Ethiopia', 'sub': 'Spice level 0-70x · open daily · cash only', 'koru': 'Start low!'}},
  {'say': "Two. Kitchen {Nankai|nɑnkɑi}. Get the katsu curry, and go early. It closes when it sells out.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '2 / 4', 'big': 'Kitchen Nankai', 'sub': 'Katsu curry · closes when sold out', 'koru': 'Go early!'}},
  {'say': "Three. {Manten|mɑntɛn}. Fourteen counter seats since 1981. Try the katsu curry or the jumbo curry.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '3 / 4', 'big': 'Manten', 'sub': 'Katsu or jumbo curry · 14 seats · cash only'}},
  {'say': "Four. {Sendai|sɛndɑi}. Beef tongue curry for about eight hundred fifty yen. Cash only.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '4 / 4', 'big': 'Sendai', 'sub': 'Beef tongue curry ~¥850 · cash only', 'koru': 'Closed Sundays!'}},
  {'say': "Most are closed on Sundays, so check my free app for hours. Link in bio.",
   'v2': {'kind': 'screen', 'clip': 'hub', 'title': 'Check hours & closed days\nFree app, link in bio'}},
]}

SCRIPTS['v2_05_sendai'] = {'title': 'Sendai v2', 'style': 'v2', 'led': "JIMBOCHO CURRY · 神保町", 'scenes': [
  {'say': "Beef tongue curry for about eight hundred fifty yen, in {Jinbōchō|dʒinboʊtʃˈoʊ}.",
   'v2': {'kind': 'photo', 'bg': None, 'pic': ('curry_rice_1', (0.3, 0.45, 1.0, 1.0)), 'kicker': 'CHEAP EATS', 'big': 'Beef tongue curry\n~¥850', 'sub': 'Sendai 仙臺 · Jimbocho'}},
  {'say': "Want it bigger? A large is about eleven fifty. On a budget? Pork curry is about six hundred.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'ORDER', 'big': 'Large ~¥1,150\nPork ~¥600', 'sub': 'Prices from public sources, check on the day', 'koru': 'Pork curry\nfor ¥600!'}},
  {'say': "It's cash only, and closed on Sundays. On Saturdays it's lunch only.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'BEFORE YOU GO', 'big': 'Cash only', 'sub': 'Closed Sun · Sat 11:00-15:00 only', 'stamp': 'NO SUNDAYS', 'koru': 'Bring yen!'}},
  {'say': "When you're done, say {gochisōsama deshita|ɡoʊtʃisoʊsɑmɑ dɛʃitɑ}. Thanks for the meal.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAY THIS', 'big': 'ごちそうさま\nでした', 'sub': 'gochisosama deshita · thanks for the meal', 'koru': 'Staff will smile!'}},
  {'say': "Hours, closed days, and what to say are in my free app. Link in bio. Send this to your curry friend.",
   'v2': {'kind': 'screen', 'clip': 'shop_sendai', 'title': 'Hours · closed days · what to say\nFree app, link in bio'}},
]}

SCRIPTS['v2_06_tamazen'] = {'title': 'Tamazen v2', 'style': 'v2', 'led': "YU'S PICK · YUSHIMA 湯島", 'scenes': [
  {'say': "I had the oyster hot pot at this izakaya in {Yushima|juːʃˈimɑ}, and honestly, it blew me away.",
   'v2': {'kind': 'photo', 'bg': None, 'pic': ('tokyo_alley_restaurant_1', (0.0, 0.25, 1.0, 0.8)), 'pictag': 'Photo: not this shop', 'kicker': "YU'S PICK", 'big': 'This oyster hot pot\nblew me away', 'sub': 'Tamazen 玉善 · Yushima izakaya'}},
  {'say': "They buy fish at the market every day, so ask what's fresh today, and if the oyster hot pot is on.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'ORDER', 'big': 'Oyster hot pot\n+ today\'s fish', 'sub': 'Fish from the market every day', 'koru': 'Ask if the\noysters are on!'}},
  {'say': "It's dinner only, from five, and closed on Sundays and holidays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'BEFORE YOU GO', 'big': 'Dinner only', 'sub': 'Mon-Sat 17:00-22:00 · closed Sun & holidays', 'stamp': 'NO SUNDAYS'}},
  {'say': "No credit cards, so bring cash. Plan on about four to six thousand yen.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'PAY', 'big': 'Bring cash', 'sub': 'No cards · PayPay OK · about ¥4,000-6,000', 'koru': 'Cash is easiest!', 'stamp': 'NO CARDS'}},
  {'say': "Start with, {nama bīru kudasai|nɑmɑ biːɾu kudɑsɑi}. A draft beer, please.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAY THIS', 'big': '生ビール\nください', 'sub': 'nama biiru kudasai · a draft beer, please', 'koru': 'Kanpai!'}},
  {'say': "Hours, closed days, and what to say are in my free app. Link in bio. Send this to your oyster friend.",
   'v2': {'kind': 'screen', 'clip': 'shop_tamazen', 'title': 'Hours · closed days · what to say\nFree app, link in bio'}},
]}

# ---- Experiment 1, day A (11/3): practical hacks ----
_F = "Follow for a new Tokyo hack every day. My free app is in my bio."
SCRIPTS['h_01_sunday'] = {'title': 'Sunday trap', 'style': 'v2', 'led': "TOKYO HACKS #1 · 東京ハック", 'scenes': [
  {'say': "I checked two hundred ninety-nine restaurants in east Tokyo. One in three is closed on Sundays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'TOKYO HACKS #1', 'big': '1 in 3 close\non Sundays', 'sub': '94 of the 299 places I checked', 'stamp': 'CLOSED SUN'}},
  {'say': "So if your food day falls on a Sunday, half your list can be shut.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'THE TRAP', 'big': 'Sunday =\nshutters down', 'sub': 'Small family shops rest on Sundays', 'koru': 'Been there.\nSo sad!'}},
  {'say': "Fix it. Plan your Sunday around places that are open every day, and keep the small shops for weekdays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'DO THIS', 'big': 'Sunday: open-daily\nspots only', 'sub': 'Save the tiny shops for weekdays'}},
  {'say': "In my free app, set Open on Sunday, and you get only the places that are open. " + _F,
   'v2': {'kind': 'screen', 'clip': 'search_0_all', 'title': '"Open on Sunday" filter: 205 places\nFollow for daily Tokyo hacks'}},
]}
SCRIPTS['h_02_holiday'] = {'title': 'Holiday trap', 'style': 'v2', 'led': "TOKYO HACKS #2 · 東京ハック", 'scenes': [
  {'say': "November third and November twenty-third are public holidays in Japan. Check your food list.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'TOKYO HACKS #2', 'big': 'Nov 3 & Nov 23\nare holidays', 'sub': 'National holidays in Japan', 'stamp': 'HOLIDAY'}},
  {'say': "Of the two hundred ninety-nine places I checked, eighty-six close on public holidays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'THE TRAP', 'big': '86 of 299\nclose on holidays', 'sub': 'Even if they open on weekdays', 'koru': 'Not just\nSundays!'}},
  {'say': "Look for, closed on public holidays, on the shop page, and have a backup nearby.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'DO THIS', 'big': 'Check "holidays"\n+ have a backup', 'sub': 'Hours change, check Google Maps that morning'}},
  {'say': "Every shop page in my free app shows closed days. " + _F,
   'v2': {'kind': 'screen', 'clip': 'shop_mochizuki-curry', 'title': 'Closed days on every shop page\nFollow for daily Tokyo hacks'}},
]}
SCRIPTS['h_03_cash'] = {'title': 'Cash hack', 'style': 'v2', 'led': "TOKYO HACKS #3 · 東京ハック", 'scenes': [
  {'say': "About four in ten of the places I checked in east Tokyo are cash only, or tell you to bring cash.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'TOKYO HACKS #3', 'big': '4 in 10:\nbring cash', 'sub': 'From the 299 places I checked', 'stamp': 'CASH ONLY'}},
  {'say': "The cheap, old, tiny places are the ones most likely to be cash only.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'THE TRAP', 'big': 'Cheap + tiny\n= often cash', 'sub': 'The places you came for', 'koru': 'Card declined?\nNope, no card!'}},
  {'say': "Take out yen at a convenience store ATM before lunch, and keep coins for ticket machines.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'DO THIS', 'big': 'Get yen first,\nkeep coins', 'sub': 'Convenience store ATMs are everywhere'}},
  {'say': "In my free app, search cash, to see which places want it. " + _F,
   'v2': {'kind': 'screen', 'clip': 'search_any_cash', 'title': 'Search "cash" in the free app\nFollow for daily Tokyo hacks'}},
]}
SCRIPTS['h_04_sumimasen'] = {'title': 'Sumimasen', 'style': 'v2', 'led': "TOKYO HACKS #4 · 東京ハック", 'scenes': [
  {'say': "Waiting for the server to come to your table in Tokyo? They might not. Here's what to do.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'TOKYO HACKS #4', 'big': "Staff won't\ncome to you?", 'sub': 'Do this instead'}},
  {'say': "Raise your hand and say, {sumimasen|sumimɑsɛn}. Out loud. It's normal here, not rude.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAY THIS', 'big': 'すみません！', 'sub': 'sumimasen · excuse me!', 'koru': 'Hand up,\nsay it loud!'}},
  {'say': "Some places have a call button on the table instead. Press it, and someone comes.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'OR', 'big': 'Call button\non the table', 'sub': 'Press it, staff will come'}},
  {'say': "Thirty restaurant phrases with sound are in my free app. " + _F,
   'v2': {'kind': 'screen', 'clip': 'phr', 'title': '30 phrases with sound: free app\nFollow for daily Tokyo hacks'}},
]}
SCRIPTS['h_05_notip'] = {'title': 'No tipping', 'style': 'v2', 'led': "TOKYO HACKS #5 · 東京ハック", 'scenes': [
  {'say': "Don't tip in Japan. Leave money on the table, and staff may run after you to give it back.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'TOKYO HACKS #5', 'big': "Don't tip\nin Japan", 'sub': 'Leftover money gets returned', 'stamp': 'NO TIPS'}},
  {'say': "Want to say thanks? Say it instead. {gochisōsama deshita|ɡoʊtʃisoʊsɑmɑ dɛʃitɑ}. Thank you for the meal.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAY THIS', 'big': 'ごちそうさま\nでした', 'sub': 'gochisosama deshita · thanks for the meal', 'koru': 'Better than\na tip!'}},
  {'say': "Say it when you pay or leave. Small shops love it.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'WHEN', 'big': 'When you pay\nor leave', 'sub': 'The cook will often say thank you back'}},
  {'say': "More phrases like this are in my free app. " + _F,
   'v2': {'kind': 'screen', 'clip': 'phr', 'title': 'Restaurant Japanese: free app\nFollow for daily Tokyo hacks'}},
]}
SCRIPTS['h_06_lunchonly'] = {'title': 'Lunch only', 'style': 'v2', 'led': "TOKYO HACKS #6 · 東京ハック", 'scenes': [
  {'say': "Some of Tokyo's best cheap spots don't do dinner. Forty-two of the places I checked are lunch only.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'TOKYO HACKS #6', 'big': 'Best cheap spots\nclose before dinner', 'sub': '42 of 299 are lunch only', 'stamp': 'LUNCH ONLY'}},
  {'say': "Office worker tip. Make lunch your big meal. More than half the places I checked are under fifteen hundred yen.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'DO THIS', 'big': 'Lunch = your\nbig meal', 'sub': '173 of 299 are under ¥1,500', 'koru': 'Yu eats like\nthis daily!'}},
  {'say': "And go before noon, or after one. That's when office workers like me aren't in line.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'TIMING', 'big': 'Before 12\nor after 1pm', 'sub': 'Skip the office lunch rush'}},
  {'say': "My free app plans lunch, a sweet stop, and dinner, so you don't miss the lunch-only gems. " + _F,
   'v2': {'kind': 'screen', 'clip': 'plan', 'title': 'Lunch · sweets · dinner planned\nFollow for daily Tokyo hacks'}},
]}

# ---- Experiment 1, day B (11/3): shop features ----
_S = "Hours, closed days and what to say are in my free app. " + _F
SCRIPTS['b_01_shoryu'] = {'title': 'Shoryu', 'style': 'v2', 'led': "TOKYO EATS · UENO 上野", 'scenes': [
  {'say': "Jumbo gyoza, six for about eight hundred yen, by the {Ameyoko|ɑmɛjoʊkoʊ} train tracks in {Ueno|uɛnoʊ}.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'TOKYO EATS', 'big': 'Jumbo gyoza\n6 for ~¥800', 'sub': 'Shoryu 昇龍 · Ueno, by the Ameyoko tracks', 'stamp': 'JUMBO'}},
  {'say': "Order the jumbo gyoza and fried rice. The gyoza are dine-in only.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'ORDER', 'big': 'Jumbo gyoza\n+ fried rice', 'sub': 'Gyoza are dine-in only', 'koru': 'One plate\nis plenty!'}},
  {'say': "It's cash only, no reservations, and closed on Mondays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'BEFORE YOU GO', 'big': 'Cash only', 'sub': 'No reservations · closed Mondays', 'stamp': 'NO MONDAYS'}},
  {'say': "When you're done, say, {okaikei onegaishimasu|oʊkɑikɛi oʊnɛɡɑiʃimɑs}. The check, please.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAY THIS', 'big': 'お会計\nお願いします', 'sub': 'okaikei onegaishimasu · the check, please', 'koru': 'Pay at the\nregister!'}},
  {'say': _S, 'v2': {'kind': 'screen', 'clip': 'shop_shoryu', 'title': 'Hours · closed days · what to say\nFollow for daily Tokyo hacks'}},
]}
SCRIPTS['b_02_aun'] = {'title': 'A-un dandan', 'style': 'v2', 'led': "YU'S PICK · YUSHIMA 湯島", 'scenes': [
  {'say': "At this dandan noodle shop in {Yushima|juːʃˈimɑ}, you pick the chili heat and the numbness, separately, from zero to six.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': "YU'S PICK", 'big': 'Pick your heat\nAND numbness', 'sub': 'A-un 阿吽 · Szechuan dandan noodles', 'stamp': '0 - 6'}},
  {'say': "Order the soupless dandan noodles. The black sesame one is about twelve hundred yen.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'ORDER', 'big': 'Soupless\ndandan noodles', 'sub': 'Black sesame ~¥1,200', 'koru': 'Start at 2.\nTrust me!'}},
  {'say': "It's closed on Tuesdays, and it may close early when it sells out.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'BEFORE YOU GO', 'big': 'Closed Tuesdays', 'sub': 'May close early if sold out · 2 min from Yushima Exit 5', 'stamp': 'NO TUESDAYS'}},
  {'say': "Not sure what to get? Ask, {osusume wa nan desu ka|oʊsusumɛ wɑ nɑn dɛs kɑ}.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAY THIS', 'big': 'おすすめは\n何ですか？', 'sub': 'osusume wa nan desu ka · what do you recommend?'}},
  {'say': _S, 'v2': {'kind': 'screen', 'clip': 'shop_szechuan-dandan-noodles-a-un', 'title': 'Hours · closed days · what to say\nFollow for daily Tokyo hacks'}},
]}
SCRIPTS['b_03_pelican'] = {'title': 'Pelican', 'style': 'v2', 'led': "TOKYO EATS · ASAKUSA 浅草", 'scenes': [
  {'say': "This {Asakusa|ɑsɑkusɑ} bakery makes only two kinds of bread, and it still sells out.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'TOKYO EATS', 'big': 'Only 2 breads.\nStill sells out.', 'sub': 'Pelican パンのペリカン · Tawaramachi', 'stamp': 'SOLD OUT'}},
  {'say': "The sandwich loaf, and rolls. That's it. It's on Tabelog's top bakery list six times.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'ORDER', 'big': 'Shokupan loaf\nor rolls', 'sub': "On Tabelog's top 100 bakeries 6 times", 'koru': 'Toast it\nat the hotel!'}},
  {'say': "Reserve online before you go. It's takeout only, cash only, and closed on Sundays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'BEFORE YOU GO', 'big': 'Reserve online', 'sub': 'Takeout only · cash only · closed Sundays', 'stamp': 'CASH ONLY'}},
  {'say': "When you pick it up, say, {yoyaku shimashita|joʊjɑku ʃimɑʃitɑ}. I have a reservation.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAY THIS', 'big': '予約しました', 'sub': 'yoyaku shimashita · I have a reservation'}},
  {'say': _S, 'v2': {'kind': 'screen', 'clip': 'shop_pelican', 'title': 'Hours · closed days · what to say\nFollow for daily Tokyo hacks'}},
]}
SCRIPTS['b_04_kandagawa'] = {'title': 'Kandagawa unagi', 'style': 'v2', 'led': "SPLURGE · SUEHIROCHO 末広町", 'scenes': [
  {'say': "One splurge near {Akihabara|ɑkihɑbɑɾɑ}. Grilled eel at {Kandagawa|kɑndɑɡɑwɑ}, on Tabelog's top eel list five times.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SPLURGE', 'big': 'Grilled eel,\n5x top 100', 'sub': 'Myojinshita Kandagawa 神田川 · Suehirocho', 'stamp': 'TREAT'}},
  {'say': "Order the eel over rice, {unajū|unɑdʒuː}. Lunch is about six to eight thousand yen.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'ORDER', 'big': 'Unaju', 'sub': 'Eel over rice · lunch ~¥6,000-8,000', 'koru': 'Save up\nfor this one!'}},
  {'say': "Book ahead. It's closed on Sundays and Mondays. Visa and Mastercard are accepted.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'BEFORE YOU GO', 'big': 'Book ahead', 'sub': 'Closed Sun & Mon · Visa / Mastercard OK', 'stamp': 'NO SUN·MON'}},
  {'say': "After the meal, say, {gochisōsama deshita|ɡoʊtʃisoʊsɑmɑ dɛʃitɑ}.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAY THIS', 'big': 'ごちそうさま\nでした', 'sub': 'gochisosama deshita · thanks for the meal'}},
  {'say': _S, 'v2': {'kind': 'screen', 'clip': 'shop_myojinshita-kandagawa-honten', 'title': 'Hours · closed days · what to say\nFollow for daily Tokyo hacks'}},
]}

# ---- Experiment 1, day C (11/4): saveable roundups ----
_R = "Save this, and check hours in my free app. " + _F
SCRIPTS['c_01_kissaten'] = {'title': 'Jimbocho kissaten', 'style': 'v2', 'led': "SAVE THIS · 神保町喫茶", 'scenes': [
  {'say': "Four old-school coffee houses in {Jinbōchō|dʒinboʊtʃˈoʊ}, the book town. Save this.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAVE THIS', 'big': '4 retro coffee\nhouses', 'sub': 'Jimbocho & Kanda · kissaten 喫茶店'}},
  {'say': "One. Cafe Trois Bagues. A basement cafe since 1976. Get the house blend or coffee jelly. Closed Sundays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '1 / 4', 'big': 'Trois Bagues', 'sub': 'Since 1976 · blend or coffee jelly ¥650 · closed Sun'}},
  {'say': "Two. {Kura|kuɾɑ}. Blend coffee and the tart of the day. Cash only, and smoking is allowed at all seats.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '2 / 4', 'big': 'Coffee-sha Kura', 'sub': 'Blend + tart of the day · cash only · smoking OK', 'koru': 'Heads up:\nsmoking!'}},
  {'say': "Three. {Kanda Brazil|kɑndɑ bɾɑziɾu}. Under a bookshop since 1972, and open every day.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '3 / 4', 'big': 'Sabo Kanda Brazil', 'sub': 'Since 1972 · open daily · rare cheesecake'}},
  {'say': "Four. {Takayama|tɑkɑjɑmɑ} Coffee in {Kanda|kɑndɑ}. Cinnamon toast. But it's only open Monday to Thursday.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '4 / 4', 'big': 'Takayama Coffee', 'sub': 'Cinnamon toast · Mon-Thu only · cash only', 'stamp': 'MON-THU'}},
  {'say': _R, 'v2': {'kind': 'screen', 'clip': 'search_any_kissaten', 'title': 'Search "kissaten" in the free app\nFollow for daily Tokyo hacks'}},
]}
SCRIPTS['c_02_asakusa_sweets'] = {'title': 'Asakusa sweets', 'style': 'v2', 'led': "SAVE THIS · 浅草甘味", 'scenes': [
  {'say': "Four {Asakusa|ɑsɑkusɑ} sweets, all under a thousand yen. Save this for your temple day.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAVE THIS', 'big': '4 Asakusa sweets\nunder ¥1,000', 'sub': 'Near Senso-ji'}},
  {'say': "One. Hand-grilled rice crackers at {Ichibanya|itʃibɑnjɑ}, from eighty yen.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '1 / 4', 'big': 'Ichibanya senbei', 'sub': 'Charcoal-grilled · from ¥80 · open daily'}},
  {'say': "Two. Fried bean buns at {Kokonoe|koʊkoʊnɛ}, from a hundred sixty yen. Get the smooth red bean.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '2 / 4', 'big': 'Kokonoe age-manju', 'sub': 'From ¥160 · open daily · no cards (PayPay OK)'}},
  {'say': "Three. Matcha gelato at {Suzukien|suzukiɛn}, in strengths up to number seven, the strongest.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '3 / 4', 'big': 'Matcha gelato No.7', 'sub': 'Suzukien · the strongest level', 'koru': 'Try No.7.\nIf you dare!'}},
  {'say': "Four. {Mamekan|mɑmɛkɑn} at {Umemura|umɛmuɾɑ}, beans and agar jelly with syrup. Cash only, closed Sundays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '4 / 4', 'big': 'Umemura mamekan', 'sub': 'Cash only · closed Sundays', 'stamp': 'NO SUNDAYS'}},
  {'say': _R, 'v2': {'kind': 'screen', 'clip': 'hub', 'title': 'Hours for every stop: free app\nFollow for daily Tokyo hacks'}},
]}
SCRIPTS['c_03_ueno_1000'] = {'title': 'Ueno under 1000', 'style': 'v2', 'led': "SAVE THIS · 上野¥1,000以下", 'scenes': [
  {'say': "Four places to eat in {Ueno|uɛnoʊ} for under a thousand yen. Save this.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAVE THIS', 'big': 'Ueno under\n¥1,000', 'sub': 'Ameyoko & Okachimachi'}},
  {'say': "One. A seafood bowl at {Minatoya|minɑtoʊjɑ} in {Ameyoko|ɑmɛjoʊkoʊ}. The tokumori bowl is seven fifty.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '1 / 4', 'big': 'Minatoya ¥750 bowl', 'sub': 'Tuna, salmon, squid, salmon roe · open daily'}},
  {'say': "Two. Fruit on a stick at {Hyakkaen|hjɑkkɑɛn}. Pineapple for two hundred yen.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '2 / 4', 'big': 'Fruit stick ¥200', 'sub': 'Hyakkaen · classic Ameyoko snack', 'koru': 'Walk and eat!'}},
  {'say': "Three. {Tanmen|tɑnmɛn}, vegetable noodle soup, at {Chinchinken|tʃintʃinkɛn}. Most dishes five hundred to nine hundred. Cash only.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '3 / 4', 'big': 'Chinchinken tanmen', 'sub': 'Most dishes ¥500-900 · cash · closed Mon'}},
  {'say': "Four. South Indian dosa at Andhra Kitchen. It's won eight Tabelog awards.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '4 / 4', 'big': 'Andhra Kitchen', 'sub': 'Dosa or thali · 8 Tabelog awards · cards OK'}},
  {'say': _R, 'v2': {'kind': 'screen', 'clip': 'hub', 'title': 'Hours for every stop: free app\nFollow for daily Tokyo hacks'}},
]}
SCRIPTS['c_04_akiba_sunday'] = {'title': 'Akiba Sunday ramen', 'style': 'v2', 'led': "SAVE THIS · 秋葉原ラーメン", 'scenes': [
  {'say': "Sunday in {Akihabara|ɑkihɑbɑɾɑ}? Four ramen shops that are open every day. Save this.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAVE THIS', 'big': 'Open on Sunday:\n4 ramen spots', 'sub': 'Akihabara & Suehirocho', 'stamp': 'OPEN DAILY'}},
  {'say': "One. Tanaka Soba-ten. Clear pork-bone soy broth, under a thousand yen. No cards.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '1 / 4', 'big': 'Tanaka Soba-ten', 'sub': 'Chuka soba · under ¥1,000 · no cards'}},
  {'say': "Two. {Tsujita|tsudʒitɑ} in {Suehirocho|suɛhiɾoʊtʃoʊ}. Rich dipping noodles from eleven ten.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '2 / 4', 'big': 'Tsujita tsukemen', 'sub': 'Rich tsukemen from ¥1,110 · 18 seats'}},
  {'say': "Three. Menya {Noroshi|noɾoʊʃi}. Hakodate-style miso ramen, about eleven seventy.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '3 / 4', 'big': 'Menya Noroshi', 'sub': 'Hakodate miso ~¥1,170 · PayPay OK'}},
  {'say': "Four. {Ifu|ifu}. Miso ramen, open twenty-four hours, one minute from the station.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '4 / 4', 'big': 'Ifu, open 24h', 'sub': 'Rich miso ramen · under ¥1,000', 'koru': 'Midnight\nramen!'}},
  {'say': _R, 'v2': {'kind': 'screen', 'clip': 'search_0_ramen', 'title': '"Open on Sunday" + ramen: free app\nFollow for daily Tokyo hacks'}},
]}
SCRIPTS['c_05_ueno_sweets'] = {'title': 'Ueno sweets', 'style': 'v2', 'led': "SAVE THIS · 上野・湯島 甘味", 'scenes': [
  {'say': "Four Japanese sweet stops near {Ueno|uɛnoʊ} and {Yushima|juːʃˈimɑ}. Save this.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAVE THIS', 'big': '4 Japanese\nsweet stops', 'sub': 'Ueno · Yushima · Kanda'}},
  {'say': "One. {Anmitsu|ɑnmitsu} at {Mihashi|mihɑʃi}. Cream anmitsu, seven sixty. Seventy seats, open almost every day.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '1 / 4', 'big': 'Mihashi anmitsu', 'sub': 'Cream anmitsu ¥760 · 70 seats'}},
  {'say': "Two. Bean {daifuku|dɑifuku} at {Tsuruse|tsuɾusɛ}, with a tea room. Closed Mondays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '2 / 4', 'big': 'Tsuruse daifuku', 'sub': 'Mame daifuku · tea room · closed Mon'}},
  {'say': "Three. {Amazake|ɑmɑzɑkɛ} at {Amanoya|ɑmɑnoʊjɑ}, by the gate of {Kanda Myōjin|kɑndɑ mjoʊdʒin}. Founded in 1846.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '3 / 4', 'big': 'Amanoya amazake', 'sub': 'Since 1846 · by Kanda Myojin · closed Tue', 'koru': 'Warm and\nsweet!'}},
  {'say': "Four. Shaved ice or a kinako parfait at {Kuriya Kuroki|kuɾijɑ kuɾoʊki} in {Ueno|uɛnoʊ}. Cards OK.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '4 / 4', 'big': 'Kuriya Kuroki', 'sub': 'Kakigori · kinako parfait · ~¥2,000-3,000'}},
  {'say': _R, 'v2': {'kind': 'screen', 'clip': 'hub', 'title': 'Hours for every stop: free app\nFollow for daily Tokyo hacks'}},
]}
SCRIPTS['c_06_cash_free'] = {'title': 'Cards OK', 'style': 'v2', 'led': "SAVE THIS · カードOK", 'scenes': [
  {'say': "Out of cash in east Tokyo? Four good spots that take cards. Save this.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAVE THIS', 'big': 'Out of cash?\n4 spots, cards OK', 'sub': 'From the 299 places I checked', 'stamp': 'CARDS OK'}},
  {'say': "One. Andhra Kitchen near {Okachimachi|oʊkɑtʃimɑtʃi}. Visa, J C B and Amex. Dosa under a thousand yen.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '1 / 4', 'big': 'Andhra Kitchen', 'sub': 'Visa / JCB / Amex · under ¥1,000'}},
  {'say': "Two. {Suzukien|suzukiɛn} matcha gelato in {Asakusa|ɑsɑkusɑ}. Cards, e-money and QR.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '2 / 4', 'big': 'Suzukien', 'sub': 'Matcha gelato · cards, e-money, QR'}},
  {'say': "Three. {Tsuruse|tsuɾusɛ} in {Yushima|juːʃˈimɑ}. Cards and PayPay, but not transit cards.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '3 / 4', 'big': 'Tsuruse', 'sub': 'Daifuku · cards & PayPay · no IC cards', 'koru': 'Suica won\'t\nwork here!'}},
  {'say': "Four. Eel at {Kandagawa|kɑndɑɡɑwɑ}. Visa and Mastercard, for your big splurge.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '4 / 4', 'big': 'Kandagawa unagi', 'sub': 'Visa / Mastercard · book ahead'}},
  {'say': _R, 'v2': {'kind': 'screen', 'clip': 'hub', 'title': 'Payment notes on every shop page\nFollow for daily Tokyo hacks'}},
]}

# ---- 11/2 Yu: never "use my app"; lead with what the viewer gets ----
_F = "Follow for one Tokyo tip a day, and your trip just works."
_S = "Want to know what's open before you walk there? Hours and closed days are free in my bio. " + _F
_R = "Save this, and check what's open before you go. It's free in my bio. " + _F

# ---- Experiment 1, round 2 (11/5 A, 11/6 B, 11/7 C) — benefit-first endings ----
_T2 = '\nFollow for one Tokyo tip a day'
def _end(q): return "Want to know " + q + " before you go? It's free in my bio. " + _F
SCRIPTS['h_07_lastorder'] = {'title': 'Last order', 'style': 'v2', 'led': "TOKYO HACKS #7 · 東京ハック", 'scenes': [
  {'say': "Tokyo restaurants stop taking orders before they close. A hundred and eight of the places I checked list a last order time.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'TOKYO HACKS #7', 'big': 'Closing time\nis not last order', 'sub': '108 of the 299 places I checked list one', 'stamp': 'L.O.'}},
  {'say': "It's usually thirty minutes to an hour before closing. Walk in later, and the kitchen may be done.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'THE TRAP', 'big': '30-60 min\nbefore closing', 'sub': 'L.O. = last order ラストオーダー', 'koru': 'Arrived late?\nKitchen closed!'}},
  {'say': "Not sure? Ask at the door. {mada daijōbu desu ka|mɑdɑ dɑidʒoʊbu dɛs kɑ}. Is it still OK?",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAY THIS', 'big': 'まだ大丈夫\nですか？', 'sub': 'mada daijobu desu ka · is it still OK?'}},
  {'say': _end("the last order time"),
   'v2': {'kind': 'screen', 'clip': 'shop_shinpuku-saikan-akihabara', 'title': 'Last order on the shop page' + _T2}},
]}
SCRIPTS['h_08_break'] = {'title': '3pm trap', 'style': 'v2', 'led': "TOKYO HACKS #8 · 東京ハック", 'scenes': [
  {'say': "The three p.m. trap. Ninety-two of the places I checked close between lunch and dinner.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'TOKYO HACKS #8', 'big': 'The 3pm trap', 'sub': '92 of 299 close between lunch & dinner', 'stamp': 'CLOSED'}},
  {'say': "The most common break is three to five p.m. Show up at four, and the door is locked.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'THE TRAP', 'big': 'Most common:\n3pm - 5pm', 'sub': 'Lunch ends 2-3pm, dinner starts 5-6pm', 'koru': 'Locked door\nat 4pm!'}},
  {'say': "Use the gap for coffee, sweets, or a temple, and eat your big meal before or after.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'DO THIS', 'big': '3-5pm =\ncoffee & sweets', 'sub': 'Big meal before 2pm or after 5pm'}},
  {'say': "Want lunch, a sweet stop and dinner lined up so nothing's closed? It's free in my bio. " + _F,
   'v2': {'kind': 'screen', 'clip': 'plan', 'title': 'Lunch · sweets · dinner, all open' + _T2}},
]}
SCRIPTS['h_09_soldout'] = {'title': 'Sold out', 'style': 'v2', 'led': "TOKYO HACKS #9 · 東京ハック", 'scenes': [
  {'say': "Some Tokyo shops don't really have a closing time. They close when the food runs out.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'TOKYO HACKS #9', 'big': 'Closes when\nsold out', 'sub': '16 of the places I checked do this', 'stamp': 'SOLD OUT'}},
  {'say': "Think bakeries, soba shops, and small noodle counters. They make a set amount each day.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'WHO', 'big': 'Bakeries, soba,\nsmall noodle shops', 'sub': 'They make a set amount each day', 'koru': 'Go early,\neat happy!'}},
  {'say': "Go soon after they open. And if the sign says {urikire|uɾikiɾɛ}, it means sold out.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'READ THIS', 'big': '売り切れ', 'sub': 'urikire · sold out'}},
  {'say': _end("which places sell out"),
   'v2': {'kind': 'screen', 'clip': 'search_any_soldout', 'title': 'Sell-out spots, flagged' + _T2}},
]}
SCRIPTS['h_10_smoking'] = {'title': 'Smoking', 'style': 'v2', 'led': "TOKYO HACKS #10 · 東京ハック", 'scenes': [
  {'say': "Heads up if you hate smoke. Ten of the places I checked still let people smoke inside.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'TOKYO HACKS #10', 'big': 'Smoking\ninside?', 'sub': '10 of 299 allow it somewhere inside', 'stamp': 'SMOKING'}},
  {'say': "Most of them are old-school coffee houses, called {kissaten|kissɑtɛn}.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'WHERE', 'big': 'Mostly retro\ncoffee houses', 'sub': '7 of the 10 are kissaten 喫茶店', 'koru': 'Retro vibes,\nsmoky air!'}},
  {'say': "Some have a smoke-free floor. Ask, {kin'en seki arimasu ka|kinʔɛn sɛki ɑɾimɑs kɑ}. Any non-smoking seats?",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAY THIS', 'big': '禁煙席\nありますか？', 'sub': 'kin-en seki arimasu ka · non-smoking seats?'}},
  {'say': _end("about smoking"),
   'v2': {'kind': 'screen', 'clip': 'search_any_smoking', 'title': 'Smoking rules, before you walk in' + _T2}},
]}
SCRIPTS['h_11_otoshi'] = {'title': 'Otoshi', 'style': 'v2', 'led': "TOKYO HACKS #11 · 東京ハック", 'scenes': [
  {'say': "At a Japanese {izakaya|izɑkɑjɑ}, a small dish may arrive that you didn't order. It's not free.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'TOKYO HACKS #11', 'big': "A dish you\ndidn't order?", 'sub': 'At many izakaya (Japanese pubs)', 'stamp': 'OTOSHI'}},
  {'say': "It's called {otōshi|oʊtoʊʃi}. A table charge that comes as a snack. Normal, not a scam.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'WHAT IT IS', 'big': 'お通し', 'sub': 'otoshi · a table charge served as a snack', 'koru': 'Not a scam,\njust a snack!'}},
  {'say': "Some places also add a service charge at night. Check the menu, or ask before you sit down.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'ALSO', 'big': 'Night = maybe\nservice charge', 'sub': 'One Kanda soba bar adds 10% after 5pm'}},
  {'say': _end("about extra charges"),
   'v2': {'kind': 'screen', 'clip': 'shop_kanda-mikian', 'title': 'Extra charges, on the shop page' + _T2}},
]}
SCRIPTS['h_12_ticket'] = {'title': 'Ticket machine', 'style': 'v2', 'led': "TOKYO HACKS #12 · 東京ハック", 'scenes': [
  {'say': "No menu, no server? Look for a ticket machine by the door.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'TOKYO HACKS #12', 'big': 'Order at\nthe machine', 'sub': 'Common at ramen, soba & udon shops', 'stamp': '食券'}},
  {'say': "Put the money in first, press the button for your dish, and take the ticket.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'HOW', 'big': 'Money in →\npress → ticket', 'sub': 'Some also take transit IC cards', 'koru': 'Pictures help.\nPoint & press!'}},
  {'say': "Hand the ticket to the staff, or leave it on the counter. Then sit and wait.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'THEN', 'big': 'Hand it over,\nthen sit', 'sub': 'Small notes and coins help'}},
  {'say': _end("which places use a ticket machine"),
   'v2': {'kind': 'screen', 'clip': 'search_any_ticket', 'title': 'Ticket-machine shops, flagged' + _T2}},
]}

SCRIPTS['b_05_onihei'] = {'title': 'Onihei', 'style': 'v2', 'led': "YU'S PICK · SUEHIROCHO 末広町", 'scenes': [
  {'say': "Sashimi set lunch, eight hundred eighty yen, near {Akihabara|ɑkihɑbɑɾɑ}.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': "YU'S PICK", 'big': 'Sashimi lunch\n¥880', 'sub': 'Uogashi Onihei 魚河岸 おに平 · Suehirocho', 'stamp': '¥880'}},
  {'say': "Get the sashimi set, or the tuna {kirioshi|kiɾioʊʃi} set.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'ORDER', 'big': 'Sashimi set\nor tuna set', 'sub': 'Lunch Mon-Sat 11:30-14:30', 'koru': "Yu's lunch\nspot!"}},
  {'say': "Dinner is Thursday to Saturday only. Closed Sundays and holidays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'BEFORE YOU GO', 'big': 'Dinner Thu-Sat', 'sub': 'Closed Sun & holidays · cards & PayPay OK', 'stamp': 'NO SUNDAYS'}},
  {'say': "Point at the menu and say, {kore onegaishimasu|koɾɛ oʊnɛɡɑiʃimɑs}. This one, please.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAY THIS', 'big': 'これ\nお願いします', 'sub': 'kore onegaishimasu · this one, please'}},
  {'say': _S, 'v2': {'kind': 'screen', 'clip': 'shop_uogashi-onihei', 'title': 'Hours · closed days · what to say' + _T2}},
]}
SCRIPTS['b_06_tankiyo'] = {'title': 'Tankiyo', 'style': 'v2', 'led': "TOKYO EATS · AKIHABARA 秋葉原", 'scenes': [
  {'say': "A whole restaurant just for beef tongue, two minutes from {Akihabara|ɑkihɑbɑɾɑ} station.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'TOKYO EATS', 'big': 'Beef tongue,\nonly tongue', 'sub': 'Tankiyo たん清 · Akihabara · basement', 'stamp': 'TONGUE'}},
  {'say': "You grill it at your table. Get the salted tongue, and try the miso tongue.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'ORDER', 'big': 'Salt tongue\n+ miso tongue', 'sub': 'Grill it yourself · dinner ~¥4,000-6,000', 'koru': 'Grill it\nyourself!'}},
  {'say': "Book ahead, diners say it fills up. It's closed Sundays and holidays, and takes no credit cards.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'BEFORE YOU GO', 'big': 'Book ahead', 'sub': 'Closed Sun & holidays · no credit cards', 'stamp': 'RESERVE'}},
  {'say': "When you arrive, say, {yoyaku shimashita|joʊjɑku ʃimɑʃitɑ}. I have a reservation.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAY THIS', 'big': '予約しました', 'sub': 'yoyaku shimashita · I have a reservation'}},
  {'say': _S, 'v2': {'kind': 'screen', 'clip': 'shop_tankiyo', 'title': 'Hours · closed days · what to say' + _T2}},
]}
SCRIPTS['b_07_azuma'] = {'title': 'Kibidango Azuma', 'style': 'v2', 'led': "TOKYO EATS · ASAKUSA 浅草", 'scenes': [
  {'say': "Warm {kibi dango|kibi dɑŋɡoʊ}, rolled in soybean powder, three minutes from {Asakusa|ɑsɑkusɑ} station.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'TOKYO EATS', 'big': 'Warm\nkibi dango', 'sub': 'Asakusa Kibidango Azuma あづま', 'stamp': 'FRESH'}},
  {'say': "Five skewers are about three hundred thirty to four hundred yen. Staff add the {kinako|kinɑkoʊ} when you order.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'ORDER', 'big': '5 skewers\n~¥330-400', 'sub': 'Kinako (soybean powder) added fresh', 'koru': 'Eat it\nwarm!'}},
  {'say': "It's open nine thirty to seven, or until it sells out. Closing days are irregular.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'BEFORE YOU GO', 'big': '9:30-19:00', 'sub': 'Or until sold out · irregular days off', 'stamp': 'SOLD OUT?'}},
  {'say': "Getting two? Say, {futatsu kudasai|ɸutɑtsu kudɑsɑi}. Two, please.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAY THIS', 'big': '二つ\nください', 'sub': 'futatsu kudasai · two, please'}},
  {'say': _S, 'v2': {'kind': 'screen', 'clip': 'shop_asakusa-kibidango-azuma', 'title': 'Hours · closed days · what to say' + _T2}},
]}
SCRIPTS['b_08_sarashina'] = {'title': 'Nishikicho Sarashina', 'style': 'v2', 'led': "TOKYO EATS · KANDA 神田", 'scenes': [
  {'say': "Cold soba with a hot chicken dipping broth, in {Kanda|kɑndɑ}.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'TOKYO EATS', 'big': 'Cold soba,\nhot chicken dip', 'sub': 'Kanda Nishikicho Sarashina 更科', 'stamp': 'SOBA'}},
  {'say': "Order the {torijiru seiro|toɾidʒiɾu sɛiɾoʊ}. Or {ten seiro|tɛn sɛiɾoʊ}, with tempura.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'ORDER', 'big': 'Torijiru seiro', 'sub': 'or ten-seiro with tempura · ¥1,000-2,000', 'koru': 'Dip, slurp,\nrepeat!'}},
  {'say': "It's cash only, with no reservations. Dinner ends at six thirty. Closed Sundays and holidays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'BEFORE YOU GO', 'big': 'Cash only', 'sub': 'Dinner until 18:30 · closed Sun & holidays', 'stamp': 'CASH ONLY'}},
  {'say': "When you leave, say, {gochisōsama deshita|ɡoʊtʃisoʊsɑmɑ dɛʃitɑ}. Thanks for the meal.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAY THIS', 'big': 'ごちそうさま\nでした', 'sub': 'gochisosama deshita · thanks for the meal'}},
  {'say': _S, 'v2': {'kind': 'screen', 'clip': 'shop_kanda-nishikicho-sarashina', 'title': 'Hours · closed days · what to say' + _T2}},
]}
SCRIPTS['b_09_shinpuku'] = {'title': 'Shinpuku Saikan', 'style': 'v2', 'led': "YU'S PICK · AKIHABARA 秋葉原", 'scenes': [
  {'say': "Kyoto-style ramen with a dark soy broth, near {Akihabara|ɑkihɑbɑɾɑ}.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': "YU'S PICK", 'big': 'Kyoto ramen,\ndark soy broth', 'sub': 'Shinpuku Saikan 新福菜館 · Akihabara', 'stamp': 'KYOTO'}},
  {'say': "Get the {chūka soba|tʃuːkɑ sobɑ}. Small is eight hundred eighty yen, regular nine hundred eighty.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'ORDER', 'big': 'Chuka soba\n¥880 / ¥980', 'sub': 'Small / regular · checked by Yu, Sep 2026', 'koru': 'Yu eats\nthis one!'}},
  {'say': "No credit cards, but PayPay works. It may sell out early.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'BEFORE YOU GO', 'big': 'No cards\n(PayPay OK)', 'sub': 'Break 15:00-17:30 · may sell out early', 'stamp': 'NO CARDS'}},
  {'say': "To order, say, {chūka soba hitotsu|tʃuːkɑ sobɑ hitoʊtsu}. One chuka soba.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAY THIS', 'big': '中華そば\nひとつ', 'sub': 'chuka soba hitotsu · one chuka soba'}},
  {'say': _S, 'v2': {'kind': 'screen', 'clip': 'shop_shinpuku-saikan-akihabara', 'title': 'Hours · closed days · what to say' + _T2}},
]}

SCRIPTS['c_07_breakfast'] = {'title': 'Breakfast', 'style': 'v2', 'led': "SAVE THIS · 朝ごはん", 'scenes': [
  {'say': "Lots of Tokyo restaurants don't open until eleven. Here are four breakfast spots near {Kanda|kɑndɑ} and {Ueno|uɛnoʊ}. Save this.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAVE THIS', 'big': '4 breakfast\nspots', 'sub': 'Open by 8:30 on weekdays · Kanda & Ueno'}},
  {'say': "One. Kanda {Shinoda|ʃinoʊdɑ} Sushi. Inari sushi since 1902, from seven thirty. Cash only, closed Tuesdays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '1 / 4', 'big': 'Kanda Shinoda Sushi', 'sub': 'Inari since 1902 · from 7:30 · cash · closed Tue'}},
  {'say': "Two. Kanda Coffee {En|ɛn}, under the tracks at the north exit. From seven on weekdays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '2 / 4', 'big': 'Kanda Coffee En', 'sub': 'Breakfast menu · from 7:00 Mon-Fri · 2F smoking', 'koru': 'Smoke-free\non 1F!'}},
  {'say': "Three. Coffee {Ōjō|oʊdʒoʊ} in {Ueno|uɛnoʊ}. Open every day from eight. Get the morning set.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '3 / 4', 'big': 'Coffee Ojo 王城', 'sub': 'Daily from 8:00 · morning set or thick toast'}},
  {'say': "Four. Cafe {Lapin|lɑpɛn} in {Okachimachi|oʊkɑtʃimɑtʃi}. Chiffon cake and toast from eight thirty. Closed Sundays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '4 / 4', 'big': 'Cafe Lapin', 'sub': 'Chiffon cake & toast · from 8:30 · closed Sun'}},
  {'say': _R, 'v2': {'kind': 'screen', 'clip': 'search_any_morning', 'title': 'Breakfast spots, before you go' + _T2}},
]}
SCRIPTS['c_08_late'] = {'title': 'Open late', 'style': 'v2', 'led': "SAVE THIS · 深夜メシ", 'scenes': [
  {'say': "Hungry after ten p.m. in east Tokyo? Four places that stay open late. Save this.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAVE THIS', 'big': 'Open late,\nafter 10pm', 'sub': 'Yushima · Ueno · Jimbocho · Asakusa'}},
  {'say': "One. {Garyū|ɡɑɾjuː} Tantanmen in {Yushima|juːʃˈimɑ}. Open until five thirty a.m., Monday to Saturday. Smoking is allowed.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '1 / 4', 'big': 'Garyu Tantanmen', 'sub': 'Until 5:30am Mon-Sat · smoking OK · no cards'}},
  {'say': "Two. Yokohama Ramen {Asagaya|ɑsɑɡɑjɑ} in {Ueno|uɛnoʊ}. Open until three a.m., every day.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '2 / 4', 'big': 'Asagaya Ueno', 'sub': 'Iekei ramen · until 3:00 daily · cards OK'}},
  {'say': "Three. {Sankōen|sɑnkoʊɛn} in {Jinbōchō|dʒinboʊtʃˈoʊ}. Big gyoza until two thirty on weeknights. Closed Saturdays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '3 / 4', 'big': 'Sankouen 三幸園', 'sub': 'Gyoza · until 2:30am Mon-Thu · closed Sat', 'koru': 'Closed on\nSATURDAY!'}},
  {'say': "Four. Coffee Lodge {Akaishi|ɑkɑiʃi} in {Asakusa|ɑsɑkusɑ}. A retro cafe open until three a.m., Tuesday to Saturday.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '4 / 4', 'big': 'Coffee Lodge Akaishi', 'sub': 'Until 3:00 Tue-Sat · closed Mon'}},
  {'say': _R, 'v2': {'kind': 'screen', 'clip': 'search_any_late', 'title': 'Late-night spots, before you go' + _T2}},
]}
SCRIPTS['c_09_soba'] = {'title': 'Standing soba', 'style': 'v2', 'led': "SAVE THIS · 立ち食いそば", 'scenes': [
  {'say': "Four standing soba shops near {Akihabara|ɑkihɑbɑɾɑ}. Fast, cheap, and under a thousand yen. Save this.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAVE THIS', 'big': '4 standing\nsoba spots', 'sub': 'Near Akihabara · tachigui soba 立ち食いそば'}},
  {'say': "One. {Minogasa|minoʊɡɑsɑ}. House-made noodles, and it opens at six. Kakiage soba was five hundred ten yen in 2025.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '1 / 4', 'big': 'Minogasa', 'sub': 'Kakiage soba ¥510 (2025) · from 6:00 · closed holidays'}},
  {'say': "Two. Shin {Tagoto|tɑɡoʊtoʊ}, by the station. Six a.m. to eleven p.m., every day. Try the steak curry.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '2 / 4', 'big': 'Shin-Tagoto', 'sub': '6:00-23:00 daily · soba or steak curry · no cards'}},
  {'say': "Three. {Futaba|ɸutɑbɑ}. Tempura and egg soba at a standing counter. Daytime only, closed Sundays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '3 / 4', 'big': 'Futaba 二葉', 'sub': 'Tendama soba · 7:30-17:00 · closed Sun'}},
  {'say': "Four. {Kawaichi|kɑwɑitʃi}. Famous for squid tempura soba. Cash only, closed Sundays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '4 / 4', 'big': 'Kawaichi 川一', 'sub': 'Ika (squid) soba · cash only · closed Sun', 'koru': 'Crunchy\nsquid!'}},
  {'say': _R, 'v2': {'kind': 'screen', 'clip': 'search_any_soba', 'title': 'Soba spots, before you go' + _T2}},
]}
SCRIPTS['c_10_asakusa_en'] = {'title': 'Asakusa English menu', 'style': 'v2', 'led': "SAVE THIS · 浅草 英語メニュー", 'scenes': [
  {'say': "Four {Asakusa|ɑsɑkusɑ} spots with an English menu. Save this.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAVE THIS', 'big': 'English menu\nin Asakusa', 'sub': '4 places near Senso-ji'}},
  {'say': "One. {Owariya|oʊwɑɾijɑ}. Tempura soba for about sixteen hundred yen. Closed Fridays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '1 / 4', 'big': 'Owariya 尾張屋', 'sub': 'Tempura soba ¥1,600 · closed Fri'}},
  {'say': "Two. {Sometarō|soʊmɛtɑɾoʊ}. Okonomiyaki you cook at your table, since 1937. Or ask the staff to cook it.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '2 / 4', 'big': 'Sometaro 染太郎', 'sub': 'Cook-it-yourself okonomiyaki · since 1937', 'koru': 'Staff can\ncook it too!'}},
  {'say': "Three. {Yoroiya|joʊɾoijɑ}. Ramen for about nine hundred yen, a minute's walk from {Sensōji|sɛnsoʊdʒi}.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '3 / 4', 'big': 'Yoroiya 与ろゐ屋', 'sub': 'Ramen ~¥900 · 1 min from Senso-ji'}},
  {'say': "Four. {Kokonoe|koʊkoʊnoʊɛ}. Fried sweet buns from a hundred sixty yen. Open every day.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '4 / 4', 'big': 'Kokonoe 九重', 'sub': 'Age-manju from ¥160 · 10:00-19:00 daily'}},
  {'say': _R, 'v2': {'kind': 'screen', 'clip': 'search_any_asakusa', 'title': 'Asakusa spots, before you go' + _T2}},
]}
SCRIPTS['c_11_ueno_drinks'] = {'title': 'Ueno cheap drinks', 'style': 'v2', 'led': "SAVE THIS · 上野 せんべろ", 'scenes': [
  {'say': "Cheap drinks in {Ueno|uɛnoʊ}, any time of day. Three standing spots. Save this.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAVE THIS', 'big': 'Cheap drinks\nin Ueno', 'sub': 'Standing bars & grilled skewers'}},
  {'say': "One. {Takioka|tɑkioʊkɑ}. A standing bar open from seven a.m., every day. Cash only, and smoking is allowed.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '1 / 3', 'big': 'Tachinomi Takioka', 'sub': '7:00-23:30 daily · standing · cash · smoking OK'}},
  {'say': "Two. {Daitōryō|dɑitoʊɾjoʊ}, under the {Ameyoko|ɑmɛjoʊkoʊ} tracks since 1950. Offal skewers, two for a hundred eighty yen.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '2 / 3', 'big': 'Motsuyaki Daitoryo', 'sub': 'Since 1950 · 2 skewers from ¥180 · 10:00-24:00'}},
  {'say': "Three. Niku no {Ōyama|oʊjɑmɑ}. A butcher with a standing counter. Meat cutlets from a hundred fifty yen.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '3 / 3', 'big': 'Niku no Oyama', 'sub': 'Menchi-katsu from ¥150 · 11:00-23:00', 'koru': 'Cutlet +\na cold one!'}},
  {'say': _R, 'v2': {'kind': 'screen', 'clip': 'search_any_standing', 'title': 'Standing bars, before you go' + _T2}},
]}
SCRIPTS['c_12_eel_en'] = {'title': 'Eel English menu', 'style': 'v2', 'led': "SAVE THIS · うなぎ 英語メニュー", 'scenes': [
  {'say': "Three eel restaurants with an English menu. A splurge worth saving.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': 'SAVE THIS', 'big': 'Eel, with an\nEnglish menu', 'sub': 'Ueno · Asakusa · Kanda'}},
  {'say': "One. {Izuei|izuɛi} in {Ueno|uɛnoʊ}, facing {Shinobazu|ʃinoʊbɑzu} Pond. Eel over rice from three thousand six hundred thirty yen.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '1 / 3', 'big': 'Izuei 伊豆榮', 'sub': 'Unaju from ¥3,630 · 11:00-21:00 · by the pond'}},
  {'say': "Two. {Irokawa|iɾoʊkɑwɑ}, by {Kaminarimon|kɑminɑɾimoʊn}, since 1861. Lunch only, Monday to Saturday.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '2 / 3', 'big': 'Unagi Irokawa 色川', 'sub': 'Since 1861 · lunch only · closed Sun'}},
  {'say': "Three. {Kikukawa|kikukɑwɑ} in {Kanda|kɑndɑ}. You can book online. Closed Mondays.",
   'v2': {'kind': 'photo', 'bg': None, 'kicker': '3 / 3', 'big': 'Kanda Kikukawa', 'sub': 'Unaju ~¥5,000-8,000 · closed Mon · cards OK', 'koru': 'Save up\nfor this!'}},
  {'say': _R, 'v2': {'kind': 'screen', 'clip': 'search_any_unagi', 'title': 'Eel spots, before you go' + _T2}},
]}
NEW_R2 = ['h_07_lastorder','h_08_break','h_09_soldout','h_10_smoking','h_11_otoshi','h_12_ticket','b_05_onihei','b_06_tankiyo','b_07_azuma','b_08_sarashina','b_09_shinpuku','c_07_breakfast','c_08_late','c_09_soba','c_10_asakusa_en','c_11_ueno_drinks','c_12_eel_en']
