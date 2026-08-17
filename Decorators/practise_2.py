def add(*args,**details):
    sum=0
    for i in args:
        sum+=i
    print(sum)
    for key,value in details.items():
        print(f"{key} : {value}")

def dec1(func):
    def wrapper1(*args,**kwargs):
        print("Before")
        func(*args,**kwargs)
    return wrapper1
x= dec1(add)
x(10,20,30,40,name="Gowtham",major="CS")

#manual
def add(a,b):
    print(a+b)
def decorator1(func):
    def wrapper(*args,**kwargs):
        print("Before calling")
        func(*args,**kwargs)
    return wrapper
add= decorator1(add)
add(10,20)

#shorthand

@decorator1
def add(a,b):
    print(a+b)
add(20,30)