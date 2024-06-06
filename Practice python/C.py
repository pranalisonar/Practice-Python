def print_C(size):
    if size < 3:
        print("Size should be at least 3.")
        return
    print("*" * size)
    for _ in range(size - 2):
        print("*")
    print("*" * size)
print_C(5)  