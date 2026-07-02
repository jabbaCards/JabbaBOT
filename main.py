import os
import requests
from bs4 import BeautifulSoup

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": texto})

def buscar_oferta_real():
    print("🔎 Varrendo o Mercado Livre por Pokémon TCG ETB...")
    # URL de busca focada em ETB para testarmos
    url = "https://lista.mercadolivre.com.br/pokemon-tcg-etb"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        resposta = requests.get(url, headers=headers)
        soup = BeautifulSoup(resposta.text, "html.parser")
        
        # Pega a lista de produtos
        itens = soup.select(".ui-search-layout__item")
        
        # Vai olhar o primeiro produto válido da lista
        for item in itens:
            titulo = item.select_one(".ui-search-item__title")
            preco = item.select_one(".andes-money-amount__fraction")
            link = item.select_one("a.ui-search-link")
            
            if titulo and preco and link:
                return {
                    "titulo": titulo.text,
                    "preco": preco.text,
                    "link": link["href"]
                }
    except Exception as e:
        print(f"Erro durante a raspagem: {e}")
        
    return None

def main():
    print("🚀 JabbaBOT v1.1 - Iniciando...")
    oferta = buscar_oferta_real()
    
    if oferta:
        mensagem = f"""🔥 *OFERTA ENCONTRADA!*

📦 {oferta['titulo']}
💰 R$ {oferta['preco']}

🔗 Link: {oferta['link']}"""
        
        enviar_mensagem(mensagem)
        print("✅ Oferta real enviada com sucesso no Telegram!")
    else:
        print("❌ Nenhuma oferta encontrada ou o layout do ML mudou.")

if __name__ == "__main__":
    main()
