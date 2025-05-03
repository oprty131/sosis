import requests
import time
from flask import Flask
import threading

app = Flask(__name__)
last_deleted = None  # Only store if deletion was successful

@app.route('/')
def home():
    return "Webhook Auto-Deleter is Running!"

def delete_loop():
    global last_deleted
    while True:
        try:
            webhook_url = requests.get("https://raw.githubusercontent.com/oprty131/Audios/refs/heads/main/Webhook").text.strip()
            if webhook_url.startswith("https://discord.com/api/webhooks/"):
                if webhook_url != last_deleted:
                    r = requests.delete(webhook_url)
                    if r.status_code == 204:
                        print(f"Deleted: {webhook_url}")
                        last_deleted = webhook_url
                    else:
                        print(f"Failed to delete ({r.status_code}): {webhook_url}")
                else:
                    print(f"Skipped (already deleted): {webhook_url}")
            else:
                print(f"Skipped (invalid URL): {webhook_url}")
            time.sleep(0.1)
        except Exception:
            pass

if __name__ == "__main__":
    threading.Thread(target=delete_loop).start()
    app.run(host="0.0.0.0", port=8080)
