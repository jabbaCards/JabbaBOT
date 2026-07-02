import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycby5g79zg2nbNKRLUjzIQLyyPvZQzgvsF_juNKEfIBSGJCP0qtodVGbE0XFUduKBsJIl/exec"

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": texto})

def buscar_oferta_google():
    try:
        # Aumentamos o limite para ter mais chances de capturar algo
        url_busca = f"{URL_DO_GOOGLE}?q=pokemon+tcg+etb&limit=5"
        resposta = requests.get(url_busca, timeout=20)
        
        # Vamos depurar: se o JSON estiver vazio, ele nos avisa
        dados = resposta.json()
        
        # Se você quiser ver o que o ML responde, cheque os logs do GitHub Actions
        print("Resposta bruta do ML:", dados)
        
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
            return "⚠️ O Google acessou, mas a lista de 'results' veio vazia. O ML pode ter mudado a forma de listar."
            
    except Exception as e:
        return f"❌ Erro na busca: {str(e)}"

def main():
    resultado = buscar_oferta_google()
    
    if isinstance(resultado, dict):
        mensagem = f"🔥 *OFERTA ENCONTRADA!* \n\n📦 {resultado['titulo']}\n💰 R$ {resultado['preco']}\n🔗 {resultado['link']}"
        enviar_mensagem(mensagem)
    else:
        # Envia o erro pro Telegram para sabermos o que aconteceu sem precisar abrir o GitHub
        enviar_mensagem(f"🔍 Debug JabbaBOT: {resultado}")

if __name__ == "__main__":
    main()
