from main import db
from model import User

u = User('task')
db.session.add(u)
db.session.commit()
