/* Offline support: network first, cached copy when there is no signal (e.g. in the subway). */
var C = 'koru-v1';
var CORE = ['./', 'trip/', 'planner/', 'phrases/', 'tips/', 'config.js', 'planner/planner.js', 'planner/shops.json', 'icon-192.png'];
self.addEventListener('install', function (e) { e.waitUntil(caches.open(C).then(function (c) { return c.addAll(CORE); }).catch(function () {})); self.skipWaiting(); });
self.addEventListener('activate', function (e) { e.waitUntil(self.clients.claim()); });
self.addEventListener('fetch', function (e) {
  var u = new URL(e.request.url);
  if (e.request.method !== 'GET' || u.origin !== location.origin || u.pathname.indexOf('/videos/') >= 0) return;
  e.respondWith(fetch(e.request).then(function (r) { if (r.ok) { var cp = r.clone(); caches.open(C).then(function (c) { c.put(e.request, cp); }); } return r; })
    .catch(function () { return caches.match(e.request, { ignoreSearch: true }).then(function (m) { return m || caches.match('trip/'); }); }));
});
