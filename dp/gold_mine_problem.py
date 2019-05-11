
def getMaxGold(gold, m, n):
    table = [[0 for i in range(n)] for j in range(m)]
    for i in range(0, n):
        for j in range(0, m):
            table[i][j] = gold[i][j]
    for j in range(1, m):
        for i in range(0, n):
            answer = 0
            if i -1 >= 0:
                answer = max(answer, table[i-1][j-1])
            answer = max(answer, table[i][j-1])
            if i + 1 < n:
                answer = max(answer, table[i+1][j-1])
            table[i][j] = answer + table[i][j]
            # print ('Answer for i, j : ', i, j , ' is ', answer)
    return max([table[i][m-1] for i in range(n)])

gold = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]

m = 4
n = 4

print(getMaxGold(gold, m, n))
