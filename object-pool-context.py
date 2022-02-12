
"""
Now we are going to create a context manager that automatically 
acquires and releases objects 
"""

from typing import List


class PoolManager():
    def __init__(self, pool):
        self.pool = pool

    def __enter__(self):
        self.obj = self.pool.acquire()
        return self.obj

    def __exit__(self, type, value, traceback):
        self.pool.release(self.obj)


class Reusable:
    def test(self):
        print(f"Using object {id(self)}")


class ReusablePool:

    def __init__(self, size):
        self.size = size
        self.free = []
        self.in_use = []
        for _ in range(size):
            self.free.append(Reusable())

    def acquire(self) -> Reusable:
        if(len(self.free) <= 0):
            raise Exception("No more objects are available")
        r = self.free[0]
        self.free.remove(r)
        self.in_use.append(r)
        return r

    def release(self, r: Reusable):
        self.in_use.remove(r)
        self.free.append(r)


pool = ReusablePool(2)

with PoolManager(pool) as r:
    r.test()
with PoolManager(pool) as r2:
    r2.test()
with PoolManager(pool) as r3:
    r3.test()

# you need reset your object when you release it
# object pool is responsible to reset.
# if you dont reset properly, are gonna to leaking information
