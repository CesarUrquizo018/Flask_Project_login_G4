from functools import wraps
from flask import session, redirect, url_for

def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if 'logged_in' in session:
            return view(*args, **kwargs)
        else:
<<<<<<< HEAD
            return redirect(url_for('portal.portal'))
=======
            return redirect(url_for('login.login'))
>>>>>>> c86f0b439ec6531db697860263277189ddd3c334
    return wrapped_view
