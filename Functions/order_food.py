"""
Write a function order_food(*items, **preferences) that accepts multiple food items
and optional preferences like spice level or delivery time.
Display the order summary.
"""
def order_food(*items , **preferences):
    print("Items : " )
    for item in items:
        print(item)
    print("Preferences :")
    for note,value in preferences.items():
        print(f"{note} = {value}")


order_food("Roti 10" , "Butter Naan" , "Panner butter masala" ,  "Coke" , "Chill water bottle",
           Bags = "Separate bags for cold and hot items " ,
           Cutlery = "Yes",
           Note = "Leave it at the door step.")