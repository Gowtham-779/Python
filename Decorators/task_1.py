"""
1.Create a function get_message() that returns "hello user".
 Write a decorator using @ syntax that converts the output to uppercase.
 """

def decorator1(func):
    def wrapper():
        print(func().upper())
    return wrapper

@decorator1
def get_message():
    return "hello user"
get_message()


"""
2.     Create a function get_number() that returns 10
    Use a decorator to return double the value.
"""
def decorator2(func):
    def wrapper2():
        return func()*2
    return wrapper2

@decorator2
def get_number():
    return 10
print(get_number())

"""
3.     Create a function place_order(item)
    Use a decorator to print:
    * “Order process started”
    * “Order process completed”
"""
def decorator3(func):
    def wrapper3(a):
        print("Order process started")
        func(a)
        print("Order process completed")
    return wrapper3

@decorator3
def place_order(item):
    print(item)

place_order("Biryani")
"""
4.     Create a function login(username)
    Use a decorator to print:
    * “Authenticating user…”
    * “Login successful”
"""
def decorator4(func):
    def wrapper4(name):
        print("Authentication user")
        func(name)
        print("Login successful")
    return wrapper4

@decorator4
def login(username):
    print(username)
login("Gowtham")
"""

5.     Create a function send_message(msg)
    Use a decorator to print:
    * “Sending message…”
    * “Message sent”
"""
def decorator5(func):
    def wrapper5(msg):
        print("Sending message")
        func(msg)
        print("Message sent")
    return wrapper5
@decorator5
def send_message(msg):
    print(msg)
send_message("Hello")

"""
6.     Create a function add(a, b)
    Use a decorator to print:
    * “Calculating sum…”
    * “Calculation done”
"""
def decorator6(func):
    def wrapper6(a,b):
        print("Calculating sum")
        func(a,b)
        print("Calculation done")
    return wrapper6

@decorator6
def add(a,b):
    print(a+b)
add(10,20)
"""
7.     Create a function apply_discount(price)
    Use a decorator to print:
    * “Applying discount…”
    * “Discount applied”
"""
def decorator7(func):
    def wrapper7(price):
        print("Applying discount")
        print(f"Total-price: {func(price)}")
        print("Discount applied")
    return wrapper7

@decorator7
def apply_discount(price):
    return price-(price*0.10)
apply_discount(1000)

#with arbitrary values
def decorator8(func):
    def wrapper8(*args,**kwargs):
        func(*args,**kwargs)
        print("Discount Applied")
    return wrapper8

@decorator8
def apply_discount2(*prices):
    for price in prices:
        print(price-50)
apply_discount2(100,200,300,400,500)