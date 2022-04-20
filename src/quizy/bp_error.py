"""Blueprint for error subpages."""
from flask import Blueprint, render_template

bp_error = Blueprint(
    "error", __name__, url_prefix="/error", template_folder="templates/error"
)


@bp_error.route("/opentdb")
def opentdb_page():
    """
    Page to show error that Open Trivia Database is not available.

    :return:
        Shows error page that Open Trivia Database is not available.
    """
    return render_template("opentdb.html")
