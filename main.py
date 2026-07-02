import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# Nova URL da Versão 15
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbys-7OsEYRlvdy4c97VnDpWD9Ehyf1qzGLZXMT2M4RZhfPDhH2ah2iQQDbjTE7nzlTE/exec"

def main():
    try:
        # Chamada com o parâmetro 'q' explícito
        resposta = requests.get(f"{URL_DO_GOOGLE}?q=pokemon", timeout=30)
        
        # Verifica se a requisição foi bem sucedida
        if resposta.status_code == 200:
            dados = resposta.json()
            
            titulo = dados.get('titulo', 'Sem título')
            preco = dados.get('preco', '0')
            link = dados.get('link', 'N/A')
            
            mensagem = (
                f"✅ *JABBABOT ATIVO*\n\n"
                f"📦 {titulo}\n"
                f"💰 {preco}\n"
                f"🔗 {link}"
            )
            
            requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                          json={"chat_id": CHAT_ID, "text": mensagem})
            print("✅ Sucesso!")
        else:
            print(f"❌ Erro HTTP: {resposta.status_code}")
            
    except Exception as e:
        print(f"❌ Erro na execução: {e}")

if __name__ == "__main__":
    main()
