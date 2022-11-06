# A vehicle showroom management system project!

class Vehicle:
    def __init__(self, vn, m, cn, mod, p, hp):
        self.vehicle_name = vn
        self.milage = m
        self.companyName = cn
        self.model = mod
        self.price = p
        self.horse_power = hp

    @property
    def vehicle_name(self):
        return self.vehicle_name

    @vehicle_name.setter
    def vehicle_name(self, vehicle_name):
        self.vehicle_name = vehicle_name
    pass


class Bike:
    def __init__(self, ka, ec, sh):
        self.isKickOrAuto = ka
        self.hasExtraCarrier = ec,
        self.saddleHeight = sh
    pass


class Car:
    def __init__(self, sws, ssc, noD):
        self.stearingWheelSide = sws   # False for left, True for Right
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
