from flask import Flask, render_template
from main import app
from model import User

@app.route('/')
def index():
    users = User.query.all()
    print users
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run()
