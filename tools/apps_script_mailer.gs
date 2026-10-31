/**
 * Tokyo Food Ticket Machine backend (Google Apps Script web app): email my plan, reactions
 * (like / want to go / been here), visitor comments + photos (shown only after approval), video archive.
 * Setup (once, by Yu):
 *  1. Open the Google Sheet "Koru planner leads" > Extensions > Apps Script, paste this file, Save.
 *  2. Deploy > New deployment > Web app. Execute as: Me. Who has access: Anyone. Deploy, allow access.
 *  3. Send the Web app URL to Claude (it goes into planner.js as ENDPOINT).
 * Each plan email appends one row to the "leads" sheet, then emails the plan from this Google account.
 * Moderation: new comments/photos land in the "reviews" sheet with status "pending" and you get an email.
 * Change status to "approved" to show it on the site (or "rejected"). Photos stay private until approved.
 */
var SHEET = 'leads';
var FROM_NAME = 'Yu & Koru (Tokyo food)';

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(10000);
  try {
    var d = JSON.parse((e && e.postData && e.postData.contents) || '{}');
    if (d.action === 'archive') return out(archive(d));
    if (d.action === 'event') return out(countEvent(d));
    if (d.action === 'react') return out(react(d));
    if (d.action === 'review') return out(review(d));
    var email = String(d.email || '').trim();
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return out({ ok: false, error: 'bad email' });
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sh = ss.getSheetByName(SHEET) || ss.insertSheet(SHEET);
    if (sh.getLastRow() === 0) {
      sh.appendRow(['received_at', 'email', 'country', 'tips_opt_in', 'start', 'days', 'areas', 'budget', 'avoid', 'link', 'places', 'unsubscribed']);
    }
    var places = [];
    (d.plan || []).forEach(function (day) { (day.meals || []).forEach(function (m) { places.push(m.name_ja); }); });
    sh.appendRow([new Date(), email, d.country || '', d.tips ? 'yes' : 'no', d.start || '', d.days || '', d.areas || '', d.budget || '', d.avoid || '', d.link || '', places.join(' / '), '']);
    MailApp.sendEmail({ to: email, subject: 'Your Tokyo meal tickets', htmlBody: html(d), name: FROM_NAME });
    return out({ ok: true });
  } catch (err) {
    return out({ ok: false, error: String(err) });
  } finally {
    lock.releaseLock();
  }
}

/**
 * Video archive: GitHub Actions posts {action:'archive', url, name} after a reel is published.
 * Only our own repo's videos are accepted. Saves the mp4 into ARCHIVE_FOLDER_ID (falls back to a
 * "koru_reels_archive" folder in My Drive). Skips files that are already there.
 */
var ARCHIVE_FOLDER_ID = '1rzsrehXDUuC1UH_0aTb7msJmGpEYZoEg'; // Drive: TokyoGuide_動画プロジェクト/04_完成動画
var ARCHIVE_URL_PREFIXES = [
  'https://github.com/YuOnozawa/koru-tokyo-reels/releases/download/video-store/',
  'https://yuonozawa.github.io/koru-tokyo-reels/videos/'
];

function archive(d) {
  var url = String(d.url || ''), name = String(d.name || '');
  if (!/^[a-z0-9_]+\.mp4$/i.test(name)) return { ok: false, error: 'bad name' };
  if (!ARCHIVE_URL_PREFIXES.some(function (p) { return url.indexOf(p) === 0; })) return { ok: false, error: 'url not allowed' };
  var folder;
  try { folder = ARCHIVE_FOLDER_ID ? DriveApp.getFolderById(ARCHIVE_FOLDER_ID) : null; } catch (err) { folder = null; }
  if (!folder) {
    var it = DriveApp.getFoldersByName('koru_reels_archive');
    folder = it.hasNext() ? it.next() : DriveApp.createFolder('koru_reels_archive');
  }
  var existing = folder.getFilesByName(name);
  if (existing.hasNext()) { var f0 = existing.next(); return { ok: true, id: f0.getId(), size: f0.getSize(), existed: true }; }
  var res = UrlFetchApp.fetch(url, { followRedirects: true, muteHttpExceptions: true });
  if (res.getResponseCode() !== 200) return { ok: false, error: 'fetch ' + res.getResponseCode() };
  var blob = res.getBlob().setName(name).setContentType('video/mp4');
  if (blob.getBytes().length < 100000) return { ok: false, error: 'too small' };
  var f = folder.createFile(blob);
  return { ok: true, id: f.getId(), size: f.getSize() };
}

function doGet(e) {
  if (e && e.parameter && e.parameter.action === 'community') return out(community());
  return out({ ok: true, service: 'koru planner backend' });
}

// ---------- anonymous usage counts: one row per day + event name ----------
function countEvent(d) {
  var name = String(d.name || '').replace(/[^a-z0-9_]/gi, '').slice(0, 40); if (!name) return { ok: false };
  var day = Utilities.formatDate(new Date(), 'Asia/Tokyo', 'yyyy-MM-dd');
  var sh = sheet('events', ['date', 'event', 'count']), rows = sh.getDataRange().getValues();
  for (var i = rows.length - 1; i >= 1 && i >= rows.length - 400; i--) {
    var rd = rows[i][0] instanceof Date ? Utilities.formatDate(rows[i][0], 'Asia/Tokyo', 'yyyy-MM-dd') : String(rows[i][0]);
    if (rd === day && rows[i][1] === name) { sh.getRange(i + 1, 3).setValue((+rows[i][2] || 0) + 1); return { ok: true }; }
  }
  sh.appendRow([day, name, 1]); return { ok: true };
}

// ---------- community: reactions, comments, photos ----------
var REACTIONS = ['like', 'want', 'been'];
var UGC_FOLDER = 'koru_ugc_photos';
function sheet(name, header) {
  var ss = SpreadsheetApp.getActiveSpreadsheet(), sh = ss.getSheetByName(name) || ss.insertSheet(name);
  if (sh.getLastRow() === 0) sh.appendRow(header);
  return sh;
}
function validSlug(s) { return /^[a-z0-9-]{2,80}$/.test(String(s || '')); }
function react(d) {
  if (!validSlug(d.slug) || REACTIONS.indexOf(d.type) < 0) return { ok: false, error: 'bad input' };
  var delta = d.delta === -1 ? -1 : 1;
  var sh = sheet('reactions', ['slug'].concat(REACTIONS)), rows = sh.getDataRange().getValues(), col = REACTIONS.indexOf(d.type) + 2;
  for (var i = 1; i < rows.length; i++) {
    if (rows[i][0] === d.slug) { var c = sh.getRange(i + 1, col); c.setValue(Math.max(0, (+c.getValue() || 0) + delta)); CacheService.getScriptCache().remove('community'); return { ok: true }; }
  }
  if (delta < 0) return { ok: true };
  var row = [d.slug, 0, 0, 0]; row[col - 1] = 1; sh.appendRow(row);
  CacheService.getScriptCache().remove('community');
  return { ok: true };
}
function review(d) {
  var name = String(d.name || '').trim().slice(0, 40), text = String(d.text || '').trim().slice(0, 500);
  if (!validSlug(d.slug) || !d.consent || (!text && !d.photo)) return { ok: false, error: 'bad input' };
  var fileId = '';
  if (d.photo) {
    var m = /^data:image\/(jpeg|png|webp);base64,(.+)$/.exec(String(d.photo));
    if (!m) return { ok: false, error: 'bad photo' };
    var bytes = Utilities.base64Decode(m[2]);
    if (bytes.length > 2500000) return { ok: false, error: 'photo too big' };
    var it = DriveApp.getFoldersByName(UGC_FOLDER), folder = it.hasNext() ? it.next() : DriveApp.createFolder(UGC_FOLDER);
    fileId = folder.createFile(Utilities.newBlob(bytes, 'image/' + m[1], d.slug + '_' + Date.now() + '.' + (m[1] === 'jpeg' ? 'jpg' : m[1]))).getId();
  }
  var sh = sheet('reviews', ['received_at', 'slug', 'name', 'text', 'photo_file_id', 'status', 'photo_public']);
  sh.appendRow([new Date(), d.slug, name, text, fileId, 'pending', '']);
  try {
    MailApp.sendEmail({ to: Session.getEffectiveUser().getEmail(), subject: 'New visitor comment to check: ' + d.slug,
      body: (name || 'Someone') + ' wrote about ' + d.slug + ':\n\n' + text + (fileId ? '\n\nPhoto: https://drive.google.com/file/d/' + fileId + '/view' : '') +
        '\n\nTo show it on the site, set status to "approved" in the reviews sheet: ' + SpreadsheetApp.getActiveSpreadsheet().getUrl() });
  } catch (err) {}
  return { ok: true, pending: true };
}
function community() {
  var cache = CacheService.getScriptCache(), hit = cache.get('community');
  if (hit) return JSON.parse(hit);
  var counts = {}, reviews = {};
  var r = sheet('reactions', ['slug'].concat(REACTIONS)).getDataRange().getValues();
  for (var i = 1; i < r.length; i++) counts[r[i][0]] = { like: +r[i][1] || 0, want: +r[i][2] || 0, been: +r[i][3] || 0 };
  var sh = sheet('reviews', ['received_at', 'slug', 'name', 'text', 'photo_file_id', 'status', 'photo_public']), v = sh.getDataRange().getValues();
  for (var j = 1; j < v.length; j++) {
    if (String(v[j][5]).toLowerCase() !== 'approved') continue;
    var fid = v[j][4];
    if (fid && v[j][6] !== 'yes') {
      try { DriveApp.getFileById(fid).setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW); sh.getRange(j + 1, 7).setValue('yes'); } catch (err) { fid = ''; }
    }
    (reviews[v[j][1]] = reviews[v[j][1]] || []).push({ name: v[j][2] || 'A traveler', text: v[j][3], date: Utilities.formatDate(new Date(v[j][0]), 'Asia/Tokyo', 'yyyy-MM'),
      photo: fid ? 'https://drive.google.com/thumbnail?id=' + fid + '&sz=w1000' : '' });
  }
  var res = { ok: true, counts: counts, reviews: reviews };
  cache.put('community', JSON.stringify(res), 300);
  return res;
}

function out(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}

function esc(s) {
  return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) {
    return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
  });
}

function html(d) {
  var h = '<div style="font-family:Helvetica,Arial,sans-serif;max-width:560px;margin:auto;color:#22303a">';
  h += '<div style="background:#17110c;color:#ffa22b;padding:14px;border-radius:10px;font-family:monospace;font-size:18px">いらっしゃいませ / your Tokyo meal tickets</div>';
  h += '<p>Here is the plan you printed on the Tokyo Food Ticket Machine. Hours change, so check Google Maps the same morning.</p>';
  (d.plan || []).forEach(function (day) {
    h += '<h2 style="margin:24px 0 8px">Day ' + esc(day.day) + ': ' + esc(day.area) + ' <span style="font-weight:normal;color:#5d6b75;font-size:15px">' + esc(day.date) + '</span></h2>';
    (day.meals || []).forEach(function (m) {
      h += '<div style="background:#fffef8;border:1px dashed #c9c6ba;border-radius:8px;padding:12px 14px;margin:0 0 10px">';
      h += '<div style="font-family:monospace;color:#6f7287">食券 ' + esc(m.slot) + '</div>';
      h += '<div style="font-size:18px;font-weight:bold">' + esc(m.name_en) + ' <span style="color:#6f7287;font-size:14px">' + esc(m.name_ja) + '</span></div>';
      if (m.order && m.order !== 'unknown') h += '<div>&#9654; ' + esc(m.order) + '</div>';
      if (m.hours && m.hours !== 'unknown') h += '<div style="font-size:14px;color:#5d6b75">Hours: ' + esc(m.hours) + '</div>';
      if (m.closed && m.closed !== 'unknown') h += '<div style="font-size:14px;color:#5d6b75">Closed: ' + esc(m.closed) + '</div>';
      h += '<div style="margin-top:6px"><a href="' + esc(m.maps) + '" style="color:#d7262e">Open in Google Maps</a></div></div>';
    });
  });
  h += '<p><a href="' + esc(d.link) + '" style="color:#d7262e">Open this plan on the web</a>. Follow <a href="https://www.instagram.com/koru.tokyo_guide/">@koru.tokyo_guide</a> for more.</p>';
  h += '<p style="font-size:12px;color:#5d6b75">You got this because you asked the planner to email your plan. Reply "unsubscribe" to stop any future emails.</p></div>';
  return h;
}
