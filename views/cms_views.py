import flask

from infrastructure.view_modifiers import response
from services import cms_services as cms_services

blueprint = flask.Blueprint('cms', __name__, template_folder='templates')


##################### CMS PAGE ##########################

@blueprint.route('<path:full_url>')
@response(template_file='cms/page.html')
def cms_page(full_url: str):
    print("Getting CMS page for {}".format(full_url))

    page = cms_services.get_page(full_url)
    if not page:
        return flask.abort(404)

    return page
