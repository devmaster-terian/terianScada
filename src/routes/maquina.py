from flask import Blueprint, jsonify

maquina = Blueprint('maquina', __name__)


@maquina.route("/maquina")
def home():
    return jsonify({"response": "maquina"})
