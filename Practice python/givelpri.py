n1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = []
for num in n1 :
    if num == 0 or num == 1 :
        continue
    for i in range(1, num // 2 + 1) :
        if num % i == 0 :
            break
    else :
        l.append(num)
if len(l) :
    print("prime number : ",end = "-> ")
    for ans in l :
        print(ans, end = ", ")
