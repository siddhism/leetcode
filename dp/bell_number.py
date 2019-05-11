def bellNumber(n):
    B = [[0 for i in range(n+1)] for j in range(n+1)]
    B[0][0] = 1
    for i in range(1, n + 1):
        for j in range(0, i+1):
            if j == 0:
                B[i][j] = B[i-1][i-1]
            else:
                B[i][j] = B[i-1][j-1] + B[i][j-1]
    return B

for num in range(7):
    B = bellNumber(num)
    print 'Here is bell triangle for number ', num
    for i in range(num):
        for j in range(i):
            print B[i][j],
        print '\n'

