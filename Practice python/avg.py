n = int(input("enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
average = sum / n
print("the average of first", n, "natural no is", average)