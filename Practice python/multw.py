def multiplication_table(num):
    multiply = 1
    while multiply <= 10:
        result = num * multiply
        print(num, "x", multiply, "=", result)
        multiply += 1

num = int(input("Enter a number for multiplication table: "))
multiplication_table(num)
