import sys
from models.importFile import *

# ECRC: Instanciando la Base de Datos
dbBase = declarative_base()

# ECRC: Creando el modelo de la Tabla
@dataclass
class basMaquina(dbBase):
    __tablename__ = 'basMaquina'

    rowid:int = Column(Integer(), primary_key=True)
    cod_maquina:str = Column(String(24), nullable=False, unique=True)
    descripcion:str = Column(String(64), nullable=False)
    mac_address:str = Column(String(64), nullable=False)
    created_at:datetime = Column(DateTime(), default=datetime.now())
    created_by:str = Column(String(64), nullable=False)
    updated_at:datetime = Column(DateTime())
    updated_by:str = Column(String(64))

    def __str__(self):
        return self.cod_maquina

def creaTabla():
    dbEngine = create_engine('postgresql://root:root@postgres/terian-scada', echo=True) #Se utiliza el nombre de la Imagen en docker-compose como HOST
    dbBase.metadata.drop_all(dbEngine)
    dbBase.metadata.create_all(dbEngine)   

def cargaDatos():
    consola("Cargando datos en basMaquina...")


