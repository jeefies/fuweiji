from .bp import bp

from flask import (url_for, flash, render_template,
                    redirect, session, send_file, jsonify, abort)
from flask import (request as req,
                    make_response as mkrsp,
                    Response as Rsp,
                    )

@bp.route('/')
def index():
    return render_template('info/info.html')

@bp.route('/2')
def hidden():
    return render_template('info/info2.html')
