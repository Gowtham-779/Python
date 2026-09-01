"""
1)
A company wants to generate basic salary information when employee objects are created. Create a class Employee with class variables company = "TechCorp" and employee_count = 0. The constructor should accept name, department, salary, and experience. Validate that salary and experience are not negative. Based on experience, calculate a bonus inside the constructor: employees with more than 5 years receive 15%, employees with 3–5 years receive 10%, and employees with less than 3 years receive 5%. Create an instance dictionary pay_details containing the employee’s name, salary, experience, bonus, and final salary. Generate an employee ID using employee_count. Create three employee objects and display their __dict__.
"""
class Employee:
    company = "TechCorp"
    employee_count = 0
    def __init__(self, name, department, salary, experience):
        self.name = name
        self.department = department
        if salary > 0 and experience > 0:
            self.salary = salary
            self.experience = experience
        self.bonus = 0
        if self.experience < 3:
            self.bonus = self.salary*0.05
        elif 3 <= self.experience <= 5:
            self.bonus=self.salary*0.10
        else:
            self.bonus=self.salary*0.15
        Employee.employee_count+=1
        self.pay_details ={
            "name":self.name,
            "salary": self.salary,
            "experience" :self.experience,
            "bonus_":self.bonus,
            "final_salary" : self.bonus+self.salary,
            "employee_id":Employee.employee_count
        }

e1=Employee("Gowtham","CSE",60000,2)
print(e1.__dict__)
e2=Employee("Ramana","CSE",75000,4)
print(e2.__dict__)
e3=Employee("Sid","Ece",69000,6)
print(e3.__dict__)

"""
2)
A mobile store creates a purchase object whenever a customer buys a phone. Create a class MobilePurchase with a class variable store_name = "Smart Mobiles" and purchase_count = 0. The constructor should accept customer, brand, price, storage, and quantity. Validate that price and quantity are positive and that storage is either 64, 128, 256, or 512 GB. Calculate the total price inside the constructor. If the total exceeds ₹50,000, apply a 10% discount; otherwise, apply a 5% discount. Store the complete purchase information in a dictionary called purchase_details. Increment purchase_count for every valid purchase. Create three objects and display their __dict__.
"""
class MobilePurchase:
    store_name = "Smart Mobiles"
    purchase_count = 0
    def __init__(self,customer,brand,price,storage,quantity):
        self.customer = customer
        self.brand = brand
        if price >0 and quantity >0:
            self.price = price
            self.quantity = quantity
        if storage==64 or storage == 128 or storage ==256 or storage ==512:
            self.storage = storage
        self.total_price = self.price* self.quantity
        if self.total_price > 50000:
            self.discount = self.total_price*0.10
        else:
            self.discount = self.total_price*0.05
        MobilePurchase.purchase_count+=1
        self.purchase_details = {
            "Customer":self.customer,
            "Brand": self.brand,
            "Storage":self.storage,
            "Price":self.price,
            "Quantity":self.quantity,
            "Total Bill": self.total_price - self.discount,
            "Purchase ID":MobilePurchase.purchase_count
        }
c1=MobilePurchase("Sa","Samsung",50000,256,2)
print(c1.__dict__)
c2=MobilePurchase("Aa","Apple",80000,256,5)
print(c2.__dict__)
c3=MobilePurchase("fa","Ntg",45000,512,1)
print(c3.__dict__)

"""
3)
Create a class Product with a class variable store = "ShopEasy". The constructor should accept name, price, and quantity and create an instance dictionary product_details containing the product name, price, quantity, and the calculated total price.

Create two Product objects. After creating the objects, change the price of the first product using its instance variable. Then change the price stored inside the product_details dictionary of the first product.

Display the __dict__ of the first product and explain why the two price values can be different.
"""
class Product:
    store = "ShopEasy"
    def __init__(self,name,price,quantity,):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.product_details ={
            "Name" : self.name,
            "Price" :self.price,
            "Quantity" : self.quantity,
            "Total Price" : self.price * self.quantity,
        }
        if self.product_details["Price"] != self.price :
            self.price = self.product_details["Price"]

p1 = Product("Spoon",50,5)
print(p1.__dict__)
p1.name="Fork"
# p1.product_details["Price"]=60
p1.price = 60
print(p1.__dict__)
p2 = Product("Jar",100,5)
print(p2.__dict__)