def arms(num):
    original_number = num
    num_digits = len(str(num))
    soc = 0
    while num > 0:
        digit = num % 10
        soc += digit ** num_digits
        num //= 10
    return soc == original_number
num = int(input("Enter a no: "))
if arms(num):
    print(num, "is an armstrong number")
else:
    print(num, "is not an armstrong number")
