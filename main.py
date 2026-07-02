import os
import requests
from bs4 import BeautifulSoup

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

SEARCH_URL = "https://lista.mercadolivre.com.br/pokemon-tcg"

KEYWORDS = ["pokemon", "pokémon", "etb", "booster", "box", "tcg"]

def buscar_oferta():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    resp = requests.get(SEARCH_URL, headers=headers)
    soup = BeautifulSoup(resp.text, "lxml")

    itens = soup.select(".ui-search-result__wrapper")

    for item in itens:
        titulo_tag = item.select_one(".ui-search-item__title")
        preco_tag = item.select_one(".andes-money-amount__fraction")
        link_tag = item.select_one("a.ui-search-link")

        if not titulo_tag or not preco_tag or not link_tag:
            continue

        titulo = titulo_tag.text.lower()
        preco = preco_tag.text
        link = link_tag["href"]

        if any(k in titulo for k in KEYWORDS):
            return {
                "titulo": titulo_tag.text,
                "preco": preco,
                "link": link
            }

    return None

def enviar_telegram(oferta):
    mensagem = f"""🚀 OFERTA ENCONTRADA!

🎴 {oferta['titulo']}
💰 R$ {oferta['preco']}

🔗 {oferta['link']}
"""

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": mensagem
    })

def main():
    oferta = buscar_oferta()

    if oferta:
        enviar_telegram(oferta)
        print("Oferta enviada!")
    else:
        print("Nenhuma oferta encontrada.")

if __name__ == "__main__":
    main()
