"""
Write a function shopping_cart(discount=0, *prices) that calculates
the total price after applying a discount.
Demonstrate calling the function with and without the discount argument.
"""

def shopping_cart(discount=0, *prices):
    sum = 0
    for price in prices:
        sum += price
    print(f"Total cart value : {sum - discount}")



shopping_cart(250,450,60,900,475)
#shopping_cart(discount = 25, 450 , 650 , 954) ---> error : positional argumets cannot follow keyword arguments
