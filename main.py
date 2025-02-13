# Criando uma API 
from fastapi import FastAPI, Query
import requests

app = FastAPI()

# queremos disponibilizar um recurso atraves do get, então:
@app.get('/api/hello') # 'rota' no API
def hello_World():
    '''Endpoint que exibe Hello World'''
    return {'Hello':'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):  # None = valor default    
    '''Endpoint para ver os cardápios dos restaurantes.'''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)

    if response.status_code == 200:
        dados_json =  response.json()
        if restaurante is None: # entao exiba todos os restaurantes
            return {'Dados':dados_json}

        dados_restaurante = []

        for i in dados_json:
            if i['Company'] == restaurante:            
                dados_restaurante.append({
                    'item':i['Item'],
                    'price':i['price'],
                    'description':i['description']
                })
        return {'Restaurante':restaurante, 'Cardapio':dados_restaurante}
    else:
        return {'Erro':('{} - {}').format(response.status_code, response.text)}