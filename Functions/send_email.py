"""
Design a function send_email(sender, receiver, subject="No Subject", *attachments,
 **options)
that simulates sending an email with optional attachments and settings.
"""
def send_email(sender,receiver,subject="No Subject",*attachments,**options):
    print("Sender : ", sender)
    print("Receiver : ",receiver)
    print("Subject :" , subject)
    if attachments:
        print("Attachments :")
        for attachment in attachments:
            print(attachment)

    if options:
        print("Options :")
        for option,value in options.items():
            print(f"{option} = {value}")

send_email("gowtham@gmail.com","shiva@gmail.com","Electricity bill",
           "bill.pdf","prev_bill.png",
            date ="18-07-2026",urgent= "Yes"
           )