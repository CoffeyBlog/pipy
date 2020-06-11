import flask

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')

##################### PACKAGE NAME ##########################

@blueprint.route('/project/<package_name>')
# @response(template_file='packages/details.html')
def package_details(package_name: str):
    return "Package details for {}".format(package_name)

##################### PACKAGE RANK ##########################

@blueprint.route('/<int:rank>')
# @response(template_file='packages/details.html')
def popular(rank: int):
    print(type(rank),rank)
    return "Package details for {}th most popular package".format(rank)
