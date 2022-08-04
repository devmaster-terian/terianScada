import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def sessionDbEngine():
    # ECRC: Creando la Instancia de la Base
    dbEngine = create_engine('postgresql://root:root@postgres/terian-scada') #Se utiliza el nombre de la Imagen en docker-compose como HOST
    Session = sessionmaker(dbEngine)
    dbSession = Session()
    return dbSession

def dbEngine():    
    dbEngine = create_engine('postgresql://root:root@postgres/terian-scada') #Se utiliza el nombre de la Imagen en docker-compose como HOST
    return dbEngine

