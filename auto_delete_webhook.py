import requests

url = "https://raw.githubusercontent.com/oprty131/Audios/refs/heads/main/Webhook"
last_webhook = None

while True:
    try:
        # Always get the current webhook
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            current_webhook = response.text.strip()

            if current_webhook != last_webhook:
                print(f"New webhook detected: {current_webhook}")
                last_webhook = current_webhook

            # Try to send "hi" to the latest webhook
            requests.post(current_webhook, json={"content": "hi"}, timeout=3)

    except Exception as e:
        pass  # Ignore errors and keep going
