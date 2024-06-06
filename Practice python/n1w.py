def print_natural_numbers(n):
    count = 1
    while count <= n:
        print(count)
        count += 1
n = int(input("enter the value of 'n': "))
print("first", n, "natural numbers:")
print_natural_numbers(n)
