from flask import Blueprint, render_template

from quizy.app_data import get_quizy_data

bp_ranking = Blueprint('ranking', __name__, url_prefix='/ranking', template_folder='templates/ranking')


@bp_ranking.route('/show')
def show_page():
    ranking = get_quizy_data().get_ranking()
    return render_template('ranking.html', ranking=ranking)


@bp_ranking.route('/json')
def json_page():
    ranking = get_quizy_data().get_ranking()
    return {'ranking': ranking}
