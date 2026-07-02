import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# URL da Amazon (Nova Versão)
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbz0YFi47Qy5QHTD03QziUwMiGVyh7sAHn-5_qD0F-OQNnbF6NESZqLtHtQjg-fnRb3z/exec"

def main():
    try:
        # Busca os dados processados pelo seu Script (Amazon)
        resposta = requests.get(f"{URL_DO_GOOGLE}?q=pokemon", timeout=30)
        dados = resposta.json()
        
        titulo = dados.get('titulo', 'Produto não capturado')
        preco = dados.get('preco', '0')
        link = dados.get('link', 'Sem link')
        
        # Formatação da mensagem para o Telegram
        mensagem = (
            f"🚀 *JABBABOT (Amazon Edition)* 🚀\n\n"
            f"📦 {titulo}\n"
            f"💰 {preco}\n"
            f"🔗 {link}"
        )
        
        # Envio para o Telegram
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": mensagem})
        
        print("✅ Sucesso! Dados da Amazon enviados.")
        
    except Exception as e:
        print(f"❌ Erro na execução: {e}")

if __name__ == "__main__":
    main()
