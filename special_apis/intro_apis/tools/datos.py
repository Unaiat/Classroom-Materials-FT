<<<<<<< HEAD
from flask import Flask, request 

@app.route("/fer")
def datos_fer():
    diccionario = {"nombre": "Fer",
                   "amigos" : ["Ana", "Ras", "Sheriff", "Dobby"],
                   "edad" : 28}
    return diccionario

@app.route("/ana")
def datos_ana():
    diccionario = {"nombre": "Ana",
                   "amigos" : ["Fer", "Ras", "Sheriff", "Dobby"],
                   "edad" : 32}
    return diccionario

=======

def datosAna():
    diccionario = {"Nombre": "Ana",
    "Amigos": ["Ras", "Fer", "Sheriff", "Dobby"],
    "Edad": 32
    }
    return diccionario



def datosFer():
    diccionario = {"Nombre": "Fer",
    "Amigos": ["Ras", "Ana", "Sheriff", "Dobby"],
    "Edad": 28
    }
    return diccionario
>>>>>>> 3bf1e634a7606046587b6b1758dd1af3c7b3759f
