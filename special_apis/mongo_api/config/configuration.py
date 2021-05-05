<<<<<<< HEAD
import os 
import dotenv 
=======
import os
import dotenv
>>>>>>> 3bf1e634a7606046587b6b1758dd1af3c7b3759f
from pymongo import MongoClient

dotenv.load_dotenv()

dburl = os.getenv("URL")

print(dburl)
if not dburl:
<<<<<<< HEAD
    raise ValueError(("no tienes url mongodb"))

# Connect with the database
client = MongoClient(dburl)
db = client.get_database()
collection = db["frases"]

# If the env doesn't work put here the link. We put it in the .env so people doesn't know where we are getting our data from 

=======
    raise ValueError("no tienes url mongodb")

#Vamos a conectar con la base de datos
client = MongoClient(dburl)
db = client.get_database()
collection = db["frases"]
>>>>>>> 3bf1e634a7606046587b6b1758dd1af3c7b3759f
