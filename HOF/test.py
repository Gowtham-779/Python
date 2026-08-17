from functools import reduce
# def weighted_average(**scores):
#     x=0
#     avg=0
#     for key,values in scores.items():
#
#
#
# weighted_average(maths=45,english=66,chemsitry=90)

#1.
# prices = [2900,2000, 3500, 2500,1000]
# x= list(map(lambda x:x-(x*0.1),filter(lambda x:x>500,prices)))
# print(x)

#2
# l= [-1,-2,8,16,-6,-5,3]
# print(reduce(lambda x,y:x+y,(map(lambda x:x*(-1),
#                            filter(lambda x:x<0,l)))))

#3
# l=[40,60,50,30,20,100,77,65,24]
# print(reduce(lambda x,y:x if x>y else y,
#              map(lambda x:x*3,
#                  filter(lambda x:x<50,l))))

#4
# l = ["mary","jon","sony","rox","ved","valli"]
# print(reduce(lambda x,y:x+" "+y,
#                              map(lambda x:x.upper(),
#                                  filter(lambda x:len(x)>3,l))))

#5
# l=[20000,40000,33000,45000]
# print(reduce(lambda x,y:x+y,filter(lambda x:x>30000,l)))

#6
# l=[1,2,3,4,5,6,7,8,9,10]
# print(reduce(lambda x,y:x+y,filter(lambda x:x%2==1,l)))

#7
# l=[200,300,500,600,700,900]
# print(reduce(lambda x,y:x+y,map(lambda x:x-x*0.10,
#                                 filter(lambda x:x>500,l))))

#8
# l=[-1000,2000,-500,6000,-2000,40000]
# print(reduce(lambda x,y:x+y,map(lambda x:x+10,l)))