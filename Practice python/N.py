def print_N(size):
    if size < 2:
        print("Size should be at least 2.")
        return
    for i in range(size):
        for j in range(size):
            if j == 0 or j == size - 1 or i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_N(5) 