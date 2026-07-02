import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# URL da sua nova implementação do Google Apps Script
URL_DO_GOOGLE = "https://script.google.com/macros/s/AKfycbzfecD82Q7D4jpwT-jsLQlsldy4-JmSiprBb_3wyEkJvNsJVx2kEbPVPdCZRQwirD4/exec"

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": texto})

def buscar_oferta_platinum():
    try:
        # Busca focada em Pokémon TCG via seu script otimizado
        url_busca = f"{URL_DO_GOOGLE}?q=pokemon+tcg"
        resposta = requests.get(url_busca, timeout=20)
        dados = resposta.json()
        
        # Filtra apenas itens de lojas oficiais (Platinum/Gold)
        if "results" in dados:
            for item in dados["results"]:
                if item.get("official_store_id") is not None:
                    return {
                        "titulo": item["title"],
                        "preco": f"{item['price']:.2f}".replace(".", ","),
                        "link": item["permalink"]
                    }
            return "⚠️ O Google acedeu, mas não encontrou resultados ativos de Lojas Oficiais (Platinum)."
        
        return "⚠️ Nenhum resultado encontrado."
            
    except Exception as e:
        return f"❌ Erro na busca: {str(e)}"

def main():
    print("🚀 A buscar ofertas Platinum via Túnel VIP...")
    resultado = buscar_oferta_platinum()
    
    if isinstance(resultado, dict):
        mensagem = f"""🔥 *ALERTA DE OPORTUNIDADE (Platinum)* 🔥

📦 {resultado['titulo']}
💰 R$ {resultado['preco']}

🔗 {resultado['link']}

💡 *Ação:* Este produto é de uma Loja Oficial. Pode postar no grupo!"""
        enviar_mensagem(mensagem)
        print("✅ Sucesso! Oferta Platinum enviada.")
    else:
        enviar_mensagem(f"🔍 Debug JabbaBOT: {resultado}")
        print("Aviso enviado.")

if __name__ == "__main__":
    main()
