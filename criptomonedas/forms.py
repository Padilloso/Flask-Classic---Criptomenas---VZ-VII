from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import DateField
from wtforms.fields.core import BooleanField, FloatField, SelectField, StringField,TimeField
from wtforms.fields.simple import HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from datetime import date, datetime
from criptomonedas.dataaccess import *





def today():
    hoy = datetime.today().strftime('%d/%m/%Y')
    return(hoy)

def clock():
    reloj = datetime.now().strftime("%H:%M:%S")
    return(reloj)



class MovimientosForm(FlaskForm):
    id = HiddenField()
    date = StringField("Fecha",default=today())
    time = StringField("Hora",default=clock())
    moneda_from = SelectField("Tipo de moneda", choices=[("EUR"),("ETH"),("LTC"),("BNB"),("EOS"),("XLM"),("BTC"),("XRP"),("BCH"),("USDT"),("BSV"),("ADA"),("TRX")],validators=[DataRequired()])
    cantidad_from = FloatField("Cantidad",validators=[DataRequired()])
    moneda_to = SelectField("Tipo de moneda", choices=[("EUR"),("ETH"),("LTC"),("BNB"),("EOS"),("XLM"),("BTC"),("XRP"),("BCH"),("USDT"),("BSV"),("ADA"),("TRX")],validators=[DataRequired()])
    cantidad_to = StringField("Cantidad")
    precioUnidad = StringField("Precio Unidad")
    submit = SubmitField("Aceptar")
    calculadora = SubmitField("Calcular")
    monedero = StringField("Monedero")


class Estado(FlaskForm):
    invertido = FloatField()
    valoractual = FloatField()


class Monedero(FlaskForm):
    moneda1= StringField()
    moneda2 = StringField() 
    moneda3 = StringField()
    moneda4 = StringField()
    moneda5 = StringField() 
    moneda6 = StringField()
    moneda7 = StringField()
    moneda8 = StringField()
    moneda9 = StringField()
    moneda10 = StringField()
    moneda11 = StringField()
    moneda12 = StringField()
    moneda13= StringField() 