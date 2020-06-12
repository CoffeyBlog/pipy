import flask

from infrastructure.view_modifiers import response
from services import package_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


##################### INDEX / HOMEPAGE ##########################

@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    test_packages = package_service.get_latest_package()
    return {'packages': test_packages}
    # return render_template('home/index.html', packages=test_packages)


##################### ABOUT PAGE ##########################

@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {}
