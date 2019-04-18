from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_,or_

db = SQLAlchemy()

class Flight(db.Model):

    __tablename__ = "Flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String,nullable=False)
    destination = db.Column(db.String,nullable=False)
    duration = db.Column(db.Integer,nullable=False)
    passengers = db.relationship("Passenger",backref="Flight",lazy=True)
           
    def delay(self,amount) :
        self.duration += amount

    def addPassenger(self,name) :
        #p = Passenger(name = name,flight_id = self.id)
        p = Passenger(name = name,flight_id = self.id)
        db.session.add(p)
        db.session.commit()


class Passenger(db.Model):

    __tablename__ = "Passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable=False)
    flight_id = db.Column(db.Integer,db.ForeignKey("Flights.id"),nullable=False)
