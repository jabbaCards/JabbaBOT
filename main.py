import os
import requests
from bs4 import BeautifulSoup

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": texto})

def buscar_oferta_real():
    url = "https://lista.mercadolivre.com.br/pokemon-tcg-etb"
    
    # Cabeçalho para fingir que somos um navegador de verdade e evitar bloqueio
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "pt-BR,pt;q=0.9"
    }
    
    try:
        resposta = requests.get(url, headers=headers)
        
        # Se o Mercado Livre barrar, ele avisa no Telegram
        if resposta.status_code != 200:
            return f"⚠️ O Mercado Livre bloqueou o robô (Status: {resposta.status_code})"
            
        soup = BeautifulSoup(resposta.text, "html.parser")
        
        # Tenta pegar os cards de produtos
        itens = soup.select(".ui-search-layout__item")
        
        if not itens:
            return "⚠️ O robô acessou o site, mas o Mercado Livre mudou o código HTML (nenhum card encontrado)."
            
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
                
        return "⚠️ Encontrou produtos, mas não achou a tag de preço ou título."
        
    except Exception as e:
        return f"❌ Erro no código do robô: {str(e)}"

def main():
    resultado = buscar_oferta_real()
    
    # Se o resultado for um dicionário (oferta real), ele monta a mensagem bonita
    if isinstance(resultado, dict):
        mensagem = f"""🔥 *OFERTA ENCONTRADA!*

📦 {resultado['titulo']}
💰 R$ {resultado['preco']}

🔗 Link: {resultado['link']}"""
        enviar_mensagem(mensagem)
    else:
        # Se deu algum problema, envia o erro pro Telegram pra gente não precisar olhar o GitHub
        enviar_mensagem(resultado)

if __name__ == "__main__":
    main()
