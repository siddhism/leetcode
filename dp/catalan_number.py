cache = {}
def catalan(n):
    print 'calling catalan for n = ', n
    if n == 0 or n == 1:
        return 1
    if n in cache:
        return cache[n]

    cat = 0
    for i in range(1, n):
        cat = cat + catalan(i) * catalan(n-i)
    cache[n] = cat
    return cache[n]


for i in range(0, 10):
    print catalan(i)