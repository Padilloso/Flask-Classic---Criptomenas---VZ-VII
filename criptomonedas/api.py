from requests import Request, Session
import json
from criptomonedas import forms
import apiKEY



class api():
  def apiConversor():

    formulario = forms.MovimientosForm()

    simbolo = formulario.moneda_from.data
    cantidad = formulario.cantidad_from.data            
    convertidor = formulario.moneda_to.data


    url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'
    parameters = {
    'amount':cantidad,
    'symbol':simbolo,
    'convert':convertidor
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': apiKEY.API_KEY,
        }

    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    print(parameters)
    consulta = json.loads(response.text)
    conversor = consulta['data']['quote'][convertidor]['price']
    formulario.cantidad_to = conversor
    print(conversor)
    return(conversor)




  def apiErrores():
    formulario = forms.MovimientosForm()

    simbolo = formulario.moneda_from.data
    cantidad = formulario.cantidad_from.data            
    convertidor = formulario.moneda_to.data


    url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'
    parameters = {
    'amount':cantidad,
    'symbol':simbolo,
    'convert':convertidor
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': apiKEY.API_KEY,
        }

    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    consulta = json.loads(response.text)
    print(parameters)
    errorKey = consulta['status']['error_code'] 
    return(errorKey)


  #def apiPrecioUnidad():

    #formulario = forms.MovimientosForm()
    #simbolo = formulario.moneda_to.data
    #convertidor = formulario.moneda_from.data

    #url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    #parameters = {
      #'symbol':simbolo,
      #'convert':convertidor
      #}
    #headers = {
     # 'Accepts': 'application/json',
      #'X-CMC_PRO_API_KEY': '12b83118-8f46-4644-9093-1490b0ea6521',
       # }

    #session = Session()
    #session.headers.update(headers)
    #response = session.get(url, params=parameters)
    #consulta = json.loads(response.text)

    #respuesta = consulta['data'][simbolo]['quote'][convertidor]['price']
    #formulario.precioUnidad = respuesta

    #print(respuesta)
    #return(respuesta)

  #def apiPrecioUnidadfalso():
    #formulario = forms.MovimientosForm()
    #simbolo = formulario.moneda_from.data
    #convertidor = formulario.moneda_to.data

    #url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    #parameters = {
     # 'symbol':simbolo,
      #'convert':convertidor
      #}
    #headers = {
     # 'Accepts': 'application/json',
      #'X-CMC_PRO_API_KEY': '12b83118-8f46-4644-9093-1490b0ea6521',
       # }

    #session = Session()
    #session.headers.update(headers)
    #response = session.get(url, params=parameters)
    #consulta = json.loads(response.text)

    #respuesta = consulta['data'][simbolo]['quote'][convertidor]['price']
    #formulario.precioUnidad = respuesta

    #print(respuesta)
    #return(respuesta)







  


