from utils.db import db

class Rol_Usuario(db.Model):
    id_rol_usuario = db.Column(db.Integer, primary_key=True)
    nombre_rol_usuario = db.Column(db.String(20),)

    def __init__(self, id_rol_usuario, nombre_rol_usuario=None) -> None:
        self.id_rol_usuario = id_rol_usuario
        self.nombre_rol_usuario = nombre_rol_usuario


    