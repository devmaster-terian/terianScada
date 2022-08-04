from models.importFile import *

# ECRC: Instanciando la Base de Datos
dbBase = declarative_base()

# ECRC: Creando el modelo de la Tabla
@dataclass
class movParoMaquina(dbBase):
    __tablename__ = 'movParoMaquina'

    rowid: int = Column(Integer(), primary_key=True)
    cod_maquina: str = Column(String(24), nullable=False, unique=True)
    dt_inicio: datetime = Column(DateTime(), default=datetime.now())
    dt_termino: datetime = Column(DateTime(), default=datetime.now())
    dt_duracion: datetime = Column(DateTime(), default=datetime.now())
    motivo_paro: str = Column(String(64))
    created_at: datetime = Column(DateTime(), default=datetime.now())
    created_by: str = Column(String(64), nullable=False)
    updated_at: datetime = Column(DateTime())
    updated_by: str = Column(String(64))

    def __str__(self):
        return self.cod_maquina

def creaTabla():
    dbEngine = create_engine('postgresql://root:root@postgres/terian-scada', echo=True) #Se utiliza el nombre de la Imagen en docker-compose como HOST
    dbBase.metadata.drop_all(dbEngine)
    dbBase.metadata.create_all(dbEngine)   