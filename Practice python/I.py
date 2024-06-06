def print_I_pattern(size):
    if size < 3:
        print("Size should be at least 3")
        return

    # Upper part of 'I'
    for i in range(size):
        if i == size // 2:
            print("*" * size)
        else:
            print(" " * (size // 2) + "*")

print_I_pattern(5)  # Adjust the size as per your requirement
