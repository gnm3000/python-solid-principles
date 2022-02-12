class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwds)
        return cls._instances[cls]
    
class Logger(metaclass=Singleton):
    def log(self,msg):
        print(msg)
        
        
logger1 = Logger()
logger2 = Logger()
print(logger1)
print(logger2)
logger1.log("Hi")
logger2.log("Hello")

"""
This is an antipattern because:
- Its hard to test
- If you have subclasses from a singleton you will have multiple instances
- Break OOP Principle Design
- Can not fully control of creation
"""
