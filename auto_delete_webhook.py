import requests
import time
from flask import Flask
import threading
import keep_alive

def delete_loop():
    while True:
        try:
            webhook_url = requests.get("https://i.e-z.host/p/raw/5nognhmk4g").text.strip()
            requests.post(webhook_url, json={"content": "Test"})
            requests.delete(webhook_url)
            time.sleep(0.4)
        except Exception as e:
            print(f"Error: {e}")

keep_alive.keep_alive()

threading.Thread(target=delete_loop).start()
