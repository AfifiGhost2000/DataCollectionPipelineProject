from application import db
from datetime import datetime

class AvgMonthlyIncome(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    name = db.Column(db.String(30), nullable=False)
    country = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(30), nullable=True)
    address = db.Column(db.String(30), nullable=True)
    phonenumber = db.Column(db.String(30), nullable=True)
    gender = db.Column(db.String(15), nullable=False)
    satisfactionrate = db.Column(db.Integer, nullable=False)
    income = db.Column(db.Integer, nullable=False)


   

    def __str__(self):
        return self.id




