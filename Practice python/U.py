def print(size):
    if size < 3:
        print("Size should be at least 3.")
        return

    print("*" + " " * (size - 2) + "*")
    for _ in range(size - 2):
        print("*" + " " * (size - 2) + "*")

    print("*" * size)

print(5)  
