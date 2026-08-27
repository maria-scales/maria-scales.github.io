"""Seven figures for «Job boards are full of marketing. Most of it isn't.»
Hand-built SVG in the mariascales.com palette (Tailwind grays + blue-700 accent).
Monochrome by design (the site uses one blue and grays): identity is carried by lightness steps, 2px gaps, legend and direct labels, not by hue.
"""
import pathlib, html

OUT = pathlib.Path(__file__).parent
W = 800
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', 'Liberation Sans', 'DejaVu Sans', sans-serif"
INK, INK2, MUTED, GRID, SURF = "#111827", "#374151", "#6b7280", "#e5e7eb", "#ffffff"
# Site palette only: link blue + Tailwind grays. No second hue anywhere on mariascales.com.
BLUE, DARK, GRAY, LIGHT = "#2563eb", "#93c5fd", "#cbd5e1", "#e2e8f0"  # blue family + slate: livelier than gray, still the site
AMBER, TEAL = DARK, LIGHT  # legacy names: sales -> dark gray, PMM+brand -> light gray
BAR = 22  # bar thickness (<= 24)
SRC = "Source: author's job-search database, 18,436 open postings at 590 companies, 6 Jul – 26 Aug 2026. mariascales.com"


def tw(s, size):  # rough text width
    return len(s) * size * 0.56


def esc(s):
    return html.escape(str(s), quote=True)


def note_lines(text, x, y, maxc=108, size=12):
    import textwrap
    out = []
    for i, line in enumerate(textwrap.wrap(text, maxc)):
        out.append(f'<text x="{x}" y="{y + i*16}" font-size="{size}" fill="{MUTED}">{esc(line)}</text>')
    return "\n".join(out), y + 16 * len(out)


def frame(title, subtitle, body, h, legend=None):
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" '
             f'font-family="{FONT}" role="img" aria-label="{esc(title)}">',
             f'<rect width="{W}" height="{h}" fill="{SURF}"/>',
             f'<text x="32" y="38" font-size="19" font-weight="600" fill="{INK}">{esc(title)}</text>',
             f'<text x="32" y="60" font-size="13" fill="{MUTED}">{esc(subtitle)}</text>']
    if legend:
        x = 32
        for color, label, hatch in legend:
            fill = f"url(#hatch-{color[1:]})" if hatch else color
            parts.append(f'<rect x="{x}" y="{76}" width="12" height="12" rx="2" fill="{fill}"/>')
            parts.append(f'<text x="{x+18}" y="{86}" font-size="12" fill="{INK2}">{esc(label)}</text>')
            x += 18 + tw(label, 12) + 22
    parts.append(body)
    parts.append(f'<text x="32" y="{h-16}" font-size="11" fill="{MUTED}">{esc(SRC)}</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def hatch_def(color):
    cid = f"hatch-{color[1:]}"
    return (f'<defs><pattern id="{cid}" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
            f'<rect width="6" height="6" fill="{SURF}"/><line x1="0" y1="0" x2="0" y2="6" stroke="{color}" stroke-width="2.2"/></pattern></defs>')


def bar_path(x, y, w, h, r=4, horizontal=True):
    """Rounded at the data end only, square at the baseline."""
    if w <= 0 and horizontal:
        return ""
    if horizontal:
        r = min(r, w / 2, h / 2)
        return (f'<path d="M{x},{y} h{w-r} a{r},{r} 0 0 1 {r},{r} v{h-2*r} a{r},{r} 0 0 1 -{r},{r} h-{w-r} z"/>')
    else:  # vertical column, y is top, grows down to baseline y+h
        r = min(r, w / 2, h / 2)
        return (f'<path d="M{x},{y+h} v-{h-r} a{r},{r} 0 0 1 {r},-{r} h{w-2*r} a{r},{r} 0 0 1 {r},{r} v{h-r} z"/>')


def hbars(rows, top, left, right, vmax, fmt, note=None):
    """rows: [(label, value, color, sublabel)] horizontal bars with direct labels."""
    body = []
    scale = (right - left) / vmax
    y = top
    for label, val, color, sub in rows:
        body.append(f'<text x="{left-12}" y="{y+BAR/2+4}" font-size="13" text-anchor="end" fill="{INK}">{esc(label)}</text>')
        w = val * scale
        body.append(f'<g fill="{color}">{bar_path(left, y, w, BAR)}</g>')
        lab = fmt(val)
        body.append(f'<text x="{left+w+8}" y="{y+BAR/2+4}" font-size="13" font-weight="600" fill="{INK}">{esc(lab)}</text>')
        if sub:
            body.append(f'<text x="{left+w+8+tw(lab,13)*1.15+8}" y="{y+BAR/2+4}" font-size="12" fill="{MUTED}">{esc(sub)}</text>')
        y += BAR + 14
    body.append(f'<line x1="{left}" y1="{top-6}" x2="{left}" y2="{y-8}" stroke="{GRID}" stroke-width="1"/>')
    if note:
        t, y = note_lines(note, 32, y + 10)
    body.append(t if note else "")
    return "\n".join(body), y


# ── Figure 1 ──────────────────────────────────────────────────────────────────
def fig1():
    rows = [("Sales & adjacent", 3818, AMBER, "63%"),
            ("Other marketing", 1397, GRAY, "23%"),
            ("Performance / Growth / UA", 627, BLUE, "10% — my disciplines"),
            ("Product marketing", 160, GRAY, "3%"),
            ("Brand", 82, GRAY, "1%")]
    body, y = hbars(rows, 100, 230, 640, 3818, lambda v: f"{v:,}",
                    note="Sales & adjacent = accounts, sales, partnerships, field, customer success, GTM, demand gen. Marketing operations (583) sits in “Other marketing”.")
    return frame("Two thirds of “marketing” hiring is commercial roles",
                 "6,084 open postings whose broad type is Marketing, by discipline group", body, y + 32)


# ── Figure 2 ──────────────────────────────────────────────────────────────────
def fig2():
    segs = [("Sales & adjacent", AMBER), ("Other marketing", GRAY), ("Product marketing + brand", TEAL), ("Performance / Growth / UA", BLUE)]
    cols = [("B2B companies", 3902, [2667, 726, 131, 378]),
            ("B2C companies", 642, [187, 319, 43, 93])]
    top, H, cw, gap = 110, 250, 130, 110
    x0 = 230
    body = []
    for i, (name, n, vals) in enumerate(cols):
        x = x0 + i * (cw + gap)
        ycur = top
        for (lab, col), v in zip(segs, vals):
            h = H * v / n
            hh = max(h - 2, 0)  # 2px surface gap
            body.append(f'<rect x="{x}" y="{ycur+1}" width="{cw}" height="{hh}" fill="{col}"/>')
            pct = round(100 * v / n)
            if h >= 18:
                ink = "#ffffff" if col == BLUE else INK
                body.append(f'<text x="{x+cw/2}" y="{ycur+h/2+5}" font-size="13" font-weight="600" text-anchor="middle" fill="{ink}">{pct}%</text>')
            else:
                body.append(f'<text x="{x+cw+8}" y="{ycur+h/2+4}" font-size="12" fill="{INK2}">{pct}%</text>')
            ycur += h
        body.append(f'<text x="{x+cw/2}" y="{top+H+22}" font-size="13" font-weight="600" text-anchor="middle" fill="{INK}">{esc(name)}</text>')
        body.append(f'<text x="{x+cw/2}" y="{top+H+40}" font-size="12" text-anchor="middle" fill="{MUTED}">{n:,} marketing postings</text>')
    t, _ = note_lines("Mixed-audience companies (1,540 postings) behave like B2B: 63% commercial. Audience is a property of the company, not of the posting.", 32, top + H + 70)
    body.append(t)
    legend = [(c, l, False) for l, c in segs]
    return frame("A B2C company means marketing. A B2B company means sales.",
                 "Share of each company type's marketing postings, by discipline group", "\n".join(body), top + H + 130, legend)


# ── Figure 3 ──────────────────────────────────────────────────────────────────
def fig3():
    xs = ["any board", "5+ openings", "10+", "25+", "50+"]
    ns = [590, 418, 306, 164, 85]
    s1 = [22, 8, 6, 2, 1]      # no marketing role
    s2 = [62, 51, 46, 36, 25]  # no role of my kind
    left, right, top, bottom = 90, 700, 110, 340
    body = []
    def X(i): return left + i * (right - left) / (len(xs) - 1)
    def Y(v): return bottom - (bottom - top) * v / 70
    for g in (0, 20, 40, 60):
        body.append(f'<line x1="{left}" y1="{Y(g)}" x2="{right}" y2="{Y(g)}" stroke="{GRID}" stroke-width="1"/>')
        body.append(f'<text x="{left-10}" y="{Y(g)+4}" font-size="12" text-anchor="end" fill="{MUTED}">{g}%</text>')
    for i, lab in enumerate(xs):
        body.append(f'<text x="{X(i)}" y="{bottom+22}" font-size="12" text-anchor="middle" fill="{INK2}">{esc(lab)}</text>')
        body.append(f'<text x="{X(i)}" y="{bottom+38}" font-size="11" text-anchor="middle" fill="{MUTED}">n = {ns[i]}</text>')
    for series, col, name in ((s2, BLUE, "No performance / growth / UA role"), (s1, AMBER, "No marketing role at all")):
        pts = " ".join(f"{X(i)},{Y(v)}" for i, v in enumerate(series))
        body.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
        for i, v in enumerate(series):
            body.append(f'<circle cx="{X(i)}" cy="{Y(v)}" r="5" fill="{col}" stroke="{SURF}" stroke-width="2"/>')
        body.append(f'<text x="{X(0)-2}" y="{Y(series[0])-12}" font-size="13" font-weight="600" fill="{INK}">{series[0]}%</text>')
        body.append(f'<text x="{X(4)+12}" y="{Y(series[-1])+4}" font-size="13" font-weight="600" fill="{INK}">{series[-1]}%</text>')
    legend = [(BLUE, "No performance / growth / UA role", False), (AMBER, "No marketing role at all", False)]
    return frame("The bigger the board, the more certain the answer",
                 "Share of companies with no such opening, by minimum board size (companies with at least one real open posting)",
                 "\n".join(body), bottom + 85, legend)


# ── Figure 4 ──────────────────────────────────────────────────────────────────
def fig4():
    rows = [("United States", 2357, 1697, 660), ("United Kingdom", 135, 71, 64), ("Canada", 110, 82, 28), ("Germany", 73, 48, 25)]
    left, right, top = 200, 640, 106
    body = [hatch_def(GRAY)]
    y = top
    for name, n, locked, unres in rows:
        body.append(f'<text x="{left-12}" y="{y+BAR/2+4}" font-size="13" text-anchor="end" fill="{INK}">{esc(name)}</text>')
        w1 = (right - left) * locked / n
        w2 = (right - left) * unres / n
        body.append(f'<rect x="{left}" y="{y}" width="{w1-1}" height="{BAR}" fill="{BLUE}"/>')
        body.append(f'<rect x="{left+w1+1}" y="{y}" width="{w2-1}" height="{BAR}" fill="url(#hatch-{GRAY[1:]})"/>')
        body.append(f'<text x="{left+8}" y="{y+BAR/2+4}" font-size="12" font-weight="600" fill="#ffffff">{locked:,}</text>')
        body.append(f'<text x="{left+w1+8}" y="{y+BAR/2+4}" font-size="12" fill="{INK2}">{unres:,}</text>')
        body.append(f'<text x="{right+10}" y="{y+BAR/2+4}" font-size="12" font-weight="600" fill="{INK}">0 open</text>')
        body.append(f'<text x="{right+60}" y="{y+BAR/2+4}" font-size="11" fill="{MUTED}">of {n:,}</text>')
        y += BAR + 16
    t, y = note_lines("Across the whole dataset: 4,462 remote postings; 2,977 resolved → 2,474 residents-only (83%), 169 region-locked, 66 worldwide (2%). Unresolved rows are not yet read, not open.", 32, y + 12)
    body.append(t)
    legend = [(BLUE, "Residents of this country only", False), (GRAY, "Scope not yet resolved", True)]
    return frame("“Remote” means “remote, if you already live here”",
                 "Postings labelled remote, by country, split by who may actually apply", "\n".join(body), y + 30, legend)


# ── Figure 5 ──────────────────────────────────────────────────────────────────
def fig5():
    rows = [("Data", 48.9, BLUE, "627 of 1,283"), ("Business", 5.0, GRAY, "17 of 340"), ("Engineering", 4.1, GRAY, "202 of 4,880"),
            ("Marketing", 2.1, GRAY, "126 of 6,084"), ("Analytics", 2.0, GRAY, "10 of 496"), ("Product", 1.2, GRAY, "9 of 727")]
    body, y = hbars(rows, 100, 150, 600, 48.9, lambda v: f"{v:.0f}%" if v >= 10 else f"{v:.1f}%",
                    note="Title search only: ai, artificial intelligence, machine learning, ML, GenAI, generative, agentic, LLM, copilot. 995 titles in all.")
    return frame("AI hiring is not spread across the company. It is one column.",
                 "Share of open postings whose title mentions AI, by broad type", body, y + 32)


# ── Figure 6 ──────────────────────────────────────────────────────────────────
def fig6():
    rows = [("Security", 3.4, GRAY, "323 at 96 companies"), ("Machine learning", 3.3, GRAY, "255 at 77"), ("AI", 2.8, GRAY, "383 at 139"),
            ("Product management", 2.8, GRAY, "727 at 259"), ("My disciplines", 2.8, BLUE, "627 at 226"), ("Analytics", 2.7, GRAY, "416 at 153"),
            ("Data engineering", 2.4, GRAY, "322 at 137"), ("Design", 2.1, GRAY, "193 at 93")]
    body, y = hbars(rows, 100, 200, 560, 3.4, lambda v: f"{v:.1f}",
                    note="Openings per hiring company — the one comparison this sample supports. Off the chart: engineering at 12.3 (about 9 once city clones are collapsed).")
    return frame("Every neighbouring profession is the same width",
                 "Open postings per company that has at least one, by profession", body, y + 32)


# ── Figure 7 ──────────────────────────────────────────────────────────────────
def fig7():
    rows = [("My disciplines", 20.0, BLUE, "1 entry per 4 senior+"), ("Marketing", 17.0, BLUE, "1 per 5"), ("Data", 4.8, GRAY, "1 per 20"),
            ("Product", 4.6, GRAY, "1 per 21"), ("Engineering", 4.1, GRAY, "1 per 23")]
    body, y = hbars(rows, 100, 170, 540, 20, lambda v: f"{v:.0f}%" if v >= 10 else f"{v:.1f}%",
                    note="Entry = intern, junior, associate, assistant, working student, trainee. Roughly 40–60% of postings name no level and are excluded.")
    return frame("Marketing is the most open door of the four — which is not the same as open",
                 "Entry-level share of postings that state a level in the title", body, y + 32)


if __name__ == "__main__":
    for i, f in enumerate([fig1, fig2, fig3, fig4, fig5, fig6, fig7], 1):
        p = OUT / f"fig{i}.svg"
        p.write_text(f())
        print(p.name, len(p.read_text()))
