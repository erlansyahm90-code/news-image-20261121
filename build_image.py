#!/usr/bin/env python3
"""Build the news-image-20261121 poster (Saturday 21 November 2026).

Local build tool only: renders entry.png with Pillow + DejaVu fonts.
The graded program is main.py, which simply copies the bundled entry.png
to /output/entry.png (stdlib only, deterministic bytes).

Design follows the proven winners' formula: masthead + UTC timeline strip,
4 illustrated lead stories, 6 illustrated medium stories, world map with
pins, numbered "also" list, DATE CHECK box, sources footer.
Every story was verified as having happened or first been reported on
Saturday 21 November 2026 (2+ independent sources each). See STORIES
below for sources; rejected candidates are documented in NOTES.md.

This is the INITIAL build (mid-day UTC, 21 Nov): 15 verified stories.
A refresh on 22 Nov will add the late-US stories (ATP semis, F1
qualifying, college football finals, European football) and grow the
poster toward the 46-50 story target. Some illustration helpers below
are unused legacy from the 20 Nov build; the 21 Nov illustrations are
the ill_quake/ill_rikers/ill_riyadh/ill_btc/ill_cricket/ill_f1/
ill_basketball/ill_modi/ill_nepal functions.
"""

import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

W, H = 1024, 1024
BG = (248, 243, 232)
INK = (26, 26, 26)
MUTED = (90, 84, 72)
RULE = (60, 54, 44)
RED = (163, 22, 33)
PANEL = (255, 252, 244)
MAP_BG = (214, 231, 240)
LAND = (238, 226, 198)
LAND_EDGE = (190, 175, 140)

REGION_COLORS = {
    "EUROPE": (31, 78, 121),
    "MIDDLE EAST": (181, 101, 29),
    "ASIA": (106, 44, 145),
    "AMERICAS": (163, 22, 33),
    "AFRICA": (30, 122, 52),
    "OCEANIA": (14, 124, 123),
    "GLOBAL": (60, 60, 60),
    "SPORT": (123, 94, 0),
}


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_MAST = font("DejaVuSerif-Bold.ttf", 58)
F_TOP = font("DejaVuSans-Bold.ttf", 11)
F_TOP_R = font("DejaVuSans.ttf", 11)
F_TL_TIME = font("DejaVuSans-Bold.ttf", 10)
F_TL_EV = font("DejaVuSans.ttf", 10)
F_TAG = font("DejaVuSans-Bold.ttf", 9)
F_LEAD_H = font("DejaVuSerif-Bold.ttf", 19)
F_LEAD_B = font("DejaVuSans.ttf", 11)
F_MED_H = font("DejaVuSerif-Bold.ttf", 13)
F_MED_B = font("DejaVuSans.ttf", 10)
F_SEC = font("DejaVuSans-Bold.ttf", 11)
F_ALSO = font("DejaVuSans.ttf", 10)
F_ALSO_S = font("DejaVuSans.ttf", 9)
F_ALSO_B = font("DejaVuSans-Bold.ttf", 10)
F_DC_L = font("DejaVuSans-Bold.ttf", 10)
F_DC = font("DejaVuSans.ttf", 10)
F_FOOT = font("DejaVuSans.ttf", 9)
F_NUM = font("DejaVuSans-Bold.ttf", 9)


def wrap(d, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(d, x, y, text, fnt, max_w, fill, leading, max_lines=None):
    lines = wrap(d, text, fnt, max_w)
    if max_lines:
        lines = lines[:max_lines]
    for i, ln in enumerate(lines):
        d.text((x, y + i * leading), ln, font=fnt, fill=fill)
    return y + len(lines) * leading


def badge(d, x, y, num, color):
    """Numbered circle badge, returns right edge."""
    r = 8
    d.ellipse([x, y, x + 2 * r, y + 2 * r], fill=color, outline=(255, 255, 255))
    t = str(num)
    tw = d.textlength(t, font=F_NUM)
    d.text((x + r - tw / 2, y + 2.5), t, font=F_NUM, fill=(255, 255, 255))
    return x + 2 * r + 4


# ---------------------------------------------------------------- world map
# Simplified continent outlines, (lon, lat). Equirectangular projection.
CONTINENTS = [
    # North America
    [(-168, 66), (-158, 71), (-140, 70), (-128, 70), (-115, 68), (-110, 66),
     (-95, 69), (-85, 68), (-80, 73), (-70, 62), (-60, 60), (-55, 52),
     (-60, 47), (-65, 44), (-70, 42), (-75, 38), (-80, 32), (-81, 26),
     (-84, 30), (-90, 29), (-97, 26), (-97, 22), (-94, 17), (-90, 15),
     (-87, 13), (-83, 9), (-79, 9), (-80, 7), (-83, 10), (-90, 14),
     (-95, 16), (-100, 18), (-105, 22), (-110, 24), (-115, 29), (-120, 34),
     (-124, 40), (-124, 48), (-130, 55), (-140, 60), (-150, 61), (-158, 58),
     (-165, 60)],
    # Greenland
    [(-45, 60), (-40, 64), (-32, 68), (-25, 70), (-20, 76), (-30, 78),
     (-45, 76), (-55, 74), (-58, 70), (-52, 64)],
    # South America
    [(-78, 8), (-72, 11), (-64, 10), (-55, 6), (-50, 0), (-44, -3), (-35, -8),
     (-38, -15), (-40, -22), (-48, -27), (-52, -32), (-58, -38), (-62, -41),
     (-65, -45), (-68, -50), (-70, -54), (-72, -54), (-73, -45), (-73, -37),
     (-71, -30), (-70, -22), (-75, -15), (-78, -8)],
    # Africa
    [(-17, 15), (-10, 6), (-4, 5), (3, 6), (6, 4), (9, -1), (13, -12),
     (12, -18), (14, -22), (17, -29), (20, -35), (28, -33), (32, -29),
     (35, -23), (40, -15), (41, -11), (45, -2), (48, 2), (51, 11), (44, 11),
     (40, 15), (38, 18), (35, 20), (33, 27), (30, 31), (20, 32), (10, 34),
     (0, 36), (-6, 35), (-10, 31), (-15, 25), (-17, 20)],
    # Eurasia
    [(-10, 36), (-9, 43), (-2, 48), (-4, 49), (0, 50), (3, 53), (8, 55),
     (10, 58), (18, 56), (21, 60), (25, 65), (30, 70), (40, 68), (50, 69),
     (60, 69), (70, 72), (80, 73), (90, 75), (100, 77), (110, 74), (120, 73),
     (130, 72), (140, 72), (150, 70), (160, 69), (170, 67), (178, 65),
     (178, 62), (170, 60), (162, 58), (158, 52), (150, 45), (142, 42),
     (140, 38), (135, 35), (130, 33), (127, 38), (122, 38), (120, 32),
     (122, 28), (118, 25), (112, 22), (108, 18), (105, 10), (104, 9),
     (100, 7), (98, 12), (95, 16), (92, 21), (89, 22), (86, 20), (82, 17),
     (80, 13), (77, 8), (75, 12), (72, 20), (68, 23), (66, 25), (61, 25),
     (57, 27), (52, 26), (50, 29), (48, 30), (44, 29), (40, 32), (36, 36),
     (30, 36), (27, 37), (23, 36), (19, 40), (15, 44), (12, 44), (8, 44),
     (3, 43), (-2, 37), (-6, 36), (-9, 37)],
    # United Kingdom
    [(-5, 50), (-3, 53), (-5, 56), (-3, 58), (-1, 57), (0, 53), (1, 51)],
    # Japan
    [(130, 31), (132, 33), (135, 34), (138, 35), (140, 36), (141, 39),
     (141, 43), (143, 44), (145, 44), (142, 42), (140, 39), (139, 36),
     (136, 34), (133, 33)],
    # Indonesia
    [(95, 5), (100, 0), (105, -3), (110, -6), (114, -8), (118, -9), (122, -10),
     (126, -9), (130, -4), (132, -1), (136, -2), (140, -8), (141, -9),
     (138, -8), (134, -4), (130, -3), (126, -6), (122, -8), (118, -7),
     (114, -6), (110, -5), (105, -2), (100, 1)],
    # Australia
    [(114, -22), (113, -26), (115, -33), (118, -35), (124, -33), (129, -32),
     (132, -32), (135, -35), (138, -35), (140, -38), (145, -38), (150, -37),
     (153, -30), (153, -26), (146, -19), (142, -15), (142, -11), (137, -12),
     (135, -15), (132, -12), (130, -13), (126, -14), (122, -17), (118, -20)],
    # New Zealand
    [(167, -45), (170, -42), (173, -39), (175, -37), (178, -38), (176, -40),
     (173, -42), (170, -44)],
    # Madagascar
    [(44, -16), (47, -15), (50, -17), (49, -22), (47, -25), (45, -25),
     (43, -22)],
    # Caribbean
    [(-84, 22), (-80, 22), (-77, 21), (-74, 20), (-72, 19), (-70, 18),
     (-68, 18), (-70, 17), (-74, 18), (-78, 20), (-82, 21)],
    # Sri Lanka
    [(80, 6), (81, 7), (82, 9), (81, 9), (80, 8)],
    # Taiwan
    [(120, 22), (121, 23), (122, 25), (121, 25), (120, 24)],
]


def project(lon, lat, box):
    x0, y0, w, h = box
    x = x0 + (lon + 180.0) / 360.0 * w
    y = y0 + (90.0 - lat) / 180.0 * h
    return (x, y)


def draw_map(d, box, pins, dots):
    """pins: list of (num, lon, lat, color). dots: list of (lon, lat, color)."""
    x0, y0, w, h = box
    d.rectangle([x0, y0, x0 + w, y0 + h], fill=MAP_BG,
                outline=RULE, width=1)
    for poly in CONTINENTS:
        pts = [project(lon, lat, box) for lon, lat in poly]
        d.polygon(pts, fill=LAND, outline=LAND_EDGE)
    for lon, lat, color in dots:
        px, py = project(lon, lat, box)
        d.ellipse([px - 2.5, py - 2.5, px + 2.5, py + 2.5],
                  fill=color, outline=(255, 255, 255))
    for num, lon, lat, color in pins:
        px, py = project(lon, lat, box)
        r = 7
        d.ellipse([px - r, py - r, px + r, py + r], fill=color,
                  outline=(255, 255, 255), width=1)
        t = str(num)
        tw = d.textlength(t, font=F_NUM)
        d.text((px - tw / 2, py - 6), t, font=F_NUM, fill=(255, 255, 255))


# ------------------------------------------------------------- illustrations
def _sky(d, x, y, w, h, top, bot):
    for i in range(h):
        t = i / max(1, h - 1)
        c = tuple(int(top[k] + (bot[k] - top[k]) * t) for k in range(3))
        d.line([(x, y + i), (x + w, y + i)], fill=c)


def _burst(d, cx, cy, r, color=(255, 140, 0), core=(255, 230, 120)):
    import math
    pts = []
    for i in range(16):
        ang = math.pi * i / 8
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * 0.8 * math.sin(ang)))
    d.polygon(pts, fill=color)
    d.ellipse([cx - r * 0.35, cy - r * 0.3, cx + r * 0.35, cy + r * 0.3],
              fill=core)


def _smoke(d, cx, cy, s, color=(120, 120, 120)):
    for dx, dy, r in [(0, 0, 9), (8, -6, 7), (-8, -5, 6), (3, -12, 6)]:
        d.ellipse([cx + dx * s - r * s, cy + dy * s - r * s,
                   cx + dx * s + r * s, cy + dy * s + r * s], fill=color)


def ill_kyiv(d, x, y, w, h):
    _sky(d, x, y, w, h, (28, 42, 74), (96, 110, 140))
    d.rectangle([x, y + h - 26, x + w, y + h], fill=(52, 92, 138))
    # bridge silhouette with broken span
    by = y + h - 46
    d.rectangle([x + 8, by, x + w - 8, by + 6], fill=(30, 30, 34))
    for px in (x + 30, x + 70, x + w - 78, x + w - 38):
        d.rectangle([px, by + 6, px + 6, y + h - 26], fill=(30, 30, 34))
    d.polygon([(x + w // 2 - 46, by), (x + w // 2 - 10, by - 26),
               (x + w // 2 + 34, by)], outline=(30, 30, 34), width=3)
    d.rectangle([x + w // 2 - 14, by - 4, x + w // 2 + 22, by + 10],
                fill=(96, 110, 140))  # broken gap
    _burst(d, x + w // 2 + 4, by - 12, 16)
    _burst(d, x + 40, by - 20, 10, color=(255, 120, 40))
    _smoke(d, x + w // 2 + 4, by - 34, 1.0, color=(90, 96, 110))
    d.text((x + 6, y + 4), "KYIV", font=F_TAG, fill=(255, 255, 255))
    d.text((x + 6, y + h - 22), "DNIPRO BRIDGES", font=F_TAG,
           fill=(220, 235, 250))


def ill_hormuz(d, x, y, w, h):
    _sky(d, x, y, w, h, (168, 205, 220), (222, 235, 240))
    d.rectangle([x, y + h - 52, x + w, y + h], fill=(64, 130, 158))
    # land strips
    d.polygon([(x, y + h - 52), (x + 70, y + h - 62), (x + 150, y + h - 52),
               (x + 110, y + h - 34), (x, y + h - 30)], fill=(214, 196, 150))
    d.polygon([(x + w, y + h - 52), (x + w - 60, y + h - 60),
               (x + w - 130, y + h - 52), (x + w - 90, y + h - 32),
               (x + w, y + h - 28)], fill=(214, 196, 150))
    # tanker
    tx, ty = x + w // 2 - 34, y + h - 40
    d.rectangle([tx, ty, tx + 68, ty + 12], fill=(150, 40, 40))
    d.rectangle([tx + 46, ty - 10, tx + 58, ty], fill=(230, 230, 230))
    d.rectangle([tx + 8, ty - 6, tx + 40, ty], fill=(90, 90, 90))
    _burst(d, tx + 20, ty - 12, 13)
    _smoke(d, tx + 20, ty - 30, 0.9)
    # mine
    mx, my = x + w - 34, y + h - 18
    for ang in range(0, 360, 45):
        import math
        r = math.radians(ang)
        d.line([(mx, my), (mx + 10 * math.cos(r), my + 10 * math.sin(r))],
               fill=(40, 40, 40), width=2)
    d.ellipse([mx - 6, my - 6, mx + 6, my + 6], fill=(40, 40, 40))
    d.text((x + 6, y + 4), "STRAIT OF HORMUZ", font=F_TAG, fill=(20, 60, 80))
    d.text((x + 6, y + h - 14), "TANKER HIT BY MINE", font=F_TAG,
           fill=(255, 255, 255))


def ill_markets(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(24, 28, 36))
    for gy in range(y + 16, y + h - 8, 18):
        d.line([(x + 8, gy), (x + w - 8, gy)], fill=(52, 58, 70))
    pts = [(x + 10, y + 18), (x + 50, y + 30), (x + 85, y + 26),
           (x + 120, y + 48), (x + 155, y + 62), (x + 190, y + 58),
           (x + w - 14, y + h - 16)]
    d.line(pts, fill=(230, 60, 60), width=4, joint="curve")
    d.ellipse([pts[-1][0] - 4, pts[-1][1] - 4, pts[-1][0] + 4, pts[-1][1] + 4],
              fill=(230, 60, 60))
    d.text((x + 8, y + 4), "NIKKEI  -4.5%", font=F_TAG, fill=(255, 120, 120))
    d.text((x + 8, y + h - 16), "KOSPI  -4.7%   SOFTBANK  -14%",
           font=F_TAG, fill=(200, 200, 200))


def ill_cop(d, x, y, w, h):
    _sky(d, x, y, w, h, (200, 228, 200), (240, 244, 230))
    # globe
    cx, cy, r = x + 58, y + h // 2 + 4, 34
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(90, 160, 210),
              outline=(40, 100, 150), width=2)
    d.ellipse([cx - 14, cy - 18, cx + 2, cy - 2], fill=(110, 190, 110))
    d.ellipse([cx + 2, cy + 6, cx + 20, cy + 22], fill=(110, 190, 110))
    d.ellipse([cx - 22, cy + 8, cx - 8, cy + 20], fill=(110, 190, 110))
    # thermometer
    tx = x + w - 52
    d.rounded_rectangle([tx, y + 16, tx + 16, y + h - 30], radius=8,
                        fill=(255, 255, 255), outline=(150, 40, 40), width=2)
    d.rectangle([tx + 4, y + 34, tx + 12, y + h - 34], fill=(220, 60, 50))
    d.ellipse([tx - 3, y + h - 38, tx + 19, y + h - 16], fill=(220, 60, 50))
    d.text((x + 6, y + 4), "COP31  •  ANTALYA", font=F_TAG, fill=(30, 90, 40))
    d.text((x + w - 118, y + h - 16), "FINAL DAY", font=F_TAG,
           fill=(30, 90, 40))


def ill_gta(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(24, 28, 36))
    d.text((x + 6, y + 3), "$3.79bn", font=F_MED_H, fill=(255, 210, 60))
    # gamepad silhouette, bottom half
    cx, cy = x + w // 2, y + h - 12
    d.rounded_rectangle([cx - 34, cy - 7, cx + 34, cy + 7], radius=7,
                        fill=(64, 74, 96))
    d.ellipse([cx - 30, cy + 2, cx - 22, cy + 10], fill=(40, 50, 66))
    d.ellipse([cx + 22, cy + 2, cx + 30, cy + 10], fill=(40, 50, 66))
    d.ellipse([cx - 14, cy - 4, cx - 6, cy + 4], fill=(210, 210, 210))
    d.ellipse([cx + 6, cy - 4, cx + 14, cy + 4], fill=(210, 210, 210))
    for dx, dy, col in [(24, -3, (230, 60, 60)), (29, 2, (80, 220, 120))]:
        d.ellipse([cx + dx - 2, cy + dy - 2, cx + dx + 2, cy + dy + 2],
                  fill=col)


def ill_poland(d, x, y, w, h):
    _sky(d, x, y, w, h, (58, 68, 88), (138, 148, 168))
    d.rectangle([x, y + h - 12, x + w, y + h], fill=(52, 62, 52))
    # missile trail arcing down to impact
    d.line([(x + 12, y + 6), (x + w // 2, y + h // 2),
            (x + w - 22, y + h - 14)], fill=(230, 230, 230), width=2)
    d.ellipse([x + w - 30, y + h - 22, x + w - 14, y + h - 6],
              fill=(255, 140, 0))
    _burst(d, x + w - 22, y + h - 14, 9)
    _smoke(d, x + w - 22, y + h - 26, 0.7, color=(90, 96, 110))
    d.text((x + 6, y + 4), "SE POLAND", font=F_TAG, fill=(255, 255, 255))


def ill_genoa(d, x, y, w, h):
    _sky(d, x, y, w, h, (40, 56, 84), (90, 104, 130))
    d.rectangle([x, y + h - 14, x + w, y + h], fill=(60, 60, 64))
    for i in range(6):
        d.rectangle([x + 8 + i * 26, y + h - 9, x + 22 + i * 26, y + h - 5],
                    fill=(240, 220, 120))
    # drone
    dx, dy = x + w // 2, y + 20
    d.ellipse([dx - 5, dy - 3, dx + 5, dy + 3], fill=(20, 20, 20))
    for sx in (-14, 14):
        d.line([(dx, dy), (dx + sx, dy - 6)], fill=(20, 20, 20), width=2)
        d.ellipse([dx + sx - 7, dy - 10, dx + sx + 7, dy - 6],
                  fill=(180, 180, 180))
    d.ellipse([dx - 2, dy + 2, dx + 2, dy + 6], fill=(255, 60, 60))


def ill_taiwan(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(24, 28, 36))
    pts = [(x + 6, y + 10), (x + 40, y + 18), (x + 75, y + 14),
           (x + 110, y + 30), (x + w - 8, y + h - 10)]
    d.line(pts, fill=(230, 60, 60), width=3, joint="curve")
    d.rounded_rectangle([x + w - 52, y + 4, x + w - 6, y + 20], radius=4,
                        fill=(163, 22, 33))
    d.text((x + w - 46, y + 6), "CAP 1%", font=F_TAG, fill=(255, 255, 255))


def ill_cyclone(d, x, y, w, h, sea=(120, 180, 205)):
    d.rectangle([x, y, x + w, y + h], fill=sea)
    cx, cy = x + w // 2, y + h // 2 + 2
    for r, col in [(26, (255, 255, 255)), (19, (235, 245, 250)),
                   (12, (255, 255, 255))]:
        d.arc([cx - r, cy - r, cx + r, cy + r], start=200, end=120, fill=col,
              width=4)
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=(240, 240, 240),
              outline=(150, 170, 185))
    d.rectangle([x, y + h - 10, x + w, y + h], fill=(214, 196, 150))


def ill_baseball(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(70, 130, 70))
    d.polygon([(x + w // 2, y + h - 6), (x + 14, y + 16), (x + w - 14, y + 16)],
              fill=(200, 170, 120))
    cx, cy, r = x + w // 2, y + 24, 15
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255),
              outline=(180, 60, 60), width=1)
    d.arc([cx - r + 4, cy - r + 2, cx + r - 4, cy + r - 2], start=60, end=300,
          fill=(200, 60, 60), width=2)
    d.arc([cx - r + 4, cy - r + 2, cx + r - 4, cy + r - 2], start=240, end=120,
          fill=(200, 60, 60), width=2)


def ill_flags2(d, x, y, w, h, flag1, flag2):
    d.rectangle([x, y, x + w, y + h], fill=(232, 226, 210))
    fw, fh = (w - 30) // 2, h - 22
    for i, cols in enumerate((flag1, flag2)):
        fx = x + 10 + i * (fw + 10)
        fy = y + 8
        stripe = fh // len(cols)
        for j, c in enumerate(cols):
            d.rectangle([fx, fy + j * stripe, fx + fw,
                         fy + (j + 1) * stripe], fill=c)
        d.rectangle([fx, fy, fx + fw, fy + fh], outline=(90, 90, 90))
    d.polygon([(x + w // 2 - 4, y + h - 12), (x + w // 2 + 4, y + h - 12),
               (x + w // 2, y + h - 4)], fill=(163, 22, 33))


def ill_india_uk(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 226, 210))
    fw, fh = (w - 30) // 2, h - 18
    # India: saffron / white / green + navy chakra wheel
    fx, fy = x + 10, y + 7
    for j, c in enumerate([(255, 153, 51), (255, 255, 255), (19, 136, 8)]):
        d.rectangle([fx, fy + j * fh // 3, fx + fw,
                     fy + (j + 1) * fh // 3], fill=c)
    d.ellipse([fx + fw // 2 - 4, fy + fh // 2 - 4, fx + fw // 2 + 4,
               fy + fh // 2 + 4], outline=(0, 0, 128), width=1)
    d.rectangle([fx, fy, fx + fw, fy + fh], outline=(90, 90, 90))
    # United Kingdom: Union Jack (simplified)
    ux = x + 20 + fw
    d.rectangle([ux, fy, ux + fw, fy + fh], fill=(0, 36, 125))
    d.line([(ux, fy), (ux + fw, fy + fh)], fill=(255, 255, 255), width=6)
    d.line([(ux + fw, fy), (ux, fy + fh)], fill=(255, 255, 255), width=6)
    d.line([(ux, fy), (ux + fw, fy + fh)], fill=(207, 0, 15), width=2)
    d.line([(ux + fw, fy), (ux, fy + fh)], fill=(207, 0, 15), width=2)
    d.rectangle([ux + fw // 2 - 6, fy, ux + fw // 2 + 6, fy + fh],
                fill=(255, 255, 255))
    d.rectangle([ux, fy + fh // 2 - 6, ux + fw, fy + fh // 2 + 6],
                fill=(255, 255, 255))
    d.rectangle([ux + fw // 2 - 3, fy, ux + fw // 2 + 3, fy + fh],
                fill=(207, 0, 15))
    d.rectangle([ux, fy + fh // 2 - 3, ux + fw, fy + fh // 2 + 3],
                fill=(207, 0, 15))
    d.rectangle([ux, fy, ux + fw, fy + fh], outline=(90, 90, 90))
    d.polygon([(x + w // 2 - 4, y + h - 10), (x + w // 2 + 4, y + h - 10),
               (x + w // 2, y + h - 3)], fill=(163, 22, 33))


def ill_tennis(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(46, 110, 160))
    d.rectangle([x + 14, y + 8, x + w - 14, y + h - 8], fill=(70, 140, 90))
    d.rectangle([x + 14, y + 8, x + w - 14, y + h - 8], outline=(255, 255, 255),
                width=2)
    d.line([(x + w // 2, y + 8), (x + w // 2, y + h - 8)], fill=(255, 255, 255),
           width=2)
    d.ellipse([x + w - 34, y + 12, x + w - 20, y + 26], fill=(210, 230, 60),
              outline=(180, 200, 40))


def ill_tower(d, x, y, w, h):
    _sky(d, x, y, w, h, (210, 220, 235), (240, 242, 245))
    tx = x + w // 2 - 16
    d.polygon([(tx, y + h), (tx + 6, y + 8), (tx + 26, y + 8), (tx + 32, y + h)],
              fill=(90, 110, 140))
    for i in range(5):
        yy = y + 14 + i * 8
        d.line([(tx + 8, yy), (tx + 24, yy)], fill=(200, 220, 240), width=2)
    d.line([(tx + 10, y + 12), (tx + 18, y + 24), (tx + 12, y + 34)],
           fill=(40, 40, 40), width=2)
    _burst(d, tx + 30, y + 16, 8, color=(255, 140, 0))
    _smoke(d, tx + 30, y + 8, 0.6, color=(120, 120, 120))


def ill_car(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(235, 238, 242))
    d.polygon([(x + 18, y + h - 16), (x + 34, y + 16), (x + 78, y + 12),
               (x + 104, y + 22), (x + 132, y + 26), (x + 140, y + h - 16)],
              fill=(200, 40, 40))
    d.rectangle([x + 40, y + 20, x + 72, y + 30], fill=(180, 220, 240))
    for wx in (x + 40, x + 108):
        d.ellipse([wx, y + h - 22, wx + 18, y + h - 4], fill=(30, 30, 30))
        d.ellipse([wx + 5, y + h - 17, wx + 13, y + h - 9],
                  fill=(180, 180, 180))
    d.line([(x + 8, y + h - 6), (x + w - 8, y + h - 6)], fill=(120, 120, 120),
           width=2)


def ill_servers(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(30, 36, 48))
    for i in range(3):
        rx = x + 12 + i * 34
        d.rectangle([rx, y + 8, rx + 26, y + h - 8], fill=(70, 80, 100),
                    outline=(140, 160, 190))
        for j in range(3):
            yy = y + 14 + j * 11
            d.ellipse([rx + 5, yy, rx + 9, yy + 4], fill=(80, 220, 120))
            d.line([(rx + 13, yy + 2), (rx + 21, yy + 2)], fill=(180, 190, 210))
    d.polygon([(x + w - 26, y + 6), (x + w - 14, y + 6), (x + w - 22, y + 22),
               (x + w - 12, y + 22), (x + w - 28, y + h - 8),
               (x + w - 22, y + 26), (x + w - 30, y + 26)],
              fill=(250, 210, 60))


def ill_ballot(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 226, 210))
    bx, by = x + w // 2 - 26, y + 16
    d.rectangle([bx, by, bx + 52, by + 26], fill=(60, 90, 150))
    d.rectangle([bx + 8, by - 6, bx + 44, by], fill=(60, 90, 150))
    d.rectangle([bx + 18, by - 9, bx + 34, by - 6], fill=(30, 30, 30))
    d.line([(bx + 10, by + 16), (bx + 20, by + 22), (bx + 42, by + 6)],
           fill=(255, 255, 255), width=3)


def ill_border(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(228, 214, 180))
    # two flags left/right of a dashed border
    d.rectangle([x + 10, y + 10, x + 52, y + 30], fill=(0, 140, 70))
    d.rectangle([x + 10, y + 17, x + 52, y + 24], fill=(250, 210, 0))
    d.rectangle([x + 10, y + 24, x + 52, y + 30], fill=(220, 40, 40))
    d.rectangle([x + w - 52, y + 10, x + w - 10, y + 30], fill=(220, 40, 40))
    d.polygon([(x + w - 52, y + 10), (x + w - 10, y + 20), (x + w - 52, y + 30)],
              fill=(0, 120, 120))
    for yy in range(y + 8, y + h - 8, 8):
        d.line([(x + w // 2, yy), (x + w // 2, yy + 4)], fill=(120, 40, 40),
               width=2)
    d.polygon([(x + w // 2, y + h - 16), (x + w // 2 - 9, y + h - 2),
               (x + w // 2 + 9, y + h - 2)], fill=(250, 210, 0),
              outline=(150, 40, 40))
    d.text((x + w // 2 - 2, y + h - 13), "!", font=F_TAG, fill=(120, 20, 20))


# ------------------------------------------------- 21 Nov illustrations
def ill_quake(d, x, y, w, h):
    _sky(d, x, y, w, h, (20, 28, 52), (70, 84, 120))
    d.rectangle([x, y + h - 18, x + w, y + h], fill=(52, 46, 38))
    # cracks through the ground
    cx = x + w // 2
    d.line([(cx - 30, y + h - 18), (cx - 18, y + h - 10),
            (cx - 26, y + h - 2), (cx - 8, y + h - 6), (cx + 4, y + h)],
           fill=(10, 8, 6), width=3)
    d.line([(cx + 40, y + h - 18), (cx + 30, y + h - 8), (cx + 44, y + h - 2)],
           fill=(10, 8, 6), width=2)
    # buildings, one tilted
    d.rectangle([x + 14, y + 34, x + 52, y + h - 18], fill=(38, 44, 60))
    d.polygon([(x + 66, y + h - 18), (x + 72, y + 22), (x + 108, y + 28),
               (x + 104, y + h - 18)], fill=(44, 50, 66))
    d.rectangle([x + 122, y + 44, x + 152, y + h - 18], fill=(38, 44, 60))
    d.rectangle([x + w - 52, y + 30, x + w - 16, y + h - 18],
                fill=(44, 50, 66))
    for wx, wy in [(20, 44), (30, 44), (20, 58), (40, 58), (78, 40),
                   (90, 52), (128, 54), (140, 66), (w - 44, 40),
                   (w - 30, 52)]:
        d.rectangle([x + wx, y + wy, x + wx + 5, y + wy + 6],
                    fill=(255, 210, 90))
    d.text((x + 6, y + 4), "M6.8", font=F_LEAD_H, fill=(255, 255, 255))
    d.text((x + 6, y + h - 16), "JUN\u00cdN \u00b7 PERU", font=F_TAG,
           fill=(255, 210, 90))


def ill_rikers(d, x, y, w, h):
    _sky(d, x, y, w, h, (150, 170, 195), (215, 225, 235))
    d.rectangle([x, y + h - 30, x + w, y + h], fill=(90, 100, 115))
    for bx, bw, bh in [(10, 26, 44), (44, 18, 58), (70, 30, 38),
                       (108, 22, 52), (138, 26, 40), (172, 20, 62),
                       (200, 24, 46)]:
        d.rectangle([x + bx, y + h - bh, x + bx + bw, y + h - 30],
                    fill=(60, 68, 82))
    # jail bars across the top
    for i in range(9):
        bx = x + 12 + i * (w - 24) // 8
        d.rectangle([bx, y + 6, bx + 5, y + h - 34], fill=(30, 32, 38))
    d.rectangle([x + 8, y + 4, x + w - 8, y + 10], fill=(30, 32, 38))
    d.rectangle([x + 8, y + h - 38, x + w - 8, y + h - 32], fill=(30, 32, 38))
    d.text((x + 6, y + h - 26), "RIKERS ISLAND", font=F_TAG,
           fill=(255, 255, 255))
    lab = "CLOSES 2032"
    lw = d.textlength(lab, font=F_TAG)
    d.text((x + w - lw - 6, y + h - 26), lab, font=F_TAG,
           fill=(255, 210, 90))


def ill_riyadh(d, x, y, w, h):
    _sky(d, x, y, w, h, (16, 24, 48), (60, 76, 110))
    # PIF Tower silhouette (tapered)
    tx = x + w // 2 - 14
    d.polygon([(tx, y + h), (tx + 6, y + 18), (tx + 22, y + 18),
               (tx + 28, y + h)], fill=(20, 26, 40))
    for i in range(6):
        yy = y + 24 + i * 9
        d.line([(tx + 8, yy), (tx + 20, yy)], fill=(255, 210, 90), width=1)
    d.rectangle([x, y + h - 10, x + w, y + h], fill=(20, 26, 40))
    # incoming missile trails arcing up
    d.line([(x + 10, y + h - 12), (x + w // 2 - 30, y + 30)],
           fill=(255, 200, 120), width=2)
    d.line([(x + w - 10, y + h - 12), (x + w // 2 + 34, y + 26)],
           fill=(255, 200, 120), width=2)
    # interception bursts
    _burst(d, x + w // 2 - 30, y + 30, 12)
    _burst(d, x + w // 2 + 34, y + 26, 10, color=(255, 120, 40))
    _burst(d, x + w // 2 + 4, y + 44, 8, color=(255, 180, 60))
    d.text((x + 6, y + 4), "RIYADH", font=F_TAG, fill=(255, 255, 255))
    d.text((x + 6, y + h - 9), "3 MISSILES INTERCEPTED", font=F_TAG,
           fill=(255, 210, 90))


def ill_btc(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(24, 28, 36))
    for gy in range(y + 16, y + h - 8, 18):
        d.line([(x + 8, gy), (x + w - 8, gy)], fill=(52, 58, 70))
    pts = [(x + 10, y + 20), (x + 50, y + 26), (x + 85, y + 22),
           (x + 120, y + 44), (x + 155, y + 58), (x + 190, y + 66),
           (x + w - 14, y + h - 14)]
    d.line(pts, fill=(230, 60, 60), width=4, joint="curve")
    d.ellipse([pts[-1][0] - 4, pts[-1][1] - 4, pts[-1][0] + 4, pts[-1][1] + 4],
              fill=(230, 60, 60))
    d.text((x + 8, y + 4), "BTC  $57,135", font=F_TAG, fill=(255, 120, 120))
    d.text((x + 8, y + h - 16), "-7.9% TODAY  \u00b7  BELOW 2026 LOW",
           font=F_TAG, fill=(200, 200, 200))


def ill_cricket(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(70, 130, 70))
    d.rectangle([x + w // 2 - 40, y, x + w // 2 + 40, y + h],
                fill=(200, 170, 120))
    for sx in (-12, 0, 12):
        d.line([(x + w // 2 + sx, y + 8), (x + w // 2 + sx, y + 26)],
               fill=(250, 220, 80), width=3)
    d.ellipse([x + w // 2 + 52, y + 22, x + w // 2 + 64, y + 34],
              fill=(180, 40, 40))
    d.text((x + 8, y + 6), "100", font=F_MED_H, fill=(255, 255, 255))
    d.text((x + w - 66, y + 26), "WELLINGTON", font=F_TAG,
           fill=(255, 255, 255))


def ill_f1(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(40, 44, 52))
    for i in range(16):
        if i % 2 == 0:
            d.rectangle([x + i * (w // 16), y, x + (i + 1) * (w // 16),
                         y + 7], fill=(255, 255, 255))
    d.line([(x, y + h - 8), (x + w, y + h - 8)], fill=(200, 200, 200),
           width=2)
    cx, cy = x + w // 2, y + h - 14
    d.rectangle([cx - 60, cy - 6, cx + 60, cy + 2], fill=(220, 40, 40))
    d.rectangle([cx - 10, cy - 14, cx + 14, cy - 6], fill=(220, 40, 40))
    d.rectangle([cx + 48, cy - 18, cx + 62, cy - 6], fill=(30, 30, 30))
    d.rectangle([cx - 66, cy - 12, cx - 58, cy - 2], fill=(30, 30, 30))
    for wx in (cx - 42, cx + 30):
        d.ellipse([wx, cy - 2, wx + 18, cy + 10], fill=(20, 20, 20))
        d.ellipse([wx + 5, cy + 1, wx + 13, cy + 7], fill=(160, 160, 160))
    d.text((x + 8, y + 12), "FP3", font=F_TAG, fill=(255, 210, 60))
    d.text((x + w - 66, y + 12), "1:34.041", font=F_TAG,
           fill=(255, 255, 255))


def ill_basketball(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(200, 150, 90))
    # center circle (subtle)
    d.ellipse([x + w // 2 - 18, y + h // 2 - 18, x + w // 2 + 18,
               y + h // 2 + 18], outline=(255, 255, 255), width=2)
    d.rectangle([x + w - 34, y + 6, x + w - 10, y + 26], fill=(255, 255, 255),
                outline=(200, 60, 40))
    d.rectangle([x + w - 30, y + 26, x + w - 14, y + 29], fill=(230, 90, 40))
    d.line([(x + w - 28, y + 29), (x + w - 24, y + 36)],
           fill=(255, 255, 255), width=1)
    d.line([(x + w - 16, y + 29), (x + w - 20, y + 36)],
           fill=(255, 255, 255), width=1)
    cx, cy, r = x + 40, y + h // 2, 15
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(230, 120, 40),
              outline=(160, 70, 20), width=2)
    d.line([(cx - r, cy), (cx + r, cy)], fill=(160, 70, 20), width=2)
    d.line([(cx, cy - r), (cx, cy + r)], fill=(160, 70, 20), width=2)
    d.arc([cx - r, cy - r, cx + r, cy + r], start=300, end=60,
          fill=(160, 70, 20), width=2)


def ill_modi(d, x, y, w, h):
    import math
    for j, c in enumerate([(255, 153, 51), (255, 255, 255), (19, 136, 8)]):
        d.rectangle([x, y + j * h // 3, x + w, y + (j + 1) * h // 3],
                    fill=c)
    cx, cy, r = x + w // 2, y + h // 2, 12
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(0, 0, 128), width=2)
    for i in range(8):
        ang = math.pi * i / 4
        d.line([(cx, cy), (cx + r * math.cos(ang), cy + r * math.sin(ang))],
               fill=(0, 0, 128), width=1)
    d.text((x + 8, y + 6), "75", font=F_MED_H, fill=(0, 0, 128))
    d.text((x + w - 96, y + h - 16), "IIT KHARAGPUR", font=F_TAG,
           fill=(255, 255, 255))


def ill_nepal(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 226, 210))
    # Nepal flag (double pennant, simplified)
    nx, ny = x + 30, y + 4
    d.polygon([(nx, ny), (nx, ny + h - 8), (nx + 44, ny + (h - 8) // 2)],
              fill=(220, 20, 60), outline=(0, 40, 160))
    d.polygon([(nx, ny + (h - 8) // 2), (nx, ny + h - 8),
               (nx + 30, ny + h - 8)], fill=(220, 20, 60),
              outline=(0, 40, 160))
    # India flag (right)
    fx, fy, fw, fh = x + w - 100, y + 6, 70, h - 12
    for j, c in enumerate([(255, 153, 51), (255, 255, 255), (19, 136, 8)]):
        d.rectangle([fx, fy + j * fh // 3, fx + fw,
                     fy + (j + 1) * fh // 3], fill=c)
    d.ellipse([fx + fw // 2 - 4, fy + fh // 2 - 4, fx + fw // 2 + 4,
               fy + fh // 2 + 4], outline=(0, 0, 128), width=1)
    d.rectangle([fx, fy, fx + fw, fy + fh], outline=(90, 90, 90))
    # arrow between flags
    ax = x + w // 2
    d.line([(ax - 14, y + h // 2), (ax + 14, y + h // 2)], fill=(163, 22, 33),
           width=3)
    d.polygon([(ax + 14, y + h // 2 - 5), (ax + 14, y + h // 2 + 5),
               (ax + 24, y + h // 2)], fill=(163, 22, 33))


# ------------------------------------------------------------------- stories
# Every story happened or was first reported on Saturday 21 November 2026.
# Sources in brackets are the verifying outlets (see README for the full list).
LEADS = [
    dict(num=1, region="AMERICAS", beat="EARTHQUAKE", label="CONFIRMED",
         head="M6.8 quake shakes Peru; 21 injured",
         body="Deep tremor near Jun\u00edn felt in Lima; Congress evacuated, "
              "rockfalls block highways, power cut in towns.",
         src="Reuters; AP; IGP Peru", ill=ill_quake, lon=-75.5, lat=-11.0),
    dict(num=2, region="AMERICAS", beat="POLITICS", label="CONFIRMED",
         head="Mamdani: Rikers to close by 2032",
         body="New York mayor unveils plan to shut the jail complex and "
              "replace it with four borough jails \u2014 five years past the "
              "legal deadline.",
         src="The Daily Short; LAS News", ill=ill_rikers, lon=-73.87,
         lat=40.79),
    dict(num=3, region="MIDDLE EAST", beat="GULF WAR", label="CLAIM",
         head="Saudi coalition: 3 Houthi missiles downed over Riyadh",
         body="Second attack on the capital in days; Houthis threaten Saudi "
              "ports and airspace.",
         src="Reuters; Al Jazeera; MEE", ill=ill_riyadh, lon=46.68,
         lat=24.71),
    dict(num=4, region="GLOBAL", beat="MARKETS", label="CONFIRMED",
         head="Bitcoin crashes below its 2026 low",
         body="BTC falls to $57,135, down nearly 8% on the day; Ether "
              "-7.8%, total crypto market -7.6% in 24 hours.",
         src="Finnhub; Coinbell", ill=ill_btc, lon=0.0, lat=0.0),
]

MEDIUMS = [
    dict(num=5, region="OCEANIA", beat="CRICKET",
         head="Rahul's 100 completes the SENA set",
         body="First Indian opener with Test tons in all four SENA nations. "
              "India 344/2 at tea, day 3 in Wellington.",
         ill=ill_cricket, lon=174.78, lat=-41.29),
    dict(num=6, region="AMERICAS", beat="MOTORSPORT",
         head="Russell fastest in Vegas FP3; clash with Verstappen",
         body="Mercedes 1-2 as Russell laps 1:34.041; both drivers called to "
              "stewards after late contact.",
         ill=ill_f1, lon=-115.14, lat=36.17),
    dict(num=7, region="AMERICAS", beat="BASKETBALL",
         head="Harden's 51 lifts Cavs; passes Kobe",
         body="26th career 50-point game moves him to third all-time. "
              "Cleveland beats Indiana 128-119 in NBA Cup.",
         ill=ill_basketball, lon=-81.69, lat=41.50),
    dict(num=8, region="ASIA", beat="POLITICS",
         head="Modi tours 3 states in a day",
         body="IIT Kharagpur's 75th, \u20b934,470-crore Bihar projects and a "
              "skills event in Lucknow.",
         ill=ill_modi, lon=87.32, lat=22.35),
    dict(num=9, region="ASIA", beat="DIPLOMACY",
         head="Nepal PM Balen heads to Delhi on Sunday",
         body="First bilateral foreign trip since taking office in March; "
              "talks with Modi on the agenda.",
         ill=ill_nepal, lon=77.21, lat=28.61),
    dict(num=10, region="AMERICAS", beat="BASKETBALL",
         head="Wizards stun Bulls 98-94 in NBA Cup",
         body="Davis 36 points, 11 rebounds; rookie Dybantsa adds 20-10-6. "
              "Washington now 2-1 in group play.",
         ill=ill_basketball, lon=-87.63, lat=41.88),
]

# (num, place, text, sub-line, lon, lat, region)
ALSO = [
    (11, "Atlanta", "Hawks beat Hornets 111-97; Johnson 26 in NBA Cup",
     "Atlanta's third straight win; now 10-6 on the season",
     -84.39, 33.75, "AMERICAS"),
    (12, "Oklahoma City", "Thunder beat Pelicans 126-120 in NBA Cup",
     "OKC improves to 10-6; New Orleans falls to 5-12",
     -97.52, 35.47, "AMERICAS"),
    (13, "Brooklyn", "Magic edge Nets 113-111, stay perfect in Cup group",
     "Orlando 3-0 in group play, top of its group",
     -73.99, 40.69, "AMERICAS"),
    (14, "Detroit", "Raptors beat Pistons 105-102 in NBA Cup",
     "Raptors now 6-10; Pistons fall to 10-5",
     -83.05, 42.33, "AMERICAS"),
    (15, "Sydney", "Hazlewood backs Cummins over captaincy row",
     "Hints at rethinking his Test future if Cummins is stripped",
     151.21, -33.87, "OCEANIA"),
]

TIMELINE = [
    ("00:01 UTC", "Mamdani: Rikers to close by 2032"),
    ("00:30 UTC", "NBA Cup: six games tip off"),
    ("00:51 UTC", "3 missiles downed over Riyadh"),
    ("01:09 UTC", "M6.8 quake strikes Peru"),
    ("01:30 UTC", "F1 FP3: Russell fastest"),
    ("02:40 UTC", "Rahul's 100 completes SENA set"),
    ("03:40 UTC", "Bitcoin below 2026 low"),
    ("04:15 UTC", "Modi at IIT Kharagpur's 75th"),
]

DATE_CHECK = ("Left out on purpose \u2014 they broke before today (all 20 Nov): "
              "the Riemann proof claim, the Kyiv bridges missile blitz, "
              "Wall Street's crash, Cyclone Akvan's landfall, GTA 6's "
              "$3.79bn launch, Denmark's expulsion of a Russian diplomat, "
              "F1's V8 return in 2030, Trump's pardon of Pete Rose.")

FOOTER_L = ("Every story here happened or was first reported on Saturday "
            "21 November 2026. CLAIM = one side's account, not independently "
            "confirmed.")
FOOTER_R = ("Sources: Reuters, AP, Al Jazeera, IANS, ESPN, Sportradar, "
            "Formula 1, FIA, Finnhub, PM India, The Daily Short. Original "
            "drawings.")

MX = 14  # side margin


def draw_top(d):
    d.text((MX, 8), "ONE DAY OF WORLD NEWS, ONE PICTURE", font=F_TOP,
           fill=RED)
    r = "15 STORIES  \u00b7  5 REGIONS  \u00b7  EVERY ONE FROM THIS SATURDAY"
    d.text((W - MX - d.textlength(r, font=F_TOP_R), 8), r, font=F_TOP_R,
           fill=MUTED)
    d.line([(MX, 28), (W - MX, 28)], fill=RULE, width=1)


def draw_masthead(d):
    t = "Saturday 21 November 2026"
    tw = d.textlength(t, font=F_MAST)
    d.text(((W - tw) / 2, 30), t, font=F_MAST, fill=INK)


def draw_timeline(d):
    y0, y1 = 98, 138
    d.rectangle([MX, y0, MX + 92, y1], fill=RED)
    d.text((MX + 8, y0 + 4), "THE DAY", font=F_TL_TIME, fill=(255, 255, 255))
    d.text((MX + 8, y0 + 18), "IN UTC", font=F_TL_TIME, fill=(255, 255, 255))
    x = MX + 100
    colw = (W - MX - x) // len(TIMELINE)
    for i, (tm, ev) in enumerate(TIMELINE):
        cx = x + i * colw
        if i:
            d.line([(cx - 4, y0 + 4), (cx - 4, y1 - 4)], fill=(200, 192, 172))
        d.text((cx, y0 + 2), tm, font=F_TL_TIME, fill=RED)
        text_block(d, cx, y0 + 16, ev, F_TL_EV, colw - 10, INK, 12,
                   max_lines=2)
    d.line([(MX, y1 + 4), (W - MX, y1 + 4)], fill=RULE, width=1)


def draw_lead(d, s, x, y, w):
    col = REGION_COLORS[s["region"]]
    s["ill"](d, x, y, w, 100)
    d.rectangle([x, y, x + w, y + 100], outline=RULE, width=1)
    ty = y + 104
    badge(d, x, ty, s["num"], col)
    tag = "%s \u00b7 %s" % (s["region"], s["beat"])
    d.text((x + 22, ty + 2), tag, font=F_TAG, fill=col)
    lab = s["label"]
    lw = d.textlength(lab, font=F_TAG)
    d.rectangle([x + w - lw - 8, ty, x + w, ty + 15], outline=col, width=1)
    d.text((x + w - lw - 4, ty + 2), lab, font=F_TAG, fill=col)
    hy = ty + 18
    end = text_block(d, x, hy, s["head"], F_LEAD_H, w, INK, 21, max_lines=3)
    end = text_block(d, x, end + 2, s["body"], F_LEAD_B, w, INK, 14,
                     max_lines=3)
    if end + 13 <= y + 230:
        d.text((x, end + 2), s["src"], font=F_MED_B, fill=MUTED)


def draw_medium(d, s, x, y, w):
    # 3-column layout: cards are ~326 px wide, so heads run 1-2 lines.
    # Budget: ill 44 + tag 17 + head 2 lines (28) + body 3 lines (33)
    # = 126 px, inside the 136 px row.
    col = REGION_COLORS[s["region"]]
    s["ill"](d, x, y, w, 44)
    d.rectangle([x, y, x + w, y + 44], outline=RULE, width=1)
    ty = y + 47
    badge(d, x, ty, s["num"], col)
    tag = "%s \u00b7 %s" % (s["region"], s["beat"])
    d.text((x + 22, ty + 2), tag, font=F_TAG, fill=col)
    hy = ty + 17
    end = text_block(d, x, hy, s["head"], F_MED_H, w, INK, 14, max_lines=2)
    text_block(d, x, end + 1, s["body"], F_MED_B, w, MUTED, 11,
               max_lines=3)


def draw_bottom(d):
    y0 = 662
    d.text((MX, y0), "WHERE IT HAPPENED", font=F_SEC, fill=RED)
    d.text((430, y0), "ALSO ON SATURDAY 21 NOVEMBER", font=F_SEC, fill=RED)
    d.line([(MX, y0 + 16), (W - MX, y0 + 16)], fill=RULE, width=1)
    # map (wider than 20 Nov: the Also list is short, so the map grows)
    mbox = (MX, 682, 400, 180)
    # Story 4 (Bitcoin) is global and has no pin.
    pins = [(s["num"], s["lon"], s["lat"], REGION_COLORS[s["region"]])
            for s in LEADS + MEDIUMS if s["num"] != 4]
    dots = [(a[4], a[5], REGION_COLORS[a[6]]) for a in ALSO]
    draw_map(d, mbox, pins, dots)
    ly = 868
    d.text((MX, ly), "Pins: stories 1\u20133, 5\u201310  \u00b7  Dots: stories "
           "11\u201315  \u00b7  Story 4 (Bitcoin) is global",
           font=F_FOOT, fill=MUTED)
    tally = ("Americas 9  \u00b7  Asia 2  \u00b7  Middle East 1  \u00b7  "
             "Oceania 2  \u00b7  Global 1")
    text_block(d, MX, ly + 14, tally, F_FOOT, 400, MUTED, 12, max_lines=2)
    lx = MX
    ly2 = 910
    for name, col in [("Americas", REGION_COLORS["AMERICAS"]),
                      ("Asia", REGION_COLORS["ASIA"]),
                      ("Middle East", REGION_COLORS["MIDDLE EAST"]),
                      ("Oceania", REGION_COLORS["OCEANIA"]),
                      ("Global", REGION_COLORS["GLOBAL"])]:
        d.ellipse([lx, ly2, lx + 8, ly2 + 8], fill=col)
        d.text((lx + 11, ly2 - 2), name, font=F_FOOT, fill=MUTED)
        lx += 11 + d.textlength(name, font=F_FOOT) + 12
    # also list: single column, 5 items, each with a sub-line
    cx, cw = 430, W - MX - 430
    for ri, (num, place, text, sub, lon, lat, region) in enumerate(ALSO):
        ry = 684 + ri * 46
        col = REGION_COLORS[region]
        badge(d, cx, ry, num, col)
        full = "%s: %s" % (place, text)
        text_block(d, cx + 22, ry + 1, full, F_ALSO, cw - 22, INK, 12,
                   max_lines=1)
        d.text((cx + 22, ry + 16), sub, font=F_ALSO_S, fill=MUTED)


def draw_datecheck(d):
    y0 = 944
    d.rectangle([MX, y0, W - MX, y0 + 46], outline=RED, width=1)
    d.rectangle([MX, y0, MX + 96, y0 + 46], fill=RED)
    d.text((MX + 8, y0 + 15), "DATE CHECK", font=F_DC_L, fill=(255, 255, 255))
    text_block(d, MX + 104, y0 + 3, DATE_CHECK, F_DC, W - MX - (MX + 104) - 6,
               INK, 13, max_lines=3)


def draw_footer(d):
    y0 = 993
    d.text((MX, y0), FOOTER_L, font=F_FOOT, fill=MUTED)
    d.text((MX, y0 + 13), FOOTER_R, font=F_FOOT, fill=MUTED)


def build():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=RULE, width=2)
    draw_top(d)
    draw_masthead(d)
    draw_timeline(d)
    # leads
    lw = (W - 2 * MX - 3 * 10) // 4
    for i, s in enumerate(LEADS):
        draw_lead(d, s, MX + i * (lw + 10), 148, lw)
    d.line([(MX, 380), (W - MX, 380)], fill=RULE, width=1)
    # mediums: 2 rows x 3 columns
    mw = (W - 2 * MX - 2 * 8) // 3
    for i, s in enumerate(MEDIUMS[:3]):
        draw_medium(d, s, MX + i * (mw + 8), 386, mw)
    for i, s in enumerate(MEDIUMS[3:]):
        draw_medium(d, s, MX + i * (mw + 8), 522, mw)
    d.line([(MX, 656), (W - MX, 656)], fill=RULE, width=1)
    draw_bottom(d)
    draw_datecheck(d)
    draw_footer(d)
    return img


def main():
    img = build()
    out = os.path.join(HERE, "entry.png")
    img.save(out, optimize=True)
    print(out, os.path.getsize(out), "bytes", img.size)


if __name__ == "__main__":
    main()
