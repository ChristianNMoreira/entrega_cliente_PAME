from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
mail = Mail()
migrate = Migrate()
jwt = JWTManager()