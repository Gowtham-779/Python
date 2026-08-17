#1.
store_prices = [200,400,500,600,700]
print(list(map(lambda x:int(x+x*0.10),store_prices)))
#________________________________________________________________

#2
usernames =["gowtham","ramana","satish"]
x=list(map(lambda x: x[0].upper()+x[1:],usernames))
print(x)
#or x.capitalize()
#________________________________________________________________

#3
prices = [299,370,650,170,980,800,920,150]
print(list(filter(lambda x: x>500 ,prices)))
#________________________________________________________________

#4
numbers = [1,2,3,4,5,6,7]
print(list(map(lambda x: x*5,numbers)))
#________________________________________________________________

#5
names = ["gowtham","ramana","siddu","satish","shiva"]
print(list(map(lambda x:len(x),names)))
#________________________________________________________________

#6
numbers = [1,70,60,22,35,69,40,47,52,63]
print(list(filter(lambda x: x>50,numbers)))
#________________________________________________________________

#7
numbers = [4,9,12,16,22,15,47,28]
print(list(filter(lambda x:x%4==0,numbers)))

#________________________________________________________________
numbers = [4,9,12,16,22,15,47,28]
print(list(filter(lambda x:x%4==0,(map(lambda x: x**2,numbers)))))

l = [10,20,3,7,4]
print(list(filter(lambda x:x%4==0,list(map(lambda x: x**2,l))))) #single pipeline solution


l=[1,2,3,4,5,6,7,8]
def square(x):
    return x**2
y=lambda x:square(x)
print(y(25))


