from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

# initialising sqlalchemy
db = SQLAlchemy()
DB_NAME = "info.db"

# initialising flask_login for handling login task and session
login_manager = LoginManager()
login_manager.login_view = "auth.login"

# creating flask app
def create_app():
    app = Flask(__name__)
    app.secret_key = "bsdktorimaikechodomcbc"

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from webapp.views import views
    from webapp.auth import auth

    app.register_blueprint(views , url_prefix="/")
    app.register_blueprint(auth , url_prefix="/users/auth")

    from .models import User , Todo
    create_db(app)

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# creating database if it doesn;t exists
def create_db(app):
    if not path.exists("webapp/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Database created...")