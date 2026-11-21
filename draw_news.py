#!/usr/bin/env python3
"""Draw the 20 November 2026 front page in code (Pillow only, no photos).

Stories (all reported Friday 20 November 2026):
  1. ICJ rules Myanmar committed genocide against the Rohingya (The Hague, 9-6)
  2. Trump, Xi and Putin hold first three-way summit in Shenzhen; joint peace declaration
  3. Russian overnight strikes hit Kyiv (1 killed; Austrian & Dutch embassies damaged);
     Ukraine strikes the Kerch Bridge for a third time in four days
  4. Houthi missile damages the PIF tower in Riyadh's financial district
  5. Markets slide: S&P 500 down ~2%, fifth straight day; Nikkei -4.8% after
     Anthropic's Nasdaq debut
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (247, 243, 234)      # newsprint cream
INK = (24, 24, 28)
NAVY = (18, 38, 74)
RED = (178, 34, 34)
BLUE = (30, 90, 160)
GOLD = (198, 148, 32)
GREY = (90, 90, 92)
LINE = (180, 175, 162)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---------- masthead ----------
d.rectangle([0, 0, W, 124], fill=NAVY)
d.text((512, 20), "THE WORLD IN ONE DAY", font=font(SERIF_B, 58),
       fill=(255, 255, 255), anchor="ma")
d.text((512, 88), "FRIDAY  •  20 NOVEMBER 2026", font=font(SANS_B, 30),
       fill=(255, 214, 90), anchor="ma")
d.rectangle([0, 124, W, 130], fill=GOLD)

# ---------- lead story: ICJ ruling ----------
d.rectangle([28, 144, 996, 430], outline=INK, width=3)
d.rectangle([28, 144, 996, 196], fill=INK)
d.text((512, 152), "LEAD  •  THE HAGUE", font=font(SANS_B, 24),
       fill=(255, 214, 90), anchor="ma")
# scales of justice pictogram, left
cx, cy = 150, 316
d.line([cx, cy - 62, cx, cy + 62], fill=NAVY, width=7)
d.line([cx - 62, cy - 62, cx + 62, cy - 62], fill=NAVY, width=6)
d.polygon([(cx - 14, cy - 62), (cx + 14, cy - 62), (cx, cy - 84)], fill=GOLD)
d.line([cx - 62, cy - 62, cx - 62, cy - 30], fill=NAVY, width=4)
d.line([cx + 62, cy - 62, cx + 62, cy - 30], fill=NAVY, width=4)
d.pieslice([cx - 90, cy - 34, cx - 34, cy + 6], 0, 180, fill=NAVY)
d.pieslice([cx + 34, cy - 34, cx + 90, cy + 6], 0, 180, fill=NAVY)
d.rectangle([cx - 42, cy + 62, cx + 42, cy + 74], fill=NAVY)
d.text((280, 212), "WORLD COURT: MYANMAR", font=font(SERIF_B, 44),
       fill=INK, anchor="la")
d.text((280, 266), "COMMITTED GENOCIDE", font=font(SERIF_B, 44),
       fill=RED, anchor="la")
d.text((280, 330), "ICJ finds Rohingya genocide — first such", font=font(SANS, 26),
       fill=INK, anchor="la")
d.text((280, 362), "ruling against a state, by 9 votes to 6", font=font(SANS, 26),
       fill=INK, anchor="la")
d.text((512, 394), "THE HAGUE  •  INTERNATIONAL COURT OF JUSTICE", font=font(SANS_B, 20),
       fill=GREY, anchor="ma")

# ---------- middle row: two panels ----------
def panel(x0, y0, x1, y1, tag, color):
    d.rectangle([x0, y0, x1, y1], outline=INK, width=3)
    d.rectangle([x0, y0, x1, y0 + 44], fill=color)
    d.text(((x0 + x1) // 2, y0 + 8), tag, font=font(SANS_B, 23),
           fill=(255, 255, 255), anchor="ma")


# Shenzhen summit panel
panel(28, 452, 500, 726, "SHENZHEN  •  DIPLOMACY", NAVY)
# three small flags on poles
for i, (c1, c2) in enumerate([((178, 34, 34), (255, 255, 255)),
                             ((220, 40, 40), (255, 214, 0)),
                             ((255, 255, 255), (0, 60, 160))]):
    fx = 96 + i * 118
    d.line([fx, 540, fx, 640], fill=INK, width=5)
    d.rectangle([fx, 540, fx + 92, 540 + 52], outline=INK, width=2, fill=c1)
    if i == 0:  # US stripes
        for s in range(3):
            d.rectangle([fx, 540 + 8 + s * 16, fx + 92, 540 + 16 + s * 16], fill=(255, 255, 255))
        d.rectangle([fx, 540, fx + 38, 540 + 28], fill=(18, 38, 74))
    if i == 1:  # China star
        d.text((fx + 46, 544), "*", font=font(SANS_B, 40), fill=(255, 214, 0), anchor="ma")
    if i == 2:  # Russia tricolour
        d.rectangle([fx, 540 + 17, fx + 92, 540 + 35], fill=(0, 60, 160))
        d.rectangle([fx, 540 + 35, fx + 92, 540 + 52], fill=(178, 34, 34))
d.text((264, 648), "TRUMP, XI AND PUTIN MEET", font=font(SERIF_B, 27),
       fill=INK, anchor="ma")
d.text((264, 676), "Joint peace declaration — no", font=font(SANS, 22),
       fill=INK, anchor="ma")
d.text((264, 700), "mention of Ukraine or Iran", font=font(SANS, 22),
       fill=INK, anchor="ma")

# Kyiv strikes panel
panel(524, 452, 996, 726, "KYIV  •  WAR IN UKRAINE", RED)
# skyline + explosion (explosion sits above the rooftops, below the tag band)
for bx, bw, bh in [(560, 52, 56), (622, 44, 72), (676, 58, 48), (744, 46, 64),
                   (800, 56, 44), (866, 48, 60), (924, 52, 52)]:
    d.rectangle([bx, 640 - bh, bx + bw, 640], fill=(70, 70, 78))
d.polygon([(700, 500), (724, 546), (700, 566), (676, 546)], fill=GOLD)
d.polygon([(724, 526), (760, 546), (730, 566)], fill=(255, 120, 40))
d.polygon([(676, 526), (640, 546), (672, 566)], fill=(255, 120, 40))
d.ellipse([688, 500, 736, 542], fill=(255, 200, 60))
d.text((760, 648), "RUSSIAN STRIKES HIT KYIV", font=font(SERIF_B, 27),
       fill=INK, anchor="ma")
d.text((760, 676), "1 killed; embassies damaged.", font=font(SANS, 22),
       fill=INK, anchor="ma")
d.text((760, 700), "Ukraine hits Kerch Bridge again", font=font(SANS, 22),
       fill=INK, anchor="ma")

# ---------- bottom row: two panels ----------
# Riyadh panel
panel(28, 738, 500, 978, "RIYADH  •  MIDDLE EAST", (90, 60, 30))
# tower with smoke
d.rectangle([196, 812, 300, 884], fill=(60, 60, 70))
for fy in range(820, 876, 16):
    for fx in range(204, 292, 24):
        d.rectangle([fx, fy, fx + 12, fy + 8], fill=(255, 214, 90))
d.polygon([(238, 788), (258, 812), (218, 812)], fill=(60, 60, 70))
d.ellipse([300, 792, 336, 822], fill=(120, 120, 120))
d.ellipse([326, 772, 368, 808], fill=(150, 150, 150))
d.ellipse([360, 756, 404, 794], fill=(180, 180, 180))
d.text((264, 894), "HOUTHI MISSILE HITS", font=font(SERIF_B, 24),
       fill=INK, anchor="ma")
d.text((264, 922), "RIYADH TOWER", font=font(SERIF_B, 24),
       fill=INK, anchor="ma")
d.text((264, 950), "Saudi wealth-fund tower damaged", font=font(SANS, 20),
       fill=INK, anchor="ma")

# Markets panel
panel(524, 738, 996, 978, "NEW YORK  •  MARKETS", BLUE)
# falling chart
d.rectangle([560, 792, 960, 880], outline=GREY, width=2)
pts = [(575, 806), (640, 820), (705, 816), (770, 842), (835, 856), (900, 868), (945, 874)]
d.line(pts, fill=RED, width=6, joint="curve")
d.polygon([(945, 874), (915, 858), (940, 842)], fill=RED)
d.text((760, 890), "MARKETS SLIDE", font=font(SERIF_B, 26), fill=INK, anchor="ma")
d.text((760, 920), "S&P 500 −2%, 5th day down;", font=font(SANS, 21),
       fill=INK, anchor="ma")
d.text((760, 944), "Nikkei −4.8% after Anthropic debut", font=font(SANS, 21),
       fill=INK, anchor="ma")

# footer
d.rectangle([0, 990, W, 1024], fill=INK)
d.text((512, 998), "All events reported Friday 20 November 2026  •  One day, five stories",
       font=font(SANS, 20), fill=(255, 255, 255), anchor="ma")

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
