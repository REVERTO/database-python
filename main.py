import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Setting database URL
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
if bool(os.environ.get('LOCAL_DEV', False)):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    print 'env prod'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    print 'env local'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
