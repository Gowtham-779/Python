""""
1. Given a list of tuples (name, marks), sort the list:
    * first by marks (descending)
    * then by name (ascending)
2. Given a list of strings, sort them based on:
    * length of string
    * and then alphabetically
"""
#1
details = [
    ("abi",65),
    ("ram",76),
    ("singh",83)
]
print(sorted((sorted(details,key=lambda x:x[1],reverse=True)),key=lambda x:x[0]))

#2
names = ["abi","ram","singh","malli"]
print(sorted((sorted(names,key=lambda x:len(x))),key=lambda x:x))

""""
Given a list of integers, filter numbers divisible by both 2 and 5, add 5 to each using map(),
 then find the product using reduce().
 """

l =[23,45,76,10,55,96,16,69]
print(list(map(lambda x:x+5,filter(lambda x:x%2==0 and x%5==0,l))))