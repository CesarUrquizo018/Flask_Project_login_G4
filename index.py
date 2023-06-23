from app import crear_app
from utils.db import db

# Crea la aplicación Flask usando la función crear_app() definida en app.py
app = crear_app()

db.init_app(app)

if __name__ == "__main__":
    # Ejecuta la aplicación en el servidor local
    app.run()
