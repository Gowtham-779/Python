"""
A bank wants to create a simple system to store customer account details.
Create a class BankAccount with a class variable bank_name = "ABC Bank" and instance variables
account_holder, account_number, and balance. Initialize the instance variables using a constructor.
 The constructor should validate that the initial balance is not negative; if it is negative,
  set the balance to 0. Create two account objects and display their details.
"""
class BankAccount:
    bank_name="ABC Bank"
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number =account_number
        if balance <0:
            self.balance=0
        else:
            self.balance = balance
print(BankAccount.__dict__)
obj1= BankAccount("hi",1231,-25)

print(obj1.__dict__)
obj2 = BankAccount("hello",123541,500)
print(obj2.__dict__)


"""
A college wants to maintain student records.
 Create a class Student with a class variable college = "ABC College" and instance variables name,
  roll_no, and marks. Initialize these values using _init_(). 
  The constructor should validate that marks are between 0 and 100; 
  if invalid marks are provided, set them to 0. Create three student objects and display 
  their details
"""
class Student:
    college="ABC College"
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        if 0 < marks < 100:
            self.marks= marks
        else:
            self.marks=0
s1=Student("Gowtham",21,45)
print(s1.__dict__)
s2=Student("Gow",45,-23)
print(s2.__dict__)
s3=Student("G",45,0)
print(s3.__dict__)
"""
An online store wants to maintain a list of products added to its system.
 Create a global list products = []. Create a class Product with a class variable
  store_name = "ABC Store" and instance variables name, price, and quantity. 
  Initialize the values using the constructor and validate that price and quantity 
  cannot be negative. Whenever a product object is created, add its name to the global products
   list. Create three products and display the product details and the complete product list.
"""
product=[]
class Product:
    store_name = "ABC Store"
    def __init__(self,name,price,quantity):
        global product
        self.name = name
        if price >0 and quantity >0:
            self.price= price
            self.quantity= quantity
        else:
            print("Invalid")
        product.append(self.name)



p1 = Product("Apple",25,1)
print(p1.__dict__)
p2 = Product("chocolate",23,1)
print(p2.__dict__)
p3= Product("milk",50,1)
print(p3.__dict__)
print(product)
