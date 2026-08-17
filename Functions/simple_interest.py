"""
Write a function simple_interest(principal, rate=5, time=1) to calculate simple interest.
Demonstrate different function calls by passing only required arguments and then overriding
default values.
"""
def simple_interest(principal , rate = 5 , time=1):
    print(f"Simple Interest : {principal + principal * (rate / 100) * time}")

simple_interest(2000)
simple_interest(5000 , 6)
simple_interest(70000 ,4 , 2)
simple_interest(4000 ,rate=4)
simple_interest(6000 ,rate =3 , time =2)
simple_interest(5000,time=4,rate=6)