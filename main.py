import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": "🚨 TESTE DEFINITIVO DO BOT"
}

r = requests.post(url, json=payload)

print("STATUS:", r.status_code)
print("RESPOSTA:", r.text)
