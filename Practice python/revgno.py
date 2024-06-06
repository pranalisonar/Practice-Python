def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num = num // 10
    return reversed_num
num = 12345
reversed_number = reverse_number(num)
print("Original number:", num)
print("Reversed number:", reversed_number)
