"""
Quatre idées pour une production plus agile - Leoni Wiring Systems Berchid
Interface de présentation - Alternance GIPR, ENSAM Meknès
Fatiha Mahnoun, Karima Abdous, Oumaima Khair - Novembre 2026

Lancer :  streamlit run app.py
"""
import altair as alt
import pandas as pd
import streamlit as st

import types
from openpyxl.styles import Font, PatternFill

# ------------------------------------------------------------------ illustrations (dessins SVG)


NAVY = "#0A2A5E"
BLUE = "#1F5FAD"
CYAN = "#00A3E0"
SKY = "#DCEBFA"
ORANGE = "#F4A261"
RED = "#E5484D"
GREEN = "#2BB673"
GREY = "#C9D3E0"
BG = "#F4F7FB"


def _op(x, y, color=BLUE, scale=1.0, dashed=False):
    """Petit opérateur : tête + corps."""
    s = scale
    if dashed:
        return (f'<g opacity="0.9"><circle cx="{x}" cy="{y}" r="{9*s}" fill="none" stroke="{RED}" stroke-width="2" stroke-dasharray="4 3"/>'
                f'<path d="M{x-14*s},{y+34*s} q0,-20 {14*s},-20 q{14*s},0 {14*s},20 z" fill="none" stroke="{RED}" stroke-width="2" stroke-dasharray="4 3"/></g>')
    return (f'<g><circle cx="{x}" cy="{y}" r="{9*s}" fill="{color}"/>'
            f'<path d="M{x-14*s},{y+34*s} q0,-20 {14*s},-20 q{14*s},0 {14*s},20 z" fill="{color}"/>'
            f'<rect x="{x-9*s}" y="{y-11*s}" width="{18*s}" height="{6*s}" rx="{3*s}" fill="{ORANGE}"/></g>')


def hero():
    wires = ""
    cols = [CYAN, ORANGE, "#FFFFFF", "#7FB3F0", GREEN]
    for i, c in enumerate(cols):
        y = 150 + i * 9
        wires += (f'<path d="M0,{y} C120,{y-40} 220,{y+40} 340,{y} S560,{y-40} 700,{y}" '
                  f'fill="none" stroke="{c}" stroke-width="3.2" stroke-linecap="round" opacity="0.85"/>')
    clips = "".join(f'<rect x="{x}" y="140" width="14" height="56" rx="4" fill="{NAVY}" stroke="#ffffff" stroke-width="1.5"/>'
                    for x in (110, 300, 480, 620))
    return f"""<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Faisceau de câbles">
<defs><linearGradient id="hg" x1="0" x2="1"><stop offset="0" stop-color="#0E3A7A"/><stop offset="1" stop-color="{NAVY}"/></linearGradient></defs>
<rect width="700" height="300" rx="22" fill="url(#hg)"/>
<circle cx="610" cy="60" r="90" fill="{CYAN}" opacity="0.12"/><circle cx="80" cy="260" r="70" fill="{ORANGE}" opacity="0.12"/>
{wires}{clips}
<g transform="translate(470,40)"><rect width="170" height="70" rx="12" fill="#ffffff" opacity="0.95"/>
<rect x="14" y="40" width="16" height="18" rx="3" fill="{BLUE}"/><rect x="38" y="28" width="16" height="30" rx="3" fill="{CYAN}"/>
<rect x="62" y="20" width="16" height="38" rx="3" fill="{BLUE}"/><rect x="86" y="34" width="16" height="24" rx="3" fill="{CYAN}"/>
<line x1="10" y1="30" x2="110" y2="30" stroke="{ORANGE}" stroke-width="2" stroke-dasharray="4 3"/>
<circle cx="140" cy="38" r="16" fill="none" stroke="{GREY}" stroke-width="6"/>
<path d="M140,22 a16,16 0 0 1 14,24" fill="none" stroke="{GREEN}" stroke-width="6" stroke-linecap="round"/></g>
{_op(70,60,"#ffffff",1.1)}{_op(130,60,"#7FB3F0",1.1)}
<g transform="translate(40,230)" fill="#ffffff" opacity="0.9" font-family="Inter,Segoe UI,Arial" font-size="13" font-weight="600">
<text>Câblage automobile · Gestion de production</text></g>
</svg>"""


def idea1():
    stations = ""
    for i, x in enumerate((40, 170, 300, 430)):
        stations += (f'<rect x="{x}" y="170" width="110" height="60" rx="10" fill="#ffffff" stroke="{GREY}" stroke-width="2"/>'
                     f'<rect x="{x+10}" y="182" width="90" height="10" rx="5" fill="{SKY}"/>'
                     f'<text x="{x+55}" y="218" text-anchor="middle" font-family="Inter,Arial" font-size="13" font-weight="700" fill="{NAVY}">P0{i+1}</text>')
    ops = _op(95, 110) + _op(225, 110) + _op(355, 110, dashed=True) + _op(485, 110)
    # Opérateur polyvalent qui remplace
    spare = _op(600, 60, GREEN, 1.0)
    arrow = (f'<path d="M585,95 C520,40 420,40 372,92" fill="none" stroke="{GREEN}" stroke-width="3" stroke-dasharray="6 5"/>'
             f'<path d="M366,84 l6,12 l10,-8" fill="none" stroke="{GREEN}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    badge = (f'<circle cx="620" cy="40" r="12" fill="{GREEN}"/><path d="M614,40 l4,4 l8,-8" stroke="#fff" stroke-width="2.5" fill="none" stroke-linecap="round"/>')
    absent = (f'<g transform="translate(320,58)"><rect width="70" height="22" rx="11" fill="{RED}"/>'
              f'<text x="35" y="15" text-anchor="middle" font-family="Inter,Arial" font-size="11" font-weight="700" fill="#fff">Absent</text></g>')
    # Matrice de polyvalence
    grid = '<g transform="translate(560,150)"><rect width="120" height="100" rx="10" fill="#ffffff" stroke="' + GREY + '" stroke-width="2"/>'
    grid += f'<text x="60" y="18" text-anchor="middle" font-family="Inter,Arial" font-size="10" font-weight="700" fill="{NAVY}">Matrice</text>'
    pattern = [[1, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 1, 0]]
    for r, row in enumerate(pattern):
        for c, v in enumerate(row):
            col = (GREEN if (c == 2 and v) else BLUE) if v else "#E8EEF6"
            grid += f'<circle cx="{24+c*24}" cy="{36+r*17}" r="6" fill="{col}"/>'
    grid += "</g>"
    return f"""<svg viewBox="0 0 700 270" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Répartition du travail">
<rect width="700" height="270" rx="20" fill="{BG}"/>
<rect x="30" y="232" width="520" height="10" rx="5" fill="{GREY}"/>
{stations}{ops}{arrow}{spare}{badge}{absent}{grid}
</svg>"""


def idea2():
    bars = ""
    vals = [120, 140, 95, 150, 110, 165, 130]
    for i, v in enumerate(vals):
        x = 60 + i * 55
        over = v > 140
        bars += f'<rect x="{x}" y="{230-v}" width="34" height="{v}" rx="6" fill="{ORANGE if over else BLUE}"/>'
        bars += f'<text x="{x+17}" y="250" text-anchor="middle" font-family="Inter,Arial" font-size="11" fill="#5B6B82">S{i+1}</text>'
    cap = f'<line x1="45" y1="90" x2="440" y2="90" stroke="{GREEN}" stroke-width="3" stroke-dasharray="8 6"/>'
    cap += f'<g transform="translate(330,64)"><rect width="104" height="20" rx="10" fill="{GREEN}"/><text x="52" y="14" text-anchor="middle" font-family="Inter,Arial" font-size="11" font-weight="700" fill="#fff">Capacité</text></g>'
    gauge = f"""<g transform="translate(560,120)">
<path d="M-80,0 A80,80 0 0 1 80,0" fill="none" stroke="#E8EEF6" stroke-width="18" stroke-linecap="round"/>
<path d="M-80,0 A80,80 0 0 1 40,-69" fill="none" stroke="{CYAN}" stroke-width="18" stroke-linecap="round"/>
<line x1="0" y1="0" x2="40" y2="-58" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/>
<circle r="9" fill="{NAVY}"/>
<text y="38" text-anchor="middle" font-family="Inter,Arial" font-size="13" font-weight="700" fill="{NAVY}">Couverture</text></g>"""
    scen = f"""<g transform="translate(490,180)" font-family="Inter,Arial" font-size="11" font-weight="600">
<rect width="68" height="26" rx="13" fill="#ffffff" stroke="{GREY}"/><text x="34" y="17" text-anchor="middle" fill="{NAVY}">Absences</text>
<rect x="76" width="68" height="26" rx="13" fill="#ffffff" stroke="{GREY}"/><text x="110" y="17" text-anchor="middle" fill="{NAVY}">Pic +20 %</text>
<rect x="38" y="34" width="68" height="26" rx="13" fill="{NAVY}"/><text x="72" y="51" text-anchor="middle" fill="#fff">Heures sup</text></g>"""
    return f"""<svg viewBox="0 0 700 270" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Étude de capacité">
<rect width="700" height="270" rx="20" fill="{BG}"/>
<line x1="45" y1="230" x2="440" y2="230" stroke="{GREY}" stroke-width="2"/>
{bars}{cap}{gauge}{scen}
</svg>"""


def idea3():
    stacks = ""
    data = [[30, 25, 20], [28, 35, 24], [40, 30, 27], [22, 26, 18], [30, 36, 28], [20, 22, 23]]
    cols = [NAVY, BLUE, CYAN]
    for i, seg in enumerate(data):
        x = 125 + i * 48
        y = 190
        for j, h in enumerate(seg):
            y -= h
            stacks += f'<rect x="{x}" y="{y}" width="30" height="{h-2}" rx="3" fill="{cols[j]}"/>'
        if sum(seg) > 90:
            stacks += f'<circle cx="{x+15}" cy="{y-12}" r="7" fill="{RED}"/><text x="{x+15}" y="{y-8}" text-anchor="middle" font-family="Arial" font-size="10" font-weight="700" fill="#fff">!</text>'
    takt = f'<line x1="112" y1="100" x2="420" y2="100" stroke="{ORANGE}" stroke-width="3" stroke-dasharray="7 5"/><text x="424" y="104" font-family="Inter,Arial" font-size="11" font-weight="700" fill="{ORANGE}">Takt</text>'
    line = ""
    for i in range(5):
        x = 120 + i * 62
        line += f'<rect x="{x}" y="247" width="40" height="14" rx="4" fill="{BLUE}"/>'
    db = f"""<g transform="translate(560,70)">
<ellipse cx="50" cy="12" rx="50" ry="12" fill="{CYAN}"/>
<path d="M0,12 v90 a50,12 0 0 0 100,0 v-90" fill="{BLUE}"/>
<ellipse cx="50" cy="12" rx="50" ry="12" fill="{CYAN}"/>
<path d="M0,45 a50,12 0 0 0 100,0 M0,78 a50,12 0 0 0 100,0" fill="none" stroke="{CYAN}" stroke-width="3"/>
<text x="50" y="135" text-anchor="middle" font-family="Inter,Arial" font-size="12" font-weight="700" fill="{NAVY}">Données ligne</text></g>"""
    link = f'<path d="M555,120 C510,120 500,120 460,120" stroke="{CYAN}" stroke-width="3" fill="none" stroke-dasharray="5 5"/>'
    return f"""<svg viewBox="0 0 700 270" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Concept Line digitale">
<rect width="700" height="270" rx="20" fill="{BG}"/>
<rect x="95" y="22" width="360" height="200" rx="14" fill="#ffffff" stroke="{NAVY}" stroke-width="4"/>
<rect x="95" y="22" width="360" height="26" rx="12" fill="{NAVY}"/>
<circle cx="113" cy="35" r="4" fill="{RED}"/><circle cx="127" cy="35" r="4" fill="{ORANGE}"/><circle cx="141" cy="35" r="4" fill="{GREEN}"/>
<text x="275" y="40" text-anchor="middle" font-family="Inter,Arial" font-size="11" font-weight="700" fill="#fff">Yamazumi</text>
{stacks}{takt}
<rect x="245" y="222" width="60" height="14" fill="{NAVY}"/>
<rect x="100" y="243" width="340" height="22" rx="8" fill="{GREY}"/>{line}
{link}{db}
</svg>"""


def idea4():
    checks = ""
    items = [(True, 150), (True, 110), (True, 130), (False, 90)]
    for i, (ok, w) in enumerate(items):
        y = 78 + i * 38
        box = (f'<rect x="268" y="{y}" width="20" height="20" rx="5" fill="{GREEN if ok else "#fff"}" stroke="{GREEN if ok else RED}" stroke-width="2"/>')
        if ok:
            box += f'<path d="M272,{y+10} l5,5 l8,-9" stroke="#fff" stroke-width="2.5" fill="none" stroke-linecap="round"/>'
        else:
            box += f'<text x="278" y="{y+15}" text-anchor="middle" font-family="Arial" font-size="13" font-weight="700" fill="{RED}">!</text>'
        checks += box + f'<rect x="298" y="{y+5}" width="{w}" height="10" rx="5" fill="{SKY if ok else "#FDE2E3"}"/>'
    paper = f"""<g transform="translate(60,70) rotate(-8)">
<rect width="120" height="150" rx="6" fill="#ffffff" stroke="{GREY}" stroke-width="2"/>
<rect x="16" y="22" width="80" height="8" rx="4" fill="{GREY}"/><rect x="16" y="42" width="60" height="8" rx="4" fill="{GREY}"/>
<rect x="16" y="62" width="88" height="8" rx="4" fill="{GREY}"/><rect x="16" y="82" width="50" height="8" rx="4" fill="{GREY}"/>
<line x1="-6" y1="-6" x2="126" y2="156" stroke="{RED}" stroke-width="6" stroke-linecap="round" opacity="0.85"/></g>"""
    arrow = f'<path d="M200,145 h40" stroke="{BLUE}" stroke-width="4" stroke-linecap="round"/><path d="M232,135 l12,10 l-12,10" fill="none" stroke="{BLUE}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
    bell = f"""<g transform="translate(560,40)">
<rect width="110" height="190" rx="16" fill="#ffffff" stroke="{GREY}" stroke-width="2"/>
<text x="55" y="26" text-anchor="middle" font-family="Inter,Arial" font-size="11" font-weight="700" fill="{NAVY}">Écarts du jour</text>
<rect x="14" y="40" width="82" height="34" rx="8" fill="#FDE2E3"/><circle cx="30" cy="57" r="7" fill="{RED}"/><rect x="44" y="53" width="44" height="8" rx="4" fill="{RED}" opacity="0.5"/>
<rect x="14" y="82" width="82" height="34" rx="8" fill="#E3F6EC"/><circle cx="30" cy="99" r="7" fill="{GREEN}"/><rect x="44" y="95" width="44" height="8" rx="4" fill="{GREEN}" opacity="0.5"/>
<rect x="14" y="124" width="82" height="34" rx="8" fill="#E3F6EC"/><circle cx="30" cy="141" r="7" fill="{GREEN}"/><rect x="44" y="137" width="44" height="8" rx="4" fill="{GREEN}" opacity="0.5"/>
</g>
<g transform="translate(640,30)"><circle r="16" fill="{ORANGE}"/>
<path d="M-6,4 v-5 a6,6 0 0 1 12,0 v5 l2,2 h-16 z M-2,8 a2,2 0 0 0 4,0" fill="#fff"/></g>"""
    link = f'<path d="M490,140 h60" stroke="{CYAN}" stroke-width="3" stroke-dasharray="5 5"/>'
    return f"""<svg viewBox="0 0 700 270" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Routines digitales">
<rect width="700" height="270" rx="20" fill="{BG}"/>
{paper}{arrow}
<rect x="250" y="30" width="240" height="220" rx="22" fill="{NAVY}"/>
<rect x="260" y="46" width="220" height="190" rx="12" fill="#ffffff"/>
<text x="370" y="66" text-anchor="middle" font-family="Inter,Arial" font-size="12" font-weight="700" fill="{NAVY}">Checklist chef de ligne</text>
{checks}{link}{bell}
</svg>"""


def synergy():
    nodes = [("Répartition du travail", 120, 70, BLUE), ("Étude de capacité", 580, 70, CYAN),
             ("Routines digitales", 120, 230, ORANGE), ("Tableaux de bord", 580, 230, GREEN)]
    out = ""
    for label, x, y, c in nodes:
        out += f'<path d="M350,150 L{x},{y}" stroke="{c}" stroke-width="4" stroke-dasharray="8 6" opacity="0.8"/>'
    for label, x, y, c in nodes:
        out += (f'<g transform="translate({x},{y})"><rect x="-100" y="-26" width="200" height="52" rx="26" fill="#ffffff" stroke="{c}" stroke-width="3"/>'
                f'<circle cx="-74" cy="0" r="12" fill="{c}"/>'
                f'<text x="10" y="5" text-anchor="middle" font-family="Inter,Arial" font-size="14" font-weight="700" fill="{NAVY}">{label}</text></g>')
    hub = f"""<g transform="translate(350,150)"><circle r="78" fill="{NAVY}"/><circle r="92" fill="none" stroke="{NAVY}" stroke-width="2" opacity="0.25"/>
<text y="-4" text-anchor="middle" font-family="Inter,Arial" font-size="18" font-weight="800" fill="#fff">Concept Line</text>
<text y="18" text-anchor="middle" font-family="Inter,Arial" font-size="12" fill="#BFD6F5">données communes</text></g>"""
    return f"""<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Synergie des idées">
<rect width="700" height="300" rx="20" fill="{BG}"/>{out}{hub}</svg>"""


ill = types.SimpleNamespace(hero=hero, idea1=idea1, idea2=idea2, idea3=idea3, idea4=idea4, synergy=synergy)

st.set_page_config(page_title="4 idées - Leoni", page_icon=":material/precision_manufacturing:", layout="wide")

# ------------------------------------------------------------------ style
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"], .stMarkdown, .stText, button, input { font-family: 'Inter', 'Segoe UI', sans-serif; }
.block-container { padding-top: 3.2rem; max-width: 1200px; }
section[data-testid="stSidebar"] { background: #0A2A5E; }
section[data-testid="stSidebar"] * { color: #E6EEF9 !important; }
section[data-testid="stSidebar"] a[aria-current="page"] { background: rgba(0,163,224,.22) !important; border-radius: 10px; }
.kicker { color:#00A3E0; font-weight:700; letter-spacing:.14em; font-size:.78rem; text-transform:uppercase; margin-bottom:.2rem; }
.h1 { color:#0A2A5E; font-size:2.1rem; font-weight:800; line-height:1.15; margin:0 0 .4rem 0; }
.lead { color:#4A5B74; font-size:1.05rem; margin-bottom:1rem; }
.card { background:#fff; border:1px solid #E3EAF3; border-radius:16px; padding:18px 20px; height:100%;
        box-shadow:0 2px 10px rgba(10,42,94,.05); transition:transform .15s, box-shadow .15s; }
.card:hover { transform:translateY(-3px); box-shadow:0 8px 24px rgba(10,42,94,.10); }
.card h4 { margin:.5rem 0 .3rem 0; color:#0A2A5E; font-size:1.02rem; font-weight:700; }
.card p, .card li { color:#4A5B74; font-size:.93rem; margin:0; }
.card ul { padding-left:1.1rem; margin:.3rem 0 0 0; } .card li { margin-bottom:.25rem; }
.ico { width:44px; height:44px; border-radius:12px; display:flex; align-items:center; justify-content:center; }
.ico svg { width:24px; height:24px; }
.num { font-size:2.4rem; font-weight:800; color:#DCEBFA; line-height:1; float:right; }
.tag { display:inline-block; padding:3px 10px; border-radius:20px; font-size:.75rem; font-weight:700; margin-right:6px; }
.band { border-radius:16px; padding:16px 20px; margin:.4rem 0 1rem 0; }
.ex { background:#FFF6EC; border-left:5px solid #F4A261; }
.ex b { color:#B4621B; }
.tl { display:flex; gap:12px; flex-wrap:wrap; }
.step { flex:1; min-width:180px; background:#fff; border:1px solid #E3EAF3; border-radius:16px; padding:16px; position:relative; }
.step .n { width:34px; height:34px; border-radius:50%; background:#0A2A5E; color:#fff; font-weight:800; display:flex; align-items:center; justify-content:center; }
.ref { background:#fff; border:1px solid #E3EAF3; border-radius:12px; padding:12px 16px; margin-bottom:10px; display:flex; gap:12px; align-items:flex-start; }
.ref a { color:#1F5FAD; font-weight:700; text-decoration:none; } .ref a:hover { text-decoration:underline; }
.ref small { color:#6B7A90; }
.avatar { width:64px; height:64px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:800; color:#fff; font-size:1.3rem; margin-bottom:.4rem; }
.ill svg { width:100%; height:auto; display:block; }
.foot { color:#8A97AB; font-size:.8rem; text-align:center; margin-top:2rem; }
div[data-testid="stMetric"] { background:#fff; border:1px solid #E3EAF3; border-radius:14px; padding:12px 16px; }
.kpi { background:#fff; border:1px solid #E3EAF3; border-radius:14px; padding:14px 16px; height:100%; box-shadow:0 2px 10px rgba(10,42,94,.05); }
.kl { color:#6B7A90; font-size:.82rem; font-weight:600; } .kv { color:#0A2A5E; font-size:1.9rem; font-weight:800; line-height:1.2; }
.ks { color:#6B7A90; font-size:.8rem; margin-top:.3rem; }
.dh { color:#0A2A5E; margin:0 0 .4rem 0; font-size:1rem; font-weight:700; }
html, body, [data-testid="stMain"], [data-testid="stAppViewContainer"], section[data-testid="stSidebar"] > div { scroll-behavior:smooth; }
* { scrollbar-width:thin; scrollbar-color:#B7C6DA transparent; }
::-webkit-scrollbar { width:10px; height:10px; } ::-webkit-scrollbar-track { background:transparent; }
::-webkit-scrollbar-thumb { background:#C9D3E0; border-radius:10px; border:2px solid #fff; }
::-webkit-scrollbar-thumb:hover { background:#1F5FAD; }
.totop { position:fixed; right:28px; bottom:28px; width:46px; height:46px; border-radius:50%; background:#0A2A5E; color:#fff !important;
         display:flex; align-items:center; justify-content:center; box-shadow:0 6px 18px rgba(10,42,94,.3); z-index:999;
         text-decoration:none !important; font-size:1.3rem; font-weight:800; transition:transform .15s, background .15s; }
.totop:hover { background:#1F5FAD; transform:translateY(-3px); }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------ icônes (trait, style Lucide)
P = {
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    "gauge": '<path d="M12 14l4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/>',
    "layers": '<path d="M12 2 2 7l10 5 10-5-10-5z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
    "check": '<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>',
    "alert": '<path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><path d="M12 9v4M12 17h.01"/>',
    "bulb": '<path d="M9 18h6M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7V17h8v-2.3A7 7 0 0 0 12 2z"/>',
    "trend": '<path d="m23 6-9.5 9.5-5-5L1 18"/><path d="M17 6h6v6"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V2H6.5A2.5 2.5 0 0 0 4 4.5v15z"/><path d="M6.5 17A2.5 2.5 0 0 0 4 19.5 2.5 2.5 0 0 0 6.5 22H20v-5"/>',
    "flag": '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><path d="M4 22v-7"/>',
    "db": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/>',
    "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "x": '<circle cx="12" cy="12" r="10"/><path d="m15 9-6 6M9 9l6 6"/>',
    "rocket": '<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/>',
    "link": '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
}


def icon(name, color="#1F5FAD", bg="#E8F1FC"):
    return (f'<div class="ico" style="background:{bg}"><svg viewBox="0 0 24 24" fill="none" stroke="{color}" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{P[name]}</svg></div>')


def html(s):
    st.markdown(s, unsafe_allow_html=True)


def header(kicker, title, lead=""):
    html(f'<div class="kicker">{kicker}</div><div class="h1">{title}</div>' + (f'<div class="lead">{lead}</div>' if lead else ""))


def card(ic, title, body, color="#1F5FAD", bg="#E8F1FC", num=""):
    n = f'<span class="num">{num}</span>' if num else ""
    return f'<div class="card">{n}{icon(ic, color, bg)}<h4>{title}</h4>{body}</div>'


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


# ------------------------------------------------------------------ contenu
IDEAS = {
    1: dict(title="Répartition du travail", short="Affecter les bons opérateurs aux bons postes, chaque jour",
            ic="users", color="#1F5FAD", svg=ill.idea1,
            what="Chaque matin, la répartition des opérateurs sur les postes est construite à partir des personnes "
                 "réellement présentes et de leurs compétences, au lieu d'un plan fixe corrigé à la main.",
            today=["Plan d'affectation fixe", "Absences gérées au cas par cas le matin", "Compétences peu visibles"],
            prop=["Matrice de polyvalence à jour", "Affectation quotidienne selon les présents", "Postes critiques couverts en priorité"],
            gain=["Démarrage de shift plus rapide", "Moins de postes non tenus", "Polyvalence mieux exploitée"],
            ex="Un opérateur clé est absent au poste de taping : la matrice indique tout de suite qui est formé pour le remplacer.",
            refs=[("Mortada & Soulhi (2023)", "Équilibrage d'une ligne de câblage au Maroc", "Advances in Science and Technology Research Journal",
                   "https://yadda.icm.edu.pl/baztech/element/bwmeta1.element.baztech-58aaad31-b12e-4b7a-ac8d-fe8fa323b5eb/c/ASTRJ_2023__vol._17__nr_4__s89-109.pdf"),
                  ("Katiraee et al. (2021)", "Affecter selon les différences entre opérateurs", "IFAC-PapersOnLine",
                   "https://www.research.unipd.it/retrieve/e14fb26f-4245-3de1-e053-1705fe0ac030/Consideration-of-workforce-differences-in-assembly-line-bala_2021_IFAC-Paper.pdf")]),
    2: dict(title="Étude de capacité", short="Savoir à l'avance si la ligne peut tenir la demande",
            ic="gauge", color="#0091C7", svg=ill.idea2,
            what="On compare la charge demandée par le client à la capacité réelle de la ligne, et on teste des "
                 "scénarios (absences, pic de commande, heures supplémentaires) avant de décider.",
            today=["Capacité calculée sur l'effectif théorique", "Écarts découverts trop tard", "Décisions prises à l'expérience"],
            prop=["Comparer charge et capacité réelle", "Tester des scénarios (absences, pics de commande)", "Simuler la ligne avant de décider"],
            gain=["Heures supplémentaires anticipées", "Décisions appuyées sur des données", "Moins de retards de livraison"],
            ex="Une hausse de commande est annoncée : la simulation montre avant le lancement si un shift supplémentaire est nécessaire.",
            refs=[("Gallego-García et al. (2019)", "Gestion de capacité simulée, usine automobile", "Applied Sciences (MDPI)",
                   "https://www.mdpi.com/2076-3417/9/24/5567"),
                  ("Adel et al. (2025)", "Simulation d'une ligne de câblage automobile", "South African Journal of Industrial Engineering",
                   "https://sajie.journals.ac.za/pub/article/view/3230")]),
    3: dict(title="Concept Line digitale", short="Une description unique et numérique de chaque ligne",
            ic="layers", color="#0A2A5E", svg=ill.idea3,
            what="Un fichier standard par ligne regroupe les postes, les opérations et leurs temps. Il calcule "
                 "automatiquement la charge de chaque poste et trace le Yamazumi par rapport au takt.",
            today=["Informations de ligne dispersées", "Fichiers différents selon les services", "Rééquilibrage long à préparer"],
            prop=["Un fichier standard : postes, opérations, temps", "Yamazumi généré automatiquement", "Base commune pour les autres idées"],
            gain=["Une seule source de vérité", "Postes surchargés visibles immédiatement", "Gain de temps pour les méthodes"],
            ex="Un nouveau modèle arrive sur la ligne : les temps sont saisis une seule fois et le Yamazumi se met à jour pour tous.",
            refs=[("Kuhn et al. (2023)", "Usine digitale et planification virtuelle (BMW)", "Springer, Advances in Automotive Production Technology",
                   "https://link.springer.com/10.1007/978-3-031-27933-1_20"),
                  ("Jebbor et al. (2023)", "Analyse et amélioration d'une ligne de faisceaux", "IOS Press",
                   "https://ebooks.iospress.nl/pdf/doi/10.3233/ATDE230031")]),
    4: dict(title="Routines digitales", short="Les routines des chefs de ligne, sans papier",
            ic="check", color="#D9822B", svg=ill.idea4,
            what="Les checklists et audits quotidiens (chef de ligne, chef d'équipe, qualité) passent sur tablette ou "
                 "téléphone, et les écarts remontent en direct sur un tableau de bord.",
            today=["Fiches papier : chef de ligne, chef d'équipe, qualité", "Données ressaisies plusieurs fois", "Écarts suivis tardivement"],
            prop=["Checklists sur tablette ou téléphone", "Tableau de bord des écarts en direct", "Outil conçu avec les utilisateurs"],
            gain=["Moins de papier et de ressaisie", "Réaction plus rapide aux écarts", "Routines réellement suivies"],
            ex="Un contrôle qualité détecte un écart : il s'affiche aussitôt sur le tableau de bord du chef de ligne, sans attendre la fiche papier.",
            refs=[("Mesarosova et al. (2024)", "Digitalisation du shop floor management", "MM Science Journal",
                   "https://mmscience.eu/journal/issues/november-2024/articles/digitalization-of-shop-floor-management-at-selected-segment-in-the-industrial-enterprise-in-the-context-of-industry-4-0/download"),
                  ("Järnberg & Samuelsson (2022)", "Outil digital pour les audits par couches (LPA)", "Chalmers University of Technology",
                   "https://odr.chalmers.se/items/f8bec703-d9bc-4201-b132-68c85298eb1b/full")]),
}


def light(hex_color):
    return {"#1F5FAD": "#E8F1FC", "#0091C7": "#E0F4FB", "#0A2A5E": "#E4E9F2", "#D9822B": "#FDF0E3"}[hex_color]


# ------------------------------------------------------------------ pages
def page_home():
    c1, c2 = st.columns([1.05, 1], gap="large")
    with c1:
        html('<div class="kicker">Réunion de suivi · Alternance</div>'
             '<div class="h1" style="font-size:2.6rem">Quatre idées pour une production plus agile</div>'
             '<div class="lead">Propositions d\'amélioration de la gestion de production pour '
             '<b>Leoni Wiring Systems Berchid</b>, construites à partir de la littérature et des besoins du terrain.</div>')
        html('<span class="tag" style="background:#E8F1FC;color:#1F5FAD">Gestion de production</span>'
             '<span class="tag" style="background:#FDF0E3;color:#B4621B">Câblage automobile</span>'
             '<span class="tag" style="background:#E3F6EC;color:#1E8A55">Faible coût</span>')
        st.write("")
        html('<div class="lead" style="font-size:.95rem">Utilisez le menu à gauche pour parcourir les idées. '
             'Chaque idée contient une explication, une illustration, un exemple concret, un outil de calcul '
             'et ses sources. Dans la page <b>Importer les données</b>, vous pouvez charger un fichier Excel de la ligne : '
             'tous les outils se recalculent avec vos données et les résultats s\'exportent en Excel.</div>')
    with c2:
        html(f'<div class="ill">{ill.hero()}</div>')

    st.write("")
    header("Notre équipe", "Qui sommes-nous ?")
    team = [("FM", "Fatiha Mahnoun", "#1F5FAD"), ("KA", "Karima Abdous", "#00A3E0"), ("OK", "Oumaima Khair", "#F4A261")]
    cols = st.columns(3)
    for col, (ini, name, c) in zip(cols, team):
        col.markdown(f'<div class="card"><div class="avatar" style="background:{c}">{ini}</div><h4>{name}</h4>'
                     f'<p>Élève ingénieure en Génie Industriel et Productique, 5e année, ENSAM Meknès</p></div>',
                     unsafe_allow_html=True)
    st.write("")
    header("Encadrement", "Nos encadrants")
    enc = [("MB", "Madame Bonou", "Encadrante académique", "ENSAM Meknès", "#0A2A5E", "book"),
           ("AM", "Anas Madani", "Encadrant industriel", "Leoni Wiring Systems Berchid", "#2BB673", "flag")]
    cols = st.columns(2)
    for col, (ini, name, role, org, c, ic) in zip(cols, enc):
        col.markdown(f'<div class="card" style="display:flex;gap:16px;align-items:center">'
                     f'<div class="avatar" style="background:{c};margin:0;flex:none">{ini}</div>'
                     f'<div><span class="tag" style="background:#E8F1FC;color:#1F5FAD">{role}</span>'
                     f'<h4 style="margin:.4rem 0 .1rem">{name}</h4><p>{org}</p></div></div>', unsafe_allow_html=True)
    st.write("")
    html('<div class="band" style="background:#0A2A5E;color:#fff"><b>Notre mission chez Leoni :</b> '
         'proposer des améliorations concrètes de la gestion de production, dans le cadre de notre alternance.</div>')

    header("Aperçu", "Les quatre idées en un coup d'œil")
    cols = st.columns(4)
    for col, (k, d) in zip(cols, IDEAS.items()):
        col.markdown(card(d["ic"], d["title"], f"<p>{d['short']}</p>", d["color"], light(d["color"]), f"0{k}"),
                     unsafe_allow_html=True)


def page_start():
    header("Point de départ", "Des défis concrets, quatre réponses",
           "Les idées répondent à des difficultés que l'on retrouve sur les lignes de câblage.")
    defis = [("alert", "Absentéisme et remplacements", "Les absences du matin obligent à refaire l'affectation dans l'urgence.", 1),
             ("users", "Polyvalence mal exploitée", "Les compétences des opérateurs ne sont pas toujours visibles ni utilisées.", 1),
             ("trend", "Production journalière à piloter", "Il faut savoir tôt si la ligne peut suivre la demande du client.", 2),
             ("clock", "Saisies et analyses manuelles", "Les données sont dispersées et ressaisies plusieurs fois.", 3)]
    cols = st.columns(4)
    for col, (ic, t, b, k) in zip(cols, defis):
        d = IDEAS[k]
        col.markdown(card(ic, t, f"<p>{b}</p><p style='margin-top:.6rem'><span class='tag' style='background:{light(d['color'])};color:{d['color']}'>"
                              f"Idée 0{k} · {d['title']}</span></p>", "#E5484D", "#FDECEC"), unsafe_allow_html=True)
    st.write("")
    html('<div class="band" style="background:#E8F1FC;color:#0A2A5E">Le quatrième volet, <b>les routines digitales</b>, '
         'répond au même problème de saisie manuelle du côté des chefs de ligne et de la qualité.</div>')


def idea_sections(k):
    d = IDEAS[k]
    c = d["color"]
    html(f'<div style="display:flex;gap:14px;align-items:center">{icon(d["ic"], c, light(c))}'
         f'<div class="kicker" style="margin:0">Idée 0{k}</div></div>'
         f'<div class="h1" style="margin-top:.4rem">{d["title"]}</div><div class="lead">{d["short"]}</div>')
    html(f'<div class="ill" style="max-width:980px;margin:0 auto 1rem">{d["svg"]()}</div>')
    p1, p2 = st.columns([1.2, 1], gap="medium")
    p1.markdown(f'<div class="card" style="border-left:5px solid {c}">{icon("target", c, light(c))}<h4>Le principe</h4><p>{d["what"]}</p></div>',
                unsafe_allow_html=True)
    p2.markdown(f'<div class="card ex" style="border:none;border-left:5px solid #F4A261">{icon("bulb", "#D9822B", "#FDE7CF")}'
                f'<h4 style="color:#B4621B">Exemple concret</h4><p style="color:#5A4630">{d["ex"]}</p></div>', unsafe_allow_html=True)
    st.write("")
    a, b, cc = st.columns(3)
    a.markdown(card("x", "Aujourd'hui", ul(d["today"]), "#E5484D", "#FDECEC"), unsafe_allow_html=True)
    b.markdown(card("bulb", "Notre proposition", ul(d["prop"]), c, light(c)), unsafe_allow_html=True)
    cc.markdown(card("trend", "Le gain pour Leoni", ul(d["gain"]), "#2BB673", "#E3F6EC"), unsafe_allow_html=True)
    st.write("")
    return d


def sources_block(d):
    with st.expander("Sources de cette idée", icon=":material/menu_book:"):
        for a, t, j, u in d["refs"]:
            html(f'<div class="ref">{icon("link", "#1F5FAD", "#E8F1FC")}<div><a href="{u}" target="_blank">{a} ↗</a><br>'
                 f'{t}<br><small>{j}</small></div></div>')


# ------------------------------------------------------------------ données : modèle, import, validation, export
import io
import datetime as dt

SHEETS = {
    "Parametres": ["Parametre", "Valeur"],
    "Postes": ["Poste", "Designation", "Nb_operateurs", "Critique"],
    "Operations": ["Poste", "Operation", "Temps_s"],
    "Competences": ["Operateur", "Poste_habituel"],          # + une colonne 0/1 par poste
    "Presence": ["Date", "Operateur", "Statut"],             # facultative
    "Routines": ["Point_de_controle", "Responsable", "Frequence"],
}
OPTIONAL = {"Presence"}
PARAM_KEYS = {"Demande_jour": 600, "Nb_shifts": 2, "Duree_shift_min": 480, "Pause_min": 30, "Rendement": 1.0}


def example_data():
    postes = pd.DataFrame({
        "Poste": ["P01", "P02", "P03", "P04", "P05", "P06"],
        "Designation": ["Préparation du kit", "Pose fils zone A", "Pose fils zone B", "Rubanage (taping)",
                        "Contrôle électrique", "Contrôle final et emballage"],
        "Nb_operateurs": [1, 1, 1, 1, 1, 1],
        "Critique": ["Non", "Non", "Non", "Oui", "Oui", "Non"],
    })
    ops = pd.DataFrame({
        "Poste": ["P01", "P01", "P02", "P02", "P03", "P03", "P03", "P04", "P04", "P05", "P05", "P06", "P06"],
        "Operation": ["Préparer le kit", "Étiqueter", "Poser fils zone A", "Clipser", "Poser fils zone B",
                      "Vérifier position", "Épissure", "Rubaner", "Poser gaine", "Test électrique",
                      "Contrôle visuel", "Contrôle final", "Emballer"],
        "Temps_s": [45, 30, 50, 32, 47, 20, 30, 48, 34, 55, 25, 40, 30],
    })
    comp = pd.DataFrame({
        "Operateur": ["Ahmed", "Salma", "Youssef", "Nadia", "Hamza", "Khadija", "Imane", "Rachid",
                      "Anas", "Karima", "Oumaima", "Fatiha", "Abdel Bar"],
        "Poste_habituel": ["P01", "P02", "P03", "P04", "P05", "P06", "Réserve", "Réserve",
                           "Réserve", "Réserve", "Réserve", "Réserve", "Réserve"],
        "P01": [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1], "P02": [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
        "P03": [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], "P04": [0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
        "P05": [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0], "P06": [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    })
    today = dt.date.today()
    pres = pd.DataFrame({"Date": [today] * len(comp), "Operateur": comp["Operateur"],
                         "Statut": ["Absent" if o == "Nadia" else "Présent" for o in comp["Operateur"]]})
    rout = pd.DataFrame({
        "Point_de_controle": ["Effectif présent conforme au plan", "Postes et outillages prêts",
                              "Premier faisceau validé (OK démarrage)", "Documents de poste à jour",
                              "Banc de test électrique vérifié", "Zone 5S en ordre"],
        "Responsable": ["Chef de ligne", "Chef d'équipe", "Qualité", "Chef d'équipe", "Qualité", "Chef de ligne"],
        "Frequence": ["Début de shift"] * 6,
    })
    params = pd.DataFrame({"Parametre": list(PARAM_KEYS), "Valeur": list(PARAM_KEYS.values())})
    return {"Parametres": params, "Postes": postes, "Operations": ops, "Competences": comp, "Presence": pres, "Routines": rout}


def get_data():
    return st.session_state.get("data") or example_data()


def source_label():
    return st.session_state.get("data_name", "Données d'exemple")


def params(data):
    p = dict(PARAM_KEYS)
    for _, r in data["Parametres"].iterrows():
        try:
            p[str(r["Parametre"]).strip()] = float(r["Valeur"])
        except (TypeError, ValueError):
            pass
    p["Ouverture_min"] = p["Nb_shifts"] * (p["Duree_shift_min"] - p["Pause_min"])
    return p


def charges(data):
    ops = data["Operations"].copy()
    ops["Temps_s"] = pd.to_numeric(ops["Temps_s"], errors="coerce").fillna(0)
    ch = ops.groupby("Poste")["Temps_s"].sum()
    po = data["Postes"].set_index("Poste")
    df = po.join(ch.rename("Charge_s")).fillna({"Charge_s": 0})
    df["Nb_operateurs"] = pd.to_numeric(df["Nb_operateurs"], errors="coerce").fillna(1).clip(lower=1)
    df["Charge_par_op_s"] = df["Charge_s"] / df["Nb_operateurs"]
    return df.reset_index()


def to_excel(sheets):
    buf = io.BytesIO()
    with pd.ExcelWriter(buf, engine="openpyxl") as xw:
        for name, df in sheets.items():
            df.to_excel(xw, sheet_name=name[:31], index=False)
            ws = xw.sheets[name[:31]]
            for c in ws[1]:
                c.font = Font(bold=True, color="FFFFFF")
                c.fill = PatternFill("solid", fgColor="0A2A5E")
            for col in ws.columns:
                ws.column_dimensions[col[0].column_letter].width = max(12, min(45, max(len(str(x.value or "")) for x in col) + 2))
    return buf.getvalue()


def template_bytes():
    d = example_data()
    lis = pd.DataFrame({"Onglet": list(SHEETS), "Contenu": [
        "Demande_jour, Nb_shifts, Duree_shift_min, Pause_min, Rendement (ne pas changer les noms de la colonne Parametre)",
        "Une ligne par poste : code, désignation, nombre d'opérateurs, poste critique (Oui / Non)",
        "Une ligne par opération : poste, désignation, temps standard en secondes (gamme du service méthodes)",
        "Une ligne par opérateur : poste habituel (ou Réserve), puis 1 si formé au poste, 0 sinon (une colonne par poste)",
        "Facultatif : pointage du jour (Date, Operateur, Statut = Présent / Absent)",
        "Points de contrôle des routines : intitulé, responsable, fréquence"]})
    return to_excel({"Lisez-moi": lis, **d})


def validate(xl):
    errors, data = [], {}
    for sh, cols in SHEETS.items():
        if sh not in xl:
            if sh not in OPTIONAL:
                errors.append(f"Onglet manquant : « {sh} »")
            continue
        df = xl[sh].dropna(how="all")
        df.columns = [str(c).strip() for c in df.columns]
        miss = [c for c in cols if c not in df.columns]
        if miss:
            errors.append(f"Onglet « {sh} » : colonnes manquantes {', '.join(miss)}")
        data[sh] = df
    if errors:
        return None, errors
    postes = set(data["Postes"]["Poste"].astype(str))
    bad = set(data["Operations"]["Poste"].astype(str)) - postes
    if bad:
        errors.append(f"Opérations : postes inconnus dans l'onglet Postes : {', '.join(sorted(bad))}")
    if pd.to_numeric(data["Operations"]["Temps_s"], errors="coerce").isna().any():
        errors.append("Opérations : certains temps ne sont pas des nombres")
    nocol = [p for p in postes if p not in data["Competences"].columns]
    if nocol:
        errors.append(f"Compétences : il manque une colonne pour les postes {', '.join(sorted(nocol))}")
    if "Presence" not in data:
        data["Presence"] = pd.DataFrame(columns=SHEETS["Presence"])
    return (None, errors) if errors else (data, [])


def data_badge():
    src = source_label()
    col = "#E3F6EC;color:#1E8A55" if src != "Données d'exemple" else "#FFF6EC;color:#B4621B"
    html(f"<span class='tag' style='background:{col}'>Source : {src}</span>")


# ------------------------------------------------------------------ page import
def page_data():
    header("Outil", "Importer les données de la ligne",
           "Téléchargez le modèle, remplissez-le avec les données de l'entreprise, puis importez-le : "
           "toutes les pages se recalculent avec vos données.")
    c1, c2, c3 = st.columns(3)
    c1.markdown(card("db", "1. Télécharger le modèle", "<p>Un fichier Excel avec les 6 onglets attendus et un exemple rempli.</p>"), unsafe_allow_html=True)
    c2.markdown(card("layers", "2. Remplir avec Leoni", "<p>Postes, gamme et temps (méthodes), compétences (RH / production), pointage, routines.</p>", "#0091C7", "#E0F4FB"), unsafe_allow_html=True)
    c3.markdown(card("check", "3. Importer", "<p>Le fichier est vérifié. En cas d'erreur, l'outil indique l'onglet et la colonne à corriger.</p>", "#2BB673", "#E3F6EC"), unsafe_allow_html=True)
    st.write("")
    a, b = st.columns([1, 1.4], gap="large")
    with a:
        st.download_button("Télécharger le modèle Excel", template_bytes(), "Modele_Donnees_Ligne_Leoni.xlsx",
                           mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                           icon=":material/download:", type="primary", use_container_width=True)
        up = st.file_uploader("Importer le fichier rempli (.xlsx)", type=["xlsx", "xlsm"])
        if up is not None and st.session_state.get("data_file_id") != up.file_id:
            try:
                xl = pd.read_excel(up, sheet_name=None)
                data, errs = validate(xl)
            except Exception as e:  # fichier illisible
                data, errs = None, [f"Fichier illisible : {e}"]
            st.session_state["data_file_id"] = up.file_id
            if errs:
                st.session_state["import_errors"] = errs
            else:
                st.session_state.update(data=data, data_name=up.name, import_errors=[],
                                        imported_at=dt.datetime.now().strftime("%d/%m/%Y %H:%M"))
        for e in st.session_state.get("import_errors", []):
            st.error(e, icon=":material/error:")
        if st.session_state.get("data"):
            st.success(f"Fichier « {source_label()} » importé le {st.session_state['imported_at']}.", icon=":material/check_circle:")
            if st.button("Revenir aux données d'exemple", icon=":material/restart_alt:"):
                for k in ("data", "data_name", "data_file_id", "import_errors"):
                    st.session_state.pop(k, None)
                st.rerun()
        else:
            st.info("Aucun fichier importé : l'outil utilise les données d'exemple.", icon=":material/info:")
    with b:
        d = get_data()
        p = params(d)
        ch = charges(d)
        takt = p["Ouverture_min"] * 60 / max(p["Demande_jour"], 1)
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Postes", len(d["Postes"]))
        m2.metric("Opérations", len(d["Operations"]))
        m3.metric("Opérateurs", len(d["Competences"]))
        m4.metric("Takt", f"{takt:.0f} s")
        tabs = st.tabs(["Paramètres", "Postes", "Opérations", "Compétences", "Présence", "Routines"])
        for t, sh in zip(tabs, ["Parametres", "Postes", "Operations", "Competences", "Presence", "Routines"]):
            t.dataframe(d[sh], hide_index=True, use_container_width=True, height=260)
    st.write("")
    with st.expander("Format attendu de chaque onglet", icon=":material/table_view:"):
        st.markdown("""
| Onglet | Colonnes | Source dans l'entreprise |
|---|---|---|
| Parametres | Parametre, Valeur (Demande_jour, Nb_shifts, Duree_shift_min, Pause_min, Rendement) | Planification / production |
| Postes | Poste, Designation, Nb_operateurs, Critique (Oui/Non) | Méthodes |
| Operations | Poste, Operation, Temps_s | Gamme et temps standards (méthodes) |
| Competences | Operateur, Poste_habituel, puis une colonne par poste (1 = formé, 0 = non) | Matrice de polyvalence (production / RH) |
| Presence *(facultatif)* | Date, Operateur, Statut (Présent / Absent) | Pointage du jour |
| Routines | Point_de_controle, Responsable, Frequence | Checklists chef de ligne / qualité |
""")


# ------------------------------------------------------------------ démonstrations branchées sur les données
def demo_head(title, text):
    html(f'<h4 style="color:#0A2A5E;margin:0">{title}</h4><p style="color:#6B7A90;font-size:.9rem;margin-bottom:.3rem">{text}</p>')
    data_badge()


def assign(comp, postes, absents):
    """Affectation du jour : titulaires présents, puis remplaçants formés (postes critiques d'abord,
    on choisit le remplaçant le moins polyvalent pour garder les plus polyvalents en réserve)."""
    pcols = [p for p in postes["Poste"].astype(str) if p in comp.columns]
    comp = comp.copy()
    comp["Operateur"] = comp["Operateur"].astype(str)
    present = comp[~comp["Operateur"].isin(absents)]
    used, rows = set(), []
    need = postes.copy()
    need["Nb_operateurs"] = pd.to_numeric(need["Nb_operateurs"], errors="coerce").fillna(1).astype(int)
    need["crit"] = need["Critique"].astype(str).str.lower().str.startswith("o")
    for _, r in need.iterrows():
        tit = present[present["Poste_habituel"].astype(str) == str(r["Poste"])]["Operateur"].tolist()[: r["Nb_operateurs"]]
        for o in tit:
            rows.append((r["Poste"], o, "habituel")); used.add(o)
    for _, r in need.sort_values("crit", ascending=False).iterrows():
        have = sum(1 for x in rows if x[0] == r["Poste"])
        for _ in range(r["Nb_operateurs"] - have):
            cand = present[(~present["Operateur"].isin(used)) &
                           (pd.to_numeric(present.get(str(r["Poste"]), 0), errors="coerce").fillna(0) >= 1)].copy()
            if len(cand):
                cand["poly"] = cand[pcols].apply(pd.to_numeric, errors="coerce").fillna(0).sum(axis=1)
                o = cand.sort_values("poly")["Operateur"].iloc[0]
                rows.append((r["Poste"], o, "remplaçant")); used.add(o)
            else:
                rows.append((r["Poste"], "Aucun", "non tenu"))
    plan = pd.DataFrame(rows, columns=["Poste", "Operateur", "Statut"])
    plan = plan.merge(need[["Poste", "Designation", "Critique"]], on="Poste", how="left")
    order = {p: i for i, p in enumerate(postes["Poste"])}
    plan = plan.sort_values("Poste", key=lambda s: s.map(order))[["Poste", "Designation", "Critique", "Operateur", "Statut"]]
    libres = [o for o in present["Operateur"] if o not in used]
    return plan, libres


def page_idea1():
    d = idea_sections(1)
    data = get_data()
    with st.container(border=True):
        demo_head("Outil : affectation du jour selon les présents",
                  "Choisissez les absents (ou la date du pointage importé) : l'outil propose un remplaçant formé, "
                  "postes critiques d'abord.")
        comp, postes, pres = data["Competences"], data["Postes"], data["Presence"]
        left, right = st.columns([1, 1.25], gap="large")
        with left:
            default_abs = []
            if len(pres):
                pres = pres.copy()
                pres["Date"] = pd.to_datetime(pres["Date"], errors="coerce").dt.date
                dates = sorted(pres["Date"].dropna().unique(), reverse=True)
                if dates:
                    day = st.selectbox("Date du pointage", dates, format_func=lambda x: x.strftime("%d/%m/%Y"))
                    default_abs = pres[(pres["Date"] == day) & pres["Statut"].astype(str).str.lower().str.startswith("a")]["Operateur"].astype(str).tolist()
            absents = st.multiselect("Opérateurs absents", comp["Operateur"].astype(str).tolist(), default=default_abs,
                                     key=f"abs_{source_label()}")
            st.caption("Matrice de polyvalence (1 = formé au poste)")
            pc = [p for p in postes["Poste"].astype(str) if p in comp.columns]
            st.dataframe(comp.set_index("Operateur")[["Poste_habituel"] + pc].style.map(
                lambda v: "background-color:#DCEBFA;color:#0A2A5E;font-weight:700" if v == 1 else "", subset=pc),
                use_container_width=True)
        with right:
            plan, libres = assign(comp, postes, absents)
            colors_ = {"habituel": "#E3F6EC;color:#1E8A55", "remplaçant": "#E8F1FC;color:#1F5FAD", "non tenu": "#FDECEC;color:#C2393D"}
            rows = ""
            for _, r in plan.iterrows():
                crit = " <span class='tag' style='background:#FFF6EC;color:#B4621B'>critique</span>" if str(r["Critique"]).lower().startswith("o") else ""
                rows += (f"<div class='ref' style='align-items:center;justify-content:space-between;padding:8px 14px'>"
                         f"<div><b>{r['Poste']}</b> <small>{r['Designation']}</small>{crit}</div>"
                         f"<div><b>{r['Operateur']}</b> <span class='tag' style='background:{colors_[r['Statut']]}'>{r['Statut']}</span></div></div>")
            html(rows)
            nt = (plan["Statut"] == "non tenu").sum()
            m1, m2, m3 = st.columns(3)
            m1.metric("Postes tenus", f"{len(plan) - nt} / {len(plan)}")
            m2.metric("Remplacements", int((plan["Statut"] == "remplaçant").sum()))
            m3.metric("Opérateurs libres", len(libres))
            if libres:
                st.caption("Disponibles en renfort : " + ", ".join(libres))
            st.download_button("Exporter l'affectation (Excel)",
                               to_excel({"Affectation": plan, "Absents": pd.DataFrame({"Operateur": absents})}),
                               f"Affectation_{dt.date.today():%Y%m%d}.xlsx", icon=":material/download:")
    sources_block(d)


def page_idea2():
    d = idea_sections(2)
    data = get_data()
    p = params(data)
    ch = charges(data)
    with st.container(border=True):
        demo_head("Outil : la ligne peut-elle suivre ?",
                  "Les paramètres viennent du fichier importé. Faites varier la demande, les absences et les heures "
                  "supplémentaires pour tester un scénario.")
        a, b, c = st.columns(3)
        dem0 = int(p["Demande_jour"])
        demande = a.slider("Demande client (pièces / jour)", max(50, dem0 // 2), dem0 * 2, dem0, 10)
        absence = b.slider("Absentéisme (%)", 0, 30, 5)
        hs = c.slider("Heures supplémentaires (min / jour)", 0, 180, 0, 10)
        cycle0 = ch["Charge_par_op_s"].max()
        goulot = ch.loc[ch["Charge_par_op_s"].idxmax(), "Poste"]

        def scen(dem, ab, h):
            ouv = p["Ouverture_min"] + h
            cyc = cycle0 * (1 + ab / 100)
            cap = int(ouv * 60 * p["Rendement"] / cyc) if cyc else 0
            return ouv, cyc, cap, cap / dem if dem else 0

        ouv, cyc, cap, couv = scen(demande, absence, hs)
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Temps d'ouverture", f"{ouv:.0f} min")
        m2.metric(f"Temps de cycle ({goulot})", f"{cyc:.0f} s")
        m3.metric("Capacité (pcs/jour)", cap)
        m4.metric("Couverture", f"{couv:.0%}", delta=f"{cap - demande:+d} pcs")
        df = pd.DataFrame({"Indicateur": ["Demande", "Capacité"], "Pièces": [demande, cap]})
        chart = alt.Chart(df).mark_bar(cornerRadiusEnd=8, height=34).encode(
            y=alt.Y("Indicateur:N", title=None, sort=["Demande", "Capacité"]), x=alt.X("Pièces:Q", title="Pièces par jour"),
            color=alt.Color("Indicateur:N", scale=alt.Scale(domain=["Demande", "Capacité"],
                            range=["#C9D3E0", "#2BB673" if couv >= 1 else "#F4A261"]), legend=None)).properties(height=130)
        st.altair_chart(chart, use_container_width=True)
        if couv >= 1:
            st.success("La ligne couvre la demande avec ces hypothèses.", icon=":material/check_circle:")
        else:
            manque = demande - cap
            hs_need = max(0, manque * cyc / 60 / p["Rendement"])
            st.warning(f"Il manque environ {manque} pièces par jour, soit environ {hs_need:.0f} minutes de production "
                       f"supplémentaires. Autres pistes : renfort polyvalent ou rééquilibrage du poste {goulot}.", icon=":material/warning:")
        st.markdown("**Comparaison de scénarios**")
        sc = [("Base", dem0, 0, 0), ("Absence 10 %", dem0, 10, 0), ("Pic +20 %", int(dem0 * 1.2), 0, 0),
              ("Pic +20 % et absence 10 %", int(dem0 * 1.2), 10, 0), ("Pic +20 % avec 60 min sup", int(dem0 * 1.2), 0, 60),
              ("Scénario choisi", demande, absence, hs)]
        rows = []
        for n, dm, ab, h in sc:
            o, cy, ca, co = scen(dm, ab, h)
            rows.append({"Scénario": n, "Demande": dm, "Absentéisme %": ab, "Heures sup (min)": h, "Cycle (s)": round(cy, 1),
                         "Capacité": ca, "Couverture": f"{co:.0%}", "Décision": "OK" if co >= 1 else f"Manque {dm - ca} pcs"})
        sdf = pd.DataFrame(rows)
        st.dataframe(sdf, hide_index=True, use_container_width=True)
        st.download_button("Exporter l'étude de capacité (Excel)",
                           to_excel({"Scenarios": sdf, "Charge_postes": ch}), f"Etude_capacite_{dt.date.today():%Y%m%d}.xlsx",
                           icon=":material/download:")
    sources_block(d)


def page_idea3():
    d = idea_sections(3)
    data = get_data()
    p = params(data)
    with st.container(border=True):
        demo_head("Outil : Concept Line et Yamazumi",
                  "La gamme vient de l'onglet Operations. Modifiez un temps ou changez le poste d'une opération pour "
                  "tester un rééquilibrage, puis exportez la nouvelle version.")
        a, b = st.columns([1, 1.3], gap="large")
        with a:
            demande = st.number_input("Demande (pièces / jour)", 1, 100000, int(p["Demande_jour"]), 10)
            takt = p["Ouverture_min"] * 60 / demande
            postes_list = data["Postes"]["Poste"].astype(str).tolist()
            ed = st.data_editor(data["Operations"][["Poste", "Operation", "Temps_s"]], hide_index=True, num_rows="dynamic",
                                use_container_width=True, height=430, key=f"ops_{source_label()}",
                                column_config={"Poste": st.column_config.SelectboxColumn(options=postes_list, required=True),
                                               "Temps_s": st.column_config.NumberColumn("Temps (s)", min_value=0, step=1)})
        with b:
            tmp = dict(data); tmp["Operations"] = ed.dropna(subset=["Poste"])
            ch = charges(tmp)
            ch["Takt_s"] = round(takt, 1)
            ch["Ecart_takt_s"] = (ch["Charge_par_op_s"] - takt).round(1)
            ch["Taux_charge"] = (ch["Charge_par_op_s"] / takt).round(3)
            ch["Statut"] = ch["Taux_charge"].map(lambda t: "Surchargé" if t > 1 else ("Sous-chargé" if t < 0.75 else "Bien chargé"))
            g = ch.loc[ch["Charge_par_op_s"].idxmax()]
            eff = ch["Charge_s"].sum() / (ch["Nb_operateurs"].sum() * g["Charge_par_op_s"]) if g["Charge_par_op_s"] else 0
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Takt", f"{takt:.0f} s")
            m2.metric("Goulot", g["Poste"], f"{g['Charge_par_op_s']:.0f} s", delta_color="off")
            m3.metric("Surchargés", int((ch["Statut"] == "Surchargé").sum()))
            m4.metric("Efficience", f"{eff:.0%}")
            e2 = tmp["Operations"].copy()
            e2["Temps_s"] = pd.to_numeric(e2["Temps_s"], errors="coerce").fillna(0)
            e2 = e2.merge(ch[["Poste", "Nb_operateurs"]], on="Poste", how="left")
            e2["Temps_par_op"] = e2["Temps_s"] / e2["Nb_operateurs"].fillna(1)
            e2["Rang"] = "Opération " + (e2.groupby("Poste").cumcount() + 1).astype(str)
            bars = alt.Chart(e2).mark_bar(stroke="#fff", strokeWidth=1.5).encode(
                x=alt.X("Poste:N", title=None, sort=postes_list, axis=alt.Axis(labelAngle=0)),
                y=alt.Y("sum(Temps_par_op):Q", title="Secondes par opérateur"),
                color=alt.Color("Rang:N", legend=alt.Legend(orient="bottom", title=None),
                                scale=alt.Scale(range=["#0A2A5E", "#1F5FAD", "#00A3E0", "#7FC8EC", "#B9DDF2", "#DCEBFA"])),
                order=alt.Order("Rang:N"), tooltip=["Poste", "Operation", "Temps_s"])
            rule = alt.Chart(pd.DataFrame({"t": [takt]})).mark_rule(color="#F4A261", strokeWidth=3, strokeDash=[7, 5]).encode(y="t:Q")
            st.altair_chart((bars + rule).properties(height=340), use_container_width=True)
        st.dataframe(ch[["Poste", "Designation", "Nb_operateurs", "Charge_s", "Charge_par_op_s", "Ecart_takt_s", "Taux_charge", "Statut"]],
                     hide_index=True, use_container_width=True,
                     column_config={"Taux_charge": st.column_config.ProgressColumn("Taux de charge", min_value=0, max_value=1.3, format="percent")})
        st.download_button("Exporter la Concept Line (Excel)",
                           to_excel({"Operations": ed, "Charge_postes": ch,
                                     "Parametres": pd.DataFrame({"Parametre": ["Demande_jour", "Takt_s"], "Valeur": [demande, round(takt, 1)]})}),
                           f"Concept_Line_{dt.date.today():%Y%m%d}.xlsx", icon=":material/download:")
    sources_block(d)


def page_idea4():
    d = idea_sections(4)
    data = get_data()
    rout = data["Routines"]
    with st.container(border=True):
        demo_head("Outil : checklist de shift et suivi des écarts",
                  "Les points de contrôle viennent de l'onglet Routines. Chaque point non conforme est enregistré "
                  "comme écart et peut être exporté.")
        h1, h2, h3 = st.columns(3)
        day = h1.date_input("Date", dt.date.today(), format="DD/MM/YYYY")
        shift = h2.selectbox("Shift", ["Matin", "Après-midi", "Nuit"])
        resp = h3.selectbox("Responsable", ["Tous"] + sorted(rout["Responsable"].astype(str).unique()), index=0)
        sel = rout if resp == "Tous" else rout[rout["Responsable"].astype(str) == resp]
        a, b = st.columns([1.1, 1], gap="large")
        res = []
        with a:
            for i, r in sel.reset_index(drop=True).iterrows():
                ok = st.toggle(str(r["Point_de_controle"]), value=True, key=f"rt_{resp}_{i}_{source_label()}")
                com = "" if ok else st.text_input("Commentaire", key=f"cm_{resp}_{i}", placeholder="Décrire l'écart",
                                                  label_visibility="collapsed")
                res.append({"Date": day, "Shift": shift, "Point_de_controle": r["Point_de_controle"],
                            "Responsable": r["Responsable"], "Conforme": "Oui" if ok else "Non", "Commentaire": com})
        with b:
            rdf = pd.DataFrame(res)
            ok = (rdf["Conforme"] == "Oui").sum() if len(rdf) else 0
            st.metric("Points conformes", f"{ok} / {len(rdf)}")
            st.progress(ok / len(rdf) if len(rdf) else 0)
            ec = rdf[rdf["Conforme"] == "Non"] if len(rdf) else rdf
            if len(ec):
                html("".join(f"<div class='ref' style='background:#FDECEC;border-color:#F7C7C9'>{icon('alert', '#E5484D', '#FFFFFF')}"
                             f"<div><b style='color:#C2393D'>Écart</b> · {e['Responsable']}<br>{e['Point_de_controle']}"
                             f"{'<br><small>' + e['Commentaire'] + '</small>' if e['Commentaire'] else ''}</div></div>" for _, e in ec.iterrows()))
            else:
                st.success("Aucun écart : démarrage validé.", icon=":material/check_circle:")
            if st.button("Enregistrer la checklist", icon=":material/save:", type="primary"):
                hist = st.session_state.get("hist", pd.DataFrame())
                st.session_state["hist"] = pd.concat([hist, rdf], ignore_index=True)
                st.toast("Checklist enregistrée", icon=":material/check:")
        hist = st.session_state.get("hist")
        if hist is not None and len(hist):
            st.markdown("**Historique de la session**")
            st.dataframe(hist, hide_index=True, use_container_width=True)
            st.download_button("Exporter l'historique (Excel)", to_excel({"Historique": hist,
                               "Ecarts": hist[hist["Conforme"] == "Non"]}), f"Routines_{dt.date.today():%Y%m%d}.xlsx",
                               icon=":material/download:")
    sources_block(d)



def page_synergy():
    header("Synergie", "Une base commune, quatre usages",
           "La Concept Line rassemble les données de la ligne. Les autres idées les réutilisent sans ressaisie.")
    html(f'<div class="ill">{ill.synergy()}</div>')
    st.write("")
    html('<div class="band" style="background:#0A2A5E;color:#fff">On commence par la <b>Concept Line</b> : '
         'elle alimente toutes les autres idées.</div>')


def page_roadmap():
    header("Feuille de route", "Une mise en œuvre progressive",
           "Chaque étape est testée sur une ligne pilote avant d'être étendue.")
    steps = [("Concept Line", "Décrire une ligne pilote : postes, opérations, temps.", "layers"),
             ("Répartition", "Affecter les opérateurs selon les présents.", "users"),
             ("Capacité", "Tester des scénarios de demande et d'absences.", "gauge"),
             ("Routines", "Digitaliser les checklists et faire le bilan.", "check")]
    html('<div class="tl">' + "".join(
        f'<div class="step"><div style="display:flex;justify-content:space-between;align-items:center">'
        f'<div class="n">{i}</div>{icon(ic)}</div><h4 style="color:#0A2A5E;margin:.7rem 0 .2rem">{t}</h4>'
        f'<p style="color:#4A5B74;font-size:.92rem;margin:0">{b}</p></div>'
        for i, (t, b, ic) in enumerate(steps, 1)) + '</div>')
    st.write("")
    header("Pour avancer", "Ce dont nous avons besoin")
    need = [("target", "Votre validation", "Choisir avec vous l'idée par laquelle commencer."),
            ("flag", "Une ligne pilote", "Et un référent méthodes ou production."),
            ("db", "L'accès aux données", "Postes, temps, compétences, présence (anonymisées).")]
    cols = st.columns(3)
    for col, (ic, t, b) in zip(cols, need):
        col.markdown(card(ic, t, f"<p>{b}</p>"), unsafe_allow_html=True)
    st.write("")
    header("À vous de choisir", "Par quelle idée commencer ?")
    choix = st.radio("Votre choix", [f"0{k} · {d['title']}" for k, d in IDEAS.items()], index=2,
                     horizontal=True, label_visibility="collapsed")
    if choix.startswith("03"):
        st.info("Concept Line digitale : c'est notre recommandation, car elle sert de base aux autres idées.", icon=":material/recommend:")
    else:
        st.info(f"Vous avez choisi « {choix[5:]} ». Nous préparerons un prototype sur la ligne pilote.", icon=":material/rocket_launch:")


def page_refs():
    header("Bibliographie", "Ce que dit la littérature sur nos idées", "Deux références par idée, avec le lien vers l'article.")
    for k, d in IDEAS.items():
        html(f'<div style="display:flex;gap:12px;align-items:center;margin:1rem 0 .5rem">{icon(d["ic"], d["color"], light(d["color"]))}'
             f'<b style="color:#0A2A5E;font-size:1.05rem">0{k} · {d["title"]}</b></div>')
        cols = st.columns(2)
        for col, (a, t, j, u) in zip(cols, d["refs"]):
            col.markdown(f'<div class="ref">{icon("book", d["color"], light(d["color"]))}<div><a href="{u}" target="_blank">{a} ↗</a>'
                         f'<br>{t}<br><small>{j}</small></div></div>', unsafe_allow_html=True)


# ------------------------------------------------------------------ tableau de bord global
def kpi(ic, label, value, sub="", status="info"):
    col = {"ok": ("#2BB673", "#E3F6EC"), "warn": ("#F4A261", "#FFF3E6"), "bad": ("#E5484D", "#FDECEC"),
           "info": ("#1F5FAD", "#E8F1FC")}[status]
    return (f'<div class="kpi" style="border-top:4px solid {col[0]}">'
            f'<div style="display:flex;justify-content:space-between;align-items:flex-start">'
            f'<div><div class="kl">{label}</div><div class="kv">{value}</div></div>{icon(ic, col[0], col[1])}</div>'
            f'<div class="ks">{sub}</div></div>')


def page_dashboard():
    data = get_data()
    p = params(data)
    header("Synthèse", "Tableau de bord de la ligne",
           "Toutes les idées réunies sur un seul écran. Modifiez le scénario : tous les indicateurs se mettent à jour.")
    data_badge()
    st.write("")
    with st.container(border=True):
        f1, f2, f3, f4 = st.columns([1, 1, 1, 1.6])
        dem0 = int(p["Demande_jour"])
        demande = f1.number_input("Demande (pcs / jour)", 1, 100000, dem0, 10, key="db_dem")
        absence = f2.slider("Absentéisme (%)", 0, 30, 0, key="db_abs")
        hs = f3.slider("Heures sup (min / jour)", 0, 180, 0, 10, key="db_hs")
        pres = data["Presence"].copy()
        default_abs = []
        if len(pres):
            pres["Date"] = pd.to_datetime(pres["Date"], errors="coerce").dt.date
            last = pres["Date"].dropna().max()
            default_abs = pres[(pres["Date"] == last) & pres["Statut"].astype(str).str.lower().str.startswith("a")]["Operateur"].astype(str).tolist()
        absents = f4.multiselect("Opérateurs absents", data["Competences"]["Operateur"].astype(str).tolist(),
                                 default=default_abs, key=f"db_absents_{source_label()}")

    # ---- calculs
    ch = charges(data)
    ouv = p["Ouverture_min"] + hs
    takt = ouv * 60 / demande
    takt0 = p["Ouverture_min"] * 60 / demande
    gi = ch["Charge_par_op_s"].idxmax()
    goulot, cyc0 = ch.loc[gi, "Poste"], ch.loc[gi, "Charge_par_op_s"]
    cyc = cyc0 * (1 + absence / 100)
    cap = int(ouv * 60 * p["Rendement"] / cyc) if cyc else 0
    couv = cap / demande
    eff = ch["Charge_s"].sum() / (ch["Nb_operateurs"].sum() * cyc0) if cyc0 else 0
    ch["Taux_charge"] = ch["Charge_par_op_s"] / takt0
    ch["Statut"] = ch["Taux_charge"].map(lambda t: "Surchargé" if t > 1 else ("Sous-chargé" if t < 0.75 else "Bien chargé"))
    nsur = int((ch["Statut"] == "Surchargé").sum())
    plan, libres = assign(data["Competences"], data["Postes"], absents)
    nt = int((plan["Statut"] == "non tenu").sum())
    nrep = int((plan["Statut"] == "remplaçant").sum())
    hist = st.session_state.get("hist")
    if hist is not None and len(hist):
        lastc = hist.iloc[-len(data["Routines"]):] if len(hist) >= len(data["Routines"]) else hist
        conf = (lastc["Conforme"] == "Oui").mean()
        ecarts = lastc[lastc["Conforme"] == "Non"]
        conf_txt, conf_st = f"{conf:.0%}", ("ok" if conf == 1 else "warn" if conf >= .8 else "bad")
        conf_sub = "dernière checklist enregistrée"
    else:
        ecarts = pd.DataFrame()
        conf_txt, conf_st, conf_sub = "—", "info", "aucune checklist enregistrée"

    # ---- KPI
    r1 = st.columns(4)
    r1[0].markdown(kpi("clock", "Takt", f"{takt0:.0f} s", f"{p['Ouverture_min']:.0f} min ÷ {demande} pcs"), unsafe_allow_html=True)
    r1[1].markdown(kpi("target", "Temps de cycle", f"{cyc:.0f} s", f"goulot {goulot}", "bad" if cyc > takt else "ok"), unsafe_allow_html=True)
    r1[2].markdown(kpi("gauge", "Capacité", f"{cap}", "pièces par jour", "ok" if couv >= 1 else "warn"), unsafe_allow_html=True)
    r1[3].markdown(kpi("trend", "Couverture", f"{couv:.0%}", f"{cap - demande:+d} pcs / jour",
                       "ok" if couv >= 1 else "warn" if couv >= .9 else "bad"), unsafe_allow_html=True)
    st.write("")
    r2 = st.columns(4)
    r2[0].markdown(kpi("layers", "Efficience d'équilibrage", f"{eff:.0%}", f"{nsur} poste(s) surchargé(s)",
                       "ok" if eff >= .85 else "warn"), unsafe_allow_html=True)
    r2[1].markdown(kpi("users", "Postes tenus", f"{len(plan) - nt} / {len(plan)}", f"{len(absents)} absent(s), {nrep} remplacement(s)",
                       "ok" if nt == 0 else "bad"), unsafe_allow_html=True)
    r2[2].markdown(kpi("flag", "Renforts disponibles", f"{len(libres)}", ", ".join(libres) if libres else "aucun opérateur libre",
                       "ok" if libres else "warn"), unsafe_allow_html=True)
    r2[3].markdown(kpi("check", "Conformité routines", conf_txt, conf_sub, conf_st), unsafe_allow_html=True)
    st.write("")

    # ---- graphiques
    g1, g2 = st.columns([1.35, 1], gap="medium")
    with g1:
        with st.container(border=True):
            html('<h4 class="dh">Yamazumi : charge par poste</h4>')
            ops = data["Operations"].copy()
            ops["Temps_s"] = pd.to_numeric(ops["Temps_s"], errors="coerce").fillna(0)
            ops = ops.merge(ch[["Poste", "Nb_operateurs"]], on="Poste", how="left")
            ops["Temps_par_op"] = ops["Temps_s"] / ops["Nb_operateurs"].fillna(1)
            ops["Rang"] = "Op. " + (ops.groupby("Poste").cumcount() + 1).astype(str)
            pl = data["Postes"]["Poste"].astype(str).tolist()
            bars = alt.Chart(ops).mark_bar(stroke="#fff", strokeWidth=1.2).encode(
                x=alt.X("Poste:N", sort=pl, title=None, axis=alt.Axis(labelAngle=0)),
                y=alt.Y("sum(Temps_par_op):Q", title="s / opérateur"),
                color=alt.Color("Rang:N", legend=alt.Legend(orient="bottom", title=None),
                                scale=alt.Scale(range=["#0A2A5E", "#1F5FAD", "#00A3E0", "#7FC8EC", "#B9DDF2"])),
                order=alt.Order("Rang:N"), tooltip=["Poste", "Operation", "Temps_s"])
            rule = alt.Chart(pd.DataFrame({"t": [takt0]})).mark_rule(color="#F4A261", strokeWidth=3, strokeDash=[7, 5]).encode(y="t:Q")
            st.altair_chart((bars + rule).properties(height=300), use_container_width=True)
    with g2:
        with st.container(border=True):
            html('<h4 class="dh">Demande et capacité par scénario</h4>')
            rows = []
            for n, dm, ab, h in [("Actuel", demande, absence, hs), ("Absence 10 %", demande, 10, hs),
                                 ("Pic +20 %", int(demande * 1.2), absence, hs), ("Pic + 60 min", int(demande * 1.2), absence, hs + 60)]:
                cy = cyc0 * (1 + ab / 100)
                ca = int((p["Ouverture_min"] + h) * 60 * p["Rendement"] / cy)
                rows += [{"Scénario": n, "Type": "Demande", "Pièces": dm}, {"Scénario": n, "Type": "Capacité", "Pièces": ca}]
            sdf = pd.DataFrame(rows)
            order_ = ["Actuel", "Absence 10 %", "Pic +20 %", "Pic + 60 min"]
            c = alt.Chart(sdf).mark_bar(cornerRadiusTopLeft=4, cornerRadiusTopRight=4).encode(
                x=alt.X("Scénario:N", sort=order_, title=None, axis=alt.Axis(labelAngle=0)),
                xOffset=alt.XOffset("Type:N", sort=["Demande", "Capacité"]), y=alt.Y("Pièces:Q", title="Pièces / jour"),
                color=alt.Color("Type:N", scale=alt.Scale(domain=["Demande", "Capacité"], range=["#C9D3E0", "#1F5FAD"]),
                                legend=alt.Legend(orient="bottom", title=None)),
                tooltip=["Scénario", "Type", "Pièces"]).properties(height=300)
            st.altair_chart(c, use_container_width=True)

    g3, g4 = st.columns([1, 1.2], gap="medium")
    with g3:
        with st.container(border=True):
            html('<h4 class="dh">Taux de charge par poste</h4>')
            tc = alt.Chart(ch).mark_bar(cornerRadiusEnd=5).encode(
                y=alt.Y("Poste:N", sort=pl, title=None), x=alt.X("Taux_charge:Q", title=None, axis=alt.Axis(format="%")),
                color=alt.Color("Statut:N", scale=alt.Scale(domain=["Surchargé", "Bien chargé", "Sous-chargé"],
                                range=["#E5484D", "#2BB673", "#F4A261"]), legend=alt.Legend(orient="bottom", title=None)),
                tooltip=["Poste", "Designation", alt.Tooltip("Taux_charge:Q", format=".0%"), "Statut"])
            one = alt.Chart(pd.DataFrame({"x": [1]})).mark_rule(color="#0A2A5E", strokeDash=[4, 4]).encode(x="x:Q")
            st.altair_chart((tc + one).properties(height=260), use_container_width=True)
    with g4:
        with st.container(border=True):
            html('<h4 class="dh">Affectation du jour</h4>')
            st.dataframe(plan, hide_index=True, use_container_width=True, height=260,
                         column_config={"Statut": st.column_config.TextColumn("Statut")})

    # ---- alertes
    alerts = []
    if couv < 1:
        alerts.append(("bad", f"Capacité insuffisante : il manque {demande - cap} pièces par jour (couverture {couv:.0%})."))
    for _, r in ch[ch["Statut"] == "Surchargé"].iterrows():
        alerts.append(("warn", f"Poste {r['Poste']} surchargé : {r['Charge_par_op_s']:.0f} s pour un takt de {takt0:.0f} s."))
    for _, r in plan[plan["Statut"] == "non tenu"].iterrows():
        alerts.append(("bad", f"Poste {r['Poste']} non tenu : aucun opérateur présent formé à ce poste."))
    for _, r in ecarts.iterrows():
        alerts.append(("warn", f"Écart routine ({r['Responsable']}) : {r['Point_de_controle']}."))
    a1, a2 = st.columns([1.6, 1], gap="medium")
    with a1:
        with st.container(border=True):
            html(f'<h4 class="dh">Alertes ({len(alerts)})</h4>')
            if alerts:
                html("".join(f"<div class='ref' style='padding:8px 12px;background:{'#FDECEC' if s == 'bad' else '#FFF6EC'};"
                             f"border-color:{'#F7C7C9' if s == 'bad' else '#F8DDBF'}'>"
                             f"{icon('alert', '#E5484D' if s == 'bad' else '#D9822B', '#FFFFFF')}<div style='align-self:center'>{t}</div></div>"
                             for s, t in alerts))
            else:
                st.success("Aucune alerte : la ligne est bien équilibrée et la demande est couverte.", icon=":material/check_circle:")
    with a2:
        with st.container(border=True):
            html('<h4 class="dh">Exporter le tableau de bord</h4><p style="color:#6B7A90;font-size:.9rem">'
                 'Un fichier Excel avec les indicateurs, la charge des postes, l\'affectation, les scénarios et les alertes.</p>')
            kp = pd.DataFrame({"Indicateur": ["Demande", "Takt (s)", "Temps de cycle (s)", "Poste goulot", "Capacité (pcs/j)",
                                              "Couverture", "Efficience", "Postes tenus", "Conformité routines"],
                               "Valeur": [demande, round(takt0, 1), round(cyc, 1), goulot, cap, f"{couv:.0%}", f"{eff:.0%}",
                                          f"{len(plan) - nt}/{len(plan)}", conf_txt]})
            st.download_button("Télécharger (Excel)", to_excel({
                "Indicateurs": kp, "Charge_postes": ch, "Affectation": plan,
                "Scenarios": sdf.pivot(index="Scénario", columns="Type", values="Pièces").reset_index(),
                "Alertes": pd.DataFrame({"Niveau": [a for a, _ in alerts], "Alerte": [b for _, b in alerts]})}),
                f"Tableau_de_bord_{dt.date.today():%Y%m%d}.xlsx", icon=":material/download:", type="primary",
                use_container_width=True)
            st.caption(f"Scénario : demande {demande}, absentéisme {absence} %, heures sup {hs} min.")



# ------------------------------------------------------------------ navigation
pages = {
    "Présentation": [
        st.Page(page_home, title="Accueil", icon=":material/home:", default=True),
        st.Page(page_start, title="Point de départ", icon=":material/flag:", url_path="depart"),
    ],
    "Outil": [
        st.Page(page_data, title="Importer les données", icon=":material/upload_file:", url_path="donnees"),
    ],
    "Les 4 idées": [
        st.Page(page_idea1, title="01 · Répartition du travail", icon=":material/groups:", url_path="repartition"),
        st.Page(page_idea2, title="02 · Étude de capacité", icon=":material/speed:", url_path="capacite"),
        st.Page(page_idea3, title="03 · Concept Line digitale", icon=":material/stacked_bar_chart:", url_path="concept-line"),
        st.Page(page_idea4, title="04 · Routines digitales", icon=":material/fact_check:", url_path="routines"),
    ],
    "Synthèse": [
        st.Page(page_synergy, title="Synergie", icon=":material/hub:", url_path="synergie"),
        st.Page(page_roadmap, title="Feuille de route", icon=":material/route:", url_path="feuille-de-route"),
        st.Page(page_refs, title="Bibliographie", icon=":material/menu_book:", url_path="bibliographie"),
    ],
    "Pilotage": [
        st.Page(page_dashboard, title="Tableau de bord", icon=":material/dashboard:", url_path="tableau-de-bord"),
    ],
}
with st.sidebar:
    html('<div style="padding:.3rem 0 1rem"><div style="font-weight:800;font-size:1.15rem;letter-spacing:.02em">LEONI · Berchid</div>'
         '<div style="font-size:.8rem;opacity:.75">Alternance GIPR · ENSAM Meknès</div></div>')
nav = st.navigation(pages)
with st.sidebar:
    st.divider()
    html('<div style="font-size:.78rem;opacity:.8">Fatiha Mahnoun<br>Karima Abdous<br>Oumaima Khair<br><br><b>Encadrante académique</b><br>Madame Bonou<br>'
         '<b>Encadrant industriel</b><br>Anas Madani<br><br>Novembre 2026</div>')
html('<div id="haut"></div>')
nav.run()
html('<div class="foot">Alternance GIPR · ENSAM Meknès × Leoni Wiring Systems Berchid · Sans fichier importé, l\'outil utilise des données d\'exemple</div>')
html('<a class="totop" href="#haut" title="Haut de page">↑</a>')
