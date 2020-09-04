# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels = 4, drive = "vroooom"):
        self.num_wheels = num_wheels
        self.drive = drive

    def __drive__(self):
        return self.drive

    # TODO


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels = 2, drive = "BRAAAP!!"):
        super().__init__(num_wheels, drive)

    def __drive__(self):
        return super().__drive__()

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO
print([vehicle.__drive__() for vehicle in vehicles])