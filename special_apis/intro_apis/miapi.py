from flask import Flask, request 
import tools.datos as dat
import tools.paraeldado as dado


app = Flask(__name__) # This makes it possible to have a programm running

@app.route("/")
def index():
    print(app)
    return "Hola mundo"

@app.route("/fer")
def datos_fer():
    fer = dat.datos_fer()
    return fer

@app.route("/ana")
def datos_ana():
    ana = dat.datos_ana()
    return ana

@app.route("/tiraeldado")
def dice():
    tirada = dado.funciondado()
    return tirada








app.run("0.0.0.0", 5000, debug = True) # This give a IP and a port to run. This example is local. 