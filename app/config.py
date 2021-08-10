import os
import uuid

base = os.path.abspath(os.path.dirname(__file__))

class Default:
    SECRET_KEY = os.getenv("SECRET_KEY", uuid.uuid1().hex)

    @staticmethod
    def init_app(app):
        pass

class WithSQLite(Default):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass

config = {
        'default': Default,
        'sqlite' : WithSQLite,
}
