import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# URL atualizada com a lógica de captura dupla
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbwdaFV36HYwT0yus7xRYpnL3J-F_74M9SR4d-Kh1X1x5gP5p9pXx0gPK1BqCR28o_Iw/exec"

def main():
    try:
        # Chamada ao script do Google
        resposta = requests.get(f"{URL_DO_GOOGLE}?q=pokemon", timeout=30)
        dados = resposta.json()
        
        titulo = dados.get('titulo', 'Produto não capturado')
        preco = dados.get('preco', '0')
        link = dados.get('link', 'Sem link')
        
        # Montagem da mensagem para o Telegram
        mensagem = (
            f"🚀 *JABBABOT ATIVO*\n\n"
            f"📦 {titulo}\n"
            f"💰 {preco}\n"
            f"🔗 {link}"
        )
        
        # Envio para o Telegram
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": mensagem})
        
        print("✅ Execução finalizada. Verifique o Telegram.")
        
    except Exception as e:
        print(f"❌ Erro na execução: {e}")

if __name__ == "__main__":
    main()
