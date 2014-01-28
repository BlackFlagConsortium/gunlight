from flask import Flask

def init_app():
    app = Flask(__name__)

    from . import views
    app.add_url_rule('/', 'track_bills', views.track_bills)

    return app