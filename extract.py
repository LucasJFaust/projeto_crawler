import requests

url = "https://www.mercadolivre.com.br/ofertas?container_id=MLB779362-9#origin=scut&filter_position=1&is_recommended_domain=false"

# Agora vamos buscar o dado na url:

data = requests.get(url).text

# Agora vamos criar um arquivo html para salvar a indexação que o crawler vai fazer dos links das páginas

with open('mercadolivre.html', 'w', encoding = 'utf-8') as f:
    f.write()