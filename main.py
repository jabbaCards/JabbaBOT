def buscar_oferta():
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(URL, headers=headers)

    print("STATUS PAGE:", r.status_code)
    print("TAMANHO HTML:", len(r.text))

    soup = BeautifulSoup(r.text, "lxml")

    itens = soup.select(".ui-search-result__wrapper")

    print("ITENS ENCONTRADOS:", len(itens))

    return None
