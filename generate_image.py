from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
OUTPUT = ROOT / "calendar_today.png"

def get_font(size, bold=False):
    names = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/noto/NotoSansArabic-Regular.ttf",
    ]
    for name in names:
        if Path(name).exists():
            return ImageFont.truetype(name, size)
    return ImageFont.load_default()

def create_calendar_image(info, username):
    W, H = 1080, 1350
    img = Image.new("RGB", (W, H), "#F5F3EE")
    d = ImageDraw.Draw(img)

    title = get_font(70, True)
    number = get_font(240, True)
    month = get_font(68, True)
    body = get_font(38)
    event = get_font(40)

    d.text((W//2, 110), info["weekday"], font=title, anchor="ma", fill="#111")
    d.text((W//2, 350), str(info["jalali_day"]), font=number, anchor="ma", fill="#111")
    d.text((W//2, 600), info["jalali_month"], font=month, anchor="ma", fill="#111")
    d.text((W//2, 690), str(info["jalali_year"]), font=month, anchor="ma", fill="#555")

    d.text((W-90, 810), "مناسبت‌های امروز", font=month, anchor="ra", fill="#111")
    y = 900
    for e in info["events"][:5]:
        d.text((W-90, y), "• " + e["title"], font=event, anchor="ra", fill="#222")
        y += 62

    d.line((90, 1130, W-90, 1130), fill="#AAA", width=2)
    d.text((W//2, 1190), "تقویم اختصاصی خودت رو سفارش بده",
           font=body, anchor="ma", fill="#111")
    d.text((W//2, 1250), username, font=body, anchor="ma", fill="#555")

    img.save(OUTPUT, quality=95)
    return str(OUTPUT)
