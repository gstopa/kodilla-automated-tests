from flask import Blueprint, render_template


bp_error = Blueprint('error', __name__, url_prefix='/error', template_folder='templates/error')


@bp_error.route('/opentdb')
def opentdb_page():
    return render_template('opentdb.html')
