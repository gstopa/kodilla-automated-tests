from flask import Blueprint, current_app, render_template


bp_ranking = Blueprint('ranking', __name__, url_prefix='/ranking', template_folder='templates/ranking')


@bp_ranking.route('/show')
def show_page():
    ranking = current_app.config['QuizyData'].get_ranking()
    return render_template('ranking.html', ranking=ranking)


@bp_ranking.route('/json')
def json_page():
    ranking = current_app.config['QuizyData'].get_ranking()
    return {'ranking': ranking}
