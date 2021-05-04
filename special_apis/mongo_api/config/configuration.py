import os 
import dotenv 
from pymongo import MongoClient

dotenv.load_dotenv()

dburl = os.getenv("URL")

print(dburl)
if not dburl:
    raise ValueError(("no tienes url mongodb"))

# Connect with the database
client = MongoClient(dburl)
db = client.get_database()
collection = db["frases"]

# If the env doesn't work put here the link. We put it in the .env so people doesn't know where we are getting our data from 

