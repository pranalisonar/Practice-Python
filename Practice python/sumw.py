def sonn(n):
    total = 0
    count = 1
    while count <= n:
        total += count
        count += 1
    return total
n = int(input("Enter a no. : "))
print("Sum of first", n, "natural numbers:", sonn(n))
