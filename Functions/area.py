"""
Write a function area(length, breadth=None) that calculates the area of a rectangle.
If breadth is not provided, assume it is a square and compute accordingly.
"""
def area(length,breadth=None):
    if not breadth:
        print("Area of square :" ,(length*length))
    else:
        print("Area of rectangle:" ,(length*breadth))
area(3)
area(3,6)