import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# URL da sua nova implementação (Versão 3)
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbxUjxWeSs1IwSL8TP0Ia6c2XzYzbhUeA7Kd2U3hIMJ0RUt77Z2_JjCEpHHiphO61V0I/exec"

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": texto})

def buscar_oferta_diagnostico():
    try:
        # Busca genérica para testar o túnel
        url_busca = f"{URL_DO_GOOGLE}?q=pokemon"
        resposta = requests.get(url_busca, timeout=20)
        
        # Se o status não for 200, sabemos que o script falhou
        if resposta.status_code != 200:
            return f"❌ Erro HTTP: {resposta.status_code}"
            
        dados = resposta.json()
        
        if "results" in dados and len(dados["results"]) > 0:
            item = dados["results"][0]
            return {
                "titulo": item["title"],
                "preco": f"{item['price']:.2f}".replace(".", ","),
                "link": item["permalink"]
            }
        
        return "⚠️ Túnel respondeu, mas lista de resultados veio vazia (JSON: " + str(dados)[:50] + ")"
            
    except Exception as e:
        return f"❌ Erro na conexão: {str(e)}"

def main():
    print("🚀 Teste de Diagnóstico JabbaBOT v3...")
    resultado = buscar_oferta_diagnostico()
    
    if isinstance(resultado, dict):
        mensagem = f"✅ *TÚNEL FUNCIONANDO!* \n\n📦 {resultado['titulo']}\n💰 R$ {resultado['preco']}\n🔗 {resultado['link']}"
        enviar_mensagem(mensagem)
        print("✅ Sucesso! O túnel está operante.")
    else:
        enviar_mensagem(f"🔍 Debug JabbaBOT: {resultado}")
        print("Aviso enviado.")

if __name__ == "__main__":
    main()
