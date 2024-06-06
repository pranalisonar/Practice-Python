import datetime
a=datetime.datetime.now()
b=datetime.datetime(2002, 6, 22)
diff_year=a.year-b.year
diff_month=a.month-b.month
diff_day=a.day-b.day
def dob():
    if (diff_year >= 0):
        if (diff_month > 0):
            if (diff_day > 0):
                print(diff_year, diff_month, diff_day)
            else:
                print(diff_year, diff_month - 1, diff_day + 30)
        else:
            if (diff_day > 0):
                print(diff_year - 1, diff_month + 11, diff_day)
            else:
                print(diff_year - 1, diff_month + 10, diff_day + 30)
dob()