import io
import os.path

from .bp import bp
from ..db import db

from flask import (url_for, flash, render_template,
                    redirect, session, send_file, jsonify, abort)
from flask import (request as req,
                    make_response as mkrsp,
                    Response as Rsp,
                )

"""
@views
    / (main.index): A main page to show my private info
"""

@bp.route('/')
def index():
    return render_template('main/main.html')

@bp.route('/favicon.ico')
def icon():
    return redirect(url_for('static', filename='favicon.ico'))

@bp.route('/redirect')
def R():
    return "Redirect Success!"

