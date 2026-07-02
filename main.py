def buscar_oferta():
    headers = {"User-Agent": "Mozilla/5.0"}

    url = "https://api.mercadolibre.com/sites/MLB/search?q=pokemon%20tcg"

    r = requests.get(url, headers=headers)
    data = r.json()

    for item in data["results"]:
        titulo = item["title"].lower()
        preco = int(item["price"])
        link = item["permalink"]

        if preco > MAX_PRICE:
            continue

        if any(k in titulo for k in KEYWORDS):
            return {
                "titulo": item["title"],
                "preco": preco,
                "link": link
            }

    return None
