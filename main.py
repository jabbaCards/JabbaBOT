import os
import requests

# As chaves do seu bot devem estar configuradas no GitHub Secrets
TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# URL da Versão 5 (Última tentativa via Script)
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbytP5p5DaUxjQS7Z0SHuLFCNwjj729SbCupSwriTuQ7lZ6AEkvXJbTqjDfdk3YKKogq/exec"

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": texto})

def buscar_oferta():
    try:
        # Busca usando a nova versão do script
        url_busca = f"{URL_DO_GOOGLE}?q=pokemon"
        resposta = requests.get(url_busca, timeout=20)
        
        if resposta.status_code != 200:
            return f"❌ Erro HTTP {resposta.status_code}."
            
        dados = resposta.json()
        
        # Verifica a estrutura da resposta do Mercado Livre
        if isinstance(dados, dict) and "results" in dados and len(dados["results"]) > 0:
            item = dados["results"][0]
            return {
                "titulo": item["title"],
                "preco": f"{item['price']:.2f}".replace(".", ","),
                "link": item["permalink"]
            }
        
        # Se chegar aqui, o JSON veio, mas os resultados estão vazios
        return f"⚠️ JSON recebido, mas vazio: {str(dados)[:100]}"
            
    except Exception as e:
        return f"❌ Erro: {str(e)}"

def main():
    print("🚀 Iniciando JabbaBOT v5...")
    resultado = buscar_oferta()
    
    if isinstance(resultado, dict):
        mensagem = f"🔥 *OFERTA ENCONTRADA!*\n\n📦 {resultado['titulo']}\n💰 R$ {resultado['preco']}\n🔗 {resultado['link']}"
        enviar_mensagem(mensagem)
    else:
        enviar_mensagem(f"🔍 Debug JabbaBOT: {resultado}")

if __name__ == "__main__":
    main()
