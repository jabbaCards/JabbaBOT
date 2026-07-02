import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

mensagem = """
🚀 JabbaBOT está ONLINE!

✅ Teste realizado com sucesso.

Em breve este grupo receberá:
🔥 Ofertas de Pokémon TCG
🎟️ Cupons
💰 Links de afiliado
📦 Produtos do Jabba Cards
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(
    url,
    json={
        "chat_id": CHAT_ID,
        "text": mensagem
    }
)

print("Mensagem enviada!")
