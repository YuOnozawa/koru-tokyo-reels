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
  var SHOPS = [], BY_SLUG = {}, lastPlan = null, lastSeed = 0;

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
  // opts.slot = [dayIndex, slotIndex] adds the edit buttons (swap / choose / skip) used on plan tickets.
  function ticket(s, slot, no, anim, priceField, opts) {
    opts = opts || {};
    var t = el('article', 'ticket' + (anim ? ' printing' : ''));
    if (opts.slot) t.dataset.slot = opts.slot.join('.');
    var top = el('div', 't-top'); top.append(el('span', 'slotname', slot), el('span', null, no)); t.appendChild(top);
    var h = el('h3', 't-name', s.name_en); h.appendChild(el('span', 't-ja', s.name_ja)); t.appendChild(h);
    if (s.yu_pick) { var hk = el('div', 'hanko'); hk.setAttribute('aria-label', "Yu's pick"); hk.append(el('b', null, '推し'), document.createTextNode("Yu's pick")); t.appendChild(hk); }
    if (s.what_to_order && s.what_to_order !== 'unknown') t.appendChild(el('p', 't-order', '▶ ' + s.what_to_order));
    var price = priceField === 'dinner' ? s.dinner_price_yen : s.lunch_price_yen;
    var chips = el('div', 't-chips');
    if (price && price !== 'unknown' && price !== 'n/a') chips.appendChild(el('span', 'chip', '¥ ' + price.replace(/^about /, '~')));
    if (s.station && s.station !== 'unknown') chips.appendChild(el('span', 'chip', '🚉 ' + s.station.replace(/\s*\(.*\)/, '') + (s.walk_min && s.walk_min !== 'unknown' ? ' · ' + s.walk_min + ' min' : '')));
    if ((s.awards || []).length) chips.appendChild(el('span', 'chip award', '🏅 ' + s.awards.length + (s.awards.length > 1 ? ' awards' : ' award')));
    t.appendChild(chips);
    var dl = el('dl', 't-facts');
    function row(d, a, b) { if (!b || b === 'unknown') return; d.append(el('dt', null, a), el('dd', null, b)); }
    row(dl, 'Hours', s.hours); row(dl, 'Closed', s.closed_days); t.appendChild(dl);
    var more = el('details', 't-more'); more.appendChild(el('summary', null, 'More: tips, awards, station'));
    var dl2 = el('dl', 't-facts'); row(dl2, 'Genre', s.genre);
    row(dl2, 'Station', s.station + (s.walk_min && s.walk_min !== 'unknown' ? ', ' + s.walk_min + ' min walk' : ''));
    if ((s.awards || []).length) row(dl2, 'Awards', s.awards.join('; '));
    row(dl2, 'Tip', s.tourist_tip); row(dl2, 'Checked', s.checked);
    more.appendChild(dl2);
    if (dl2.childNodes.length) t.appendChild(more);
    var acts = el('div', 't-actions');
    if (opts.slot) {
      var sw = el('button', 'mini edit', '↻ Swap'); sw.type = 'button'; sw.title = 'Show me a different place for this ticket';
      sw.addEventListener('click', function () { swap(opts.slot[0], opts.slot[1]); });
      var ch = el('button', 'mini edit', '☰ Choose'); ch.type = 'button';
      ch.addEventListener('click', function () { choose(opts.slot[0], opts.slot[1]); });
      var sk = el('button', 'mini edit', '✕ Skip'); sk.type = 'button';
      sk.addEventListener('click', function () { setEdit(opts.slot[0] + '.' + opts.slot[1], '-'); });
      acts.append(sw, ch, sk);
    }
    var keepB = el('button', 'mini', kept().indexOf(s.name_ja) >= 0 ? '★ Kept' : '☆ Keep'); keepB.type = 'button';
    keepB.setAttribute('aria-pressed', kept().indexOf(s.name_ja) >= 0); keepB.addEventListener('click', function () { toggleKeep(s, keepB); });
    var a = el('a', 'mini', 'Map'); a.href = mapsUrl(s); a.target = '_blank'; a.rel = 'noopener';
    acts.append(keepB, a);
    if (s.slug) { var pg = el('a', 'mini', 'Shop page'); pg.href = '../shops/' + s.slug + '/'; acts.appendChild(pg); }
    t.appendChild(acts);
    return t;
  }
  function mapsUrl(s) { return 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(s.name_ja); }

  // ---------- plan ----------
  // EDITS: {"day.slot": slug or "-"(skipped)}; DAYAREA: {day: areaKey}. Both live in the share link.
  var EDITS = {}, DAYAREA = {}, HISTORY = [], SWAPSEEN = {};
  var SLOTS = [['昼', 'LUNCH', 'lunch'], ['甘', 'SWEET STOP', 'lunch'], ['夜', 'DINNER', 'dinner']];
  function readPlanInputs() {
    return { start: $('start').value, days: +$('days').value, areas: picked('area'), band: (f.querySelector('input[name=budget]:checked') || {}).value || '1500-4000', avoid: picked('avoid') };
  }
  function slotOk(s, j) { return j === 1 ? s.kind === 'snack' : s.kind !== 'snack' && (j === 0 ? s.lunch_ok !== false : s.dinner_ok !== false); }
  function baseOk(s, o, k) { return !excluded(s, o.avoid) && fits(s, o.band) && !closedOn(s, k); }
  function dayArea(o, i) { var areas = o.areas.length ? o.areas : ['akiba']; return DAYAREA[i] || areas[i % areas.length]; }
  function plan(o, seed) {
    var start = new Date(o.start + 'T12:00:00'), used = {}, res = [];
    Object.keys(EDITS).forEach(function (key) { if (EDITS[key] !== '-') used[EDITS[key]] = 1; });
    for (var i = 0; i < o.days; i++) {
      var R = rng(seed + i * 7919), date = new Date(start.getTime() + i * 86400000), area = dayArea(o, i), k = date.getDay();
      var score = function (s) { return (s.yu_pick ? 3 : 0) + ((s.awards || []).length ? 2 : 0) + R() * 2; };
      var pool = SHOPS.filter(function (s) { return !used[s.slug] && baseOk(s, o, k); });
      var local = pool.filter(function (s) { return GROUP[s.area] === area; }); if (local.length < 3) local = pool;
      var sc = {}; local.forEach(function (s) { sc[s.slug] = score(s); });
      local.sort(function (a, b) { return sc[b.slug] - sc[a.slug]; });
      var picks = [null, null, null], state = ['auto', 'auto', 'auto'];
      [0, 1, 2].forEach(function (j) {
        var e = EDITS[i + '.' + j];
        if (e === '-') { state[j] = 'skipped'; return; }
        if (e && BY_SLUG[e]) { picks[j] = BY_SLUG[e]; state[j] = 'chosen'; }
      });
      if (state[0] === 'auto') {
        picks[0] = local.find(function (s) { return !used[s.slug] && slotOk(s, 0) && (s.budget_band === 'under1500' || s.budget_band === '1500-4000'); }) || local.find(function (s) { return !used[s.slug] && slotOk(s, 0); }) || null;
        if (picks[0]) used[picks[0].slug] = 1;
      }
      if (state[1] === 'auto') { picks[1] = local.find(function (s) { return !used[s.slug] && slotOk(s, 1); }) || null; if (picks[1]) used[picks[1].slug] = 1; }
      if (state[2] === 'auto') {
        var lf = fam(picks[0] || { genre: '' });
        picks[2] = local.find(function (s) { return !used[s.slug] && slotOk(s, 2) && fam(s) !== lf; }) || local.find(function (s) { return !used[s.slug] && slotOk(s, 2); }) || null;
        if (picks[2]) used[picks[2].slug] = 1;
      }
      res.push({ date: date, k: k, areaKey: area, area: LABEL[area], meals: SLOTS.map(function (sl, j) { return [sl[0], sl[1], picks[j], sl[2], state[j]]; }) });
    }
    return res;
  }
  function planSlugs() { var u = {}; lastPlan.days.forEach(function (d) { d.meals.forEach(function (m) { if (m[2]) u[m[2].slug] = 1; }); }); return u; }
  function alternatives(i, j, allAreas) {
    var o = lastPlan.inputs, d = lastPlan.days[i], used = planSlugs();
    return SHOPS.filter(function (s) { return !used[s.slug] && slotOk(s, j) && baseOk(s, o, d.k) && (allAreas || GROUP[s.area] === d.areaKey); })
      .sort(function (a, b) { return (b.yu_pick - a.yu_pick) || ((b.awards || []).length - (a.awards || []).length) || a.name_en.localeCompare(b.name_en); });
  }
  function setEdit(key, val, msg) {
    HISTORY.push(JSON.stringify({ e: EDITS, y: DAYAREA }));
    if (val === null) delete EDITS[key]; else EDITS[key] = val;
    rerender(key, msg || (val === '-' ? 'Ticket skipped.' : 'Ticket changed.'));
  }
  function undo() {
    var h = HISTORY.pop(); if (!h) return; h = JSON.parse(h); EDITS = h.e; DAYAREA = h.y; rerender(null, 'Undone.');
  }
  function swap(i, j) {
    var key = i + '.' + j, seenL = SWAPSEEN[key] = SWAPSEEN[key] || [];
    var cur = lastPlan.days[i].meals[j][2]; if (cur && seenL.indexOf(cur.slug) < 0) seenL.push(cur.slug);
    var alts = alternatives(i, j, false); if (alts.length < 2) alts = alts.concat(alternatives(i, j, true).filter(function (s) { return alts.indexOf(s) < 0; }));
    if (!alts.length) { toast('No other place fits this slot. Try a bigger budget.'); return; }
    var next = alts.find(function (s) { return seenL.indexOf(s.slug) < 0; });
    if (!next) { SWAPSEEN[key] = []; next = alts[0]; }
    setEdit(key, next.slug, 'Swapped to ' + next.name_en + '.');
  }
  function choose(i, j) {
    var dlg = $('picker'), list = $('pickerlist'), all = $('pickerall');
    $('pickertitle').textContent = 'Day ' + (i + 1) + ' · ' + SLOTS[j][1].toLowerCase();
    function fill() {
      list.replaceChildren();
      var alts = alternatives(i, j, all.checked);
      if (!alts.length) list.appendChild(el('p', 'empty', 'Nothing else fits. Tick "all areas" or change the budget.'));
      alts.forEach(function (s) {
        var b = el('button', 'pick'); b.type = 'button';
        var nm = el('span', 'p-name', s.name_en); if (s.yu_pick) nm.appendChild(el('span', 'p-pick', '推し'));
        b.append(nm, el('span', 'p-meta', [s.genre, (j === 2 ? s.dinner_price_yen : s.lunch_price_yen), all.checked ? s.area : ''].filter(function (x) { return x && x !== 'unknown'; }).join(' · ')));
        b.addEventListener('click', function () { dlg.close(); setEdit(i + '.' + j, s.slug, 'Changed to ' + s.name_en + '.'); });
        list.appendChild(b);
      });
    }
    all.checked = false; all.onchange = fill; fill();
    if (dlg.showModal) dlg.showModal(); else dlg.setAttribute('open', '');
  }
  function rerender(anchorKey, msg) {
    var a = anchorKey && out.querySelector('[data-slot="' + anchorKey + '"]'), before = a ? a.getBoundingClientRect().top : null;
    renderPlan(lastSeed, true);
    var b = anchorKey && out.querySelector('[data-slot="' + anchorKey + '"]');
    if (b && before !== null) window.scrollBy(0, b.getBoundingClientRect().top - before);
    if (msg) toast(msg, HISTORY.length ? undo : null);
  }
  var toastTimer;
  function toast(msg, onUndo) {
    var t = $('toast'); t.replaceChildren(el('span', null, msg));
    if (onUndo) { var u = el('button', null, 'Undo'); u.type = 'button'; u.addEventListener('click', function () { t.hidden = true; onUndo(); }); t.appendChild(u); }
    t.hidden = false; clearTimeout(toastTimer); toastTimer = setTimeout(function () { t.hidden = true; }, 5000);
  }
  function routeUrl(day) {
    var stops = day.meals.filter(function (m) { return m[2]; }).map(function (m) { return m[2].name_ja; });
    if (stops.length < 2) return stops.length ? mapsUrl(day.meals.filter(function (m) { return m[2]; })[0][2]) : null;
    var u = 'https://www.google.com/maps/dir/?api=1&travelmode=transit&origin=' + encodeURIComponent(stops[0]) + '&destination=' + encodeURIComponent(stops[stops.length - 1]);
    if (stops.length > 2) u += '&waypoints=' + encodeURIComponent(stops.slice(1, -1).join('|'));
    return u;
  }
  function renderPlan(seed, quiet) {
    out.replaceChildren();
    if (!SHOPS.length) { out.appendChild(el('p', 'empty', 'Loading the restaurant list. Press print again in a second.')); return; }
    var o = readPlanInputs(); lastSeed = seed; lastPlan = { inputs: o, days: plan(o, seed) };
    // overview
    var ov = el('section', 'overview'); ov.appendChild(el('h2', null, 'Your plan at a glance'));
    lastPlan.days.forEach(function (day, k) {
      var line = el('a', 'ov-day'); line.href = '#day' + (k + 1);
      line.append(el('b', null, 'Day ' + (k + 1)), el('span', 'ov-date', day.date.toLocaleDateString('en', { weekday: 'short', month: 'short', day: 'numeric' }) + ' · ' + day.area),
        el('span', 'ov-stops', day.meals.filter(function (m) { return m[2]; }).map(function (m) { return m[2].name_en.replace(/\s*\(.*\)/, ''); }).join(' → ') || 'nothing yet'));
      ov.appendChild(line);
    });
    var ovActs = el('div', 'ov-acts');
    var cal = el('button', 'mini', '📅 Add to calendar'); cal.type = 'button'; cal.addEventListener('click', downloadIcs);
    ovActs.append(cal);
    ov.appendChild(el('p', 'ov-hint', 'Want to change one thing? Each ticket has ↻ Swap, ☰ Choose and ✕ Skip, and each day has its own area. The rest stays put.'));
    if (Object.keys(EDITS).length || Object.keys(DAYAREA).length) {
      var rs = el('button', 'mini', '⟲ Reset my changes'); rs.type = 'button';
      rs.addEventListener('click', function () { HISTORY.push(JSON.stringify({ e: EDITS, y: DAYAREA })); EDITS = {}; DAYAREA = {}; rerender(null, 'Back to the original tickets.'); });
      ovActs.appendChild(rs);
    }
    ov.appendChild(ovActs); out.appendChild(ov);
    var n = 0;
    lastPlan.days.forEach(function (day, k) {
      var sec = el('section', 'day'); sec.id = 'day' + (k + 1);
      var head = el('div', 'day-head');
      head.append(el('b', null, (k + 1) + '日目'), el('span', null, day.date.toLocaleDateString('en', { weekday: 'short', month: 'short', day: 'numeric' })));
      var sel = el('select', 'daysel'); sel.setAttribute('aria-label', 'Area for day ' + (k + 1));
      AREAS.forEach(function (a) { var op = new Option(a[2], a[0]); op.selected = a[0] === day.areaKey; sel.appendChild(op); });
      sel.addEventListener('change', function () {
        HISTORY.push(JSON.stringify({ e: EDITS, y: DAYAREA }));
        DAYAREA[k] = sel.value; Object.keys(EDITS).forEach(function (key) { if (key.split('.')[0] === String(k)) delete EDITS[key]; });
        rerender(null, 'Day ' + (k + 1) + ' moved to ' + LABEL[sel.value] + '.');
      });
      head.appendChild(sel);
      var ru = routeUrl(day); if (ru) { var r = el('a', 'route', 'Route ↗'); r.href = ru; r.target = '_blank'; r.rel = 'noopener'; head.appendChild(r); }
      sec.appendChild(head);
      day.meals.forEach(function (m, j) {
        n++;
        if (m[4] === 'skipped') {
          var sk = el('div', 'skipped'); sk.dataset.slot = k + '.' + j;
          sk.appendChild(el('span', null, '食券 ' + m[0] + ' ' + m[1] + ' · skipped'));
          var ab = el('button', 'mini', '+ Add back'); ab.type = 'button'; ab.addEventListener('click', function () { setEdit(k + '.' + j, null, 'Added back.'); });
          sk.appendChild(ab); sec.appendChild(sk); return;
        }
        if (!m[2]) {
          var t = el('article', 'ticket'); t.dataset.slot = k + '.' + j; t.appendChild(el('p', 'empty', 'Sold out for these buttons. Try a bigger budget or another area.'));
          var cb = el('button', 'mini', '☰ Choose'); cb.type = 'button'; cb.addEventListener('click', function () { choose(k, j); }); t.appendChild(cb);
          sec.appendChild(t); return;
        }
        var tk = ticket(m[2], '食券 ' + m[0] + ' ' + m[1] + (m[4] === 'chosen' ? ' ✎' : ''), 'No.' + (k + 1) + String(n).padStart(2, '0'), !quiet, m[3], { slot: [k, j] });
        if (!quiet) tk.style.animationDelay = (n * 90) + 'ms';
        sec.appendChild(tk);
      });
      out.appendChild(sec);
    });
    cta.hidden = false; $('mailbox').hidden = !ENDPOINT; $('sharebox').hidden = false; $('tipjar').hidden = !TIP_URL;
    $('storyimg').hidden = true; updateShareLinks();
    history.replaceState(null, '', shareUrl());
  }
  function shareUrl() {
    var o = lastPlan.inputs, u = new URL(location.href.split('?')[0].split('#')[0]);
    u.searchParams.set('d', o.start); u.searchParams.set('n', o.days); u.searchParams.set('a', o.areas.join(','));
    u.searchParams.set('b', o.band); if (o.avoid.length) u.searchParams.set('x', o.avoid.join(',')); u.searchParams.set('s', lastSeed);
    var e = Object.keys(EDITS).map(function (k) { return k + ':' + EDITS[k]; }); if (e.length) u.searchParams.set('e', e.join(','));
    var y = Object.keys(DAYAREA).map(function (k) { return k + ':' + DAYAREA[k]; }); if (y.length) u.searchParams.set('y', y.join(','));
    return u.toString();
  }
  function ymd(d) { return d.getFullYear() + String(d.getMonth() + 1).padStart(2, '0') + String(d.getDate()).padStart(2, '0'); }
  function downloadIcs() {
    var times = [['120000', '133000'], ['153000', '161500'], ['190000', '203000']], L = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Tokyo Food Ticket Machine//EN', 'CALSCALE:GREGORIAN'];
    function esc(s) { return String(s || '').replace(/\\/g, '\\\\').replace(/;/g, '\;').replace(/,/g, '\\,').replace(/\n/g, '\\n'); }
    lastPlan.days.forEach(function (day, k) {
      day.meals.forEach(function (m, j) {
        if (!m[2]) return; var s = m[2], dt = ymd(day.date);
        L.push('BEGIN:VEVENT', 'UID:' + dt + '-' + j + '-' + s.slug + '@koru-tokyo', 'DTSTAMP:' + new Date().toISOString().replace(/[-:]/g, '').slice(0, 15) + 'Z',
          'DTSTART;TZID=Asia/Tokyo:' + dt + 'T' + times[j][0], 'DTEND;TZID=Asia/Tokyo:' + dt + 'T' + times[j][1],
          'SUMMARY:' + esc(m[1].charAt(0) + m[1].slice(1).toLowerCase() + ': ' + s.name_en), 'LOCATION:' + esc(s.name_ja),
          'DESCRIPTION:' + esc(['Order: ' + s.what_to_order, 'Hours: ' + s.hours, 'Closed: ' + s.closed_days, 'Times here are a suggestion. Check hours the same morning.', mapsUrl(s)].join('\n')),
          'URL:' + mapsUrl(s), 'END:VEVENT');
      });
    });
    L.push('END:VCALENDAR');
    var a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([L.join('\r\n')], { type: 'text/calendar' })); a.download = 'tokyo-meal-tickets.ics';
    document.body.appendChild(a); a.click(); a.remove(); toast('Calendar file downloaded. Open it to add the meals.');
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
    (P.get('e') || '').split(',').forEach(function (x) { var p = x.split(':'); if (p.length === 2 && /^\d+\.[0-2]$/.test(p[0])) EDITS[p[0]] = p[1]; });
    (P.get('y') || '').split(',').forEach(function (x) { var p = x.split(':'); if (p.length === 2 && LABEL[p[1]]) DAYAREA[p[0]] = p[1]; });
  }

  f.addEventListener('submit', function (e) { e.preventDefault(); EDITS = {}; DAYAREA = {}; HISTORY = []; SWAPSEEN = {}; renderPlan(Math.floor(Math.random() * 1e9)); out.scrollIntoView({ behavior: 'smooth', block: 'start' }); });
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
  function shareText(short) {
    var head = 'My Tokyo food plan 🎫';
    if (short || !lastPlan) return head + ' (made on the Tokyo Food Ticket Machine, by a local in Akihabara)';
    var icons = ['🍜', '🍡', '🏮'];
    return head + '\n' + lastPlan.days.map(function (d, k) {
      return 'Day ' + (k + 1) + ' · ' + d.date.toLocaleDateString('en', { weekday: 'short', month: 'short', day: 'numeric' }) + ' · ' + d.area + '\n' +
        d.meals.filter(function (m) { return m[2]; }).map(function (m, j) { return icons[SLOTS.findIndex(function (x) { return x[1] === m[1]; })] + ' ' + m[2].name_en.replace(/\s*\(.*\)/, ''); }).join('\n');
    }).join('\n\n') + '\n\nOpen the tickets (hours, what to order, maps):';
  }
  function updateShareLinks() {
    var u = encodeURIComponent(shareUrl()), t = encodeURIComponent(shareText());
    $('s-wa').href = 'https://wa.me/?text=' + t + '%20' + u;
    $('s-line').href = 'https://social-plugins.line.me/lineit/share?url=' + u;
    $('s-x').href = 'https://twitter.com/intent/tweet?text=' + encodeURIComponent(shareText(true)) + '&url=' + u;
    $('s-fb').href = 'https://www.facebook.com/sharer/sharer.php?u=' + u;
  }
  $('nshare').addEventListener('click', function () {
    var st = $('sstatus');
    if (navigator.share) navigator.share({ title: 'My Tokyo meal tickets', text: shareText(), url: shareUrl() }).catch(function () {});
    else navigator.clipboard && navigator.clipboard.writeText(shareText() + '\n' + shareUrl()).then(function () { st.textContent = 'Plan and link copied. Paste it anywhere.'; });
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
    SHOPS = j; j.forEach(function (s) { BY_SLUG[s.slug] = s; }); renderKept();
    if (sharedSeed !== null) renderPlan(sharedSeed);
    var m = store('koru-mode'); if (m && m !== 'plan' && sharedSeed === null) { var r = document.querySelector('input[name=mode][value=' + m + ']'); if (r) { r.checked = true; setMode(m); } }
  }).catch(function () { out.textContent = 'The restaurant list did not load. Reload the page to try again.'; });
})();
