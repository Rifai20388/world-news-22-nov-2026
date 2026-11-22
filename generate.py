#!/usr/bin/env python3
"""Draw the front page for 22 November 2026 and write entry.png.

Front-page newspaper style, 1024x1024, drawn with PIL (stdlib + Pillow).
Run: python3 generate.py  -> writes entry.png next to this file.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 44
PAPER = (248, 244, 232)
INK = (18, 18, 18)
RED = (178, 28, 28)
GREY = (90, 86, 76)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap measured with the real font."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill=INK, leading=None):
    if leading is None:
        leading = int(fnt.size * 1.28)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x, y, width, weight=2):
    draw.line([(x, y), (x + width, y)], fill=INK, width=weight)
    return y + weight


def tracked(draw, text, x, y, fnt, fill=INK, tracking=3):
    """Draw caps text with letter spacing."""
    cx = x
    for ch in text:
        draw.text((cx, y), ch, font=fnt, fill=fill)
        cx += draw.textlength(ch, font=fnt) + tracking
    return cx


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Outer frame
    d.rectangle([10, 10, W - 11, H - 11], outline=INK, width=4)
    d.rectangle([20, 20, W - 21, H - 21], outline=INK, width=1)

    content_w = W - 2 * MARGIN
    y = 34

    # Masthead
    mast = font(SERIF, 96)
    name = "THE WORLD"
    d.text(((W - d.textlength(name, font=mast)) / 2, y), name, font=mast, fill=INK)
    y += 110
    y = rule(d, MARGIN, y, content_w, 3)
    y += 10

    # Dateline strip
    date_f = font(SANS, 25)
    date_txt = "SUNDAY, 22 NOVEMBER 2026"
    d.text(((W - d.textlength(date_txt, font=date_f)) / 2, y), date_txt,
           font=date_f, fill=INK)
    y += 34
    small = font(SANS_REG, 17)
    sub = "ONE DAY  ·  SIX STORIES  ·  THE NEWS THAT MADE SUNDAY"
    d.text(((W - d.textlength(sub, font=small)) / 2, y), sub,
           font=small, fill=GREY)
    y += 26
    y = rule(d, MARGIN, y, content_w, 3)
    y += 16

    # ---- TOP STORY ----
    kick = font(SANS, 21)
    tracked(d, "SUMMIT IN SHENZHEN", MARGIN, y, kick, fill=RED, tracking=4)
    y += 28
    head = font(SERIF, 58)
    d.text((MARGIN, y), "TRUMP, XI AND PUTIN", font=head, fill=INK)
    y += 62
    d.text((MARGIN, y), "MEET IN SHENZHEN", font=head, fill=INK)
    y += 64
    deck = font(SERIF_REG, 25)
    deck_txt = ("The three leaders hold the first trilateral summit in "
                "Shenzhen and issue a joint peace declaration — but critics "
                "question what was achieved. Zelenskyy calls it “very "
                "unsuccessful for Russia” as Moscow launches its biggest "
                "attacks of the year on Ukraine.")
    y = draw_lines(d, wrap(d, deck_txt, deck, content_w), MARGIN, y, deck)
    y += 8
    y = rule(d, MARGIN, y, content_w, 2)
    y += 16

    # ---- ROW 2: two columns ----
    col_w = (content_w - 28) // 2
    x2 = MARGIN + col_w + 28
    y_row2 = y
    y_end = y_row2

    h2 = font(SANS, 27)
    b2 = font(SERIF_REG, 21)

    # Left: ICJ genocide ruling
    yy = draw_lines(d, wrap(d, "ICJ: MYANMAR COMMITTED GENOCIDE", h2, col_w),
                    MARGIN, y_row2, h2, leading=32)
    yy += 4
    yy = draw_lines(d, wrap(d, "The International Court of Justice finds "
                               "Myanmar committed genocide against the "
                               "Rohingya — a watershed for the Genocide "
                               "Convention. Refugees welcome the verdict but "
                               "say they want to go home.", b2, col_w),
                    MARGIN, yy, b2, leading=27)
    y_end = max(y_end, yy)

    # Right: Iran strikes Bahrain
    yy = draw_lines(d, wrap(d, "IRAN STRIKES BAHRAIN, HORMUZ HIT", h2, col_w),
                    x2, y_row2, h2, leading=32)
    yy += 4
    yy = draw_lines(d, wrap(d, "Bahrain accuses Iran of hitting a civilian "
                               "industrial site; the IRGC claims missile and "
                               "drone attacks on US Navy positions. Attacks on "
                               "Hormuz shipping reach the highest level of "
                               "the war.", b2, col_w), x2, yy, b2, leading=27)
    y_end = max(y_end, yy)

    y = y_end + 8
    y = rule(d, MARGIN, y, content_w, 2)
    y += 12

    # ---- ROW 3: three columns ----
    col3_w = (content_w - 56) // 3
    xs = [MARGIN, MARGIN + col3_w + 28, MARGIN + 2 * (col3_w + 28)]
    h3 = font(SANS, 22)
    b3 = font(SERIF_REG, 19)
    stories = [
        ("DRONE HITS RUSSIAN SHIP",
         "A Russian cargo ship catches fire after a drone strike in the Gulf "
         "of Finland; a missile on Kryvyi Rih kills 2 and wounds about 60."),
        ("COP31 STALLS IN ANTALYA",
         "Climate talks enter a second day of overtime, delegates still split "
         "over fossil-fuel language in the final text."),
        ("FBI DATABASE HACKED",
         "Trump confirms a breach of the FBI's NCIC system — fingerprints, "
         "wanted persons and missing persons records exposed."),
    ]
    y_end = y
    for (title, body), x in zip(stories, xs):
        yy = draw_lines(d, wrap(d, title, h3, col3_w), x, y, h3, leading=27)
        yy += 4
        yy = draw_lines(d, wrap(d, body, b3, col3_w), x, yy, b3, leading=24)
        y_end = max(y_end, yy)

    y = y_end + 8
    y = rule(d, MARGIN, y, content_w, 3)
    y += 8

    # Footer
    foot = font(SANS_REG, 16)
    foot_txt = "THE WORLD — SUNDAY, 22 NOVEMBER 2026"
    d.text(((W - d.textlength(foot_txt, font=foot)) / 2, y), foot_txt,
           font=foot, fill=INK)
    y += 20
    src = font(SANS_REG, 13)
    src_txt = "Sources: AP · BBC · Reuters · The Guardian · Financial Times"
    d.text(((W - d.textlength(src_txt, font=src)) / 2, y), src_txt,
           font=src, fill=GREY)

    img.save("entry.png", "PNG", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
