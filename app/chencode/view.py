from .bp import bp

from flask import (url_for, flash, render_template,
        redirect, session, send_file, jsonify, abort)
from flask import ( request as req,
        make_response as mkrsp,
        Response as Rsp,
        )

from .. import _chencode as ccd

@bp.route('/')
def index():
    return render_template('chencode/index.html')

@bp.route('/encode', methods=["GET", "POST"])
def encode():
    return ccd.encode(req.values.get("ctx", ''))

@bp.route('/decode', methods=["GET", "POST"])
def decode():
    return ' '.join(ccd.decode(req.values.get("ctx", '')))

@bp.route('/result', methods=["POST"])
def result():
    ctx = req.values.get("ctx", '').strip()
    code = req.values.get("code")

    sec = None
    ori = None
    if code == 'en':
        try:
            sec = ccd.encode(ctx)
            ori = ctx
        except Exception as e:
            return render_templace("error.html", e = str(e))
    elif code == 'de':
        try:
            sec = ctx
            ori = ''.join(ccd.decode(ctx))
        except Exception as e:
            return render_template('error.html', e = str(e))
    return render_template("chencode/result.html", origin = ori, secret = sec)
