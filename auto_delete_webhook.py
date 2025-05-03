import requests
import time
from flask import Flask
import threading

app = Flask(__name__)
last_webhook = None

@app.route('/')
def home():
    return "Webhook Auto-Deleter is Running!"

def delete_loop():
    global last_webhook
    while True:
        try:
            webhook_url = requests.get("https://jacki.nuked.asia/p/raw/5nognhmk4g").text.strip()
            if webhook_url.startswith("https://discord.com/api/webhooks/") and webhook_url != last_webhook:
                print(f"Deleting: {webhook_url}")
                requests.delete(webhook_url)
                last_webhook = webhook_url
            else:
                print(f"Skipped (same or invalid): {webhook_url}")
            time.sleep(0.1)
        except Exception:
            pass

if __name__ == "__main__":
    threading.Thread(target=delete_loop).start()
    app.run(host="0.0.0.0", port=8080)
