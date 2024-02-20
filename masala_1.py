def fibonachi(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


N = int(input())
fib_generator = fibonachi(N)
fib_list = list(fib_generator)
print(fib_list)
