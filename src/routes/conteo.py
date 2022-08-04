import sys
from flask import Blueprint, jsonify, request

conteo = Blueprint('conteo', __name__)

@conteo.route("/conteo")
def home():
    return jsonify({"response": "conteoxs"})

@conteo.route('/conteo', methods=['POST'])
def fnConteo():
    args = request.args
    print (args.get("cod_maquina"))
    print ("Cosa de Debig")
    sys.stdout.flush()
    return jsonify(args)
    #return jsonify({"response": "Conteo posteado d"})