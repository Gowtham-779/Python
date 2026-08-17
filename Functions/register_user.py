"""
Design a function register_user(username, role="user", *permissions, **details)
that stores user information, including optional permissions and additional attributes.
"""

def register_user(username , role='user',*permissions , **details):
    print("Username :" ,username)
    print("Role :",role)
    if permissions:
        print("Permissions :")
        for permission in permissions:
            print(permission)
    if details:
        print("Details: ")
        for key,value in details.items():
            print(f"{key} : {value}")
    print()

register_user("mahesh")
register_user("gowtham","employee")
register_user("reyansh", "manager" , "approve_leave","manage_schedule",
              "edit_schedule")
register_user("martin",age=57 , email="martin23@gamil.com")