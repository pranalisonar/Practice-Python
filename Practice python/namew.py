def output(name, n):
    while n > 0:
        print(name)
        n -= 1
name = input("enter your name: ")
times = int(input(" how many times should it print your name? "))
output(name, times)

