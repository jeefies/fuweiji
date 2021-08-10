import os.path

from ..db import db
from .bp import bp

from flask import (url_for, flash, render_template,
                    redirect, session, send_file, jsonify, abort)
from flask import (request as req,
                    make_response as mkrsp,
                    Response as Rsp)

base = os.path.sep.join(os.path.split(os.path.abspath(os.path.dirname(__file__)))[:-1])
print(base)

@bp.route('/ip', methods=['get', 'post'])
def smpip():
    if req.method == 'GET':
        ip = db.get('smpip', None)
        if ip:
            ip = ip.decode()
        return jsonify({'ip': ip})
    elif req.method == 'POST':
        ip = req.values.get('ip')
        if not ip:
            abort(505)
        db['smpip'] = ip
        db.sync()
        return jsonify({'state': 200, 'success': True})

    abort(505)

@bp.route('/download')
def download():
    return send_file(os.path.join(base, 'static/smpip/setip.py'), 'plain/text', as_attachment=True, attachment_filename='initip.py')
