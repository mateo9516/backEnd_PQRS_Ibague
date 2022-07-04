from flask import Blueprint, jsonify, request
from models.radicacionesModel import radicacionesModel



main = Blueprint("radicaciones_bp", __name__)

@main.route('/')
def get_radicaciones():
    try:
        pqrs = radicacionesModel.get_radicaciones()
        return jsonify(pqrs)
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
