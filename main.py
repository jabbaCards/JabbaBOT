import os
import requests

# As chaves do seu bot devem estar configuradas no GitHub Secrets
TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# URL da Versão 7 (Extração via HTML)
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbzS1tT2GA0zcrgMKDSr7ev94wuXKo2cjF1d1qkfj_MYSNk9aFdNeb6BwDhRcMbQjBku/exec"

def main():
    try:
        # Busca os dados processados pelo seu Script
        # Adicionamos um parâmetro ?q=pokemon para garantir a busca
        resposta = requests.get(f"{URL_DO_GOOGLE}?q=pokemon", timeout=30).json()
        
        # Prepara a mensagem formatada
        mensagem = f"🔥 *JABBABOT ATIVO (Versão 7)* 🔥\n\n📦 {resposta['titulo']}\n💰 R$ {resposta['preco']}"
        
        # Envia para o Telegram
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": mensagem})
        
        print("✅ Sucesso! Oferta enviada para o Telegram.")
        
    except Exception as e:
        print(f"❌ Erro ao executar o JabbaBOT: {e}")

if __name__ == "__main__":
    main()
