"""[summary]

We have a problem in application.Register_vehicle. 
Its doing a lot of different things. So this method has low cohesion. And meny responsabilities.
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

class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

class VehicleRegistry:
    
    def generate_vehicle_id(self,length):
        return ''.join(random.choices(string.ascii_uppercase,k=length))
    
    def generate_vehicle_license(self,id):
        return f"{id[:2]}-{''.join(random.choices(string.digits,k=2))}-{''.join((random.choices(string.ascii_uppercase,k=2)))}"
    
class Application:
    
    def register_vehicle(self, brand: string):
        # create registry instance
        registry = VehicleRegistry()
        
        #generate a vehicle id of length 12
        vehicle_id = registry.generate_vehicle_id(12)
        
        #now generate a license plate 
        license_plate = registry.generate_vehicle_license(vehicle_id)
        
        #compute catalogue price
        catalogue_price = 0
        if brand == "Tesla Model 3":
            catalogue_price = 60000
        elif brand == "Volkswagen ID3":
            catalogue_price = 35000
        elif brand == "BMW 5":
            catalogue_price = 45000
        
        # compute tax price
        tax_percentage = 0.05
        if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
            tax_percentage=0.02
        
        # compute payable tax
        payable_tax = tax_percentage * catalogue_price
        
        # print out registration
        print("Registration complete, vehicle information:")
        print(f"Brand: {brand}")
        print(f"ID: {vehicle_id}")
        print(f"License plate: {license_plate}")
        print(f"Payable tax: {payable_tax}")
        
app = Application()
app.register_vehicle("Volkswagen ID3")