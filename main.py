import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

print("TOKEN OK:", bool(TOKEN))
print("CHAT_ID:", CHAT_ID)

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": "🚨 TESTE DEFINITIVO DO BOT - SE ISSO NÃO CHEGAR, É TOKEN OU CHAT_ID"
}

r = requests.post(url, json=payload)

print("STATUS:", r.status_code)
print("RESPOSTA:", r.text)
