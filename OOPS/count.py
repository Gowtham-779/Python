class Student:
    count=0
    def __init__(self):
        Student.count+=1

obj1=Student()
obj2=Student()
print(Student.count)