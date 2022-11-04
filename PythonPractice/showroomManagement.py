##A vehicle showroom management system project!

class Showroom:
    showroom_name = ""
    showroom_address = ""

    def __init__():
        pass
    pass

class Vehicle:
    vehicle_name = ""
    milage = ""
    company_name = ""
    model = ""
    price = ""
    horse_power = ""
    
    def __init__(self, vn, m, cn, mod, p, hp):
        self.vehicle_name = vn
        self.milage = m
        self.companyName = cn
        self.model = mod
        self.price = p
        self.horse_power = hp

    def getVehicleName(self):
        print("Vehicle Name is vn" + self.vehicle_name)

    pass

class Bike:
    isKickOrAuto = False
    hasExtraCarrier = False
    saddleHeight = float

    def __init__(self, ka, ec, sh):
        self.isKickOrAuto = ka
        self.hasExtraCarrier = ec,
        self.saddleHeight = sh
    pass

class Car:
    stearingWheelSide = False ## False for left, True for Right
    soundSystemCompany = ""
    numberOfDoors = 0

    def __init__(self, sws, ssc, noD):
        self.stearingWheelSide = sws
        self.soundSystemCompany = ssc
        self.numberOfDoors = noD
    pass

class Bus:
    pass

class Truck:
    roof_height = ""

    spare_tires = 0
    pass

class Address:
    pass

class Account:
    pass

class Teachers:
    pass

if __name__ == "__main__":
    print("Welcome to School Management System")
    v1  = Vehicle("1", "2","3", "4","5", "6") 
    v1.getVehicleName()
