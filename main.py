import os
from calendar_utils import get_today_info
from generate_image import create_calendar_image
from telegram_bot import send_photo

def main():
    info = get_today_info(os.getenv("TIMEZONE", "Asia/Tehran"))
    image_path = create_calendar_image(info, os.getenv("CTA_USERNAME", "@YOUR_USERNAME"))
    send_photo(
        os.environ["TELEGRAM_BOT_TOKEN"],
        os.environ["TELEGRAM_CHANNEL_ID"],
        image_path,
        info["caption"],
    )
    print(f"Published {info['jalali_date']}")

if __name__ == "__main__":
    main()
