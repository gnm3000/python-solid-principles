class LightBulb:
    def turn_on(self):
        print("LightBulb: turned on...")
    
    def turn_off(self):
        print("LightBulb: turned off...")
        
class ElectricPowerSwitch:
    
    def __init__(self, l:LightBulb):
        self.lightBulb = l
        self.on = False
        
    def press(self):
        if self.on:
            self.lightBulb.turn_off()
            self.on = False
        else:
            self.lightBulb.turn_on()
            self.on = True
            
l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()

# here we can see a dependency between the light bulb and the PowerSwitch. because 
# the powerswitch call directly to the lightbulb, to turn on,off the lightbulb. 
# we are going to use dependency inversion to remove this dependency. 
# to do this, we're gonna to use un abstract class. In a abstract class you can
# specify what interface should be that a class should adhere. 