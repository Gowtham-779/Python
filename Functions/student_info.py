"""
Create a function student_info(name, *subjects, **details) that prints a
student’s name, subjects enrolled, and additional details like grade and school
"""



def student_info(name,*subjects,**details):
    print("Name :" , name)
    print("Subjects :" , end =" ")
    print(*subjects)
    print("Details :")
    for detail,value in details.items():
        print(f"{detail} = {value}")

student_info("Gowtham","Maths","Physics","Social","English" ,
             age = 16 ,
             grade = 10,
             School= "Kallam Anji Reddy Vidyalaya" ,
             hobbies= ["Reading" , "Playing" , "Watching movies"])