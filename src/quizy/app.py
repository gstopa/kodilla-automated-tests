from dataclasses import dataclass
from typing import Dict, Any, List
from uuid import uuid4
from flask import Flask, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin, current_user
from requests import get


POINTS_MULTIPLIER: Dict[str, int] = {
    'easy': 1,
    'medium': 3,
    'hard': 6,
}

@dataclass
class QuizQuestion:
    question: str
    correct_answer: str


@dataclass
class QuizTest:
    uuid: str
    difficulty: str
    questions: Dict[str, QuizQuestion]


RANKING: List[Dict[str, Any]] = []
QUIZZES: Dict[str, QuizTest] = {}


def get_ranking(sort: bool = True, reverse: bool = True) -> list:
    ranking = RANKING
    if sort:
        ranking = sorted(RANKING, key=lambda result: result['score'], reverse=reverse)
    return ranking


def calculate_quiz_score(quiz_uuid, answers):
    quiz = QUIZZES[quiz_uuid]
    multiplier = POINTS_MULTIPLIER[quiz.difficulty]
    questions = quiz.questions
    questions_points = [
        multiplier
        for key in questions
        if questions[key].correct_answer == answers[key]
    ]
    return sum(questions_points)


def add_score_to_ranking(quiz_uuid, user_id, score):
    RANKING.append(
        {
            'quiz_uuid': quiz_uuid,
            'user_id': user_id,
            'score': score,
        }
    )


def create_new_quiz(difficulty) -> str:
    quiz_uuid = str(uuid4())
    response = get(f'https://opentdb.com/api.php?amount=10&difficulty={difficulty}&type=boolean')
    questions = response.json()['results']
    quiz_questions = {
        str(index): QuizQuestion(question=question['question'], correct_answer=question['correct_answer'])
        for index, question in enumerate(questions)
    }
    QUIZZES[quiz_uuid] = QuizTest(uuid=quiz_uuid, difficulty=difficulty, questions=quiz_questions)
    return quiz_uuid


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

    @app.route('/ranking')
    def ranking_page():
        return render_template('ranking.html', ranking=get_ranking())

    @app.route('/ranking.json')
    def ranking_json_page():
        return {'ranking': get_ranking()}

    @app.route('/quizy_choose')
    # @login_required
    def quizy_choose_page():
        return render_template('quizy_choose.html')

    @app.route('/quizy_create', methods=['GET', 'POST'])
    # @login_required
    def quizy_create_page():
        if request.method != 'POST':
            return redirect(url_for('quizy_choose_page'))
        difficulty = request.form.get('difficulty')
        if difficulty not in {'easy', 'medium', 'hard'}:
            return redirect(url_for('quizy_choose_page'))
        quiz_uuid = create_new_quiz(difficulty=request.form['difficulty'])
        return redirect(url_for('quizy_take_page', uuid=quiz_uuid))

    @app.route('/quizy_take/<uuid>')
    # @login_required
    def quizy_take_page(uuid):
        if uuid not in QUIZZES:
            return redirect(url_for('quizy_choose_page'))
        quiz = QUIZZES[uuid]
        session['quiz_uuid'] = uuid
        return render_template('quizy_take.html', quiz=quiz.questions)

    @app.route('/quizy_count_me_in', methods=['GET', 'POST'])
    # @login_required
    def quizy_count_me_in_page():
        if request.method != 'POST':
            return redirect(url_for('quizy_choose_page'))
        print(request.form)
        quiz_uuid = session.pop('quiz_uuid')
        score = calculate_quiz_score(quiz_uuid=quiz_uuid, answers=request.form)
        user_id = current_user.id if current_user.is_authenticated else 666
        add_score_to_ranking(quiz_uuid=quiz_uuid, user_id=user_id, score=score)
        return render_template('quizy_count_me_in.html', score=score, uuid=quiz_uuid)

    return app
