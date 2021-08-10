from flask import Flask
from .config import config

def create_app(cfg):
    print(cfg)
    app = Flask(__name__)
    app.config.from_object(config[cfg])
    config[cfg].init_app(app)

    from .main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix="/")

    from .info import bp as info_bp
    app.register_blueprint(info_bp, url_prefix='/info')

    from .smp import bp as smp_bp
    app.register_blueprint(smp_bp, url_prefix='/smp')

    return app
