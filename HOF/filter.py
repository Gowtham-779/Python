def is_even(x):
    if x%2 ==0:
        return True
    else:
        return False

l= [17,15,16,98,76,12,6]
x=list(filter(is_even,l))
print(x)

l=[1,2,3,4]
p=list(map(lambda x: x**2,l))
print(p)
q=list(filter(is_even,p))
print(q)

#or
l=[1,2,3,4]
print(list(filter(is_even,list(map(lambda x: x**2,l)))))


