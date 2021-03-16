def fibonacci(n):
    assert n >= 0 and int(n) == n, "The number has to be a positive integer."
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(3))