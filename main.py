import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbzS1tT2GA0zcrgMKDSr7ev94wuXKo2cjF1d1qkfj_MYSNk9aFdNeb6BwDhRcMbQjBku/exec"

def main():
    try:
        print("🚀 Iniciando diagnóstico...")
        # Busca o conteúdo bruto
        resposta = requests.get(f"{URL_DO_GOOGLE}?q=pokemon", timeout=60)
        conteudo = resposta.text
        
        # Imprime no log do GitHub (essencial para nós)
        print(f"Resposta bruta recebida: {conteudo}")
        
        # Envia para o Telegram para vermos o erro na hora
        mensagem = f"🔍 *Diagnóstico JabbaBOT*:\n\n{conteudo[:500]}"
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": mensagem})
                      
    except Exception as e:
        erro = f"❌ Erro crítico no robô: {str(e)}"
        print(erro)
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": erro})

if __name__ == "__main__":
    main()
