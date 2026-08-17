"""
 PARAMETERS + LAMBDA: Write a function apply_operation(a, b, op) where op is a lambda.
 Call it with operations for add, subtract, and multiply.
"""
def apply_operation(a,b,op):
    for key,value in op.items():
        print(f"{key} = {value(a,b)}")


operations={
    'addition': lambda a,b:a+b,
    'subtraction': lambda a,b:a-b,
    'multiplication': lambda a,b:a*b
}

apply_operation(10,20,operations)


""""
DEFAULT + KEYWORD + LAMBDA: Write a function
 make_greeting(name, prefix='Hello', formatter=lambda x: x) that applies formatter 
 to the final greeting string. Test with str.upper as the formatter. 
"""

def make_greeting(name,prefix='hello',formatter=lambda x:x):
    message = name +' '+prefix
    print(formatter(message))


make_greeting("Gowtham",formatter = lambda x:x.upper())
