n = []
for i in range(1, 700):
    if i % 7 == 0 and i % 9 == 0:
        n.append(i)

print("numbers divisible by both 7 and 9:")
for num in n:
    print(num)
