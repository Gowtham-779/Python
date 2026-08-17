def decorator1(func):
    def wrapper8(*args, **kwargs):
        y = func(*args, **kwargs)
        return y
        print("Discount Applied")
    return wrapper8

def decorator2(func):
    def wrapper8(*args, **kwargs):
        y = func(*args, **kwargs)
        print(y)
        return y
    return wrapper8

@decorator2
@decorator1
def apply_discount(*prices):
    l=[]
    discount=50
    for price in prices:
        l.append(price-discount)
    return l
x = apply_discount(100,200,300,400,500)
apply_discount(*x)
#y=apply_discount(apply_discount(100,200,300,400,500))
#print(y)