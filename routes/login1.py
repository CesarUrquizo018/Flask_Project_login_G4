from flask import Blueprint, render_template as rt, request, url_for, redirect
from utils.config import getURI
import psycopg2 

bp = Blueprint('login1', __name__,url_prefix="/login1") #al llamar el blue print en base sería (NomreBP.FuncionAsociadaARuta)

@bp.route('/', methods=['GET', 'POST'])
def login1():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = psycopg2.connect(getURI())
        cursor = conn.cursor()

        query = "SELECT nombre_usuario, email, password FROM usuario WHERE email = %s AND id_rol_usuario == 1"
        cursor.execute(query, (email,))
        row = cursor.fetchone()

        if row is not None:
            d_password = row
            if password == d_password:
                print("Éxito")
                return redirect(url_for('index.index'))
            else:
                print("Fallo")
        else:
            print("Fallo")

        cursor.close()
        conn.close()

    return rt("login.html")