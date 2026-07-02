import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# URL da Versão 9
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbwBBK4uH5H1EtUNrXtUPM_QZ4BjuaPrGastz3_oUb_OJm-Ng-7o-4LMmf_YUtnwERgI/exec"

def main():
    try:
        # Aumentamos o timeout para garantir que o script tenha tempo de buscar
        resposta = requests.get(f"{URL_DO_GOOGLE}?q=pokemon", timeout=40)
        dados = resposta.json()
        
        titulo = dados.get('titulo', 'Sem título')
        preco = dados.get('preco', '0')
        
        mensagem = f"🔥 *JABBABOT ATIVO (Versão 9)* 🔥\n\n📦 {titulo}\n💰 R$ {preco}"
        
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": mensagem})
        print("✅ Sucesso! Mensagem enviada.")
        
    except Exception as e:
        print(f"❌ Erro final: {e}")

if __name__ == "__main__":
    main()
