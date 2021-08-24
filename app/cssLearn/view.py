from .bp import bp

from flask import (url_for, flash, render_template,
                    redirect, session, send_file, jsonify, abort)
from flask import (request as req,
                    make_response as mkrsp,
                    Response as Rsp,
                )

@bp.route('/')
def scrollPages():
    return render_template('css/scrollPages.html')

@bp.route('/pagebtns')
def clickToScrollPages():
    return render_template('css/clickToScrollPages.html')

@bp.route('/svgs')
def svgLearn():
    return render_template('css/svgLearns.html')
