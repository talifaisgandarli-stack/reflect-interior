import os
from PIL import Image
S=os.path.dirname(os.path.abspath(__file__))
R={f[:-4]:Image.open(f'{S}/img/{f}').width/Image.open(f'{S}/img/{f}').height for f in os.listdir(f'{S}/img')}
FR='fontsource-cormorant-garamond-5.3.0/files/cormorant-garamond'
FJ='fontsource-jost-5.3.0/files/jost'
G='#0F2A22'; GOLD='#B08D57'; BG='#F6F1E8'
W,H,P=420,297,14
CW=W-2*P; CH=H-2*P-26  # content height
pages=[]; N=[0]
def frame(body, title='', dark=False, idx=True):
    N[0]+=1
    hdr='' if dark else f'''<div class="hdr"><span class="brand">SPRING · CAKE BOUTIQUE</span><span class="sec">{title}</span><span class="no">{N[0]:02d}</span></div>'''
    ftr=f'''<div class="ftr {'d' if dark else ''}"><span class="reflect">REFLECT <b>ARCHITECTS</b></span><span>Konsept moodboard · Bakı · 2026</span></div>'''
    pages.append(f'<section class="page {"dark" if dark else ""}">{hdr}<div class="body">{body}</div>{ftr}</section>')
def row(items, h=None, gap=5, maxw=CW, maxh=CH-10):
    rs=sum(R[i] for i,_ in items); hh=min((maxw-gap*(len(items)-1))/rs, maxh) if h is None else h
    out=''.join(f'<figure style="width:{R[i]*hh:.1f}mm"><img src="img/{i}.jpg" style="height:{hh:.1f}mm"><figcaption>{c}</figcaption></figure>' for i,c in items)
    return f'<div class="row" style="gap:{gap}mm">{out}</div>'
def swatches(lst):
    return '<div class="sw">'+''.join(f'<div><i style="background:{c}"></i><span>{n}</span></div>' for c,n in lst)+'</div>'
# 1 cover
frame(f'''<div class="cover">
<div class="cl"><img class="logo" src="spring-logo.png"><div class="kicker">Konsept moodboard</div><h1>İki istiqamət</h1>
<div class="ab"><span><b>A</b> The Cake Table</span><span><b>B</b> London Tea Room</span></div></div>
<div class="cr">{row([("s1-000",""),("s2-003","")],h=205,gap=5)}</div></div>''', dark=True)
def divider(letter,name,logic,keys,img):
    h=CH; w=R[img]*h
    frame(f'''<div class="div"><div class="dt"><div class="big">{letter}</div><h2>{name}</h2><p class="logic">{logic}</p><div class="keys">{"".join(f"<span>{k}</span>" for k in keys)}</div></div>
    <img src="img/{img}.jpg" style="height:{h}mm;width:{w:.1f}mm;object-fit:cover"></div>''', title=f'Konsept {letter}')
A='Konsept A — The Cake Table'; B='Konsept B — London Tea Room'
divider('A','The Cake Table','Tort masada. Səma tavanda. Mətbəx göz önündə.',['Masa','Səma','Səmimiyyət'],'s1-000')
frame(row([('s1-001','Rənglənmiş tavan'),('s1-002','Şüşə qapaqlar'),('s1-003','Seçim anı')]),A)
frame(row([('s1-004','Mətbəx pəncərəsi · kassa'),('s1-005','Skamya'),('s1-006','Pəncərə sərisi')]),A)
frame(row([('s1-008','Fasad'),('s1-007','Oxlov tutacaq'),('s1-009','Əl işi')]),A)
pa=[('#EFD9A0','Yağ sarısı'),('#B9CDA1','Püstə'),('#B88A55','Bal palıd'),('#C7714E','Terakota'),('#CFE0E3','Səma'),('#E9CFC2','Krem mərmər')]
frame(f'<div class="pm">{row([("s1-011","Plan"),("s1-010","Materiallar")],maxw=CW-70)}{swatches(pa)}</div>',A)
divider('B','London Tea Room','Divarlar hekayə danışır, piştaxta tort kimi qatlanır.',['Qalereya','Qat-qat','Yaşıl salon'],'s2-003')
frame(row([('s2-001','Qalereya divarı'),('s2-002','Hekayə'),('s2-006','Çay vaxtı')]),B)
frame(row([('s2-004','Piştaxta'),('s2-005','Qat-qat forma'),('s2-008','Konsultasiya nişi')]),B)
# P10 custom: tall + stacked
hh=CH-10; wt=R['s2-007']*hh; Wc=(hh-5-6)/(1/R['s2-010']+1/R['s2-009'])
frame(f'''<div class="row" style="gap:5mm"><figure style="width:{wt:.1f}mm"><img src="img/s2-007.jpg" style="height:{hh:.1f}mm"><figcaption>Pəncərə skamyası</figcaption></figure>
<div class="stack" style="width:{Wc:.1f}mm"><figure><img src="img/s2-010.jpg" style="width:{Wc:.1f}mm"><figcaption>Divar üçün əsərlər</figcaption></figure>
<figure><img src="img/s2-009.jpg" style="width:{Wc:.1f}mm"><figcaption>Oxlov çırağı</figcaption></figure></div></div>''',B)
pb=[('#F4EFE6','İsti ağ'),('#A9B79A','Adaçayı'),('#6E4A33','Qoz'),('#E3B8AA','Tort çəhrayısı'),('#C8402F','Pomidor'),('#D9A53A','Xardal')]
frame(f'<div class="pm">{row([("s2-000","Plan"),("s2-011","Materiallar")],maxw=CW-70)}{swatches(pb)}</div>',B)
# compare
hc=150
frame(f'''<div class="cmp"><div><img src="img/s1-000.jpg" style="height:{hc}mm;width:{R["s1-000"]*hc:.0f}mm"><div class="cl2"><b>A</b><h3>The Cake Table</h3><p>Masa · Səma · Səmimiyyət</p></div></div>
<div><img src="img/s2-001.jpg" style="height:{hc}mm;width:{R["s2-001"]*hc:.0f}mm"><div class="cl2"><b>B</b><h3>London Tea Room</h3><p>Qalereya · Qat-qat · Yaşıl salon</p></div></div></div>''','A / B')
# closing
frame('''<div class="close"><img class="logo" src="spring-logo.png"><div class="by">Hazırladı</div><div class="reflect big2">REFLECT <b>ARCHITECTS</b></div></div>''',dark=True)
css=f'''
@font-face{{font-family:CG;src:url({FR}-latin-400-normal.woff2)}}@font-face{{font-family:CG;src:url({FR}-latin-ext-400-normal.woff2);unicode-range:U+0100-024F,U+0259,U+018F}}
@font-face{{font-family:CG;font-style:italic;src:url({FR}-latin-400-italic.woff2)}}@font-face{{font-family:CG;font-style:italic;src:url({FR}-latin-ext-400-italic.woff2);unicode-range:U+0100-024F,U+0259,U+018F}}
@font-face{{font-family:CG;font-weight:500;src:url({FR}-latin-500-normal.woff2)}}@font-face{{font-family:CG;font-weight:500;src:url({FR}-latin-ext-500-normal.woff2);unicode-range:U+0100-024F,U+0259,U+018F}}
@font-face{{font-family:J;src:url({FJ}-latin-400-normal.woff2)}}@font-face{{font-family:J;src:url({FJ}-latin-ext-400-normal.woff2);unicode-range:U+0100-024F,U+0259,U+018F}}
@font-face{{font-family:J;font-weight:500;src:url({FJ}-latin-500-normal.woff2)}}@font-face{{font-family:J;font-weight:500;src:url({FJ}-latin-ext-500-normal.woff2);unicode-range:U+0100-024F,U+0259,U+018F}}
@page{{size:{W}mm {H}mm;margin:0}}*{{box-sizing:border-box;margin:0}}body{{background:#888}}
.page{{width:{W}mm;height:{H}mm;padding:{P}mm;background:{BG};color:{G};font-family:J;position:relative;display:flex;flex-direction:column;page-break-after:always;overflow:hidden;margin:0 auto}}
.page.dark{{background:{G};color:#EFE6D2}}
.hdr{{display:flex;justify-content:space-between;align-items:baseline;font-size:8pt;letter-spacing:.25em;height:8mm}}
.hdr .brand{{font-family:CG;font-weight:500;font-size:10pt;letter-spacing:.3em}}.hdr .sec{{text-transform:uppercase;color:{GOLD}}}
.body{{flex:1;display:flex;align-items:center;justify-content:center}}
.ftr{{height:10mm;display:flex;justify-content:space-between;align-items:flex-end;font-size:7.5pt;letter-spacing:.2em;text-transform:uppercase;color:#6d6a60;border-top:.3mm solid #d8cdb8;padding-top:3mm}}
.ftr.d{{border-color:rgba(239,230,210,.25);color:rgba(239,230,210,.7)}}
.reflect{{font-family:J;letter-spacing:.42em;font-size:8.5pt;color:{G}}}.ftr.d .reflect,.close .reflect{{color:#EFE6D2}}.reflect b{{font-weight:500}}
.row{{display:flex;align-items:flex-start;justify-content:center}}
figure img{{display:block;width:100%;object-fit:cover}}figcaption{{font-size:7.5pt;letter-spacing:.22em;text-transform:uppercase;margin-top:3mm;color:#5b5a50}}
.dark figcaption{{display:none}}
.stack{{display:flex;flex-direction:column;gap:6mm}}
.cover{{display:flex;width:100%;height:100%;align-items:center;justify-content:space-between}}
.cl{{width:150mm}}.logo{{width:62mm;height:62mm;display:block}}
.kicker{{margin-top:14mm;font-size:8pt;letter-spacing:.35em;text-transform:uppercase;color:{GOLD}}}
h1{{font-family:CG;font-weight:400;font-size:54pt;line-height:1;margin-top:4mm}}
.ab{{margin-top:10mm;display:flex;flex-direction:column;gap:3mm;font-family:CG;font-size:16pt}}.ab b{{font-family:J;font-weight:500;font-size:9pt;color:{GOLD};margin-right:5mm;letter-spacing:.2em}}
.div{{display:flex;width:100%;height:100%;justify-content:space-between;align-items:center}}
.dt{{width:150mm}}.big{{font-family:CG;font-size:150pt;line-height:.8;color:{GOLD}}}
h2{{font-family:CG;font-weight:400;font-size:40pt;margin-top:6mm}}
.logic{{font-family:CG;font-style:italic;font-size:17pt;line-height:1.35;margin-top:8mm;max-width:120mm}}
.keys{{margin-top:12mm;display:flex;gap:4mm}}.keys span{{border:.3mm solid {G};padding:2mm 4mm;font-size:8pt;letter-spacing:.25em;text-transform:uppercase}}
.pm{{display:flex;align-items:flex-start;gap:10mm}}
.sw{{display:flex;flex-direction:column;gap:4mm;width:55mm;padding-top:2mm}}.sw div{{display:flex;align-items:center;gap:4mm;font-size:7.5pt;letter-spacing:.18em;text-transform:uppercase}}
.sw i{{width:16mm;height:16mm;border-radius:50%;border:.2mm solid rgba(0,0,0,.08);display:block}}
.cmp{{display:flex;gap:14mm;justify-content:center}}.cmp>div{{display:flex;flex-direction:column}}.cmp img{{object-fit:cover;display:block}}
.cl2{{margin-top:5mm}}.cl2 b{{color:{GOLD};font-weight:500;letter-spacing:.2em;font-size:9pt}}.cl2 h3{{font-family:CG;font-weight:400;font-size:24pt;margin-top:1mm}}.cl2 p{{font-size:8pt;letter-spacing:.25em;text-transform:uppercase;margin-top:2mm;color:#5b5a50}}
.close{{display:flex;flex-direction:column;align-items:center;gap:8mm}}.by{{font-size:8pt;letter-spacing:.35em;text-transform:uppercase;color:{GOLD};margin-top:10mm}}.big2{{font-size:20pt;letter-spacing:.5em}}
'''
open(f'{S}/moodboard.html','w').write(f'<!doctype html><html lang="az"><head><meta charset="utf-8"><title>SPRING konsept moodboard</title><style>{css}</style></head><body>{"".join(pages)}</body></html>')
print(len(pages))
