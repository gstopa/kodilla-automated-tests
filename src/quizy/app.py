"""Quizy main APP."""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager, UserMixin

from quizy.app_data import init_app_quizy_data
from quizy.bp_error import bp_error
from quizy.bp_quizy import bp_quizy
from quizy.bp_ranking import bp_ranking


class ConfigClass:  # pylint: disable=too-few-public-methods
    """Flask app configuration class."""

    # Flask settings
    SECRET_KEY = "something"
    # Flask-SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = "sqlite:///"  # in memory SQL database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Avoids SQLAlchemy warning
    # Flask-User settings
    USER_APP_NAME = "quizy"  # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = False  # Disable email authentication
    USER_ENABLE_USERNAME = True  # Enable username authentication
    USER_REQUIRE_RETYPE_PASSWORD = False  # Simplify register form


def create_app() -> Flask:
    """
    Factory creating new instance of Quizy APP.

    :return:
        Quizy APP
    """
    app = Flask(__name__)
    app.config.from_object(__name__ + ".ConfigClass")
    database = SQLAlchemy(app)

    class User(database.Model, UserMixin):
        """User definition class."""

        # pylint: disable=no-member
        __tablename__ = "users"
        id = database.Column(database.Integer, primary_key=True)
        active = database.Column(
            "is_active", database.Boolean(), nullable=False, server_default="1"
        )
        username = database.Column(
            database.String(100, collation="NOCASE"),
            nullable=False,
            unique=True,
        )
        password = database.Column(
            database.String(255), nullable=False, server_default=""
        )

    database.create_all()
    UserManager(app, database, User)

    @app.route("/")
    def index_page():
        return render_template("index.html")

    app.register_blueprint(bp_quizy)
    app.register_blueprint(bp_ranking)
    app.register_blueprint(bp_error)

    init_app_quizy_data(app=app)

    return app
