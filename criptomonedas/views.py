from wtforms.fields.core import FloatField
import criptomonedas
from criptomonedas.forms import Estado, MovimientosForm
from flask import Flask
import sqlite3
from criptomonedas import app
from flask_wtf import form
from flask import jsonify , render_template ,request,redirect,url_for,flash
from criptomonedas.forms import  MovimientosForm
from datetime import date
from criptomonedas.dataaccess import *
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from criptomonedas.api import *


dbManager = DBmanager()

@app.route("/")
def index():
    query = "SELECT * FROM criptomonedas WHERE 1 = 1;"
    parametros = []
    resultado = dbManager.consultaMuchasSQL(query, parametros)
    
    if not resultado:
            flash("NO SE HA ENCONTRADO NINGUN MOVIMIENTO", "error")
            return render_template('movimientos.html' , datos = resultado)
        
    return render_template('movimientos.html' , datos = resultado)

@app.route("/purchase", methods=["GET","POST"])
def nuevo():
    formulario = MovimientosForm()
    query = "SELECT * FROM criptomonedas WHERE 1 = 1;"
    parametros = []
    resultado = dbManager.consultaMuchasSQL(query,parametros)

    listaMonedas = ['EUR','ETH','LTC','BNB','EOS','XLM','BTC','XRP','BCH','USDT','BSV','ADA','TRX']
    cantidadMonedasAtrapadas = {"EUR":0,"ETH":0,"LTC":0,"BNB":0,"EOS":0,"XLM":0,"BTC":0,"XRP":0,"BCH":0,"USDT":0,"BSV":0,"ADA":0,"TRX":0}
    cantidadMonedasUsadas = {"EUR":0,"ETH":0,"LTC":0,"BNB":0,"EOS":0,"XLM":0,"BTC":0,"XRP":0,"BCH":0,"USDT":0,"BSV":0,"ADA":0,"TRX":0}

    
       
    if request.method==["GET"]:
        return render_template("calcular.html",form=formulario)

    elif formulario.cantidad_from.data == None:
        flash("La cantidad que quiere calcular debe ser introducida en números")
        return render_template("purchase.html", form = formulario)


    elif  not resultado:
        while formulario.moneda_from.data != 'EUR' :
            flash("LA PRIMERA COMPRA TIENE QUE SER DE EUROS('EUR') A UNA CRIPTOMONEDA , GRACIAS.","error")
            return render_template("purchase.html", form = formulario)
    

                  
        else:
            
            if formulario.validate():
                               
                api.apiConversor()
                
                formulario.cantidad_to = api.apiConversor()
                    
                query = "INSERT INTO criptomonedas (date , time ,moneda_from, cantidad_from, moneda_to, cantidad_to) VALUES (?,?,?,?,?,?)"
                
                if "calculadora" in request.form:
                    try:
                        if formulario.moneda_from.data == formulario.moneda_to.data:
                            flash("LA MONEDA FROM Y LA MONEDA TO NO PUEDEN SER IGUALES")
                            return render_template("purchase.html", form = formulario)
                       
                        else:
                            dbManager.consultaMuchasSQL(query,[formulario.date.data, formulario.time.data, formulario.moneda_from.data, formulario.cantidad_from.data, formulario.moneda_to.data, formulario.cantidad_to])

                    except sqlite3.Error as el_error:
                        print("Se ha producido un error en SQLITE3",el_error)
                        flash("Se ha producido un error en la base de datos. Pruebe en unos minutos", "error")
                        return render_template("purchase.html" , form= formulario)

                    return render_template("compra.html", form = formulario)

                elif "submit" in request.form:

                    try:

                        dbManager.modificaTablaSQL(query,[formulario.date.data, formulario.time.data, formulario.moneda_from.data, formulario.cantidad_from.data, formulario.moneda_to.data, formulario.cantidad_to])

                    except sqlite3.Error as el_error:
                        print("Se ha producido un error en SQLITE3",el_error)
                        flash("Se ha producido un error en la base de datos. Pruebe en unos minutos", "error")
                        return render_template("purchase.html" , form= formulario)

                    return redirect(url_for("index"))
                

    else:
        if formulario.validate():
            if formulario.moneda_from.data == 'EUR':

                if formulario.validate():
                
                    
                    api.apiConversor()
                    
                    formulario.cantidad_to = api.apiConversor()
                    

                    query = "INSERT INTO criptomonedas (date , time ,moneda_from, cantidad_from, moneda_to, cantidad_to) VALUES (?,?,?,?,?,?)"
                    
                    if "calculadora" in request.form:
                        try:
                            if formulario.moneda_from.data == formulario.moneda_to.data:
                                flash("LA MONEDA FROM Y LA MONEDA TO NO PUEDEN SER IGUALES")
                                return render_template("purchase.html", form = formulario)
                            
                            else:
                                dbManager.consultaMuchasSQL(query,[formulario.date.data, formulario.time.data, formulario.moneda_from.data, formulario.cantidad_from.data, formulario.moneda_to.data, formulario.cantidad_to])

                        except sqlite3.Error as el_error:
                            print("Se ha producido un error en SQLITE3",el_error)
                            flash("Se ha producido un error en la base de datos. Pruebe en unos minutos", "error")
                            return render_template("purchase.html" , form= formulario)

                        return render_template("compra.html", form = formulario)

                    elif "submit" in request.form:

                        try:

                            dbManager.modificaTablaSQL(query,[formulario.date.data, formulario.time.data, formulario.moneda_from.data, formulario.cantidad_from.data, formulario.moneda_to.data, formulario.cantidad_to])

                        except sqlite3.Error as el_error:
                            print("Se ha producido un error en SQLITE3",el_error)
                            flash("Se ha producido un error en la base de datos. Pruebe en unos minutos", "error")
                            return render_template("purchase.html" , form= formulario)

                        return redirect(url_for("index"))
                    
            else:
                
                if formulario.validate():
                
                    for m in listaMonedas:
                        for r in resultado:
                            if r['moneda_from'] == m:
                                c = r['moneda_from']
                                cantidadMonedasUsadas[c] += r['cantidad_from']
                            elif r['moneda_to'] == m:
                                c1 = r['moneda_to']
                                cantidadMonedasAtrapadas[c1] += r['cantidad_to']

                    if str(cantidadMonedasUsadas[formulario.moneda_from.data]) == '0':
                        cantidadMonedasAtrapadas[formulario.moneda_from.data] -= cantidadMonedasUsadas[formulario.moneda_from.data]

                         
                        
                    else:                              
                        cantidadMonedasAtrapadas[formulario.moneda_from.data] -= cantidadMonedasUsadas[formulario.moneda_from.data]       
                        cantidadMonedasAtrapadas[formulario.moneda_from.data] -= formulario.cantidad_from.data

                    cm = str(cantidadMonedasAtrapadas[formulario.moneda_from.data])
                    cf = str(formulario.cantidad_from.data)         

                if cf > cm:
                    flash("No tienes suficiente saldo")
                    return render_template("purchase.html", form = formulario)

                else:
                    api.apiConversor()
                    
                    formulario.cantidad_to = api.apiConversor()
                    

                    query = "INSERT INTO criptomonedas (date , time ,moneda_from, cantidad_from, moneda_to, cantidad_to) VALUES (?,?,?,?,?,?)"
                    
                    if "calculadora" in request.form:
                        try:
                            if formulario.moneda_from.data == formulario.moneda_to.data:
                                flash("LA MONEDA FROM Y LA MONEDA TO NO PUEDEN SER IGUALES")
                                return render_template("purchase.html", form = formulario)
                            
                            else:
                                dbManager.consultaMuchasSQL(query,[formulario.date.data, formulario.time.data, formulario.moneda_from.data, formulario.cantidad_from.data, formulario.moneda_to.data, formulario.cantidad_to])

                        except sqlite3.Error as el_error:
                            print("Se ha producido un error en SQLITE3",el_error)
                            flash("Se ha producido un error en la base de datos. Pruebe en unos minutos", "error")
                            return render_template("purchase.html" , form= formulario)

                        return render_template("compra.html", form = formulario)

                    elif "submit" in request.form :

                        try:

                            dbManager.modificaTablaSQL(query,[formulario.date.data, formulario.time.data, formulario.moneda_from.data, formulario.cantidad_from.data, formulario.moneda_to.data, formulario.cantidad_to])

                        except sqlite3.Error as el_error:
                            print("Se ha producido un error en SQLITE3",el_error)
                            flash("Se ha producido un error en la base de datos. Pruebe en unos minutos", "error")
                            return render_template("purchase.html" , form= formulario)

                        return redirect(url_for("index"))
                    
          
    return render_template("purchase.html",form = formulario)


        

@app.route("/status", methods = ["GET"])
def estado():
    status = Estado()
    query = "SELECT * FROM criptomonedas WHERE 1 = 1;"
    parametros = []
    resultado = dbManager.consultaMuchasSQL(query,parametros)

    cantidadMonedasInvertidasEUR = {"EUR":0}
    cantidadMonedasRecuperadasEUR = {"EUR":0}
    saldodeeurosinvertidos ={"EUR":0}

    
    for r in resultado:
        if r['moneda_from'] == 'EUR':
            c = r['moneda_from']
            cantidadMonedasInvertidasEUR[c] += r['cantidad_from']
        elif r['moneda_to'] == 'EUR':
            c1 = r['moneda_to']
            cantidadMonedasRecuperadasEUR[c1] += r['cantidad_to']

    saldodeeurosinvertidos['EUR'] = cantidadMonedasRecuperadasEUR['EUR'] - cantidadMonedasInvertidasEUR['EUR']
    si = saldodeeurosinvertidos['EUR']  #Saldo de EUROS Invertidos cantidad_to - cantidad_from
    invertido = cantidadMonedasInvertidasEUR['EUR']

    status.invertido = invertido

    listaMonedas = ['EUR','ETH','LTC','BNB','EOS','XLM','BTC','XRP','BCH','USDT','BSV','ADA','TRX']
    cantidadMonedasAtrapadas = {"EUR":0,"ETH":0,"LTC":0,"BNB":0,"EOS":0,"XLM":0,"BTC":0,"XRP":0,"BCH":0,"USDT":0,"BSV":0,"ADA":0,"TRX":0}
    cantidadMonedasUsadas = {"EUR":0,"ETH":0,"LTC":0,"BNB":0,"EOS":0,"XLM":0,"BTC":0,"XRP":0,"BCH":0,"USDT":0,"BSV":0,"ADA":0,"TRX":0}
    cantidadMonedasRestantes = {}
    contador = 0

    for m in listaMonedas: #OBTENEMOS CANTIDADES DE AMBOS DICC TANTO CANTIDADES_FROM COMO CANTIDADES_TO
        for r in resultado:
            if r['moneda_from'] == m:
                c = r['moneda_from']
                cantidadMonedasUsadas[c] += r['cantidad_from']
            elif r['moneda_to'] == m:
                c1 = r['moneda_to']
                cantidadMonedasAtrapadas[c1] += r['cantidad_to']

    for c,a in cantidadMonedasAtrapadas.items():
        cantidadMonedasRestantes[c] = a - cantidadMonedasUsadas.get(c, 0)  # RESTAMOS AMBOS DICC Y LO GUARDAMOS EN UN DICCIONARIO VACIO (CANTIDADESMONEDASRESTANTES)

    for r,t in cantidadMonedasRestantes.items():
    
        if r != 'EUR' and t != 0 :

            simbolo = r
            cantidad =  t           
            convertidor = 'EUR'

            url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'
            parameters = {
            'amount':cantidad,
            'symbol':simbolo,
            'convert':convertidor
            }
            headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '12b83118-8f46-4644-9093-1490b0ea6521',
                }

            session = Session()
            session.headers.update(headers)
            response = session.get(url, params=parameters)
            print(parameters)
            consulta = json.loads(response.text)

            conversor = consulta['data']['quote'][convertidor]['price']
            
            print(conversor)
            
            contador += conversor
            print(contador)

            valorCriptos = contador
    

    valorActualFinal = invertido + si + valorCriptos

    

    status.valoractual = valorActualFinal          
            

    return render_template("status.html",sta = status)



 