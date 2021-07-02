from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json



#cantidad = 0
#simbolos = {'EUR','ETH','LTC','BNB','EOS','XLM','TRX','BTC','XRP','BCH','USDT','BSV','ADA'}
#transformador = {'EUR','ETH','LTC','BNB','EOS','XLM','TRX','BTC','XRP','BCH','USDT','BSV','ADA'} 


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




  


