import os
import requests

# As chaves do seu bot devem estar configuradas no GitHub Secrets
TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# URL do seu Túnel Google (Versão 4, com User-Agent de navegador)
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbwZ3KvyM2TSJazfqCoSyAgASQYhMYTsRCV0Tlr55c_q6A_Th0tjIt4GCzgSimYjRjI/exec"

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": texto})

def buscar_oferta():
    try:
        # Buscando por 'iphone' para confirmar que o bloqueio 'forbidden' foi superado
        url_busca = f"{URL_DO_GOOGLE}?q=iphone"
        resposta = requests.get(url_busca, timeout=20)
        
        if resposta.status_code != 200:
            return f"❌ Erro HTTP {resposta.status_code}: O Mercado Livre bloqueou o acesso."
            
        dados = resposta.json()
        
        # Verifica se a lista não está vazia
        if "results" in dados and len(dados["results"]) > 0:
            item = dados["results"][0]
            # Formata os dados
            return {
                "titulo": item["title"],
                "preco": f"{item['price']:.2f}".replace(".", ","),
                "link": item["permalink"]
            }
        
        return "⚠️ O túnel funcionou, mas a busca por 'iphone' não retornou produtos."
            
    except Exception as e:
        return f"❌ Erro na conexão: {str(e)}"

def main():
    print("🚀 Executando JabbaBOT v4...")
    resultado = buscar_oferta()
    
    if isinstance(resultado, dict):
        mensagem = f"""🔥 *OFERTA ENCONTRADA (JabbaBOT v4)* 🔥

📦 {resultado['titulo']}
💰 R$ {resultado['preco']}

🔗 {resultado['link']}

✅ *Status:* Túnel de acesso livre!"""
        enviar_mensagem(mensagem)
        print("✅ Sucesso! Mensagem enviada para o Telegram.")
    else:
        # Caso ocorra erro ou lista vazia, envia para o Telegram
        enviar_mensagem(f"🔍 Debug JabbaBOT: {resultado}")
        print("Aviso enviado.")

if __name__ == "__main__":
    main()
