from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from Models.db import db
from Models.Cliente import Cliente
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

# Crear vengador
@app.route('/vengador', methods=['POST'])
def crear_cliente():
    data = request.json
    nuevo = Vengador(nombre=data['nombre'], alias=data['alias'], habilidades=data['habilidades'] actor=data['actor'])
    db.session.add(nuevo)
    db.session.commit()
    return jsonify(nuevo.serialize()), 201

# Obtener todos
@app.route('/Vengador', methods=['GET'])
def obtener_Vengador():
    Vengador = Vengador.query.all()
    return jsonify([c.serialize() for c in Vengador])

# Obtener uno
@app.route('/Vengador/<int:id>', methods=['GET'])
def obtener_cliente(id):
    Vengador = Vengador.query.get_or_404(id)
    return jsonify(Vengador.serialize())

# Actualizar
@app.route('/Vengador/<int:id>', methods=['PUT'])
def actualizar_Vengador(id):
    Vengador = Vengador.query.get_or_404(id)
    data = request.json
    Vengador.nombre = data.get('nombre', Vengador.nombre)
    Vengador.alias = data.get('telefono', Vengador.alias)
    Vengador.habilidades = data.get('habilidades', Vengador.habilidad)
    Vengador.actor = data.get('actor', Vengador.actor)
    db.session.commit()
    return jsonify(Vengador.serialize())

# Eliminar
@app.route('/Vengador/<int:id>', methods=['DELETE'])
def eliminar_Vengador(id):
    Vengador = Vengador.query.get_or_404(id)
    db.session.delete(Vengador)
    db.session.commit()
    return jsonify({'mensaje': 'Vengador eliminado'})

if __name__ == '__main__':
    app.run(debug=True)
# ---------------------------Vengador-Crud-------------------------------------------