"""
7. Define a function login(username, password="1234").
Demonstrate how default arguments work and
explain a potential issue with using default passwords
"""
def login(username,password = '1234'):
    print("Username :" ,username)
    print("Password :",password)
    print()

login("gowtham")
login("gowtham",password=76045)