data = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

# append 1 on boundaries
n = len(data)
m = len(data[0])
pre_row = ['0'] * m
data.insert(0, pre_row)
for i in range(len(data)):
    data[i].insert(0, '0')
print data


n = len(data)
m = len(data[0])

area = [[0 for _ in range(m)] for _ in range(n)]
# diagonal = dig here
dig = [[0 for _ in range(m)] for _ in range(n)]
print area, horizontal, vertical

for i in range(1, n):
    for j in range(1, m):
        if dig[i][j] == 0:
            dig[i][j] = 1

        # compute all three params for horizontal, vertical and dig
        is_cont_square = all(data[x][y] == 1 for x, y in coords)
        if is_cont_square:
            dig[i][j] = dig[i-1][j-1] * dig[i-1][j-1]
print dig

# for i in range(1, n):
#     for j in range(1, m):
#         if data[i][j] == '1':
#             area[i][j] = max(area[i][j], horizontal[i][j], vertical[i][j], dig[i][j])

print area