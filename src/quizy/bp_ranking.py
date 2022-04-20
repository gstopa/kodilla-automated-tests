"""Blueprint for ranking subpages."""
from flask import Blueprint, render_template

from quizy.app_data import get_quizy_data

bp_ranking = Blueprint(
    "ranking",
    __name__,
    url_prefix="/ranking",
    template_folder="templates/ranking",
)


@bp_ranking.route("/show")
def show_page():
    """
    Page to show ranking.

    :return:
        Shows page with ranking.
    """
    ranking = get_quizy_data().get_ranking()
    return render_template("ranking.html", ranking=ranking)


@bp_ranking.route("/json")
def json_page():
    """
    Page to show ranking in JSON format.

    :return:
        JSON with ranking.
    """
    ranking = get_quizy_data().get_ranking()
    return {"ranking": ranking}
