import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# Nova URL (Atualizada)
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbxm2n_qRnwtl0INS3TD1CUdL3H6ajttrq5rykDeGoXcNO7ELjUcmDKgA4teQYFhkqQU/exec"

def main():
    try:
        # Chamada ao seu Script
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
