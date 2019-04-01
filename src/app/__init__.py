from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# instância de conexão com o banco
db = SQLAlchemy(app)

app.config.from_object('settings')

from app.controllers import views
from app.models import tables

# For development (show all settings for flask app)
for key in app.config:
    print(key, app.config[key])