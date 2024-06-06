def print_hollow_square(size):
    if size < 3:
        print("Size should be at least 3.")
        return

    # Print the upper part of the square
    print("*" * size)
    for _ in range(size - 2):
        print("*" + " " * (size - 2) + "*")

    # Print the lower part of the square
    print("*" * size)

print_hollow_square(5)  # Adjust the size as per your requirement
