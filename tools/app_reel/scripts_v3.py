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
