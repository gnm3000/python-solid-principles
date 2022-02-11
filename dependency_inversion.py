from abc import ABC, abstractmethod

class Switchable(ABC):
    # abstract class
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")
    
    def turn_off(self):
        print("LightBulb: turned off...")
    
class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")
    
    def turn_off(self):
        print("Fan: turned off...")
        
class ElectricPowerSwitch:
    
    def __init__(self, l:Switchable):
        self.client = l
        self.on = False
        
    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True
            
l = LightBulb()
f=Fan()
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()

# here we can see a dependency between the light bulb and the PowerSwitch. because 
# the powerswitch call directly to the lightbulb, to turn on,off the lightbulb. 
# we are going to use dependency inversion to remove this dependency. 
# to do this, we're gonna to use un abstract class. In a abstract class you can
# specify what interface should be that a class should adhere. 

# we remove the dependency between class. The param is the interface/abstract class, NOT the class itself.