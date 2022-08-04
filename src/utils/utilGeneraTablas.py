from models.importFile import *
from models.modDbConecta import dbEngine

def generaTablas():
    dbEngine = dbEngine()
    # ECRC: Instanciando la Base de Datos
    dbBase = declarative_base()

    dbBase.metadata.drop_all(dbEngine)
    dbBase.metadata.create_all(dbEngine)      



