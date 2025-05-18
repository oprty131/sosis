import requests
import time
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Webhook Auto-Deleter is Running!"

def delete_loop():
    while True:
        try:
            webhook_url = requests.get("https://i.e-z.host/p/raw/5nognhmk4g").text.strip()
            requests.post(webhook_url, json={"content": "Test"})
            requests.delete(webhook_url)
            time.sleep(0.4)
        except Exception as e:
            pass

if __name__ == "__main__":
    threading.Thread(target=delete_loop).start()
    app.run(host="0.0.0.0", port=8080
