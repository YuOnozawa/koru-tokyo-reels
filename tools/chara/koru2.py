import math
INK='#22303a'
def P(x,y): return f'{x:.1f},{y:.1f}'
def tufts(cx,cy,rx,ry,a0,a1,n,amp,sweep=6,base_jit=0):
    """open path of swept fur tufts along an ellipse arc from a0 to a1 (deg)."""
    def pt(a,r_extra=0):
        t=math.radians(a); return (cx+(rx+r_extra)*math.cos(t), cy+(ry+r_extra)*math.sin(t))
    step=(a1-a0)/n
    d='M'+P(*pt(a0))
    for i in range(n):
        a=a0+step*i; b=a+step
        k=amp*(0.8+0.35*math.sin(i*1.9+1))
        tip=pt(a+step*0.5+sweep*(1 if step>0 else -1), k)
        c1=pt(a+step*0.15, k*0.55)
        c2=pt(a+step*0.75, k*0.2)
        d+=' Q'+P(*c1)+' '+P(*tip)+' Q'+P(*c2)+' '+P(*pt(b))
    return d
def koru(x=0,y=0,s=1.0):
    W='#ffffff'; SH='#e6ebef'; SH2='#d5dde3'
    st=f'stroke="{INK}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"'
    S=f'<g transform="translate({x},{y}) scale({s})">'
    # tail: plume curling over back on right
    S+=f'<path d="M150,190 Q196,178 214,130 Q226,92 206,70 Q236,78 244,104 Q256,92 252,74 Q272,96 262,132 Q276,128 280,116 Q284,150 258,176 Q270,178 278,172 Q262,206 220,214 Q190,220 160,214 Z" fill="{W}" {st}/>'
    S+=f'<path d="M214,140 Q236,128 246,110 M222,170 Q248,164 262,146" stroke="{SH2}" stroke-width="4" fill="none" stroke-linecap="round"/>'
    # body (sitting, tapered) with fur edge
    S+=f'<path d="M60,170 Q36,230 44,292 L176,292 Q186,230 162,170 Z" fill="{W}" {st}/>'
    # hind leg hint
    S+=f'<path d="M150,236 Q180,250 176,292" fill="none" stroke="{SH2}" stroke-width="4"/>'
    # front legs
    S+=f'<path d="M78,210 L74,284 Q74,298 90,298 L102,298 L104,212 Z" fill="{W}" {st}/>'
    S+=f'<path d="M140,210 L144,284 Q144,298 128,298 L116,298 L114,212 Z" fill="{W}" {st}/>'
    S+=f'<path d="M86,298 L86,290 M94,298 L94,290 M124,298 L124,290 M132,298 L132,290" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
    # chest ruff: big spitz mane with swept tufts
    S+=f'<path d="M34,96 Q6,146 24,176 Q8,182 4,198 Q28,196 42,206 Q34,222 44,236 Q62,224 78,234 Q84,252 98,256 Q104,242 110,260 Q116,242 122,256 Q136,252 142,234 Q158,224 176,236 Q186,222 178,206 Q192,196 216,198 Q212,182 196,176 Q214,146 186,96 Z" fill="{W}" {st}/>'
    S+=f'<path d="M46,180 Q60,196 70,214 M174,180 Q160,196 150,214 M86,196 Q96,214 100,232 M134,196 Q124,214 120,232" stroke="{SH}" stroke-width="4" fill="none" stroke-linecap="round"/>'
    # ears (tall, slightly outward)
    S+=f'<path d="M46,58 L40,-18 Q42,-26 50,-22 L98,22 Z" fill="{W}" {st}/>'
    S+=f'<path d="M54,40 L52,-4 L84,24 Z" fill="#f4c6c3"/>'
    S+=f'<path d="M174,58 L180,-18 Q178,-26 170,-22 L122,22 Z" fill="{W}" {st}/>'
    S+=f'<path d="M166,40 L168,-4 L136,24 Z" fill="#f4c6c3"/>'
    # head: fox-like with cheek tufts
    S+=f'<path d="M110,14 Q160,14 178,52 Q186,70 200,82 Q186,86 182,94 Q196,102 200,112 Q180,112 168,120 Q150,140 110,146 Q70,140 52,120 Q40,112 20,112 Q24,102 38,94 Q34,86 20,82 Q34,70 42,52 Q60,14 110,14 Z" fill="{W}" {st}/>'
    # forehead shade
    S+=f'<path d="M96,30 Q110,22 124,30" stroke="{SH}" stroke-width="4" fill="none" stroke-linecap="round"/>'
    # eyes: big, round, gentle
    for ex in (80,140):
        S+=f'<ellipse cx="{ex}" cy="70" rx="12.5" ry="13.5" fill="#2b1a12"/><circle cx="{ex+4}" cy="64" r="4.6" fill="#fff"/><circle cx="{ex-4}" cy="76" r="2" fill="#fff" opacity=".75"/>'
    # tear-line hint (spitz)
    S+=f'<path d="M64,84 Q68,90 74,92 M156,84 Q152,90 146,92" stroke="#e7cdbf" stroke-width="3" fill="none" stroke-linecap="round"/>'
    # muzzle
    S+=f'<path d="M96,112 Q110,124 124,112" stroke="{SH}" stroke-width="4" fill="none" stroke-linecap="round"/>'
    S+=f'<path d="M98,96 Q110,90 122,96 Q121,107 110,110 Q99,107 98,96 Z" fill="#111"/><ellipse cx="106" cy="98" rx="3" ry="1.8" fill="#fff" opacity=".7"/>'
    S+=f'<path d="M110,109 L110,114 M100,114 Q105,120 110,114 Q115,120 120,114" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round"/>'
    # collar with tag
    S+=f'<path d="M64,140 Q110,160 156,140" stroke="#ef5a24" stroke-width="9" fill="none" stroke-linecap="round"/><circle cx="110" cy="156" r="8" fill="#ffa22b" stroke="{INK}" stroke-width="3"/>'
    S+='</g>'
    return S
