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
       
    if request.method==["GET"]:
        return render_template("calcular.html",form=formulario)

    if  not resultado:
        while formulario.moneda_from.data != 'EUR' and formulario.moneda_to.data != 'BTC':
            flash("LA PRIMERA COMPRA TIENE QUE SER DE EUROS('EUR') A BITCOIN('BTC') , GRACIAS.","error")
            return render_template("purchase.html", form = formulario)
                  
        else:
            
            if formulario.validate():

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
                'X-CMC_PRO_API_KEY': '12b83118-8f46-4644-9093-1490b0ea6521',
                    }

                session = Session()
                session.headers.update(headers)
                response = session.get(url, params=parameters)
                print(parameters)
                consulta = json.loads(response.text)

                conversor = consulta['data']['quote'][convertidor]['price']
                formulario.cantidad_to = conversor
                query = "INSERT INTO criptomonedas (date , time ,moneda_from, cantidad_from, moneda_to, cantidad_to) VALUES (?,?,?,?,?,?)"
                
                if "calculadora" in request.form:
                    try:

                        dbManager.consultaMuchasSQL(query,[formulario.date.data, formulario.time.data, formulario.moneda_from.data, formulario.cantidad_from.data, formulario.moneda_to.data, formulario.cantidad_to])

                    except sqlite3.Error as el_error:
                        print("Se ha producido un error en SQLITE3",el_error)
                        flash("Se ha producido un error en la base de datos. Pruebe en unos minutos", "error")
                        return render_template("purchase.html" , form= formulario)

                    return render_template("purchase.html", form = formulario)

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
                'X-CMC_PRO_API_KEY': '12b83118-8f46-4644-9093-1490b0ea6521',
                    }

                session = Session()
                session.headers.update(headers)
                response = session.get(url, params=parameters)
                print(parameters)
                consulta = json.loads(response.text)

                conversor = consulta['data']['quote'][convertidor]['price']
                formulario.cantidad_to = conversor
                query = "INSERT INTO criptomonedas (date , time ,moneda_from, cantidad_from, moneda_to, cantidad_to) VALUES (?,?,?,?,?,?)"
                
                if "calculadora" in request.form:
                    try:

                        dbManager.consultaMuchasSQL(query,[formulario.date.data, formulario.time.data, formulario.moneda_from.data, formulario.cantidad_from.data, formulario.moneda_to.data, formulario.cantidad_to])

                    except sqlite3.Error as el_error:
                        print("Se ha producido un error en SQLITE3",el_error)
                        flash("Se ha producido un error en la base de datos. Pruebe en unos minutos", "error")
                        return render_template("purchase.html" , form= formulario)

                    return render_template("purchase.html", form = formulario)

                elif "submit" in request.form:

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

    return render_template("status.html",sta = status)



 