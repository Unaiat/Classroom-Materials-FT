from config.configuration import db, collection 

def mensajes():
    """
    This function returns the phrases made by Dumbledore
    """
    query = {"character_name": "Albus Dumbledore"}
    frases = list(collection.find(query, {"_id": 0}))
    return frases

def mensajepersonaje(personaje):
    """
    This function returns the phrases made by a character
    """
    query = {"character_name": f"{personaje}"}
    frases = list(collection.find(query, {"_id": 0}))
    return frases