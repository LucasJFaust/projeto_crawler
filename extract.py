import requests # type: ignore

url = "https://www.mercadolivre.com.br/ofertas?container_id=MLB779362-9#origin=scut&filter_position=1&is_recommended_domain=false"

# Agora vamos buscar o dado na url:

data = requests.get(url).text

# Agora vamos criar um arquivo html para salvar a indexação que o crawler vai fazer dos links das páginas

with open('mercadolivre.html', 'w', encoding = 'utf-8') as f:
    f.write()

# Retorna titulos dos produtos nas tags

def get_itens_title(doc):
    title_tags = doc.find_all('p', class_ = 'promotion-item_title')
    titles = []
    for tags in title_tags:
        titles.append(tags.text)

    return titles

# Retorna preços dos prosutos

def get_itens_price(doc):
    price_tags = doc.find_all('p', class_ = 'promotion-item_title')
    prices = []
    for tags in price_tags_tags:
        prices.append(tags.text)

    return prices