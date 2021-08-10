from ..db import db
from .bp import bp

from flask import (url_for, flash, render_template,
                    redirect, session, send_file, jsonify, abort)
from flask import (request as req,
                    make_response as mkrsp,
                    Response as Rsp,

@bp.route('/close')
def closedb():
    db.close()
    return jsonify({'state': 200, 'info': 'success'})

@bp.route('/reopen')
def reopendb():
    db.reopen()

@bp.route('/all')
def showdb():
    return jsonify({k:db[k] for k in db.allkeys()})
