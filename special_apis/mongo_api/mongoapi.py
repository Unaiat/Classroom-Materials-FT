from flask import Flask, request, jsonify
import tools.getdata as get
import tools.postdata as pos
import json
import markdown

app = Flask(__name__)

@app.route("/")
def index():
    readme_file = open("Readme.md", "r")
    md_template = markdown.markdown(
        readme_file.read(), extendions=["fenced_code"]
    ) 
    return md_template

@app.route("/frases")
def frases():
    frases = get.mensajes()
    return jsonify(frases) 

@app.route("/frases/<name>")
def frasepersonaje(name):
    frases = get.mensajepersonaje(name)
    return jsonify(frases)

@app.route("/nueva/frase", methods=["POST"])
def insertamensaje():
    escena = request.form.get("scene")
    personaje = request.form.get("character_name")
    frase = request.form.get("dialogue")
    pos.insertamensaje(escena, personaje, frase)
    return "Se ha introducido el mensaje en la base de datos"












app.run(debug=True)