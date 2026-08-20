import json
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from persiantools.jdatetime import JalaliDate

ROOT = Path(__file__).parent

WEEKDAYS = {
    0: "دوشنبه", 1: "سه‌شنبه", 2: "چهارشنبه",
    3: "پنجشنبه", 4: "جمعه", 5: "شنبه", 6: "یکشنبه"
}
MONTHS = {
    1:"فروردین", 2:"اردیبهشت", 3:"خرداد", 4:"تیر",
    5:"مرداد", 6:"شهریور", 7:"مهر", 8:"آبان",
    9:"آذر", 10:"دی", 11:"بهمن", 12:"اسفند"
}

def load_events():
    with open(ROOT / "events.json", encoding="utf-8") as f:
        return json.load(f)

def get_today_info(timezone="Asia/Tehran"):
    now = datetime.now(ZoneInfo(timezone))
    j = JalaliDate(now.date())
    key = f"{j.year:04d}-{j.month:02d}-{j.day:02d}"
    events = [e for e in load_events() if e.get("date") == key]
    event_text = "\n".join(f"• {e['title']}" for e in events)
    if not event_text:
        event_text = "• مناسبت ویژه‌ای ثبت نشده است."

    cta = os.getenv("CTA_USERNAME", "@YOUR_USERNAME")
    caption = (
        f"📅 {WEEKDAYS[now.weekday()]} {j.day} {MONTHS[j.month]} {j.year}\n\n"
        f"🌍 {now.strftime('%Y-%m-%d')}\n\n"
        f"مناسبت‌های امروز:\n{event_text}\n\n"
        "────────────\n\n"
        "✨ تقویم اختصاصی خودت رو داشته باش\n\n"
        "تولد، سالگرد و هر تاریخ مهمی که برات مهمه، "
        "با طراحی اختصاصی.\n\n"
        f"🛍 سفارش: {cta}"
    )
    return {
        "jalali_date": key,
        "jalali_day": j.day,
        "jalali_month": MONTHS[j.month],
        "jalali_year": j.year,
        "weekday": WEEKDAYS[now.weekday()],
        "events": events,
        "caption": caption,
    }
