import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# URL atualizada
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbx8aSucqKlJVvOIu5DDjykNlfBPyWYdeU6-HLEeloV1mU3a2BVrrUlQPPHHyaAVpQgt/exec"

def main():
    try:
        resposta = requests.get(URL_DO_GOOGLE, timeout=30)
        dados = resposta.json()
        
        titulo = dados.get('titulo', 'Produto não capturado')
        preco = dados.get('preco', '0')
        link = dados.get('link', 'Sem link')
        
        # Mensagem formatada
        mensagem = (
            f"🚀 *JABBABOT ATIVO*\n\n"
            f"📦 *Produto:* {titulo}\n"
            f"💰 *Preço:* {preco}\n\n"
            f"🔗 {link}"
        )
        
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": mensagem, "parse_mode": "Markdown"})
        
        print("✅ Execução finalizada.")
        
    except Exception as e:
        print(f"❌ Erro na execução: {e}")

if __name__ == "__main__":
    main()
