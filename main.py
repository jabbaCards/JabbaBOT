import os
import requests

# As chaves do seu bot devem estar configuradas no GitHub Secrets
TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# URL da Versão 8 (Atualizada)
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbykJdkqE9HT7eOfUa5Xx7-IjQqgNpbReBectz_ePXl2fxexSb1hXlQssnx_zTKu0ZVi/exec"

def main():
    try:
        # Busca os dados processados pelo seu Script
        resposta = requests.get(f"{URL_DO_GOOGLE}?q=pokemon", timeout=30)
        dados = resposta.json()
        
        # Extrai título e preço
        titulo = dados.get('titulo', 'Sem título')
        preco = dados.get('preco', '0')
        
        # Prepara a mensagem para o Telegram
        mensagem = f"🔥 *JABBABOT ATIVO (Versão 8)* 🔥\n\n📦 {titulo}\n💰 R$ {preco}\n\n✅ *Status:* Conectado com sucesso!"
        
        # Envia para o Telegram
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": mensagem})
        
        print("✅ Sucesso! Mensagem enviada para o Telegram.")
        
    except Exception as e:
        erro = f"❌ Erro ao executar o JabbaBOT: {e}"
        print(erro)
        # Opcional: tenta enviar o erro para o Telegram para você saber o que houve
        try:
            requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                          json={"chat_id": CHAT_ID, "text": erro})
        except:
            pass

if __name__ == "__main__":
    main()
