/**
 * Tokyo Food Ticket Machine: "email my plan" backend (Google Apps Script web app).
 * Setup (once, by Yu):
 *  1. Open the Google Sheet "Koru planner leads" > Extensions > Apps Script, paste this file, Save.
 *  2. Deploy > New deployment > Web app. Execute as: Me. Who has access: Anyone. Deploy, allow access.
 *  3. Send the Web app URL to Claude (it goes into planner.js as ENDPOINT).
 * Each request appends one row to the "leads" sheet, then emails the plan from this Google account.
 */
var SHEET = 'leads';
var FROM_NAME = 'Yu & Koru (Tokyo food)';

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(10000);
  try {
    var d = JSON.parse((e && e.postData && e.postData.contents) || '{}');
    if (d.action === 'archive') return out(archive(d));
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

function doGet() { return out({ ok: true, service: 'koru planner mailer' }); }

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
