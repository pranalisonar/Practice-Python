def print_H(size):
    if size < 3 or size % 2 == 0:
        print("Size should be an odd number greater than or equal to 3.")
        return

    for i in range(size):
        if i == size // 2:
            print("*" * size)
        else:
            print("*" + " " * (size - 2) + "*")

print_H(5)  