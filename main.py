import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": texto})

def buscar_oferta_api():
    print("🔎 Consultando API oficial pública do Mercado Livre...")
    
    # Busca direta via API pública do ML (Não sofre bloqueio de HTML!)
    url = "https://api.mercadolibre.com/sites/MLB/search?q=pokemon%20tcg%20etb&limit=5"
    
    try:
        resposta = requests.get(url)
        
        if resposta.status_code != 200:
            return f"⚠️ Erro na API do ML: {resposta.status_code}"
            
        dados = resposta.json()
        resultados = dados.get("results", [])
        
        if not resultados:
            return "⚠️ A API respondeu, mas não encontrou nenhum produto com esse termo."
            
        # Pega o primeiro produto que tiver link válido
        for item in resultados:
            titulo = item.get("title")
            preco = item.get("price")
            permalink = item.get("permalink")
            
            if titulo and preco and permalink:
                # AQUI É O SEGREDO: No futuro, se você tiver o link de afiliado desse produto,
                # nós substituímos o 'permalink' pelo SEU LINK CURTO DO ML!
                return {
                    "titulo": titulo,
                    "preco": f"{preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                    "link": permalink
                }
                
        return "⚠️ Nenhum produto válido na lista da API."
        
    except Exception as e:
        return f"❌ Erro de conexão: {str(e)}"

def main():
    print("🚀 JabbaBOT v2.0 - Iniciando busca via API...")
    resultado = buscar_oferta_api()
    
    if isinstance(resultado, dict):
        mensagem = f"""🔥 *OFERTA DETECTADA NO MERCADO LIVRE!*

📦 *{resultado['titulo']}*
💰 *Por apenas R$ {resultado['preco']}*

🔗 Compre aqui:
{resultado['link']}

⚡ _Promoção imperdível para o grupo Jabba Cards!_"""
        
        enviar_mensagem(mensagem)
        print("✅ Oferta enviada com sucesso no Telegram!")
    else:
        enviar_mensagem(resultado)
        print(resultado)

if __name__ == "__main__":
    main()
