# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle: #Parent class
    pass

class FlightVehicle(Vehicle): #Child class
    pass

class Starship(FlightVehicle): #Grandchild Class
    pass

class Airplane(FlightVehicle): #Grandchild Class
    pass

class GroundVehicle(Vehicle): #Child Class
    pass

class Motorcycle(GroundVehicle): #Grandchild Class
    pass

class Car(GroundVehicle): #Grandchild Class
    pass