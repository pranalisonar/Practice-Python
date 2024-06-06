def print_J_pattern(size):
    if size < 3:
        print("Size should be at least 3.")
        return

    # Upper part of 'J'
    for i in range(size):
        if i == 0:
            print("*" * size)
        elif i == size // 2:
            print("*" + " " * (size - 2) + "*")
        else:
            print(" " * (size // 2) + "*")

print_J_pattern(5)  # Adjust the size as per your requirement
