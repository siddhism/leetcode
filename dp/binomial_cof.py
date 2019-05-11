def binomial_cof(n, k):
    if cache[n][k]:
        print ('returning from cache')
        return cache[n][k]
    print ('Calling binomial for n: ', n, ' k : ', k)
    if k ==0 or n ==0 or k > n:
        return 1
    numerator = 1
    for i in range(0, k):
        # have to do n. n-1. n-2
        numerator = numerator * (n-i)
    denominator = 1
    for i in range(1, k+1):
        denominator = denominator * i
    answer = numerator / denominator
    cache[n][k] = answer
    return cache[n][k]

n = 10
k = 10 
cache = [[0 for i in range(k+1)] for j in range(n+1)]

for k in range(0, 10):
    print binomial_cof(5, k)
