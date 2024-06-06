from datetime import datetime
DOB=input("Enter Your Birth date in DD-MM-YYYY")
p=datetime.strptime(DOB, "%d-%m-%Y")
a=datetime.now()
diff_year=a.year-p.year
diff_month=a.month-p.month
diff_day=a.day-p.day
def dob():
    if (diff_day>0):
        if (diff_month>0):
            print("Year=",diff_year)
            print("Month=",diff_month)
            print("Day=",diff_day)
        else:
            print("Year=",diff_year-1)
            print("Month=",diff_month+12)
            print("Day=",diff_day)
    elif (diff_month>0):
        print("Year=",diff_year)
        print("Month=",diff_month-1)
        print("Day=",diff_day+31)
    else:
        print("Year=",diff_year-1)
        print("Month=",diff_month+11)
        print("Day=",diff_day+31)
dob()