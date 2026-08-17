from functools import reduce
"""
1.Given a list of strings, write a program using reduce() to concatenate all strings into a
single string
"""
text = ["Apple","is","a","product","company"]
print(reduce(lambda x,y:x+" "+y,text))

"""
2.Given a list of digits, write a program using reduce() to form a single number 
(e.g., [1,2,3] → 123).
"""
l =[1,2,3]
print(reduce(lambda x,y:x+y,l))