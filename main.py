import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": texto})

def buscar_oferta_api():
    url = "https://api.mercadolibre.com/sites/MLB/search?q=pokemon+tcg+etb&limit=1"
    
    # O Segredo: Disfarçar o robô como um navegador real
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        # Passando o disfarce (headers) junto com a requisição
        resposta = requests.get(url, headers=headers)
        
        if resposta.status_code == 403:
            return "⚠️ Erro 403 Persistente. O ML bloqueou o IP do GitHub."
            
        dados = resposta.json()
        
        if "results" in dados and len(dados["results"]) > 0:
            produto = dados["results"][0]
            titulo = produto["title"]
            preco = produto["price"]
            link = produto["permalink"]
            
            return {
                "titulo": titulo,
                "preco": f"{preco:.2f}".replace(".", ","),
                "link": link
            }
        else:
            return "⚠️ A API não encontrou produtos para essa busca."
            
    except Exception as e:
        return f"❌ Erro na API: {str(e)}"

def main():
    resultado = buscar_oferta_api()
    
    if isinstance(resultado, dict):
        mensagem = f"""🔥 *OFERTA DETECTADA!*

📦 {resultado['titulo']}
💰 R$ {resultado['preco']}

🔗 Link original: {resultado['link']}
"""
        enviar_mensagem(mensagem)
        print("✅ Oferta enviada via API com disfarce!")
    else:
        enviar_mensagem(resultado)
        print("Aviso enviado.")

if __name__ == "__main__":
    main()
