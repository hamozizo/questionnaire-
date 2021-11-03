from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime 
from flask_login import LoginManager
import os

app = Flask(__name__) 


# app.config['SECRET_KEY']= os.environ.get('SEKRET_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@localhost/classfit'

db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_message_category = 'info'
login_manager.login_message_category='info' #info bootstrap class


from questionnaire.requests import questions_blueprint
app.register_blueprint(questions_blueprint)