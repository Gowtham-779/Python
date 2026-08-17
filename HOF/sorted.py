
students =[
    {'name':'Alice','score':85,},
    {'name':'henry','score':70,},
    {'name':'candy','score':92,}
]
print(sorted(students,key=lambda x:x['score']))
print(sorted(students,key=lambda x:x['score'],reverse=True))
print(sorted(students,key=lambda x:x['name']))
print(sorted(students,key=lambda x:x['name'],reverse=True))
print(sorted(students,key=lambda x:len(x['name'])))

usernames= ["gowtham","sai","ramana","aditya"]
print(sorted(usernames,key=lambda x:len(x)))
print(sorted(usernames,key=lambda x:len(x)<=5))

#2

l=["gowtham","Sai","Ram","danny","rocky"]
print(list(filter(lambda x:x[0].isupper() ,l)))

from functools import reduce

#3
# l=[1,2,3,4,5]
# print(reduce(lambda x,y:x*y,l))

#4
value = [('gowtham',21),
         ('ram',22),
         ('sai',21),
         ('satish',25)]
print(sorted(value,key=lambda x:x[0],reverse=True))

#5
l=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:x**2,(filter(lambda x:x%2==1,l)))))

#7
l=['cat','elephant','dog','rhinoceros']
print(reduce(lambda x,y:x if len(x)>len(y) else y,l))

#6
l=[1,2,3,4,5,6,7,8,9]
def square(x):
    return x**2
def my_map(func,lst):
    x=0
    for i in lst:
        x= x+func(i)
    return x
print(my_map(square,l))





