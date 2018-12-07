#Michelle Sánchez Guerrero
#Ejercicio 1. Tipo POST

from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/palíndromo', methods= ['POST'])
def postear():
    listaBooleanos = []

    data = request.get_json()

    listaPalabras = data["palabras"]

    for palabra in listaPalabras:

        for char in palabra:
            if not char.isalnum():
                palabra = palabra.replace(char, "")

        palabra = palabra.lower()
        palabra = palabra.replace(" ", "")
        palabraInvertida = palabra[::-1]
        if palabra == palabraInvertida:
            listaBooleanos.append(True)
        else:
            listaBooleanos.append(False)

    resultado = json.dumps({"palindromos" : listaBooleanos}, indent=4)

    return resultado


if __name__ == '__main__':
    app.run()