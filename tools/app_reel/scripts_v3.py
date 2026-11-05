NOTE = 'Photos: similar dishes, not these shops'
V3 = {}
V3['f_01_soba'] = {'n': 4, 'speed': 1.22, 'beats': [
  {'say': "Soba for five hundred ten yen. At six a.m.", 'photo': 'soba_noodles_0.jpg', 'big': 'SOBA ¥510\nAT 6AM', 'hl': 0, 'size': 170, 'min': 1.6, 'note': NOTE},
  {'say': "Four standing soba spots by {Akihabara|ɑkihɑbɑɾɑ}. Save this.", 'photo': 'tokyo_alley_restaurant_0.jpg', 'tag': 'SAVE THIS', 'big': '4 STANDING\nSOBA SPOTS', 'hl': 1, 'min': 1.5},
  {'say': "{Minogasa|minoʊɡɑsɑ}. House-made noodles, from six.", 'photo': 'tempura_0.jpg', 'idx': 1, 'tag': '1 · MINOGASA', 'big': 'KAKIAGE\nSOBA', 'chips': ['¥510 (2025)', 'opens 6:00'], 'note': NOTE},
  {'say': "Shin {Tagoto|tɑɡoʊtoʊ}. Six to eleven, every day.", 'photo': 'japanese_curry_rice_1.jpg', 'idx': 2, 'tag': '2 · SHIN-TAGOTO', 'big': 'OPEN\n6AM-11PM', 'chips': ['soba or steak curry', 'no cards'], 'note': NOTE},
  {'say': "{Futaba|ɸutɑbɑ}. Tempura and egg soba. Daytime only.", 'photo': 'tempura_1.jpg', 'idx': 3, 'tag': '3 · FUTABA', 'big': 'TEMPURA\n+ EGG', 'chips': ['7:30-17:00', 'closed Sun'], 'note': NOTE},
  {'say': "{Kawaichi|kɑwɑitʃi}. Crunchy squid tempura. Cash only.", 'photo': 'soba_noodles_0.jpg', 'focus': (.3, .6), 'idx': 4, 'tag': '4 · KAWAICHI', 'big': 'SQUID\nTEMPURA', 'chips': ['cash only', 'closed Sun'], 'koru': 'CRUNCH!', 'note': NOTE},
  {'say': "Which one first? Hours and closed days are free in my bio.", 'photo': 'tokyo_alley_restaurant_0.jpg', 'idx': 4, 'big': 'WHICH ONE\nFIRST? 1-4', 'hl': 1, 'koru': 'Comment!', 'min': 2.2},
]}
Y = '/home/claude/koru-tokyo-reels/stock/yu/'
V3['f_02_ginkgo'] = {'speed': 1.18, 'beats': [
  {'say': "{Akihabara|ɑkihɑbɑɾɑ}, November fourth. The ginkgo trees are still green.", 'photo': Y + 'yu_ginkgo_akiba_20261104.jpg', 'focus': (.45, .3), 'tag': 'NOV 4 · AKIHABARA', 'big': 'TOKYO GINKGO:\nSTILL GREEN', 'hl': 1, 'min': 2.0, 'note': 'Photo: Yu, Nov 4 2026'},
  {'say': "My morning, almost every day. Iced coffee on the walk to work.", 'photo': Y + 'yu_coffee_20261104.jpg', 'focus': (.45, .6), 'tag': "YU'S MORNING", 'big': 'ICED COFFEE,\nALMOST DAILY', 'hl': 0, 'min': 1.8, 'note': 'Photo: Yu'},
  {'say': "The forecast says Tokyo's ginkgo turns yellow around November twenty-sixth.", 'photo': Y + 'yu_ginkgo_akiba_20261104.jpg', 'focus': (.35, .2), 'tag': 'FORECAST', 'big': 'YELLOW AROUND\nNOV 26', 'hl': 1, 'chips': ['ginkgo ~Nov 26', 'maple ~Nov 28'], 'note': 'Forecast: Japan Meteorological Corp. (via Time Out Tokyo)'},
  {'say': "I walk past this every day. Follow, and I'll show you when it turns.", 'photo': Y + 'yu_ginkgo_akiba_20261104.jpg', 'focus': (.55, .5), 'big': 'FOLLOW &\nWATCH IT TURN', 'hl': 1, 'koru': 'Wait for it!', 'min': 2.4},
]}
D = Y + 'domannaka_'
V3['f_03_domannaka'] = {'speed': 1.2, 'beats': [
  {'say': "One minute from {Akihabara|ɑkihɑbɑɾɑ} station, hidden in a basement. Fresh fish, Yu's pick.", 'photo': D + 'sashimi.jpg', 'focus': (.5, .55), 'tag': "YU'S PICK · AKIHABARA", 'big': 'SASHIMI\nON ICE', 'hl': 1, 'size': 170, 'min': 1.8, 'note': 'Photos: Yu, Nov 2026'},
  {'say': "Sea urchin hand roll, with caviar.", 'photo': D + 'uni.jpg', 'focus': (.5, .45), 'big': 'UNI\n+ CAVIAR', 'hl': 0, 'note': 'Photos: Yu'},
  {'say': "{Aji|ɑdʒi} fry. Horse mackerel, still rare inside, with the crispy bones.", 'photo': D + 'fishfry.jpg', 'focus': (.55, .5), 'big': 'RARE\nAJI FRY', 'hl': 1, 'chips': ['horse mackerel', 'crispy fried bones'], 'note': 'Photos: Yu'},
  {'say': "{Namerō|nɑmɛɾoʊ}. Chopped raw fish with salmon roe.", 'photo': D + 'namero.jpg', 'focus': (.48, .5), 'big': 'NAMERO', 'chips': ['chopped raw fish', '+ salmon roe'], 'note': 'Photos: Yu'},
  {'say': "Abalone and mushrooms.", 'photo': D + 'abalone.jpg', 'focus': (.48, .45), 'big': 'ABALONE', 'hl': 0, 'note': 'Photos: Yu'},
  {'say': "And this tower? It's potato salad, under a crispy topping.", 'photo': D + 'tower.jpg', 'focus': (.5, .4), 'big': 'POTATO SALAD\nTOWER', 'hl': 1, 'koru': 'Crunch!', 'note': 'Photos: Yu'},
  {'say': "Book online. About six to eight thousand yen a person. Closed Mondays.", 'photo': D + 'highball.jpg', 'focus': (.5, .45), 'tag': 'DOMANNAKA AKIHABARA BETTEI', 'big': 'BOOK\nAHEAD', 'hl': 1, 'chips': ['~¥6,000-8,000 (Tabelog avg)', 'closed Mon · 15:00-23:00', 'cards & PayPay OK'], 'min': 2.6, 'note': 'Photos: Yu · check hours on the day'},
  {'say': "Send this to your fish-loving friend. Hours and closed days are free in my bio.", 'photo': D + 'sashimi.jpg', 'focus': (.35, .5), 'big': 'SEND THIS TO\nYOUR FISH FRIEND', 'hl': 1, 'koru': 'Fish time!', 'min': 2.4},
]}
SV = '/home/claude/render/stockv/mixkit_'
MK = 'Footage: Mixkit (free license)'
V3['f_04_local_moves'] = {'speed': 1.2, 'beats': [
  {'say': "Eat like a local in Tokyo. Three moves.", 'video': SV + '4447.mp4', 'vstart': 3, 'tag': 'TOKYO FOOD', 'big': '3 LOCAL\nMOVES', 'hl': 1, 'size': 170, 'min': 1.6, 'note': MK},
  {'say': "One. Slurp your noodles. It's normal here, and it cools them down.", 'video': SV + '51257.mp4', 'vstart': 2, 'tag': '1 / 3', 'big': 'SLURP\nIT', 'hl': 0, 'note': MK},
  {'say': "Two. Dip sushi lightly, so the rice doesn't soak up the soy sauce.", 'video': SV + '45949.mp4', 'vstart': 0, 'tag': '2 / 3', 'big': 'DIP\nLIGHTLY', 'hl': 0, 'note': MK},
  {'say': "Three. Can't read the menu? Point and say, {kore onegaishimasu|koɾɛ oʊnɛɡɑiʃimɑs}.", 'video': SV + '45915.mp4', 'vstart': 0, 'tag': '3 / 3', 'big': 'POINT +\nKORE!', 'hl': 1, 'chips': ['これお願いします', 'this one, please'], 'note': MK},
  {'say': "Follow for one Tokyo tip a day, and your trip just works.", 'video': SV + '4109.mp4', 'vstart': 5, 'big': 'FOLLOW FOR\n1 TIP A DAY', 'hl': 1, 'koru': 'See you!', 'min': 2.4, 'note': MK},
]}

# ---- auto-convert v2 scripts to v3 fast format with stock footage (format test from 11/6) ----
import random as _r, subprocess as _sp
from scripts import SCRIPTS as _S2
_dur = {}
def _vlen(p):
    if p not in _dur:
        _dur[p] = float(_sp.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True).stdout or 6)
    return _dur[p]
def from_v2(sid, clips, note='Footage: Mixkit, similar scenes, not this shop'):
    sc = _S2[sid]['scenes']; beats = []; _r.seed(sid)
    for i, s in enumerate(sc):
        v = s['v2']; clip = SV + '%s.mp4' % clips[i % len(clips)]
        b = {'say': s['say'], 'video': clip, 'vstart': round(_r.uniform(0, max(0, _vlen(clip) - 6)), 1), 'note': note}
        if v.get('kind') == 'screen':
            b.update({'big': 'HOURS FREE\nIN MY BIO', 'hl': 0, 'koru': 'Check first!', 'min': 2.4})
        else:
            b.update({'big': v.get('big', ''), 'tag': v.get('kicker'), 'hl': 0 if i else 1})
            if v.get('sub'): b['chips'] = [c.strip() for c in v['sub'].split('·')][:3]
            if v.get('koru') and 'app' not in v['koru'].lower(): b['koru'] = v['koru'].replace('\n', ' ')[:24]
        if i == 0: b['min'] = 1.8
        beats.append(b)
    return {'speed': 1.22, 'beats': beats}
CONV = {'b_05_onihei': [4231, 45921, 46019, 5761, 4109], 'b_06_tankiyo': [4447, 51238, 4451, 20085, 4109],
        'b_07_azuma': [4403, 45086, 4405, 48686, 4404], 'b_08_sarashina': [4437, 51257, 51255, 46354, 4231],
        'b_09_shinpuku': [4447, 51255, 51257, 51236, 4451], 'v2_02_mochizuki': [4437, 46354, 4231, 51241, 4109, 4448],
        'c_07_breakfast': [4231, 48686, 4454, 45086, 46015, 4437], 'c_08_late': [4447, 51257, 4451, 46122, 4109, 4448],
        'c_09_soba': [4437, 51255, 51257, 46354, 51236, 4231], 'c_10_asakusa_en': [4403, 51238, 4405, 51257, 45086, 4404],
        'c_11_ueno_drinks': [4109, 4109, 4447, 51241, 4451], 'c_12_eel_en': [4448, 46354, 4404, 51238, 4109]}
for _k, _c in CONV.items():
    V3[_k + '_v3'] = from_v2(_k, _c)

# ---- E3: ultra-short loops (7-12 s), from 11/8 ----
V3['s_01_soba510'] = {'speed': 1.25, 'beats': [
  {'say': "Soba for five hundred ten yen, at six a.m., by {Akihabara|ɑkihɑbɑɾɑ}.", 'video': SV + '51255.mp4', 'vstart': 1, 'big': 'SOBA ¥510\nAT 6AM', 'hl': 0, 'size': 170, 'min': 2.2, 'note': 'Footage: Mixkit, similar scene · price: 2025'},
  {'say': "{Minogasa|minoʊɡɑsɑ}. Ticket machine, house-made noodles.", 'video': SV + '51257.mp4', 'vstart': 3, 'tag': 'MINOGASA みのがさ', 'big': 'KAKIAGE\nSOBA', 'chips': ['opens 6:00', 'closed holidays'], 'note': 'Footage: Mixkit, similar scene'},
  {'say': "Save it for your first morning.", 'video': SV + '51255.mp4', 'vstart': 1, 'big': 'SAVE FOR\nDAY 1', 'hl': 1, 'min': 1.4},
]}
V3['s_02_notip'] = {'speed': 1.25, 'beats': [
  {'say': "Leave a tip in Tokyo, and they might run after you to give it back.", 'video': SV + '51238.mp4', 'vstart': 2, 'big': "DON'T TIP\nIN JAPAN", 'hl': 0, 'size': 170, 'min': 2.2, 'note': 'Footage: Mixkit'},
  {'say': "Say {gochisōsama deshita|ɡoʊtʃisoʊsɑmɑ dɛʃitɑ} instead.", 'video': SV + '51241.mp4', 'vstart': 1, 'big': 'SAY THIS\nINSTEAD', 'hl': 1, 'chips': ['ごちそうさまでした', 'thanks for the meal'], 'note': 'Footage: Mixkit'},
]}
V3['s_03_sunday'] = {'speed': 1.25, 'beats': [
  {'say': "One in three places I checked in east Tokyo is closed on Sunday.", 'video': SV + '4451.mp4', 'vstart': 4, 'big': '1 IN 3\nCLOSED SUNDAY', 'hl': 1, 'size': 160, 'min': 2.2, 'note': 'From 299 East Tokyo places I checked · Footage: Mixkit'},
  {'say': "Sunday list is free in my bio.", 'video': SV + '4437.mp4', 'vstart': 5, 'big': 'SUNDAY LIST:\nLINK IN BIO', 'hl': 0, 'koru': 'Free!', 'min': 1.6},
]}
V3['s_04_check'] = {'speed': 1.25, 'beats': [
  {'say': "Want the check in Tokyo? Don't wave. Say this.", 'video': SV + '51236.mp4', 'vstart': 1, 'big': 'GET THE\nCHECK FAST', 'hl': 1, 'size': 160, 'min': 2.0, 'note': 'Footage: Mixkit'},
  {'say': "{okaikei onegaishimasu|oʊkɑikɛi oʊnɛɡɑiʃimɑs}.", 'video': SV + '51241.mp4', 'vstart': 3, 'big': 'お会計\nお願いします', 'chips': ['okaikei onegaishimasu', 'the check, please'], 'min': 2.0, 'note': 'Footage: Mixkit'},
  {'say': "Then pay at the register by the door.", 'video': SV + '51236.mp4', 'vstart': 1, 'big': 'PAY AT\nTHE DOOR', 'hl': 1, 'min': 1.4},
]}

# ---- Creative challenges (C-series) ----
V3['g_01_guess_price'] = {'speed': 1.22, 'beats': [
  {'say': "Kyoto-style ramen, five minutes from {Akihabara|ɑkihɑbɑɾɑ}. Guess the price.", 'video': SV + '51255.mp4', 'vstart': 0.5, 'tag': 'GUESS THE PRICE', 'big': 'HOW MUCH?', 'hl': 0, 'size': 190, 'min': 2.0, 'note': 'Footage: Mixkit, similar scene'},
  {'say': "A, B, or C? Comment before the reveal.", 'video': SV + '51257.mp4', 'vstart': 2, 'big': 'A, B or C?', 'hl': 0, 'chips': ['A  ¥580', 'B  ¥880', 'C  ¥1,480'], 'min': 2.6, 'note': 'Footage: Mixkit, similar scene'},
  {'say': "Three. Two. One.", 'video': SV + '51255.mp4', 'vstart': 3, 'big': '3 · 2 · 1', 'hl': 0, 'size': 200, 'min': 1.4},
  {'say': "B. Eight hundred eighty yen for a small chuka soba at {Shinpuku Saikan|ʃinpuku sɑikɑn}. Yu checked.", 'video': SV + '51257.mp4', 'vstart': 5, 'tag': 'SHINPUKU SAIKAN 新福菜館', 'big': 'B · ¥880', 'hl': 0, 'size': 190, 'chips': ['small chuka soba', 'regular ¥980 · checked by Yu'], 'koru': 'Got it?', 'min': 2.6},
]}
V3['n_01_silent_6am'] = {'silent': True, 'beats': [
  {'say': '', 'video': SV + '4231.mp4', 'vstart': 1, 'big': '6:00 AM\nAKIHABARA', 'hl': 0, 'size': 170, 'min': 1.6, 'note': 'Footage: Mixkit, similar scenes'},
  {'say': '', 'video': SV + '51257.mp4', 'vstart': 1, 'big': 'SOBA ¥510', 'hl': 0, 'chips': ['Minogasa みのがさ', 'opens 6:00'], 'min': 1.8},
  {'say': '', 'video': SV + '4454.mp4', 'vstart': 2, 'big': '7:00 AM', 'hl': 0, 'chips': ['Kanda Coffee En', 'breakfast menu'], 'min': 1.6},
  {'say': '', 'video': SV + '48686.mp4', 'vstart': 1, 'big': '8:00 AM', 'hl': 0, 'chips': ['Coffee Ojo, Ueno', 'morning set'], 'min': 1.6},
  {'say': '', 'video': SV + '4437.mp4', 'vstart': 6, 'big': 'TOKYO WAKES\nUP EARLY', 'hl': 1, 'koru': 'Save it!', 'min': 1.8},
]}
V3['p_01_pov_ticket'] = {'speed': 1.22, 'beats': [
  {'say': "P O V. Your first ramen shop in Tokyo, and there's no menu. Just a machine.", 'video': SV + '4451.mp4', 'vstart': 2, 'tag': 'POV', 'big': 'NO MENU.\nJUST A MACHINE', 'hl': 1, 'min': 2.0, 'note': 'Footage: Mixkit, similar scenes'},
  {'say': "Money in first. Small notes are easier.", 'video': SV + '51236.mp4', 'vstart': 0.5, 'tag': 'STEP 1', 'big': 'MONEY IN', 'hl': 0, 'min': 1.5},
  {'say': "Press your bowl. Take the ticket.", 'video': SV + '51241.mp4', 'vstart': 1, 'tag': 'STEP 2', 'big': 'PRESS +\nTAKE TICKET', 'hl': 0, 'min': 1.5},
  {'say': "Hand it over. Sit. Slurp.", 'video': SV + '51257.mp4', 'vstart': 3, 'tag': 'STEP 3', 'big': 'HAND IT OVER.\nSLURP.', 'hl': 1, 'koru': 'Easy!', 'min': 1.8},
]}
for _k, _c in {'h_10_smoking': [4447, 45086, 4454, 48686], 'h_11_otoshi': [4109, 51238, 51241, 4451], 'h_12_ticket': [4451, 51236, 51241, 51257]}.items():
    V3[_k + '_v3'] = from_v2(_k, _c, note='Footage: Mixkit, similar scenes')
