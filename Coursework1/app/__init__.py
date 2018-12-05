from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#create flask app
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


# Handles all migrations.
migrate = Migrate(app, db)

from app import views,models
