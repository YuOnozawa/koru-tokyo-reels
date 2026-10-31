const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({deviceScaleFactor:1});
for(const [f,bg] of process.argv.slice(2).map(a=>a.split(':'))){const svg=fs.readFileSync(f,'utf8');
await p.setContent(`<html><body style="margin:0;background:${bg||'transparent'}">${svg}</body></html>`);
const el=await p.$('svg');await el.screenshot({path:f.replace('.svg','.png'),omitBackground:!bg});}
await b.close();})();
