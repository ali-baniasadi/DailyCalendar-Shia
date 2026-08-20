# Daily Calendar Bot

ربات MVP برای انتشار خودکار تقویم روزانه در کانال تلگرام.

## راه‌اندازی

1. با @BotFather یک Bot بساز.
2. Bot را Admin کانال کن و اجازه Post Messages بده.
3. در GitHub این Secrets را اضافه کن:
   - TELEGRAM_BOT_TOKEN
   - TELEGRAM_CHANNEL_ID
   - CTA_USERNAME
4. فایل `events.json` را با دیتای واقعی مناسبت‌ها پر کن.
5. از تب Actions گزینه `Daily Calendar` و سپس `Run workflow` را بزن.

## زمان‌بندی

هر روز حدود ساعت 08:00 تهران.

نکته: GitHub Actions ممکن است cron را چند دقیقه دیرتر اجرا کند.

## ساختار مناسبت

```json
{
  "date": "1405-05-30",
  "title": "عنوان مناسبت"
}
```
