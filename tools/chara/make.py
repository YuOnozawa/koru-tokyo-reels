import math, sys
INK='#22303a'
def fluff(cx,cy,rx,ry,n,amp,start=0,end=360,closed=True,rot=0):
    pts=[]
    for i in range(n+1):
        a=math.radians(start+(end-start)*i/n+rot)
        pts.append((cx+rx*math.cos(a), cy+ry*math.sin(a)))
    d=f'M{pts[0][0]:.1f},{pts[0][1]:.1f}'
    for i in range(n):
        (x1,y1),(x2,y2)=pts[i],pts[i+1]
        mx,my=(x1+x2)/2,(y1+y2)/2
        vx,vy=mx-cx,my-cy; L=math.hypot(vx,vy) or 1
        k=amp*(1+0.25*math.sin(i*2.3))
        d+=f' Q{mx+vx/L*k:.1f},{my+vy/L*k:.1f} {x2:.1f},{y2:.1f}'
    return d+(' Z' if closed else '')

def yu(x=0,y=0,arm='wave'):
    S=f'<g transform="translate({x},{y})">'
    skin='#f7d6bb'; skin2='#ecb898'; hair='#1b1d22'; top='#24272d'; pants='#3d4b62'
    # legs
    S+=f'<path d="M262,760 L258,905 Q258,915 268,915 L300,915 Q306,915 306,905 L312,760 Z" fill="{pants}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
    S+=f'<path d="M338,760 L344,905 Q344,915 352,915 L384,915 Q394,915 392,905 L388,760 Z" fill="{pants}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
    S+=f'<path d="M248,915 Q248,890 272,895 L306,898 Q318,900 316,918 L316,928 L250,928 Z" fill="#6b4630" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
    S+=f'<path d="M340,898 L374,895 Q400,890 400,915 L400,928 L336,928 L336,918 Q334,900 340,898 Z" fill="#6b4630" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
    # torso (turtleneck)
    S+=f'<path d="M232,560 Q240,500 300,492 L350,492 Q410,500 418,560 L404,780 Q325,796 246,780 Z" fill="{top}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
    S+=f'<path d="M286,470 L364,470 L366,505 Q325,520 284,505 Z" fill="#2e3239" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
    S+=f'<path d="M290,486 Q325,496 360,486 M291,498 Q325,508 359,498" stroke="#454b55" stroke-width="3" fill="none"/>'
    # left arm (viewer left) down holding leash
    S+=f'<path d="M240,560 Q212,640 222,712 L252,716 Q256,650 268,590 Z" fill="{top}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
    S+=f'<circle cx="236" cy="726" r="20" fill="{skin}" stroke="{INK}" stroke-width="6"/>'
    if arm=='wave':
        S+=f'<path d="M410,556 Q462,520 478,452 L448,440 Q430,500 392,522 Z" fill="{top}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
        S+=f'<g transform="rotate(-12 466 418)"><path d="M444,440 Q440,402 446,394 Q450,388 456,394 L458,410 L460,382 Q462,374 469,376 Q474,378 473,386 L472,408 L478,386 Q481,378 488,381 Q493,384 491,392 L484,416 L492,402 Q497,396 502,400 Q506,405 501,413 Q492,440 478,450 Z" fill="{skin}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/></g>'
    elif arm=='phone':
        S+=f'<path d="M410,560 Q440,620 410,668 L384,650 Q398,620 388,590 Z" fill="{top}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
        S+=f'<g transform="rotate(-10 400 640)"><rect x="372" y="580" width="66" height="112" rx="12" fill="#17110c" stroke="{INK}" stroke-width="5"/><rect x="379" y="590" width="52" height="88" rx="6" fill="#ffa22b"/><rect x="386" y="600" width="38" height="10" rx="3" fill="#17110c"/><rect x="386" y="616" width="38" height="5" rx="2" fill="#9d141a"/><rect x="386" y="626" width="28" height="5" rx="2" fill="#9d141a"/><rect x="386" y="650" width="38" height="18" rx="4" fill="#d7262e"/></g>'
        S+=f'<circle cx="398" cy="664" r="19" fill="{skin}" stroke="{INK}" stroke-width="6"/>'
    # neck shadow
    # ears
    S+=f'<ellipse cx="206" cy="318" rx="20" ry="28" fill="{skin}" stroke="{INK}" stroke-width="6"/>'
    S+=f'<ellipse cx="444" cy="318" rx="20" ry="28" fill="{skin}" stroke="{INK}" stroke-width="6"/>'
    S+=f'<path d="M204,306 Q212,318 206,330 M446,306 Q438,318 444,330" stroke="{skin2}" stroke-width="5" fill="none" stroke-linecap="round"/>'
    # face
    S+=f'<path d="M212,250 Q210,180 325,176 Q440,180 438,250 L436,338 Q430,428 325,464 Q220,428 214,338 Z" fill="{skin}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
    # hair: volume swept up and to viewer's right, part on viewer's left
    S+=f'<path d="M206,304 Q186,206 226,156 Q262,104 330,92 Q392,80 440,118 Q484,156 470,214 Q462,262 452,302 L440,304 Q444,262 432,238 Q420,214 392,210 Q340,204 300,224 Q276,236 262,232 Q244,256 230,304 Z" fill="{hair}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
    S+=f'<path d="M262,232 Q258,196 296,170 Q350,138 430,152" stroke="#3a3f48" stroke-width="5" fill="none" stroke-linecap="round"/>'
    S+=f'<path d="M300,224 Q330,186 392,180 Q430,180 448,196" stroke="#3a3f48" stroke-width="4" fill="none" stroke-linecap="round"/>'
    S+=f'<path d="M282,128 Q340,100 404,112" stroke="#4b515c" stroke-width="7" fill="none" stroke-linecap="round"/>'
    # blush
    S+=f'<ellipse cx="252" cy="372" rx="22" ry="11" fill="#f2a08a" opacity=".45"/><ellipse cx="398" cy="372" rx="22" ry="11" fill="#f2a08a" opacity=".45"/>'
    # eyebrows
    S+=f'<path d="M248,268 Q275,256 300,266 M350,266 Q375,256 402,268" stroke="{hair}" stroke-width="8" fill="none" stroke-linecap="round"/>'
    # happy eyes
    S+=f'<path d="M258,322 Q275,302 292,322 M358,322 Q375,302 392,322" stroke="{INK}" stroke-width="7" fill="none" stroke-linecap="round"/>'
    # glasses
    S+=f'<rect x="236" y="286" width="80" height="62" rx="20" fill="#ffffff" fill-opacity=".14" stroke="#141518" stroke-width="10"/>'
    S+=f'<rect x="334" y="286" width="80" height="62" rx="20" fill="#ffffff" fill-opacity=".14" stroke="#141518" stroke-width="10"/>'
    S+=f'<path d="M316,302 Q325,294 334,302" stroke="#141518" stroke-width="8" fill="none"/>'
    S+=f'<path d="M236,302 L214,298 M414,302 L436,298" stroke="#141518" stroke-width="8" stroke-linecap="round"/>'
    S+=f'<path d="M250,296 L266,296 M348,296 L364,296" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".7"/>'
    # nose
    S+=f'<path d="M322,350 Q316,366 326,370" stroke="{skin2}" stroke-width="5" fill="none" stroke-linecap="round"/>'
    # big smile
    S+=f'<path d="M276,388 Q325,382 374,388 Q368,436 325,438 Q282,436 276,388 Z" fill="#7a2a2a" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
    S+=f'<path d="M282,392 Q325,386 368,392 L364,406 Q325,412 286,406 Z" fill="#fffaf2"/>'
    S+=f'<path d="M300,428 Q325,418 350,428 Q338,436 325,436 Q312,436 300,428 Z" fill="#e0676b"/>'
    S+='</g>'
    return S

from koru3 import koru, ANCHOR, BOTTOM

def full(arm='wave', bg=None, W=780, H=960):
    out=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
    if bg: out+=f'<rect width="{W}" height="{H}" fill="{bg}"/>'
    out+=f'<ellipse cx="420" cy="930" rx="320" ry="22" fill="#000" opacity=".12"/>'
    out+=yu(20,0,arm)
    # leash from hand (256,726) to koru collar
    ks=1.08; kx,ky=440,928-BOTTOM*ks
    cx,cy=kx+ANCHOR[0]*ks,ky+ANCHOR[1]*ks
    out+=f'<path d="M256,736 Q{(256+cx)/2:.0f},{max(736,cy)+70:.0f} {cx:.0f},{cy:.0f}" stroke="#ef5a24" stroke-width="7" fill="none" stroke-linecap="round"/>'
    out+=koru(kx,ky,ks)
    out+='</svg>'
    return out

def avatar(bg='#ffa22b'):
    out='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="600" height="600"><defs><clipPath id="c"><circle cx="300" cy="300" r="300"/></clipPath></defs><g clip-path="url(#c)">'
    out+=f'<rect width="600" height="600" fill="{bg}"/>'
    out+=yu(-90,40,'none')
    out+=koru(322,300,1.18)
    out+='</g></svg>'
    return out

if __name__=='__main__':
    open('chara_wave.svg','w').write(full('wave'))
    open('chara_phone.svg','w').write(full('phone'))
    open('avatar.svg','w').write(avatar())
