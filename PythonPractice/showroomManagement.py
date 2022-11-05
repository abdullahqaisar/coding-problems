##A vehicle showroom management system project!

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
    hasEmergencyExit = ""
    isBuisnessClass = False
    noOfSeats = 0
    pass

class Truck:
    roof_height = ""
    spare_tires = 0
    pass

class Account:
    name = ""
    username = ""
    password = ""
    age = ""
    email = ""
    pass


def menu():
    choice = 20
    print("Welcome to SHOWROOM")
    print("1. Login")
    print("2. Create Account")
    print("4. Admin Login")
    print("0. Exit")
    print("")
    choice = input("Your Choice: ")

    if (choice == 1):
        login()
    # print("Press 1 for Buying Vehicle")
    # print("Press 2 for Adding Vehicle")

def login():
    print("             LOGIN")
    username = input("Username: ")
    password = input("Password: ")


if __name__ == "__main__":
    menu()
    

    # v1  = Vehicle("1", "2","3", "4","5", "6") 
    # v1.getVehicleName()
