n = int(input("Enter the no. triangle: "))

print("1st Quadrant:")
for i in range(1, n+1):
    print('*' * i)

print("\n2nd Quadrant:")
for i in range(1, n+1):
    print(' ' * (n - i) + '*' * i)

print("\n3rd Quadrant:")
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * i)
    
print("\n4th Quadrant:")
for i in range(n, 0, -1):
    print('*' * i)


