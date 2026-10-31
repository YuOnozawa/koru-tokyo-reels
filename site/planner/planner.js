(function () {
  // Apps Script web app URL that stores the request in Yu's sheet and emails the plan.
  // Empty = the email box stays hidden.
  var ENDPOINT = '';
  // Tips. TIP_URL = the tip page (Ko-fi, Buy Me a Coffee, Stripe Payment Link with "customer chooses price", PayPal.me...).
  // TIP_AMOUNT_URL (optional) = a page that takes a preset amount, with {amt} replaced, e.g. 'https://paypal.me/NAME/{amt}USD'.
  // Empty TIP_URL = the tip jar stays hidden.
  var TIP_URL = '';
  var TIP_AMOUNT_URL = '';

  var AREAS = [['akiba', '秋葉原', 'Akihabara', 'cap-red', ['Akihabara', 'Suehirocho']], ['ueno', '上野・湯島', 'Ueno & Yushima', 'cap-green', ['Ueno', 'Okachimachi', 'Yushima']], ['asakusa', '浅草', 'Asakusa', 'cap-yellow', ['Asakusa', 'Kuramae']], ['kanda', '神田・神保町', 'Kanda & Jimbocho', 'cap-blue', ['Kanda', 'Jimbocho', 'Ochanomizu']]];
  var BUDGETS = [['under1500', '¥1,500', 'Cheap eats', 'cap-green'], ['1500-4000', '¥4,000', 'Everyday', 'cap-blue'], ['4000-10000', '¥10,000', 'Treat', 'cap-yellow'], ['10000plus', '上限なし', 'No limit', 'cap-red']];
  var AVOID = [['rawfish', '生魚', 'Raw fish'], ['seafood', '魚介', 'Seafood'], ['pork', '豚', 'Pork'], ['spicy', '辛い', 'Spicy'], ['meat', '肉', 'Meat']];
  var TOGGLES = [['yu', '推し', "Yu's picks"], ['award', '受賞', 'Award winners'], ['cheap', '安い', 'Under ¥1,500'], ['sweet', '甘味', 'Sweets & cafes']];
  var GROUP = {}, LABEL = {};
  AREAS.forEach(function (a) { LABEL[a[0]] = a[2]; a[4].forEach(function (x) { GROUP[x] = a[0]; }); });
  var BANDS = ['under1500', '1500-4000', '4000-10000', '10000plus'];
  var DOW = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'], DOWFULL = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];
  var FAMS = ['curry', 'ramen', 'tsukemen', 'soba', 'udon', 'sushi', 'tonkatsu', 'katsu', 'tempura', 'unagi', 'yakitori', 'izakaya', 'sukiyaki', 'gyudon', 'dandan', 'okonomiyaki', 'yoshoku'];

  var $ = function (id) { return document.getElementById(id); };
  var f = $('f'), out = $('out'), cta = $('cta');
  var SHOPS = [], lastPlan = null, lastSeed = 0;

  // ---------- helpers ----------
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function rng(seed) { return function () { seed |= 0; seed = seed + 0x6D2B79F5 | 0; var t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
  function has(s, w) { s = (s || '').toLowerCase(); return w.some(function (x) { return s.indexOf(x) >= 0; }); }
  function store(k, v) { try { if (v === undefined) return JSON.parse(localStorage.getItem(k) || 'null'); localStorage.setItem(k, JSON.stringify(v)); } catch (e) { return null; } }
  function key(box, type, name, val, jp, en, cap, checked, small) {
    var l = el('label', 'key' + (small ? ' small' : ''));
    var i = document.createElement('input'); i.type = type; i.name = name; i.value = val; i.checked = !!checked;
    var face = el('span', 'face ' + (cap || 'cap-grey'));
    var w = el('span'); w.append(el('span', 'jp', jp), el('span', 'en', en)); face.appendChild(w);
    l.append(i, face); box.appendChild(l); return i;
  }
  function excluded(s, av) {
    var g = (s.genre + ' ' + s.what_to_order).toLowerCase();
    if (av.indexOf('rawfish') >= 0 && has(g, ['sushi', 'sashimi', 'kaisendon', 'seafood bowl', 'raw', 'oyster', 'tokumori'])) return true;
    if (av.indexOf('seafood') >= 0 && has(g, ['sushi', 'sashimi', 'seafood', 'fish', 'unagi', 'eel', 'tempura', 'oden', 'takoyaki', 'octopus', 'oyster', 'monkfish', 'clam', 'shellfish', 'shrimp'])) return true;
    if (av.indexOf('pork') >= 0 && has(g, ['tonkatsu', 'pork', 'ramen', 'tsukemen', 'gyoza', 'katsu', 'menchi', 'shabu', 'motsu', 'offal'])) return true;
    if (av.indexOf('spicy') >= 0 && has(g, ['dandan', 'tantan', 'spicy', 'sichuan', 'karashibi', 'curry'])) return true;
    if (av.indexOf('meat') >= 0 && has(g, ['tonkatsu', 'pork', 'beef', 'chicken', 'yakitori', 'ramen', 'tsukemen', 'gyudon', 'sukiyaki', 'gyunabe', 'katsu', 'menchi', 'meat', 'curry', 'gyoza', 'unagi', 'eel', 'fish', 'sushi', 'sashimi', 'seafood', 'tempura', 'oden', 'motsu', 'oyakodon', 'horse'])) return true;
    return false;
  }
  function closedOn(s, k) { var c = (s.closed_days || '').toLowerCase(); return c.indexOf(DOWFULL[k]) >= 0 || new RegExp('\\b' + DOW[k] + '\\b').test(c); }
  function fits(s, band) { return BANDS.indexOf(s.budget_band) <= BANDS.indexOf(band); }
  function fam(s) { var g = (s.genre || '').toLowerCase(); for (var i = 0; i < FAMS.length; i++) { if (g.indexOf(FAMS[i]) >= 0) return FAMS[i] === 'katsu' && g.indexOf('curry') >= 0 ? 'curry' : FAMS[i]; } return g; }
  function picked(name) { return [].slice.call(document.querySelectorAll('input[name=' + name + ']:checked')).map(function (i) { return i.value; }); }

  // ---------- kept tickets ----------
  function kept() { return store('koru-kept') || []; }
  function toggleKeep(s, btn) {
    var k = kept(), i = k.indexOf(s.name_ja);
    if (i >= 0) k.splice(i, 1); else k.push(s.name_ja);
    store('koru-kept', k); if (btn) { btn.setAttribute('aria-pressed', i < 0); btn.textContent = i < 0 ? '★ Kept' : '☆ Keep'; }
    renderKept();
  }
  function renderKept() {
    var k = kept(), box = $('kept'), list = $('keptlist');
    list.replaceChildren(); box.hidden = !k.length;
    k.forEach(function (n, i) { var s = SHOPS.find(function (x) { return x.name_ja === n; }); if (s) list.appendChild(ticket(s, '★ KEPT', 'No.K' + String(i + 1).padStart(2, '0'), false)); });
  }

  // ---------- ticket ----------
  function ticket(s, slot, no, anim, priceField) {
    var t = el('article', 'ticket' + (anim ? ' printing' : ''));
    var top = el('div', 't-top'); top.append(el('span', 'slotname', slot), el('span', null, no)); t.appendChild(top);
    var h = el('h3', 't-name', s.name_en); h.appendChild(el('span', 't-ja', s.name_ja)); t.appendChild(h);
    if (s.yu_pick) { var hk = el('div', 'hanko'); hk.setAttribute('aria-label', "Yu's pick"); hk.append(el('b', null, '推し'), document.createTextNode("Yu's pick")); t.appendChild(hk); }
    if (s.what_to_order && s.what_to_order !== 'unknown') t.appendChild(el('p', 't-order', '▶ ' + s.what_to_order));
    var dl = el('dl', 't-facts');
    function row(a, b) { if (!b || b === 'unknown') return; dl.append(el('dt', null, a), el('dd', null, b)); }
    row('Genre', s.genre); row('Price', priceField === 'dinner' ? s.dinner_price_yen : s.lunch_price_yen); row('Hours', s.hours); row('Closed', s.closed_days);
    row('Station', s.station + (s.walk_min && s.walk_min !== 'unknown' ? ', ' + s.walk_min + ' min walk' : ''));
    if ((s.awards || []).length) row('Awards', s.awards.slice(0, 2).join('; '));
    row('Tip', s.tourist_tip); t.appendChild(dl);
    var acts = el('div', 't-actions');
    var keepB = el('button', 'mini', kept().indexOf(s.name_ja) >= 0 ? '★ Kept' : '☆ Keep'); keepB.type = 'button';
    keepB.setAttribute('aria-pressed', kept().indexOf(s.name_ja) >= 0); keepB.addEventListener('click', function () { toggleKeep(s, keepB); });
    var a = el('a', 'mini', 'Google Maps'); a.href = 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(s.name_ja); a.target = '_blank'; a.rel = 'noopener'; a.style.textDecoration = 'none';
    acts.append(keepB, a, el('span', 't-note', 'Checked ' + s.checked)); t.appendChild(acts);
    return t;
  }

  // ---------- plan ----------
  function readPlanInputs() {
    return { start: $('start').value, days: +$('days').value, areas: picked('area'), band: (f.querySelector('input[name=budget]:checked') || {}).value || '1500-4000', avoid: picked('avoid') };
  }
  function plan(o, seed) {
    var R = rng(seed), areas = o.areas.length ? o.areas : ['akiba'];
    var start = new Date(o.start + 'T12:00:00'), used = {}, res = [];
    var score = function (s) { return (s.yu_pick ? 3 : 0) + ((s.awards || []).length ? 2 : 0) + R() * 2; };
    for (var i = 0; i < o.days; i++) {
      var date = new Date(start.getTime() + i * 86400000), area = areas[i % areas.length], k = date.getDay();
      var pool = SHOPS.filter(function (s) { return !used[s.name_ja] && !excluded(s, o.avoid) && fits(s, o.band) && !closedOn(s, k); });
      var local = pool.filter(function (s) { return GROUP[s.area] === area; }); if (local.length < 3) local = pool;
      var sc = {}; local.forEach(function (s) { sc[s.name_ja] = score(s); });
      local.sort(function (a, b) { return sc[b.name_ja] - sc[a.name_ja]; });
      var meals = local.filter(function (s) { return s.kind !== 'snack'; }), snacks = local.filter(function (s) { return s.kind === 'snack'; });
      var lunch = meals.find(function (s) { return s.lunch_ok !== false && (s.budget_band === 'under1500' || s.budget_band === '1500-4000'); }) || meals.find(function (s) { return s.lunch_ok !== false; });
      if (lunch) used[lunch.name_ja] = 1;
      var snack = snacks.find(function (s) { return !used[s.name_ja]; }); if (snack) used[snack.name_ja] = 1;
      var dinner = meals.find(function (s) { return !used[s.name_ja] && s.dinner_ok !== false && fam(s) !== fam(lunch || { genre: '' }); }) || meals.find(function (s) { return !used[s.name_ja] && s.dinner_ok !== false; });
      if (dinner) used[dinner.name_ja] = 1;
      res.push({ date: date, area: LABEL[area], meals: [['昼', 'LUNCH', lunch, 'lunch'], ['甘', 'SWEET STOP', snack, 'lunch'], ['夜', 'DINNER', dinner, 'dinner']] });
    }
    return res;
  }
  function renderPlan(seed) {
    out.replaceChildren();
    if (!SHOPS.length) { out.appendChild(el('p', 'empty', 'Loading the restaurant list. Press print again in a second.')); return; }
    var o = readPlanInputs(); lastSeed = seed; lastPlan = { inputs: o, days: plan(o, seed) };
    var n = 0;
    lastPlan.days.forEach(function (day, k) {
      var sec = el('section', 'day'), head = el('div', 'day-head');
      head.append(el('b', null, (k + 1) + '日目'), el('span', null, day.area + ', ' + day.date.toLocaleDateString('en', { weekday: 'short', month: 'short', day: 'numeric' })));
      sec.appendChild(head);
      day.meals.forEach(function (m) {
        n++;
        if (!m[2]) { var t = el('article', 'ticket printing'); t.appendChild(el('p', 'empty', 'Sold out for these buttons. Try a bigger budget or another area.')); sec.appendChild(t); return; }
        var tk = ticket(m[2], '食券 ' + m[0] + ' ' + m[1], 'No.' + (k + 1) + String(n).padStart(2, '0'), true, m[3]);
        tk.style.animationDelay = (n * 90) + 'ms'; sec.appendChild(tk);
      });
      out.appendChild(sec);
    });
    cta.hidden = false; $('mailbox').hidden = !ENDPOINT; $('sharebox').hidden = false; $('tipjar').hidden = !TIP_URL;
    $('storyimg').hidden = true; updateShareLinks();
    history.replaceState(null, '', shareUrl());
  }
  function shareUrl() {
    var o = lastPlan.inputs, u = new URL(location.href.split('?')[0]);
    u.searchParams.set('d', o.start); u.searchParams.set('n', o.days); u.searchParams.set('a', o.areas.join(','));
    u.searchParams.set('b', o.band); if (o.avoid.length) u.searchParams.set('x', o.avoid.join(',')); u.searchParams.set('s', lastSeed);
    return u.toString();
  }

  // ---------- gacha ----------
  var seen = {};
  function fillDome() {
    var d = $('dome'), cols = ['#d7262e', '#f2b705', '#2f6db5', '#2e9c5a', '#ff8fb1', '#7b5cd6'];
    d.replaceChildren();
    for (var i = 0; i < 14; i++) { var c = el('span', 'cap'); c.style.setProperty('--c', cols[i % cols.length]); c.style.left = (4 + (i % 4) * 22 + (Math.floor(i / 4) % 2) * 10) + '%'; c.style.top = (74 - Math.floor(i / 4) * 18 - (i % 2) * 4) + '%'; c.style.transform = 'rotate(' + (i * 47 % 180) + 'deg)'; d.appendChild(c); }
  }
  function spin() {
    var h = $('spin'); h.classList.remove('turn'); void h.offsetWidth; h.classList.add('turn');
    var o = readPlanInputs(), areas = o.areas.length ? o.areas : AREAS.map(function (a) { return a[0]; });
    var pool = SHOPS.filter(function (s) { return areas.indexOf(GROUP[s.area]) >= 0 && !excluded(s, o.avoid) && fits(s, o.band); });
    var fresh = pool.filter(function (s) { return !seen[s.name_ja]; }); if (!fresh.length) { seen = {}; fresh = pool; }
    var g = $('gout'); g.replaceChildren();
    if (!fresh.length) { g.appendChild(el('p', 'empty', 'Nothing fits the buttons on the Plan tab. Try a bigger budget.')); return; }
    var s = fresh[Math.floor(Math.random() * fresh.length)]; seen[s.name_ja] = 1;
    var cap = $('capsule'); cap.replaceChildren(); var d = el('div', 'drop'); d.style.setProperty('--c', ['#d7262e', '#f2b705', '#2f6db5', '#2e9c5a'][Math.floor(Math.random() * 4)]); cap.appendChild(d);
    setTimeout(function () { g.replaceChildren(ticket(s, 'ガチャ GACHA', 'No.G' + String(Object.keys(seen).length).padStart(2, '0'), true, s.kind === 'snack' ? 'lunch' : 'dinner')); }, 650);
  }

  // ---------- search ----------
  function search() {
    var q = ($('q').value || '').toLowerCase().trim(), ar = $('sarea').value, day = $('sday').value, tg = picked('tg');
    var res = SHOPS.filter(function (s) {
      if (ar && GROUP[s.area] !== ar) return false;
      if (day !== '' && closedOn(s, +day)) return false;
      if (tg.indexOf('yu') >= 0 && !s.yu_pick) return false;
      if (tg.indexOf('award') >= 0 && !(s.awards || []).length) return false;
      if (tg.indexOf('cheap') >= 0 && s.budget_band !== 'under1500') return false;
      if (tg.indexOf('sweet') >= 0 && s.kind !== 'snack') return false;
      if (q) { var hay = [s.name_en, s.name_ja, s.genre, s.what_to_order, s.area, (s.awards || []).join(' '), s.tourist_tip].join(' ').toLowerCase(); if (hay.indexOf(q) < 0) return false; }
      return true;
    }).sort(function (a, b) { return (b.yu_pick - a.yu_pick) || ((b.awards || []).length - (a.awards || []).length) || a.name_en.localeCompare(b.name_en); });
    var o = $('sout'); o.replaceChildren(); o.appendChild(el('p', 'count', res.length + (res.length === 1 ? ' place' : ' places')));
    res.forEach(function (s, i) { o.appendChild(ticket(s, LABEL[GROUP[s.area]] || s.area, 'No.S' + String(i + 1).padStart(2, '0'), false)); });
  }

  // ---------- modes ----------
  function setMode(m) {
    document.querySelectorAll('.mode').forEach(function (x) { x.hidden = x.dataset.mode !== m; });
    out.hidden = m !== 'plan'; $('gout').hidden = m !== 'gacha'; $('sout').hidden = m !== 'search';
    $('mailbox').hidden = m !== 'plan' || !lastPlan || !ENDPOINT; cta.hidden = m !== 'plan' || !lastPlan;
    $('sharebox').hidden = m !== 'plan' || !lastPlan; $('tipjar').hidden = !TIP_URL || (m === 'plan' && !lastPlan);
    if (m === 'search') search();
    store('koru-mode', m);
  }

  // ---------- build controls ----------
  AREAS.forEach(function (a) { key($('areas'), 'checkbox', 'area', a[0], a[1], a[2], a[3], a[0] === 'akiba' || a[0] === 'ueno'); var op = new Option(a[2], a[0]); $('sarea').appendChild(op); });
  BUDGETS.forEach(function (b) { key($('budget'), 'radio', 'budget', b[0], b[1], b[2], b[3], b[0] === '1500-4000'); });
  AVOID.forEach(function (a) { key($('avoid'), 'checkbox', 'avoid', a[0], a[1], a[2], 'cap-grey', false, true); });
  TOGGLES.forEach(function (t) { key($('toggles'), 'checkbox', 'tg', t[0], t[1], t[2], 'cap-grey', false, true); });
  var d = new Date(); d.setDate(d.getDate() + 14); $('start').value = d.toISOString().slice(0, 10);
  fillDome();

  // restore a shared plan
  var P = new URLSearchParams(location.search), sharedSeed = null;
  if (P.get('s')) {
    if (P.get('d')) $('start').value = P.get('d');
    if (P.get('n')) $('days').value = P.get('n');
    var A = (P.get('a') || '').split(','), X = (P.get('x') || '').split(',');
    document.querySelectorAll('input[name=area]').forEach(function (i) { i.checked = A.indexOf(i.value) >= 0; });
    document.querySelectorAll('input[name=avoid]').forEach(function (i) { i.checked = X.indexOf(i.value) >= 0; });
    document.querySelectorAll('input[name=budget]').forEach(function (i) { i.checked = i.value === P.get('b'); });
    sharedSeed = +P.get('s');
  }

  f.addEventListener('submit', function (e) { e.preventDefault(); renderPlan(Math.floor(Math.random() * 1e9)); out.scrollIntoView({ behavior: 'smooth', block: 'start' }); });
  $('spin').addEventListener('click', spin);
  document.querySelectorAll('input[name=mode]').forEach(function (i) { i.addEventListener('change', function () { setMode(i.value); }); });
  ['q', 'sarea', 'sday'].forEach(function (id) { $(id).addEventListener('input', search); });
  $('toggles').addEventListener('change', search);
  $('share').addEventListener('click', function () {
    var url = shareUrl(), st = $('sstatus');
    if (navigator.clipboard) navigator.clipboard.writeText(url).then(function () { st.textContent = 'Link copied. Anyone with it sees this exact plan.'; }, function () { st.textContent = url; });
    else st.textContent = url;
  });
  $('mail').addEventListener('submit', function (e) {
    e.preventDefault(); var st = $('mstatus');
    if (!ENDPOINT || !lastPlan) return;
    var o = lastPlan.inputs;
    var payload = { email: $('email').value.trim(), country: $('country').value, tips: $('tips').checked, start: o.start, days: o.days, areas: o.areas.join(','), budget: o.band, avoid: o.avoid.join(','), link: shareUrl(),
      plan: lastPlan.days.map(function (dd, k) { return { day: k + 1, date: dd.date.toISOString().slice(0, 10), area: dd.area, meals: dd.meals.filter(function (m) { return m[2]; }).map(function (m) { var s = m[2]; return { slot: m[1], name_en: s.name_en, name_ja: s.name_ja, order: s.what_to_order, hours: s.hours, closed: s.closed_days, station: s.station, maps: 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(s.name_ja) }; }) }; }) };
    st.textContent = 'Sending…';
    fetch(ENDPOINT, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'text/plain;charset=utf-8' }, body: JSON.stringify(payload) })
      .then(function () { st.textContent = 'Sent. Check your inbox in a minute (and the spam folder).'; })
      .catch(function () { st.textContent = 'That did not send. Check your connection and try again.'; });
  });


  // ---------- sharing ----------
  function shareText() { return 'My Tokyo food plan, printed on the Tokyo Food Ticket Machine by a local in Akihabara 🎫'; }
  function updateShareLinks() {
    var u = encodeURIComponent(shareUrl()), t = encodeURIComponent(shareText());
    $('s-wa').href = 'https://wa.me/?text=' + t + '%20' + u;
    $('s-line').href = 'https://social-plugins.line.me/lineit/share?url=' + u;
    $('s-x').href = 'https://twitter.com/intent/tweet?text=' + t + '&url=' + u;
    $('s-fb').href = 'https://www.facebook.com/sharer/sharer.php?u=' + u;
  }
  $('nshare').addEventListener('click', function () {
    var st = $('sstatus');
    if (navigator.share) navigator.share({ title: 'My Tokyo meal tickets', text: shareText(), url: shareUrl() }).catch(function () {});
    else navigator.clipboard && navigator.clipboard.writeText(shareUrl()).then(function () { st.textContent = 'Link copied. Paste it anywhere.'; });
  });
  function storyCanvas() {
    var W = 1080, H = 1920, c = document.createElement('canvas'); c.width = W; c.height = H; var g = c.getContext('2d');
    g.fillStyle = '#c9d2d7'; g.fillRect(0, 0, W, H);
    g.fillStyle = '#dfe5e8'; roundRect(g, 60, 60, W - 120, H - 120, 40); g.fill();
    g.fillStyle = '#17110c'; roundRect(g, 110, 110, W - 220, 120, 20); g.fill();
    g.fillStyle = '#ffa22b'; g.font = '56px "DotGothic16", monospace'; g.textBaseline = 'middle'; g.fillText('MY TOKYO MEAL TICKETS', 150, 172);
    g.fillStyle = '#22303a'; g.font = '84px "Dela Gothic One", sans-serif'; g.textBaseline = 'alphabetic'; g.fillText('東京めし券売機', 120, 350);
    var y = 420, days = lastPlan.days.slice(0, 3);
    days.forEach(function (day, k) {
      g.fillStyle = '#22303a'; g.font = '50px "Dela Gothic One", sans-serif'; g.fillText((k + 1) + '日目', 120, y + 52);
      g.fillStyle = '#5d6b75'; g.font = 'bold 34px "Zen Kaku Gothic New", sans-serif'; g.fillText(day.area, 310, y + 50);
      y += 72;
      day.meals.forEach(function (m) {
        if (!m[2]) return;
        g.fillStyle = '#fffef8'; roundRect(g, 120, y, W - 240, 96, 10); g.fill();
        g.fillStyle = '#d7262e'; g.font = '40px "Dela Gothic One", sans-serif'; g.fillText(m[0], 150, y + 64);
        g.fillStyle = '#2b2f45'; g.font = 'bold 40px "Zen Kaku Gothic New", sans-serif'; g.fillText(fitText(g, m[2].name_en, W - 420), 220, y + 46);
        g.fillStyle = '#6f7287'; g.font = '30px "Zen Kaku Gothic New", sans-serif'; g.fillText(fitText(g, m[2].name_ja, W - 420), 220, y + 82);
        if (m[2].yu_pick) { g.strokeStyle = '#d7262e'; g.lineWidth = 5; g.beginPath(); g.arc(W - 190, y + 48, 36, 0, Math.PI * 2); g.stroke(); g.fillStyle = '#d7262e'; g.font = '26px "Dela Gothic One", sans-serif'; g.textAlign = 'center'; g.fillText('推し', W - 190, y + 58); g.textAlign = 'left'; }
        y += 108;
      });
      y += 16;
    });
    g.fillStyle = '#22303a'; g.font = 'bold 38px "Zen Kaku Gothic New", sans-serif'; g.fillText('Make yours free: link in @koru.tokyo_guide bio', 120, H - 190);
    g.fillStyle = '#5d6b75'; g.font = '30px "Zen Kaku Gothic New", sans-serif'; g.fillText('By Yu, an office worker in Akihabara, and Koru 🐕', 120, H - 135);
    return c;
  }
  function roundRect(g, x, y, w, h, r) { g.beginPath(); g.moveTo(x + r, y); g.arcTo(x + w, y, x + w, y + h, r); g.arcTo(x + w, y + h, x, y + h, r); g.arcTo(x, y + h, x, y, r); g.arcTo(x, y, x + w, y, r); g.closePath(); }
  function fitText(g, t, max) { if (g.measureText(t).width <= max) return t; while (t.length > 3 && g.measureText(t + '…').width > max) t = t.slice(0, -1); return t + '…'; }
  $('story').addEventListener('click', function () {
    var st = $('sstatus');
    (document.fonts ? document.fonts.ready : Promise.resolve()).then(function () {
      var c = storyCanvas();
      c.toBlob(function (blob) {
        var file = new File([blob], 'tokyo-meal-tickets.png', { type: 'image/png' });
        if (navigator.canShare && navigator.canShare({ files: [file] })) {
          navigator.share({ files: [file], title: 'My Tokyo meal tickets' }).catch(function () {});
        } else {
          var img = $('storyimg'); img.src = URL.createObjectURL(blob); img.hidden = false;
          st.textContent = 'Long-press (or right-click) the image to save it, then add it to your story.';
        }
      }, 'image/png');
    });
  });
  if (TIP_URL) document.querySelectorAll('.tip').forEach(function (a) {
    var amt = a.dataset.amt; a.href = amt && TIP_AMOUNT_URL ? TIP_AMOUNT_URL.replace('{amt}', amt) : TIP_URL;
  });

  fetch('shops.json').then(function (r) { return r.json(); }).then(function (j) {
    SHOPS = j; renderKept();
    if (sharedSeed !== null) renderPlan(sharedSeed);
    var m = store('koru-mode'); if (m && m !== 'plan' && sharedSeed === null) { var r = document.querySelector('input[name=mode][value=' + m + ']'); if (r) { r.checked = true; setMode(m); } }
  }).catch(function () { out.textContent = 'The restaurant list did not load. Reload the page to try again.'; });
})();
