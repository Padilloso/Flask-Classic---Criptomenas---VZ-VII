from requests import Request, Session
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
'symbol':'BTC',
'convert':'EUR'
}
headers = {
'Accepts': 'application/json',
'X-CMC_PRO_API_KEY': '12b83118-8f46-4644-9093-1490b0ea6521',
}

session = Session()
session.headers.update(headers)
response = session.get(url, params=parameters)
consulta = json.loads(response.text)

respuesta = consulta['data']['BTC']['quote']['EUR']['price']


print(respuesta)
    