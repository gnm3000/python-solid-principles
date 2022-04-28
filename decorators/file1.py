def f1(func):
    def wrapper(*args, **kwargs):
        print("started")
        val=func(*args, **kwargs)
        print("end")
        return val
    return wrapper

@f1
def f(a,b=9):
    print(a,b)

@f1
def add(x,y):
    return x+y

#print(add(6,5))
#f1(f)()

f("hello")