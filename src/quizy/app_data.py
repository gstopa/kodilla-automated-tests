"""Module for initializing and accessing APP's QuizyData."""
from flask import Flask, current_app

from quizy.data import QuizyData


def init_app_quizy_data(app: Flask) -> None:
    """
    Function initializing Flask app with QuizyData.

    :param app:
        Flask app to initialize with QuizyData
    :return:
        None
    """
    app.config["QuizyData"] = QuizyData(quizzes={}, quizzes_taken=[])


def get_quizy_data() -> QuizyData:
    """
    Function gets currently running Flask app and retrieves its QuizyData.

    :return:
        QuizyData for current running Flask app
    """
    return current_app.config["QuizyData"]
