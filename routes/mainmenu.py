from flask import Blueprint, render_template as rt
from utils.auth import login_required

bp = Blueprint('mainmenu', __name__, url_prefix="/mainmenu")

@bp.route('/')
@login_required
def mainmenu():
    return rt("mainmenu.html")
