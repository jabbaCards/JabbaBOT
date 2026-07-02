import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# URL da Versão 11
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbzsRvHhyduZmnmpZEoS9jm9N0WBxsCCtGna7bA1XMo0PtQ6_tU6bpkcKnqIy5ocREMv/exec"

def main():
    try:
        # Busca os dados processados pelo Script
        resposta = requests.get(f"{URL_DO_GOOGLE}?q=pokemon", timeout=30)
        dados = resposta.json()
        
        titulo = dados.get('titulo', 'Produto não capturado')
        preco = dados.get('preco', '0')
        
        # Envia para o Telegram
        mensagem = f"🔥 *JABBABOT ATIVO (Versão 11)* 🔥\n\n📦 {titulo}\n💰 R$ {preco}"
        
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": mensagem})
        
        print("✅ Execução concluída.")
        
    except Exception as e:
        print(f"❌ Erro na execução: {e}")

if __name__ == "__main__":
    main()
