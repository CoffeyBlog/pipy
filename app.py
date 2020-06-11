import flask

app = flask.Flask(__name__)


def main():
    register_blueprints()
    app.run(debug=True)


def register_blueprints():
    from views import home_view
    app.register_blueprint(home_view.blueprint)


if __name__ == '__main__':
    main()
