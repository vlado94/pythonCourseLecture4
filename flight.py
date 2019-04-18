class Flight:
    counter = 0
    def __init__(self,origin,destination,duration) :

        self.id = Flight.counter
        Flight.counter += 1

        self.passengers = []

        self.origin = origin
        self.destination = destination
        self.duration = duration

    def printInfo(self):
        print(self.origin)
        print(self.destination)
        print(f"Flight duration: {self.duration}")

        for passenger in self.passengers :
            print(f"{passenger.name}")
        
    def delay(self,amount) :
        self.duration += amount

    def addPassenger(self,passenger) :
        self.passengers.append(passenger)
        passenger.flight_id = self.id


class Passenger:

    def __init__(self,name) :
        self.name = name


def main() :
    f = Flight(origin="New York", destination="Parissss", duration= 540)
    f.duration += 10

    f.delay(30)

    f.printInfo()

    alice = Passenger("Alice")
    bob = Passenger("Bob")

    f.addPassenger(alice)
    f.addPassenger(bob)
    f.printInfo()


if __name__ == "__main__" :
    main()