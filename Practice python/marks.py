print("enter a marks of 5 subject: ")
m1 = int(input("enter your sub1 marks"))
m2 = int(input("enter your sub2 marks"))
m3 = int(input("enter your sub3 marks"))
m4 = int(input("enter your sub4 marks"))
m5 = int(input("enter your sub5 marks"))

total = m1+m2+m3+m4+m5
avg = total/5

if avg>=80 and avg<=100:
    print("Your Grade is A")
elif avg>=61 and avg<79:
    print("Your Grade is B")
elif avg>=41 and avg<60:
    print("Your Grade is C")
elif avg>=21 and avg<40:
    print("Your Grade is D")
elif avg>=0 and avg<20:
    print("Your Grade is F")
