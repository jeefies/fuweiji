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
    return ccd.encode('草泥马')
