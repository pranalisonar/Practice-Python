def print_Z(size):
    if size < 2:
        print("Size should be at least 2.")
        return
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or i + j == size - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_Z(5)  
