from flask import Flask
import requests
import time
import re
import threading

app = Flask(__name__)

def get_webhook_from_url(check_url):
    try:
        response = requests.get(check_url)
        if response.status_code == 200:
            webhook_match = re.search(r'https://discord\.com/api/webhooks/\d+/[a-zA-Z0-9_-]+', response.text)
            if webhook_match:
                return webhook_match.group(0)
    except Exception as e:
        print(f"Error checking URL: {e}")
    return None

def delete_webhook(webhook_url):
    try:
        response = requests.delete(webhook_url)
        if response.status_code == 204:
            print(f"Successfully deleted webhook: {webhook_url}")
            return True
        else:
            print(f"Failed to delete webhook. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error deleting webhook: {e}")
    return False

def monitor_webhooks():
    target_url = "https://raw.githubusercontent.com/oprty131/Audios/refs/heads/main/Webhook"
    while True:
        print(f"Checking {target_url} for webhooks...")
        webhook_url = get_webhook_from_url(target_url)
        if webhook_url:
            print(f"Found webhook: {webhook_url}")
            delete_webhook(webhook_url)
        else:
            print("No webhook found in the file.")
        time.sleep(60)  # Check every 60 seconds

@app.route('/')
def home():
    return "Webhook Auto-Deleter is running"

def run_app():
    # Start monitoring thread
    monitor_thread = threading.Thread(target=monitor_webhooks)
    monitor_thread.daemon = True
    monitor_thread.start()
    
    # Start Flask app
    app.run(host='0.0.0.0', port=10000)

if __name__ == '__main__':
    run_app()
