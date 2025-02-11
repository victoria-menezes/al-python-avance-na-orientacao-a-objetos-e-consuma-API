import requests
import json
from pathlib import Path

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)
print(response) # 200 = sucesso, 404 = not found, etc (status codes)

if response.status_code == 200:
    dados_json =  response.json()
    dados_restaurante = {}

    for i in dados_json:
        nome_restaurante = i['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []
        
        dados_restaurante[nome_restaurante].append({
            'item':i['Item'],
            'price':i['price'],
            'description':i['description']
        })
else:
    print('Erro {}'.format(response.status_code))

base_path = Path('oo-sabor-express/requested')
base_path.mkdir(exist_ok=True)

for nome_do_restaurante, dados in dados_restaurante.items():
    arquivo_nome = '{}.json'.format(nome_do_restaurante)
    json_path = base_path / (arquivo_nome)
    # criando um arquivo
    with open(json_path, 'w') as file:
        json.dump(dados, file, indent=4)