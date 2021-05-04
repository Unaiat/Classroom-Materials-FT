from config.configuration import engine
import pandas as pd


def insertamensaje(escena, personaje, frase):
    engine.execute(
        f"""
        INSERT INTO frases (scene, character_name, dialogue) 
        VALUES ({escena},"{personaje}","{frase}");
       """
    )