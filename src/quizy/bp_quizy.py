"""Blueprint for quizy subpages."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_user import current_user, login_required

from quizy.app_data import get_quizy_data
from quizy.questions import generate_questions

bp_quizy = Blueprint(
    "quizy", __name__, url_prefix="/quizy", template_folder="templates/quizy"
)


@bp_quizy.route("/choose")
@login_required
def choose_page():
    """
    Page to allow chose of quiz difficulty.

    :return:
        Shows page with difficulty chose.
    """
    return render_template("choose.html")


@bp_quizy.route("/create", methods=["POST"])
@login_required
def create_page():
    """
    Page to create new quiz.

    :return:
        Redirects to take page on successful generation of quiz;
        Redirects to error opentdb page when Open Trivia Database
            is not available;
        Redirects to choose page when difficulty was incorrectly defined.
    """
    difficulty = request.form.get("difficulty")
    try:
        questions = generate_questions(difficulty=difficulty)
    except ValueError:
        flash("Difficulty was wrong. Choose from below options.")
        return redirect(url_for("quizy.choose_page"))
    except ConnectionError:
        return redirect(url_for("error.opentdb_page"))
    quiz_uuid = get_quizy_data().create_new_quiz(
        difficulty=request.form["difficulty"], questions=questions
    )
    return redirect(url_for("quizy.take_page", uuid=quiz_uuid))


@bp_quizy.route("/take/<uuid>")
@login_required
def take_page(uuid: str):
    """
    Page for showing quiz to be taken.

    :param uuid:
        Quiz UUID
    :return:
        Shows page with quiz to be taken.
    """
    quiz_questions = get_quizy_data().get_quiz_questions(uuid)
    if not quiz_questions:
        return redirect(url_for("quizy.choose_page"))
    return render_template("take.html", quiz_uuid=uuid, quiz=quiz_questions)


@bp_quizy.route("/count_me_in", methods=["POST"])
@bp_quizy.route("/count_me_in/<uuid>/<score>", methods=["GET"])
@login_required
def count_me_in_page(uuid: str = None, score: int = None):
    """
    Page for calculation of quiz score and show the results to user.

    :param uuid:
        Quiz UUID
    :param score:
        Points scored in Quiz

    :return:
        On POST redirects to page showing results,
        On GET show results page.
    """
    if request.method == "POST":
        answers = dict(request.form)
        quiz_uuid = answers.pop("quiz_uuid")
        quizy_data = get_quizy_data()
        quiz_score = quizy_data.calculate_quiz_score(
            quiz_uuid=quiz_uuid, answers=request.form
        )
        user_id = current_user.id
        quizy_data.add_score_to_ranking(
            quiz_uuid=quiz_uuid, user_id=user_id, score=quiz_score
        )
        return redirect(
            url_for(
                "quizy.count_me_in_page",
                _method="GET",
                uuid=quiz_uuid,
                score=quiz_score,
            )
        )
    return render_template("count_me_in.html", score=score, uuid=uuid)
