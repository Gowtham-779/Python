def greet(name):
    print("My name is ",name)
def hi(func):
    print("Hi!",end=" ")
    func("Gowtham")
hi(greet)

# m1 -> wrapper

def intro():
    print("Hello")
def decorator1(func):
    def wrapper1():
        print("hi")
        func()
    return wrapper1
modify= decorator1(intro)
modify()