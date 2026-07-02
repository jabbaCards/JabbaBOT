import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbykJdkqE9HT7eOfUa5Xx7-IjQqgNpbReBectz_ePXl2fxexSb1hXlQssnx_zTKu0ZVi/exec"

def main():
    try:
        # Pega a resposta como texto bruto primeiro
        resposta = requests.get(f"{URL_DO_GOOGLE}?q=pokemon", timeout=30)
        
        # Se a resposta for 200 OK, tentamos ver o que tem dentro
        print(f"Status da resposta: {resposta.status_code}")
        print(f"Conteúdo da resposta: {resposta.text[:500]}") # Mostra os primeiros 500 caracteres
        
        # Tenta converter para JSON
        dados = resposta.json()
        mensagem = f"📦 {dados.get('titulo')}\n💰 R$ {dados.get('preco')}"
        
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": mensagem})
        
    except Exception as e:
        # Se falhar, envia o erro E o começo da resposta para o Telegram
        erro_msg = f"❌ Erro: {str(e)}\n\nResposta bruta do Google:\n{resposta.text[:300]}"
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": erro_msg})
        print(erro_msg)

if __name__ == "__main__":
    main()
