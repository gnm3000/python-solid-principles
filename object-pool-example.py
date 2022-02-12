
from typing import List

class Reusable:
    def test(self):
        print(f"Using object {id(self)}")
        
class ReusablePool:
    
    def __init__(self,size):
        self.size=size
        self.free=[]
        self.in_use=[]
        for _ in range(size):
            self.free.append(Reusable())
    def acquire(self) -> Reusable:
        if(len(self.free)<=0):
            raise Exception("No more objects are available")
        r = self.free[0]
        self.free.remove(r)
        self.in_use.append(r)
        return r 
    
    def release(self,r:Reusable):
        self.in_use.remove(r)
        self.free.append(r)
        
        
pool = ReusablePool(2)
r = pool.acquire()
r2 = pool.acquire()

r.test()
pool.release(r2)
r3 = pool.acquire()

r2.test()
r3.test()
