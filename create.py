import os
from flask import Flask,render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()
    flight = Flight(origin="Belgrade",destination="Tuzla",duration=540)
    #flight = Flight(origin="Paris",destination="Belgrade",duration=330)
    #db.session.add(flight)
    #db.session.commit()

    #flight.addPassenger("pera")
    #passengers = flight.passengers
    #print("passengers")
    #print(passengers)
    flights = Flight.query.all()
    flightCount = Flight.query.count()
    queryByIDV1 = flightCount = Flight.query.filter_by(id=2).first()
    queryByIDV2 = flightCount = Flight.query.get(2)
    parisFligts = Flight.query.filter_by(origin="Paris").all()
    firstParisFligt = Flight.query.filter_by(origin="Paris").first()
    flightNewYork = Flight.query.filter_by(origin="New York").first()
    print(flights[1])
    print(parisFligts[0])
    print(firstParisFligt)
    print(queryByIDV1)
    print(queryByIDV2)
    #db.session.delete(flightNewYork)
    #db.session.commit()
    flightsWith = Flight.query.order_by(Flight.origin).all()
    flightsWithDesc = Flight.query.order_by(Flight.origin.desc()).all()
    flightWithNotEquals = Flight.query.filter(Flight.origin != "Paris").all()
    flightWithLike = Flight.query.filter(Flight.origin.like("%a%")).all()
    flightWithIn = Flight.query.filter(Flight.origin.in_(["Tokyo","Paris"])).all()
    flightWithAnd = Flight.query.filter(and_(Flight.origin == "Tokyo",Flight.duration > 500)).all()
    print(flightWithIn)




if __name__ == "__main__" :
    with app.app_context():
        main()