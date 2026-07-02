import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

print("TOKEN OK:", bool(TOKEN))
print("CHAT_ID:", CHAT_ID)

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

r = requests.post(url, json={
    "chat_id": CHAT_ID,
    "text": "🚀 TESTE FINAL - SE ISSO NÃO CHEGAR, É CHAT_ID OU TOKEN"
})

print("STATUS:", r.status_code)
print("RESPOSTA:", r.text)
