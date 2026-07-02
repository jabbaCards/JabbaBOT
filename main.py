import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": texto})

def buscar_oferta_api():
    # A URL original da API do ML
    url_ml = "https://api.mercadolibre.com/sites/MLB/search?q=pokemon+tcg+etb&limit=1"
    
    # Novo Túnel (CodeTabs) - Mais rápido e estável
    proxy_url = f"https://api.codetabs.com/v1/proxy?quest={url_ml}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        # Fazendo a busca através do novo túnel (espera até 15s)
        resposta = requests.get(proxy_url, headers=headers, timeout=15)
        
        if resposta.status_code != 200:
            return f"⚠️ O Túnel 2 também foi bloqueado (Status: {resposta.status_code})"
            
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
            return "⚠️ O túnel funcionou, mas a busca não retornou produtos."
            
    except Exception as e:
        return f"❌ Erro no Túnel 2: {str(e)}"

def main():
    print("🚀 Testando novo túnel CodeTabs...")
    resultado = buscar_oferta_api()
    
    if isinstance(resultado, dict):
        mensagem = f"""🔥 *ALERTA DE OFERTA (JabbaBOT)* 🔥

📦 {resultado['titulo']}
💰 R$ {resultado['preco']}

🔗 *Link original:* {resultado['link']}

💡 *Ação:* Copie esse link, gere o seu link de afiliado no app do ML e poste no grupo principal!"""
        
        enviar_mensagem(mensagem)
        print("✅ Oferta enviada via Túnel 2!")
    else:
        enviar_mensagem(resultado)
        print("Aviso enviado.")

if __name__ == "__main__":
    main()
