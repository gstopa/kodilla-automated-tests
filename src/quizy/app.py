from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin


RANKING = [
    {"quiz_uuid": "1234-abcdef-123456-abcd", "user_id": 1, "score": 6},
    {"quiz_uuid": "1234-abcdef-123456-abce", "user_id": 2, "score": 5},
    {"quiz_uuid": "1234-abcdef-123456-abcf", "user_id": 3, "score": 8},
]


def get_ranking(sort: bool = True, reverse: bool = True) -> list:
    ranking = RANKING
    if sort:
        ranking = sorted(RANKING, key=lambda result: result["score"], reverse=reverse)
    return ranking


class ConfigClass(object):
    # Flask settings
    SECRET_KEY = 'something'
    # Flask-SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'  # in memory SQL database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Avoids SQLAlchemy warning
    # Flask-User settings
    USER_APP_NAME = "quizy"  # Shown in and email templates and page footers
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
        return render_template("index.html")

    @app.route('/ranking')
    def ranking_page():
        return render_template("ranking.html", ranking=get_ranking())

    @app.route('/ranking.json')
    def ranking_json_page():
        return {"ranking": get_ranking()}

    @app.route('/quizy_choose')
    @login_required
    def quizy_choose_page():
        return render_template("quizy_choose.html")

    @app.route('/quizy_take')
    @login_required
    def quizy_take_page():
        return render_template("quizy_take.html")

    @app.route('/quizy_count_me_in')
    @login_required
    def quizy_count_me_in_page():
        return redirect(url_for("ranking_page"))

    return app
