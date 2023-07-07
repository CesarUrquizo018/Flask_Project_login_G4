<<<<<<< HEAD
from flask import Flask
=======
from flask import Flask, session
>>>>>>> c86f0b439ec6531db697860263277189ddd3c334
from utils.config import Config

from routes import login, index, portal, vista, mainmenu

def crear_app():
    app = Flask(__name__)

    app.static_folder = 'static'

    app.config.from_object(Config)

    app.register_blueprint(login.bp)
    app.register_blueprint(index.bp)
    app.register_blueprint(portal.bp)
    app.register_blueprint(vista.bp)
    app.register_blueprint(mainmenu.bp)

    return app