import os
import requests
from bs4 import BeautifulSoup

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

URL = "https://lista.mercadolivre.com.br/pokemon-tcg"

KEYWORDS = ["pokemon", "pokémon", "tcg", "etb", "booster", "box"]
MAX_PRICE = 300

enviados = set()

def buscar_oferta():
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(URL, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    itens = soup.select(".ui-search-result__wrapper")

    for item in itens:
        titulo_tag = item.select_one(".ui-search-item__title")
        preco_tag = item.select_one(".andes-money-amount__fraction")
        link_tag = item.select_one("a.ui-search-link")

        if not titulo_tag or not preco_tag or not link_tag:
            continue

        titulo = titulo_tag.text.lower()
        link = link_tag["href"]

        try:
            preco = int(preco_tag.text.replace(".", ""))
        except:
            continue

        if link in enviados:
            continue

        if preco > MAX_PRICE:
            continue

        if any(k in titulo for k in KEYWORDS):
            return {
                "titulo": titulo_tag.text,
                "preco": preco,
                "link": link
            }

    return None


def enviar(oferta):
    mensagem = f"""🔥 OFERTA DETECTADA

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
        enviar(oferta)
        enviados.add(oferta["link"])
        print("Oferta enviada")
    else:
        print("Nenhuma oferta nova")


if __name__ == "__main__":
    main()
