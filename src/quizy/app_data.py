from flask import Flask, current_app

from quizy.data import QuizyData


def init_app_quizy_data(app: Flask) -> None:
    app.config['QuizyData'] = QuizyData(quizzes={}, quizzes_taken=[])


def get_quizy_data() -> QuizyData:
    return current_app.config['QuizyData']
