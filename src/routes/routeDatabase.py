from click import echo
from flask import Blueprint, jsonify,request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from models.modMaquina import creaTabla as maquinaCreaTabla
from models.modMaquina import cargaDatos as maquinaCargaDatos
from models.modConteo import creaTabla as conteoCreaTabla
from models.modParoMaquina import creaTabla as paroMaquinaCreaTabla

routeDatabase = Blueprint('routeDatabase', __name__)

@routeDatabase.route("/database.prepara", methods=['GET'])
def databasePrepara():
    jsonResponse = ""

    maquinaCreaTabla()
    maquinaCargaDatos()
    
    conteoCreaTabla()
    paroMaquinaCreaTabla()

    jsonResponse = {"success": "success", 
        "mensaje": "Preparacion de la Base de Datos realizada."
        }
    return jsonify(jsonResponse)    