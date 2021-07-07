from flask_login import LoginManager
from .login import *
from .signup import *
from .logout import *
from .update import *
from .delete import *
from .alluer import *
from Crud.config import app

login_manager = LoginManager()
login_manager.init_app(app)


