from flask import Flask, render_template
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from flask_sqlalchemy import SQLAlchemy ##para hacer nuestra persistencia

app=Flask(__name__)
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2022@localhost/flasksql'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from Controladores.ControladorEstudiante import ControladorEstudiante
miControladorEstudiante=ControladorEstudiante()

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

@app.route("/estudiantes",methods=['GET'])
def getEstudiantes():
    json=miControladorEstudiante.index()
    return jsonify(json)

@app.route("/estudiantes",methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json=miControladorEstudiante.create(data)
    return jsonify(json)

@app.route("/estudiantes/<string:id>",methods=['GET'])
def getEstudiante(id):
    json=miControladorEstudiante.show(id)
    return jsonify(json)

@app.route("/estudiantes/<string:id>",methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json=miControladorEstudiante.update(id,data)
    return jsonify(json)

@app.route("/estudiantes/<string:id>",methods=['DELETE'])
def eliminarEstudiante(id):
    json=miControladorEstudiante.delete(id)
    return jsonify(json)

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])


