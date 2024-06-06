def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False
year = int(input("Enter a year: "))
if leap_year(year):
    print(str(year) + " is a leap year")
else:
    print(str(year) + " is not a leap year")
