import json, sys, os.path
from flask import Blueprint, jsonify,request
from models.modDbConecta import sessionDbEngine
from models.modMaquina import basMaquina
from data.sessionPath import sessionDataPath

routeMaquina = Blueprint('routeMaquina', __name__)

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

@routeMaquina.route("/maquina.carga", methods=['GET'])
def maquinaCarga():

    print(sys.path)

    # ECRC: Verificando si ya hay registros en la Base
    dbSession = sessionDbEngine()

    # ECRC: Cargando el archivo JSON de Datos
    jsonArchivo = os.path.join(sessionDataPath(),'dataMaquina.json')
    jsonResponse = ""
    jsonMaquina = open(jsonArchivo)
    dataJsonMaquina = json.load(jsonMaquina)

    print(dataJsonMaquina['tempMaquina'])

    tempMaquina = dataJsonMaquina['tempMaquina']
    for maquina in tempMaquina:
        print(maquina['cod-maquina'])
        

    sys.stdout.flush()

    jsonResponse = {"success": "false", 
        "mensaje": "Debe proporcionar la Direccion MAC del microcontrolador (Arduino)"
        }
    return jsonify(jsonResponse)

@routeMaquina.route("/maquina", methods=['GET'])
def maquinaLista():
    dbSession = sessionDbEngine()
    listaMaquina = dbSession.query(basMaquina).all()
    return jsonify(listaMaquina)

@routeMaquina.route("/maquina.config", methods=['GET'])
def maquinaConfig():
    jsonResponse = ""
    args = request.args

    mac_address = args.get("mac_address")
    if mac_address is None:
        jsonResponse = {"success": "false", 
        "mensaje": "Debe proporcionar la Direccion MAC del microcontrolador (Arduino)"
        }

    print (jsonResponse)
    sys.stdout.flush()

    # ECRC: En caso de Errores los regresa al Cliente
    if jsonResponse != "":
        return jsonify(jsonResponse)

    dbSession = sessionDbEngine()
    configMaquina = dbSession.query(basMaquina).filter(
        basMaquina.mac_address == mac_address
    ).first()
    return jsonify(configMaquina)
