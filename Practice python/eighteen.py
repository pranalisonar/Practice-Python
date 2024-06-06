from datetime import datetime, timedelta
def dob(birthdate):
    turned_18 = birthdate + timedelta(days=18*365.25) 
    today = datetime.now().date()
    return today >= turned_18
birthdate_str = input("enter your birthdate (DD-MM-YYYY): ")
birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y").date()
if dob(birthdate):
    print("you have turned 18.")
else:
    print("you have not yet turned 18.")
