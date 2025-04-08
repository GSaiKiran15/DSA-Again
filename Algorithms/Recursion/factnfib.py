def factorial(n):
    if n <= 2:
        return n
    return n * factorial(n-1)

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

print(factorial(5),fib(7))
