list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1 = []
for num in list :
    if num == 0 or num == 1 :
        continue
    for i in range(2, num // 2 + 1) :
        if num % i == 0 :
            break
    else :
        l1.append(num)
if len(l1) :
    print("Prime Number : ",end = "-> ")
    for ans in l1 :
        print(ans, end = ", ")
