#Michelle Sánchez Guerrero
#Ejercicio 1. Tipo GET

import requests
from flask import Flask, request
import json

app = Flask(__name__)

def crearDatos(ciudad):
    clima = {
        "ciudad": ciudad ,
        "temperatura": "" ,
        "horaActual": ""
    }

    urlClima = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=9415e20dfaa5ebed28de8ba01d9ad5c6'
    urlTiempo = 'https://www.amdoren.com/api/timezone.php?api_key=w5bNb7bKythWGBbcyXtSPfEwah9K3F&loc=' + ciudad

    requestClima = requests.get(urlClima.format(ciudad)).json()
    requestTiempo = requests.get(urlTiempo).json()

    temperatura = requestClima['main']['temp']
    clima["temperatura"] = temperatura
    tiempo = requestTiempo['time']
    hora = tiempo[11:16]
    clima["horaActual"] = hora
    clima = json.dumps(clima, indent=4)

    return clima


@app.route('/clima')
def data():

    ciudad = request.args.get('ciudad')
    ciudad = str(ciudad)
    ciudad = ciudad.capitalize()

    datos = crearDatos(ciudad)

    return datos, 200


if __name__ == '__main__':
    app.run()
