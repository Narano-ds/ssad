from flask import Flask
from src.extensions import cors, db, ma, migrate,bcrypt
from src.modules import user,message
from flask_migrate import Migrate
from flask_login import LoginManager

from src.modules.user.models import User
MODULES = [user,message]
migrate = Migrate(compare_type=True)
def boot(settings=None, override_settings=None):
    app = Flask(__name__)
    app.config  .from_object(settings)
    app.config.from_object(override_settings)

    register_extensions(app)
    register_modules(app)


    return app

def register_extensions(app):
    cors.init_app(app,ressources={
        r"/*": {
            "origins":"*"
        }})
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))
 



def register_modules(app):
    for m in MODULES:
        if hasattr(m, "api"):
            app.register_blueprint(m.api)
