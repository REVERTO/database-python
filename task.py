from main import db
from model import User
import datetime

t = datetime.datetime.today()
u = User(t.strftime("%Y/%m/%d %H:%M:%S"))
# u = User('task')
db.session.add(u)
db.session.commit()
