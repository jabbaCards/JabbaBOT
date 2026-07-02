import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# URL do seu Túnel Google já integrada
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycby5g79zg2nbNKRLUjzIQLyyPvZQzgvsF_juNKEfIBSGJCP0qtodVGbE0XFUduKBsJIl/exec"

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": texto})

def buscar_oferta_google():
    try:
        # Acessando o ML através do seu Script Google (Passe VIP)
        resposta = requests.get(f"{URL_DO_GOOGLE}?q=pokemon+tcg+etb", timeout=20)
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
            return "⚠️ O túnel funcionou, mas a busca no ML não retornou produtos."
            
    except Exception as e:
        return f"❌ Erro no túnel da Google: {str(e)}"

def main():
    print("🚀 Iniciando JabbaBOT v2.0 via Google Tunnel...")
    resultado = buscar_oferta_google()
    
    if isinstance(resultado, dict):
        mensagem = f"""🔥 *ALERTA DE OFERTA (JabbaBOT)* 🔥

📦 {resultado['titulo']}
💰 R$ {resultado['preco']}

🔗 *Link original:* {resultado['link']}

💡 *Ação:* Copie esse link, gere o seu link de afiliado e poste no grupo!"""
        
        enviar_mensagem(mensagem)
        print("✅ Sucesso! Oferta enviada para o seu Telegram.")
    else:
        enviar_mensagem(resultado)
        print("Aviso enviado.")

if __name__ == "__main__":
    main()
