from functools import wraps
from flask import session, url_for, redirect, request, render_template


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('index'))
    return wrap


def correct_type(type_list=None):
    def decorator(f):
        @wraps(f)
        def check_type(*args, **kwargs):
            type_user = session['user']['type']
            if type_user in type_list:
                return f(*args, **kwargs)
            else:
                return redirect(url_for('index'))
        return check_type
    return decorator


def correct_form(form_list):
    def decorator(f):
        @wraps(f)
        def check_form(*args, **kwargs):
            if request.method == 'POST':
                table = []
                for item in request.form:
                    table.append(item)
                for name in form_list:
                    if name not in table:
                        return render_template('bad.html', user=session['user'])
            return f(*args, **kwargs)
        return check_form
    return decorator


def correct_json(form_list):
    def decorator(f):
        @wraps(f)
        def check_form(*args, **kwargs):
            if request.method == 'POST':
                table = []
                for item in request.json:
                    table.append(item)
                for name in form_list:
                    if name not in table:
                        return render_template('bad.html', user=session['user'])
            return f(*args, **kwargs)
        return check_form
    return decorator