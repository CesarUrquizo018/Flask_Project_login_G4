<<<<<<< HEAD
from flask import session, Blueprint, render_template as rt, request, url_for, redirect
=======
from flask import Blueprint, render_template as rt
>>>>>>> c86f0b439ec6531db697860263277189ddd3c334
from utils.auth import login_required

bp = Blueprint('mainmenu', __name__, url_prefix="/mainmenu")

<<<<<<< HEAD
@bp.route('/', methods=['GET', 'POST'])
@login_required
def mainmenu():
    if request.method == 'POST':
                session.clear()
                return redirect(url_for('index.index'))

=======
@bp.route('/')
@login_required
def mainmenu():
>>>>>>> c86f0b439ec6531db697860263277189ddd3c334
    return rt("mainmenu.html")
