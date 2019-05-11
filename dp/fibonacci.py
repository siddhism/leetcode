memo = {}


def fib(n):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n < 2:
        return 1
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]


def fib2(n):
    f = [0 for i in range(n+1)]    
    f[0], f[1] = 0, 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

print fib(1)
print fib(2)
print fib(3)
print fib(9)
print fib(10)
print fib(100)

# print fib2(1)
# print fib2(2)
# print fib2(3)
# print fib2(9)
# print fib2(10)
# print fib2(100)
