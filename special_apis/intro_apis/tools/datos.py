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

