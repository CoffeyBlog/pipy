import flask


app = flask.Flask(__name__)


def main():
    register_blueprints()
    app.run(debug=True)


def register_blueprints():
    from views import home_view
    from views import package_views

    app.register_blueprint(home_view.blueprint)
    app.register_blueprint(package_views.blueprint)


if __name__ == '__main__':
    main()
