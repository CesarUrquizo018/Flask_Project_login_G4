from flask import Blueprint, render_template as rt, request, url_for, redirect
from utils.config import getURI
import psycopg2 

bp = Blueprint('login2', __name__,url_prefix="/login2") #al llamar el blue print en base sería (NomreBP.FuncionAsociadaARuta)

@bp.route('/', methods=['GET', 'POST'])
def login2(): #esta función debe coincidir con el url_for del html (base)
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = psycopg2.connect(getURI())
        cursor = conn.cursor()

        query = "SELECT password, nombre, apellido, cargo FROM usuarios WHERE email = %s"
        cursor.execute(query, (email,))
        row = cursor.fetchone()

        if row is not None:
            d_password, nombre, apellido, cargo = row
            if password == d_password:
                print("Exito")
                return redirect(url_for('principal.principal'))
            else:
                print("Fallo")
        else:
            print("Fallo")

        cursor.close()
        conn.close()

    return rt("login.html")