# app-py - Programa donde se indican las Rutas del Servidor
from flask import Flask, jsonify
from dataUsers import dataUsers
from routes.maquina import maquina #Importando las Funciones de Maquina
app = Flask(__name__)

app.register_blueprint(maquina) #Habilitando la Ruta de Maquina

#Rutas propias de la Sesion
@app.route('/', methods=['GET'])
def root():
    return jsonify({"response": "TERIAN - Access Granted (Docker Up)"})


@app.route('/conteo', methods=['GET'])
def conteo():
    return jsonify({"response": "Conteo"})


@app.route('/users', methods=['GET'])
def userHandler():
    return jsonify({"users": dataUsers})

