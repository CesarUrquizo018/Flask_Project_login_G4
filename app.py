from flask import Flask,render_template
from utils.config import Config

def crear_app():
    app = Flask(__name__)
    app.static_folder = 'static'
    app.config.from_object(Config)
    from routes import login1
    app.register_blueprint(login1.bp)
    from routes import login2
    app.register_blueprint(login2.bp)
    from routes import index
    app.register_blueprint(index.bp)
    from routes import portal
    app.register_blueprint(portal.bp)

    return app
