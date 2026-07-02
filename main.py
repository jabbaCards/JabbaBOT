import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def enviar(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": mensagem
    })

def main():
    print("BOT RODANDO")

    # simulação de oferta (vamos trocar depois por scraping/API)
    oferta = {
        "titulo": "Pokémon TCG - Booster Box Scarlet & Violet",
        "preco": 279.90,
        "link": "https://www.mercadolivre.com.br/exemplo"
    }

    mensagem = f"""🔥 OFERTA DETECTADA

🎴 {oferta['titulo']}
💰 R$ {oferta['preco']}

🔗 {oferta['link']}
"""

    enviar(mensagem)

if __name__ == "__main__":
    main()
