from random import *
a=randint(1000,9999)
print("OTP for verification is",a)
b=int(input("Enter a OPT: "))
if(a==b):
    print("Access granted")
else:
    print("Access Denied")