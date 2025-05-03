import requests, time
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Webhook Auto-Deleter is Running!"

def delete_loop():
    while True:
        try:
            webhook_url = requests.get("https://jacki.nuked.asia/p/raw/5nognhmk4g").text.strip()
            requests.post(webhook_url, json={"content": "@everyone @here deleted by oimo6373 auto webhook deleter"})
            requests.delete(webhook_url)
            print("Webhook deleted.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    threading.Thread(target=delete_loop).start()
    app.run(host="0.0.0.0", port=8080)
