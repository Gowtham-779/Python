list1=[1,2,3,4,5]
b= list(map(lambda x: x**2,list1))
print(b)

def square(x):
    return x**2

x= list(map(square,list1))
print(x)



l1= [1,2,3,4]
l2 = [5,6,7,8,9,3]
x= list(map(lambda x,y: x+y,l2,l1))
print(x)

l3 = [5,6,7,8,9,3]
x= list(map(lambda x: x/2,l3))
print(x)