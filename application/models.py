from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=True)

    @property
    def serialize(self):
       return {
           'id': self.id,
           'text': self.text,
           'date'  : self.date.strftime("%Y-%m-%d %H:%M")
       }
