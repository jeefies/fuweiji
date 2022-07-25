from flask import Flask
from flask_compress import Compress

from .config import config

compress = Compress()

def create_app(cfg):
    print(cfg)
    app = Flask(__name__)
    app.config.from_object(config[cfg])
    config[cfg].init_app(app)
    compress.init_app(app)

    from .main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix="/")

    from .info import bp as info_bp
    app.register_blueprint(info_bp, url_prefix='/info')

    from .smp import bp as smp_bp
    app.register_blueprint(smp_bp, url_prefix='/smp')

    from .dbapi import bp as dbapi_bp
    app.register_blueprint(dbapi_bp, url_prefix= '/dbapi')

    from .cssLearn import bp as css_bp
    app.register_blueprint(css_bp, url_prefix = '/css')

    from .chencode import bp as chcode_bp
    app.register_blueprint(chcode_bp, url_prefix = '/ch-code')

    from .imdata import bp as imdata_bp
    app.register_blueprint(imdata_bp, url_prefix = '/imdata')

    return app
