def prime_numbers(n):
    prime = []
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime
n = int(input("Enter the value of n: "))
print("The prime numbers from 1 to", n, "are:")
print(prime_numbers(n))