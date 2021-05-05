import os
import dotenv
import sqlalchemy as alch

dotenv.load_dotenv()


passw = os.getenv("pass_sql")
dbName= "HP"

<<<<<<< HEAD
#Me conecto con la base de datos

connectionData=f"mysql+pymysql://root:{passw}@localhost/{dbName}"
engine = alch.create_engine(connectionData)
=======
#mE CONECTO CON LA BASE DE DATOS

connectionData=f"mysql+pymysql://root:{passw}@localhost/{dbName}"
engine = alch.create_engine(connectionData)
>>>>>>> 3bf1e634a7606046587b6b1758dd1af3c7b3759f
