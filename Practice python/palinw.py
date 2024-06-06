def palin(num):
    og_num = num
    rev_num = 0
    while num > 0:
        digit = num % 10
        rev_num = (rev_num * 10) + digit
        num //= 10
    return og_num == rev_num
num=int(input("enter a no: "))
if palin(num):
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
