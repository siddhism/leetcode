cache = {}
def fib(n):
    if n == 0 or n == 1:
        cache[n] = n

    if cache.get(n) is not None:
        return cache.get(n)

    output = fib(n-1) + fib(n-2)
    cache[n] = output
    print ('computed fib for n ', n)
    return output

fib(100)