<<<<<<< HEAD
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
=======
from flask import Flask, request
import tools.datos as dat
from  tools.paraeldado import funciondado




app = Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo"


@app.route("/fer")
def datos():
    fer = dat.datosFer()
    return fer


@app.route("/ana")
def datos2():
    ana = dat.datosAna()
    return ana


@app.route("/tiraeldado")
def dado():
    return funciondado()
>>>>>>> 3bf1e634a7606046587b6b1758dd1af3c7b3759f








<<<<<<< HEAD
app.run("0.0.0.0", 5000, debug = True) # This give a IP and a port to run. This example is local. 
=======
app.run("0.0.0.0",5000, debug=True)
 
>>>>>>> 3bf1e634a7606046587b6b1758dd1af3c7b3759f
