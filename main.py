from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Setting database URL
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
if bool(os.environ.get('LOCAL_DEV', False)):
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()