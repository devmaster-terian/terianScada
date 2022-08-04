# app-py - Programa donde se indican las Rutas del Servidor
from flask import Flask, jsonify, request
from dataUsers import dataUsers
from routes.routeMaquina   import routeMaquina   #Importando las Funciones de Maquina
from routes.conteo         import conteo         #Importando las Funciones de Conteo
from routes.routeDatabase  import routeDatabase  #Importando las Funciones de Conteo

app = Flask(__name__)

app.register_blueprint(routeMaquina)  #Habilitando la Ruta de Maquina
app.register_blueprint(routeDatabase) #Habilitando la Ruta de Maquina
app.register_blueprint(conteo)        #Habilitando la Ruta de Conteo

#Rutas propias de la Sesion
@app.route('/', methods=['GET'])
def root():
    return jsonify({"response": "TERIAN - Access Granted (Docker Up - Local)"})


@app.route('/conteox', methods=['GET'])
def conteo():
    args = request.args
    return jsonify({"response": "Conteo"})


@app.route('/users', methods=['GET'])
def userHandler():
    return jsonify({"users": dataUsers})

