from flask import Blueprint, render_template as rt

bp = Blueprint('subportal', __name__, url_prefix="/subportal") #al llamar el blue print en base sería (NomreBP.FuncionAsociadaARuta)

@bp.route('/')
def portal():
    return rt("portal.html")