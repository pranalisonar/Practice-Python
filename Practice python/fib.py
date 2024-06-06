def fib(n1, n2, n):
    fib_series = [n1, n2]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series
n1 = 1
n2 = 1
num_terms = 10
series = fib(n1, n2, num_terms)
print("Fibonacci Series:", series)
