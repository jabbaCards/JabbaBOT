import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# URL da Versão 14 (API Oficial)
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbw7NrVt1ewCOCaSaVWMCDqMoWTnKJSRSg-yMqY80X8nAf4lMf5qrBxjzUVPBQStfM6J/exec"

def main():
    try:
        # Chamada direta para o seu Script que agora consulta a API do ML
        resposta = requests.get(f"{URL_DO_GOOGLE}?q=pokemon", timeout=30)
        dados = resposta.json()
        
        # Estrutura de dados vinda da API oficial
        titulo = dados.get('titulo', 'Sem título')
        preco = dados.get('preco', '0')
        link = dados.get('link', 'N/A')
        
        mensagem = (
            f"🚀 *JABBABOT ATIVO (Versão 14)* 🚀\n\n"
            f"📦 {titulo}\n"
            f"💰 {preco}\n"
            f"🔗 {link}"
        )
        
        # Envio para o Telegram
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": mensagem})
        
        print("✅ Sucesso! Dados da API oficial entregues.")
        
    except Exception as e:
        print(f"❌ Erro na integração: {e}")

if __name__ == "__main__":
    main()
