from config.configuration import collection

<<<<<<< HEAD
def insertamensaje(escena, personaje, frase):
    dict_insert = {"scene": f"{escena}",
                   "character_name": f"{personaje}",
                   "dialogue": f"{frase}"
    }
    collection.insert_one(dict_insert)
=======

def insertamensaje(escena,personaje,frase):
    dict_insert = {"scene": escena,
    "character_name": personaje,
    "dialogue": frase 
    }
    collection.insert_one(dict_insert)
    
>>>>>>> 3bf1e634a7606046587b6b1758dd1af3c7b3759f
