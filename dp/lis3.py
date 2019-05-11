a = [3, 4, -1, 0, 6, 2, 3]

def lis(a):
    n = len(a)
    lis = [1 for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if a[j] < a[i]:
                lis[i] = max(lis[i], lis[j] + 1)
        print 'After element i : ', i , ' \n', lis
    return lis

lis_of_a = lis(a)
print max(lis_of_a)

