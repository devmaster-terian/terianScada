import modMaquina
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ECRC: Creando la Instancia de la Base
dbEngine = create_engine('postgresql://root:root@localhost/terian-scada')
# ECRC: Instanciando la Base de Datos
dbBase = declarative_base()

Session = sessionmaker(dbEngine)
dbSession = Session()

if __name__ == '__main__':
    dbBase.metadata.drop_all(dbEngine)
    dbBase.metadata.create_all(dbEngine)
