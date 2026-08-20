import requests

def send_photo(token, chat_id, image_path, caption):
    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    with open(image_path, "rb") as f:
        r = requests.post(
            url,
            data={"chat_id": chat_id, "caption": caption},
            files={"photo": f},
            timeout=60,
        )
    r.raise_for_status()
    data = r.json()
    if not data.get("ok"):
        raise RuntimeError(data)
    return data
