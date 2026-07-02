import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# URL atualizada com a lógica de link direto para Pokemon TCG
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbxJjXKM7BoeRu7gJVlo1MpzZ6wQuQGfKBUjVseKctjZd1ilthNLo4_V8ykKovk6H6PM/exec"

def main():
    try:
        # Chamada ao script. Não precisa de parâmetro pois já fixamos "pokemon tcg" no Google Script
        resposta = requests.get(URL_DO_GOOGLE, timeout=30)
        dados = resposta.json()
        
        titulo = dados.get('titulo', 'Produto não capturado')
        preco = dados.get('preco', '0')
        link = dados.get('link', 'Sem link')
        
        # Mensagem formatada
        mensagem = (
            f"🚀 *JABBABOT ATIVO (TCG Mode)*\n\n"
            f"📦 {titulo}\n"
            f"💰 {preco}\n"
            f"🔗 {link}"
        )
        
        # Envio para o Telegram
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": mensagem})
        
        print("✅ Execução finalizada com sucesso.")
        
    except Exception as e:
        print(f"❌ Erro na execução: {e}")

if __name__ == "__main__":
    main()
