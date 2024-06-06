def print_T_pattern(size):
    if size < 3:
        print("Size should be at least 3.")
        return

    # Printing the T pattern
    for i in range(size):
        if i == 0:
            print("*" * size)
        else:
            print(" " * (size // 2) + "*")

print_T_pattern(5)  # Adjust the size as per your requirement
