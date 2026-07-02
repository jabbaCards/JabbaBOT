import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# URL da Amazon (Versão Corrigida)
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbwUrcE0DF3szlOyDVBywB4FRoiSkPZ7DzkedYEB4pEdYE33VKbH0YEjskQ8kj4ty-Pr/exec"

def main():
    try:
        # Busca os dados processados pelo seu Script
        resposta = requests.get(f"{URL_DO_GOOGLE}?q=pokemon", timeout=30)
        dados = resposta.json()
        
        titulo = dados.get('titulo', 'Produto não capturado')
        preco = dados.get('preco', '0')
        link = dados.get('link', 'Sem link')
        
        mensagem = (
            f"🚀 *JABBABOT ATIVO*\n\n"
            f"📦 {titulo}\n"
            f"💰 {preco}\n"
            f"🔗 {link}"
        )
        
        # Envio para o Telegram
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": mensagem})
        
        print("✅ Execução finalizada.")
        
    except Exception as e:
        print(f"❌ Erro na execução: {e}")

if __name__ == "__main__":
    main()
