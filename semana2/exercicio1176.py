def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

t = int(input())
for _ in range(t):
    n = int(input())
    print(f"Fib({n}) = {fib(n)}")
