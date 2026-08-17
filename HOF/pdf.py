from functools import reduce
"""
Q1.  PARAMETERS + LAMBDA: Write a function apply_operation(a, b, op)
where op is a lambda. Call it with operations for add, subtract, and multiply.
"""


# def apply_operation(a,b,op):
#     return op(a,b)
# add = lambda x,y:x+y
# sub = lambda x,y:x-y
# mul = lambda x,y:x*y
#
# print(apply_operation(2,3,add))
# print(apply_operation(5,3,sub))
# print(apply_operation(5,6,mul))

"""
Q2.  *args + RECURSION: Write a recursive function that takes *args of numbers and
 returns their sum WITHOUT using the built-in sum().
"""
# def rec_sum(*args):
#     sum=0
#     for i in args:
#         sum+=rec_sum(i)
#     return sum
# print(rec_sum(1,2,3,4,5,6,7,8,9))

"""
Q3. DEFAULT + KEYWORD + LAMBDA: Write a function make_greeting(name, prefix='Hello',
 formatter=lambda x: x) that applies formatter to the final greeting string.
Test with str.upper as the formatter.
 """
# def make_greeting(name,prefix='Hello',formatter=lambda x:x):
#     greeting=prefix+" "+name
#     print(formatter(greeting))
# y=lambda x:x.upper()
# make_greeting(name='gowtham',formatter=y)

"""
Q10.  ALL CONCEPTS: Write a function calculator(*args, operation='add', **options) that: 
(a) uses *args to collect numbers, 
(b) uses a default 'add' operation, 
(c) supports operations: 'add', 'multiply', 'max', 'min' using a dict of lambda functions, 
(d) if options contains show_steps=True, prints each step of the calculation
"""
# def calculator(*args,operation='add',**options):
#     if options['show_steps']:
#         Total= args[0]
#         for i in args[1:]:
#             print(f"{Total} {operation} {i} =",end=" ")
#             Total=operations[operation](Total,i)
#             print(Total)
#
#         pass
#     else:
#         Total = args[0]
#         for i in args[1:]:
#             Total = operations[operation](Total,i)
#         print(Total)
#
#
# operations={
#     'add':lambda x,y:x+y,
#     'sub':lambda x,y:x-y,
#     'mul':lambda x,y:x*y,
#     'div':lambda x,y:x/y,
#     'max':lambda x,y:x if x>y else y,
#     'min':lambda x,y : x if x<y else y
# }
#
# calculator(10,20,30,40,operation='max',show_steps=True)

"""
Q9.  LAMBDA + sorted() + FUNCTION REFERENCE: Store three sort strategies in a 
dictionary: by_name, by_score, by_length. Let the user choose a strategy by name, 
then apply it to sort a list of tuples
"""

# students = [
#     ("Amit", 90),
#     ("Rahul", 75),
#     ("Priya", 90),
#     ("Sneha", 82),
#     ("Karanye", 75)
# ]
# by_type={
#     "by_name":lambda x:x[0],
#     "by_score":lambda x:x[1],
#     "by_length":lambda x:len(x[0])
# }
# print(sorted(students, key = by_type['by_score'],reverse=True))

"""
Q8.  FULL PIPELINE: Build a mini data pipeline. 
Start with a list of student dictionaries [{name, score}]. Use filter() to keep scores >= 60,
 map() to add a 'grade' key ('Pass'), and sorted() to sort by score descending.
  Print the final result. 
"""
students = [
    {"name": "Amit", "score": 89},
    {"name": "Rahul", "score": 45},
    {"name": "Priya", "score": 90},
    {"name": "Sneha", "score": 52},
    {"name": "Karan", "score": 75}
]

# list(map(lambda x:x.update({'grade':'pass'}),
#          filter(lambda x:x["score"]>=60,students)))
# print(students)
#
# sorted(students,key=lambda x:x['score'])
# print(students)
"""
66. Given a list of transactions where each transaction contains a type (credit or debit) 
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
print(reduce(lambda x,y:x+y,sorted(list(map(lambda x:x['amount']+x['amount']*0.05,
    filter(lambda x:x['type']=='credit',transactions))),
             key=lambda x:x,reverse=True)))