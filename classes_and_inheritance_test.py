__author__ = 'vlim'

## What is an Instance?

class Ride(object):
    def __init__(self, color, model, type, door=4):
        self.door = door
        self.color = color
        self.model = model
        self.type = type

myRide = Ride('Black', 'BMW' , 'car')

print "myRide's color: %s" % myRide.color
print "myRide's model: %s" % myRide.model
print "myRide's door: %s" % myRide.door

class Truck(Ride):
    def __init__(self, color, extragas, door=2):
        Ride.__init__(self, color, 'Hyundel', 'truck', door)
        self.extragas = extragas

myTruck = Truck('Red', 3, 2)

print "myTruck's color: %s" % myTruck.color
print "myTruck's model: %s" % myTruck.model
print "myTruck's type: %s" % myTruck.type
print "myTruck's extragas: %s" % myTruck.extragas
print "myTruck's door: %s" % myTruck.door

