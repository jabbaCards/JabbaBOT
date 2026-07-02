import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# URL da Versão 12 (Atualizada agora)
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbzBahziUHhzxDa1G9bjAHLYrce7TtbB7zh2qhckeC_cOUpXMpjrP56vSENOd4QTXUG4/exec"

def main():
    try:
        # Busca os dados processados pelo Script
        resposta = requests.get(f"{URL_DO_GOOGLE}?q=pokemon", timeout=30).json()
        
        # 'titulo' será o status e 'preco' será o link do produto
        status = resposta.get('titulo', 'Erro')
        link = resposta.get('preco', '0')
        
        mensagem = f"🔥 *JABBABOT (Versão 12)* 🔥\n\n📦 Status: {status}\n🔗 {link}"
        
        # Envia para o Telegram
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": mensagem})
        
        print("✅ Sucesso! Link enviado para o Telegram.")
        
    except Exception as e:
        print(f"❌ Erro na execução: {e}")

if __name__ == "__main__":
    main()
