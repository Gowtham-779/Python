"""
1.Create a function start_system()
    Write a decorator that prints:
    * “System starting…” before execution
    * “System started successfully” after execution
"""
def start_system():
    print("System started successfully")
def decorator(func):
    def wrapper():
        print("System starting")
        func()

    return wrapper
modify = decorator(start_system)
modify()

print()
"""
2. Create a function show_message()
    Write a decorator that prints:
    * “Welcome!” before
    * “Goodbye!” after
"""
def show_message():
    print("GoodBye!")
def decorator(func):
    def wrapper_2():
        print("Welcome")
        func()
    return wrapper_2
x= decorator(show_message)
x()

print()
"""
3.Create a function make_payment()
    Write a decorator that prints:
    * “Payment initiated”
    * “Payment successful”
"""
def make_payment():
    print("Payment Successful")
def transaction(func):
    def process():
        print("Payment Initiated")
        func()
    return process
trans= transaction(make_payment)
trans()