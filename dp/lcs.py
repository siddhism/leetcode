# s1 = 'abcdgh'
# s2 = 'aedfhr'
# s1 = 'AGGTAB'
# s2 = 'GXTXAYB'

n = len(s1)
m = len(s2)
subs = [[0 for j in range(m+1)] for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if s1[i-1] == s2[j-1]:
            subs[i][j] = subs[i-1][j-1] + 1
        else:
            subs[i][j] = max(subs[i-1][j], subs[i][j-1])

print subs
print subs[n][m]


i = n
j = m
x = []
while i > 0 and j > 0:
    if s1[i-1] == s2[j-1]:
        x.append(s1[i-1])
        i = i - 1 
        j = j - 1
    elif subs[i-1][j] > subs[i][j-1]:
        i = i -1
    else:
        j = j - 1

x.reverse()
print ''.join(x)
