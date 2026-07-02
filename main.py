import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# URL da Amazon (Versão de Limpeza)
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbwhiY0w5RSlwYyrFGQtdt5WUnyePyO-0pY2N8D-2s7Vy2Y9rbq_iz3Gf7mBDlgQGmH3/exec"

def main():
    try:
        # Busca os dados processados pelo Script
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
        
        print("✅ Dados enviados com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro na execução: {e}")

if __name__ == "__main__":
    main()
