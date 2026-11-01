const { chromium } = require('playwright'); const fs = require('fs'); const { execFileSync } = require('child_process');
const OUT = '/home/claude/render/app/clips';
const css = `@font-face{font-family:"Dela Gothic One";src:url(http://localhost:8766/DelaGothicOne-Regular.ttf)}@font-face{font-family:"DotGothic16";src:url(http://localhost:8766/DotGothic16-Regular.ttf)}@font-face{font-family:"Zen Kaku Gothic New";font-weight:900;src:url(http://localhost:8766/ZenKakuGothicNew-Black.ttf)}@font-face{font-family:"Zen Kaku Gothic New";font-weight:400 700;src:url(http://localhost:8766/ZenKakuGothicNew-Bold.ttf)}`;
const sleep = ms => new Promise(r => setTimeout(r, ms));
async function smooth(p, to, ms) { await p.evaluate(([to, ms]) => new Promise(res => { const y0 = scrollY, t0 = performance.now(); (function f(t) { const k = Math.min(1, (t - t0) / ms), e = k < .5 ? 2*k*k : 1 - Math.pow(-2*k + 2, 2) / 2; scrollTo(0, y0 + (to - y0) * e); k < 1 ? requestAnimationFrame(f) : res(); })(t0); }), [to, ms]); }
const yOf = (p, sel, off = 120) => p.evaluate(([sel, off]) => { const e = document.querySelector(sel); return e.getBoundingClientRect().top + scrollY - off; }, [sel, off]);
async function clip(b, name, url, pre, act) {
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, serviceWorkers: 'block' });
  const p = await ctx.newPage(); await p.route('https://fonts.googleapis.com/**', r => r.fulfill({ contentType: 'text/css', body: css }));
  await p.addInitScript(() => { const d = new Date(); d.setDate(d.getDate() + 14); try { localStorage.clear(); localStorage.setItem('koru-trip', JSON.stringify({ start: d.toISOString().slice(0, 10), days: 3 })); } catch (e) {}
    const fake = { lang: 'ja-JP', name: 'Kyoko' };
    Object.defineProperty(window, 'speechSynthesis', { value: { getVoices: () => [fake], cancel() {}, speak(u) { setTimeout(() => u.onend && u.onend(), 1200); }, onvoiceschanged: null } });
    window.SpeechSynthesisUtterance = function (t) { this.text = t; }; });
  await p.goto('http://localhost:8765/' + url); await p.evaluate(() => document.fonts.ready); await sleep(600);
  if (pre) await pre(p);
  const dir = `${OUT}/${name}`; fs.rmSync(dir, { recursive: true, force: true }); fs.mkdirSync(dir + '/f', { recursive: true });
  const cdp = await ctx.newCDPSession(p); const frames = []; let t0 = null;
  cdp.on('Page.screencastFrame', async f => { const ts = f.metadata.timestamp; if (t0 === null) t0 = ts; fs.writeFileSync(`${dir}/f/${String(frames.length).padStart(5, '0')}.jpg`, Buffer.from(f.data, 'base64')); frames.push(ts - t0); cdp.send('Page.screencastFrameAck', { sessionId: f.sessionId }).catch(() => {}); });
  await cdp.send('Page.startScreencast', { format: 'jpeg', quality: 92, maxWidth: 780, maxHeight: 1688, everyNthFrame: 1 });
  await sleep(300); const T0 = Date.now(); await act(p); const total = (Date.now() - T0) / 1000 + 0.3;
  await sleep(300); await cdp.send('Page.stopScreencast'); await sleep(200);
  let lst = ''; for (let i = 0; i < frames.length; i++) { const d = i + 1 < frames.length ? frames[i + 1] - frames[i] : 0.3; lst += `file 'f/${String(i).padStart(5, '0')}.jpg'\nduration ${d.toFixed(3)}\n`; }
  lst += `file 'f/${String(frames.length - 1).padStart(5, '0')}.jpg'\n`; fs.writeFileSync(`${dir}/list.txt`, lst);
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', `${dir}/list.txt`, '-vf', 'fps=30,scale=780:1688', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '16', `${OUT}/${name}.mp4`]);
  console.log(name, frames.length, 'frames', frames[frames.length - 1].toFixed(2), 's');
  await ctx.close();
}
const only = process.argv.slice(2);
(async () => { const b = await chromium.launch(); fs.mkdirSync(OUT, { recursive: true });
  const want = n => !only.length || only.includes(n);
  if (want('hook')) await clip(b, 'hook', 'planner/', async p => {
      await p.locator('label.key:has-text("Asakusa")').click(); await p.evaluate(() => document.getElementById('f').requestSubmit()); await sleep(3500);
      await p.evaluate(() => scrollTo(0, document.querySelector('#out .ticket').getBoundingClientRect().top + scrollY - 60)); await sleep(500); },
    async p => { await sleep(400); const y = await p.evaluate(() => scrollY); await smooth(p, y + 1500, 3200); await sleep(300); });
  if (want('plan')) await clip(b, 'plan', 'planner/', null, async p => {
      await smooth(p, await yOf(p, '#areas', 200), 700); await sleep(250);
      await p.locator('label.key:has-text("Asakusa")').click(); await sleep(450);
      await p.locator('label.key:has-text("Kanda")').click(); await sleep(400);
      await smooth(p, await yOf(p, '#budget', 260), 600); await sleep(200);
      await p.locator('label.key:has-text("¥1,500")').first().click(); await sleep(500);
      await smooth(p, await yOf(p, '#f button[type=submit]', 520), 500); await sleep(250);
      await p.evaluate(() => document.getElementById('f').requestSubmit()); await sleep(2600);
      await smooth(p, await yOf(p, '#out .ticket[data-slot]', 70), 700); await sleep(900);
      await p.locator('#out .ticket[data-slot] button.mini.edit').first().click(); await sleep(1800); });
  if (want('shop')) await clip(b, 'shop', 'shops/indira/', null, async p => {
      await sleep(900); await smooth(p, await yOf(p, 'dl, table, .facts', 160).catch(() => 380), 1100); await sleep(2000);
      await smooth(p, await p.evaluate(() => scrollY + 380), 900); await sleep(1600); });
  if (want('phr')) await clip(b, 'phr', 'phrases/', async p => {
      await p.evaluate(() => { const e = [...document.querySelectorAll('.ticket')].find(t => t.dataset.ja === 'いただきます'); scrollTo(0, e.getBoundingClientRect().top + scrollY - 140); }); await sleep(300); },
    async p => { await sleep(500);
      await p.evaluate(() => { const t = [...document.querySelectorAll('.ticket')].find(t => t.dataset.ja === 'いただきます'); t.querySelector('.play').click(); }); await sleep(1700);
      await p.evaluate(() => document.getElementById('cardBtn').click()); await sleep(600);
      await p.locator('#foods label:has-text("shrimp")').click(); await sleep(450); await p.locator('#foods label:has-text("peanuts")').click(); await sleep(400);
      await p.evaluate(() => document.getElementById('card').scrollIntoView({ block: 'center', behavior: 'smooth' })); await sleep(2200); });
  for (const a of only.filter(x => x.startsWith('shop:'))) { const slug = a.slice(5); await clip(b, 'shop_' + slug, 'shops/' + slug + '/', null, async p => {
      await sleep(900); await smooth(p, await yOf(p, 'dl, table, .facts', 160).catch(() => 380), 1100); await sleep(2000);
      await smooth(p, await p.evaluate(() => scrollY + 380), 900); await sleep(1600); }); }
  for (const a of only.filter(x => x.startsWith('search:'))) { const [_, day, q] = a.split(':'); await clip(b, 'search_' + (day||'any') + '_' + (q||'all'), 'planner/?m=search', null, async p => {
      await sleep(700); await p.evaluate(([day, q]) => { if (day !== '') { const s = document.getElementById('sday'); s.value = day; s.dispatchEvent(new Event('input', {bubbles:true})); } if (q) { const i = document.getElementById('q'); i.value = q; i.dispatchEvent(new Event('input', {bubbles:true})); } }, [day === 'any' ? '' : day, q || '']); await sleep(1200);
      await smooth(p, await yOf(p, '#sout', 120), 1000); await sleep(2200); }); }
  if (want('hub')) await clip(b, 'hub', '', null, async p => { await sleep(1200); await smooth(p, 220, 1400); await sleep(1600); });
  await b.close(); })();
