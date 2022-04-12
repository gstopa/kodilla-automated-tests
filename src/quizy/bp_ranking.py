from flask import Blueprint, render_template
from quizy.data import get_ranking


bp_ranking = Blueprint('ranking', __name__, url_prefix='/ranking', template_folder='templates/ranking')


@bp_ranking.route('/show')
def show_page():
    return render_template('ranking.html', ranking=get_ranking())


@bp_ranking.route('/json')
def json_page():
    return {'ranking': get_ranking()}
