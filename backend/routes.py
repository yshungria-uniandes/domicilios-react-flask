from flask import Blueprint, jsonify, request
from models import db, Domicilio

bp = Blueprint('routes', __name__)

# Obtener todos los domicilios
@bp.route('/domicilios', methods=['GET'])
def get_domicilios():
    domicilios = Domicilio.query.all()
    return jsonify([d.to_dict() for d in domicilios])

# Crear un nuevo domicilio
@bp.route('/domicilios', methods=['POST'])
def create_domicilio():
    data = request.json
    new_domicilio = Domicilio(
        nombre=data['nombre'],
        direccion=data['direccion'],
        telefono=data['telefono']
    )
    db.session.add(new_domicilio)
    db.session.commit()
    return jsonify(new_domicilio.to_dict()), 201
