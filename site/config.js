/* Site-wide settings. Fill these in and every page picks them up.
   ENDPOINT       = Apps Script web app URL (plan emails, likes/photos, usage counts). Empty = those features stay hidden.
   TIP_URL        = tip page (Ko-fi, Buy Me a Coffee, Stripe Payment Link with "customer chooses price", PayPal.me...). Empty = tip jar hidden.
   TIP_AMOUNT_URL = optional page that takes a preset amount, {amt} is replaced, e.g. 'https://paypal.me/NAME/{amt}USD'. */
window.KORU = {
  ENDPOINT: '',
  TIP_URL: '',
  TIP_AMOUNT_URL: ''
};
/* Anonymous usage counts (no personal data): koruEvent('plan_print') etc. Sent only when ENDPOINT is set. */
window.koruEvent = function (name, extra) {
  try {
    if (!window.KORU.ENDPOINT) return;
    var body = JSON.stringify({ action: 'event', name: String(name).slice(0, 40), page: location.pathname.split('/').filter(Boolean).pop() || 'home', extra: extra ? String(extra).slice(0, 60) : '' });
    if (navigator.sendBeacon) navigator.sendBeacon(window.KORU.ENDPOINT, new Blob([body], { type: 'text/plain' }));
    else fetch(window.KORU.ENDPOINT, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'text/plain' }, body: body });
  } catch (e) {}
};

/* Offline support + install as an app (saved trips last longer when opened from the home screen). */
(function () {
  try {
    var base = (document.currentScript && document.currentScript.src || '').replace(/config\.js.*$/, '');
    if ('serviceWorker' in navigator && base) navigator.serviceWorker.register(base + 'sw.js', { scope: base }).catch(function () {});
  } catch (e) {}
  window.koruInApp = /Instagram|FBAN|FBAV|FB_IAB|Line\/|TikTok|musical_ly/i.test(navigator.userAgent || '');
  window.koruIOS = /iPhone|iPad|iPod/i.test(navigator.userAgent || '');
  window.koruStandalone = (window.matchMedia && matchMedia('(display-mode: standalone)').matches) || navigator.standalone === true;
})();
