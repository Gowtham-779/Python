"""
Write a program to create a list containing dictionaries.
Perform a shallow copy and a deep copy of the list.
Modify a value inside one of the dictionaries in the original list and display all lists.
Explain the observed behavior.
"""
import copy

list1 =[{
        "one":1, "two":2, "three":3, "four":4
         },
        {
        "five":5, "six":6, "seven":7, "eight":8
        }]
#deep copy
print("deep copy")
dp_c = copy.deepcopy(list1)
dp_c[0]["three"]=5
print(list1)
print(dp_c)

print()
#shallow copy
print("shallow copy")
sw_c = copy.copy(list1)
sw_c[1]["seven"]=70
print(list1)
print(sw_c)
