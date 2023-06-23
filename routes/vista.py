from flask import Blueprint, render_template as rt, flash, redirect, url_for, request, jsonify

from models.rol_usuario import Rol_Usuario
from models.usuario import Usuario

from utils.db import db
from utils.json import model_to_dict

bp = Blueprint('vista',__name__, url_prefix="/vista")

@bp.route('/')
def vista():
    rol_usuario = Rol_Usuario.query.all()
    usuario = Usuario.query.all()

    data_rol_usuario = []
    data_usuario = []

    for obj in rol_usuario:
        x = model_to_dict(obj)
        data_rol_usuario.append(x)
    for obj in usuario:
        x = model_to_dict(obj)
        data_usuario.append(x)

    result = {
        'Usuario':data_usuario,
        'Rol_Usuario':data_usuario
    }

    return jsonify(result)

@bp.route('/rol_usuario')
def vista_rol_usuario():
    query = Rol_Usuario.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'Rol_Usuario': data
    }
    return jsonify(result)

@bp.route('/usuario')
def vista_usuario():
    query = Usuario.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'Usuario': data
    }
    return jsonify(result)