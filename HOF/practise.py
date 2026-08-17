"""
6. Given a list of transactions where each transaction contains a type (credit or debit)
 and an amount, write a program to filter only the credit transactions,
 apply a 5% bonus to each transaction amount using map(),
 sort the updated transactions in descending order based on the amount,
  and finally compute the total credited amount using reduce().
INPUT:
"""
transactions = [
    {"type": "credit", "amount": 1000},
    {"type": "debit", "amount": 500},
    {"type": "credit", "amount": 2000}
]

for i in transactions:
    for key,value in i.items():
        print(key,value)

y=list()

from functools import reduce
k=list()
print(k)
d = sorted(map((lambda x:x['amount']+x['amount']*0.05),
               filter(lambda x:x['type']=='credit',transactions)),
           key = lambda x:x , reverse=True)
print(d)
l = reduce(lambda x,y :x+y,d)
print(l)
"""
5. Given a list of words:

* Filter words that start and end with the same letter
* Convert them to lowercase
* Sort by last character, then length
* Join all words into a single string using reduce()
"""

l=["RADAR","refund","lorry","CIVIC","SAGAS","REVIVER"]

k=sorted(sorted(map(lambda x:x.lower(),
               filter(lambda x:x[0]==x[-1],l)),
             key=lambda x:x[-1]),key=lambda x:len(x))

print(reduce(lambda x,y: x+" "+y,k))

"""
1. Given a list of tuples (name, marks), sort the list:
    * first by marks (descending)
    * then by name (ascending)
2. Given a list of strings, sort them based on:
    * length of string
    * and then alphabetically
"""

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 88),
    ("Eva", 95)
]

print(sorted(sorted(students,key= lambda x:x[1]),
             key= lambda x:x[0]))

students = ["Alice", "Bob", "Charlie", "David", "Eva"]
print(sorted(sorted(students,key=lambda x:len(x)),key=lambda x:x,reverse=True))

