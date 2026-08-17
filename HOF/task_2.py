#1
l= [2000,500,250 , 600 , 700, 360,900]
print(list(map(lambda x:x-x*0.1,filter(lambda x: x>500,l))))

#_______________________________________________________________________
#2
l=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:x*3,filter(lambda x:x%2==0,l))))

#_______________________________________________________________________
#3
l=[10,20,22,50,75,63,47]
print(list(map(lambda x:x**2,filter(lambda x: x>20,l))))

#_______________________________________________________________________
#3
usernames =["gowtham","ram","satish"]
print(list(map(lambda x:x.upper(),filter(lambda x:len(x)>4,usernames))))

#4
l=[11,20,33,40,50,62]
print(list(map(lambda x:x+10,filter(lambda x:x%5==0,l))))

#_______________________________________________________________________
#5
l=[47,40,63,72,63,75]
print(list(map(lambda x:x+5,filter(lambda x: x>40,l))))
