from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'deepakgusain'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    from .model import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app