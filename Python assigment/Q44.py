#Write a program to demonstrate generator function for Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print("Fibonacci series (first 10 terms):", list(fibonacci(10)))