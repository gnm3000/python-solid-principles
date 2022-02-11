"""[summary]
 We have a problem in application. Register_vehicle.
 Its doing a lot of different things. So this method has low cohesion.
 And meny responsabilities.
 Also high copling, reply on implementation details with VehicleRegistry class.
 If I change something in VehicleRegistry I will change Register_vechicle.

1. where the information store? Where are the information expert?

"""


import string
import random


class VehicleInfo:
    bread: str
    catalogue_price: str
    electric: bool

    def __init__(self, brand, electric, catalogue_price) -> None:
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price

    def print(self):
        print(f"Brand {self.brand}")
        print(f"Payable Tax {self.compute_tax()}")


class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, id, license_plate, info) -> None:
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print(f"ID: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()


class VehicleRegistry:
    """[This class dealing with vehicles and licenses]
    """
    vehicle_info = {}

    def __init__(self) -> None:
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(
            brand, electric, catalogue_price)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits,k=2))} \
            -{''.join((random.choices(string.ascii_uppercase,k=2)))}"

    def create_vehicle(self, brand):
        # generate a vehicle id of length 12
        vehicle_id = self.generate_vehicle_id(12)

        # now generate a license plate
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(id, license_plate, self.vehicle_info[brand])


class Application:

    def register_vehicle(self, brand: string):
        # create registry instance
        registry = VehicleRegistry()

        # create a vehicle
        return registry.create_vehicle(brand)


app = Application()
vehicle = app.register_vehicle("Volkswagen ID3")
vehicle.print()


# part2  https://www.youtube.com/watch?v=Kv5jhbSkqLE
