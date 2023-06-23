from utils.db import db
    
class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    id_rol_usuario = db.Column(db.Integer, db.ForeignKey('rol_usuario.id_rol_usuario'))
    nombre_usuario = db.Column(db.String(40))
    email = db.Column(db.String(60))
    password = db.Column(db.String(20))

    def __init__(self, id_usuario, nombre_usuario=None, email=None, password=None, id_rol_usuario=None) -> None:
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.email = email
        self.password = password
        self.id_rol_usuario = id_rol_usuario

    