import os
import requests

# As chaves do seu bot devem estar configuradas no GitHub Secrets
TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# URL do seu Túnel Google (Versão 4 com User-Agent de Navegador)
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbwZ3KvyM2TSJazfqCoSyAgASQYhMYTsRCV0Tlr55c_q6A_Th0tjIt4GCzgSimYjRjI/exec"

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": texto})

def buscar_oferta():
    try:
        # Busca genérica por pokemon
        url_busca = f"{URL_DO_GOOGLE}?q=pokemon"
        resposta = requests.get(url_busca, timeout=20)
        
        if resposta.status_code != 200:
            return f"❌ Erro HTTP {resposta.status_code}: O Mercado Livre bloqueou o acesso."
            
        dados = resposta.json()
        
        # Verifica se temos resultados na busca
        if "results" in dados and len(dados["results"]) > 0:
            item = dados["results"][0]
            # Formata os dados para o Telegram
            return {
                "titulo": item["title"],
                "preco": f"{item['price']:.2f}".replace(".", ","),
                "link": item["permalink"]
            }
        
        return "⚠️ O túnel respondeu, mas não encontrou produtos para 'pokemon'."
            
    except Exception as e:
        return f"❌ Erro na conexão: {str(e)}"

def main():
    print("🚀 Iniciando JabbaBOT (Versão Final)...")
    resultado = buscar_oferta()
    
    if isinstance(resultado, dict):
        mensagem = f"""🔥 *OFERTA ENCONTRADA (JabbaBOT)* 🔥

📦 {resultado['titulo']}
💰 R$ {resultado['preco']}

🔗 {resultado['link']}

💡 *Dica:* Copie o link e gere seu afiliado!"""
        enviar_mensagem(mensagem)
        print("✅ Sucesso! Mensagem enviada para o Telegram.")
    else:
        # Em caso de erro, avisa no Telegram para você saber o que houve
        enviar_mensagem(f"🔍 Debug JabbaBOT: {resultado}")
        print("Aviso enviado.")

if __name__ == "__main__":
    main()
