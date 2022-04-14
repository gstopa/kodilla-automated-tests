from flask import Blueprint, redirect, render_template, request, session, url_for
from flask_user import current_user
from quizy.data import add_score_to_ranking, calculate_quiz_score, create_new_quiz, get_quiz_questions
from quizy.questions import generate_questions


bp_quizy = Blueprint('quizy', __name__, url_prefix='/quizy', template_folder='templates/quizy')


@bp_quizy.route('/choose')
# @login_required
def choose_page():
    return render_template('choose.html')


@bp_quizy.route('/create', methods=['POST'])
# @login_required
def create_page():
    difficulty = request.form.get('difficulty')
    try:
        questions = generate_questions(difficulty=difficulty)
    except ValueError:
        return redirect(url_for('quizy.choose_page'))
    quiz_uuid = create_new_quiz(difficulty=request.form['difficulty'], questions=questions)
    return redirect(url_for('quizy.take_page', uuid=quiz_uuid))


@bp_quizy.route('/take/<uuid>')
# @login_required
def take_page(uuid: str):
    quiz_questions = get_quiz_questions(uuid)
    if not quiz_questions:
        return redirect(url_for('quizy.choose_page'))
    session['quiz_uuid'] = uuid
    return render_template('take.html', quiz=quiz_questions)


@bp_quizy.route('/count_me_in', methods=['POST'])
# @login_required
def count_me_in_page():
    quiz_uuid = session.pop('quiz_uuid')
    score = calculate_quiz_score(quiz_uuid=quiz_uuid, answers=request.form)
    user_id = current_user.id if current_user.is_authenticated else 666
    add_score_to_ranking(quiz_uuid=quiz_uuid, user_id=user_id, score=score)
    return render_template('count_me_in.html', score=score, uuid=quiz_uuid)
