from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager, UserMixin

from quizy.bp_error import bp_error
from quizy.bp_quizy import bp_quizy
from quizy.bp_ranking import bp_ranking
from quizy.app_data import init_app_quizy_data


class ConfigClass(object):
    # Flask settings
    SECRET_KEY = 'something'
    # Flask-SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'  # in memory SQL database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Avoids SQLAlchemy warning
    # Flask-User settings
    USER_APP_NAME = 'quizy'  # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = False  # Disable email authentication
    USER_ENABLE_USERNAME = True  # Enable username authentication
    USER_REQUIRE_RETYPE_PASSWORD = False  # Simplify register form


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(__name__+'.ConfigClass')
    db = SQLAlchemy(app)

    class User(db.Model, UserMixin):
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
        username = db.Column(db.String(100, collation='NOCASE'), nullable=False, unique=True)
        password = db.Column(db.String(255), nullable=False, server_default='')

    db.create_all()
    user_manager = UserManager(app, db, User)

    @app.route('/')
    def index_page():
        return render_template('index.html')

    app.register_blueprint(bp_quizy)
    app.register_blueprint(bp_ranking)
    app.register_blueprint(bp_error)

    init_app_quizy_data(app=app)

    return app
