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
horizontal = [[0 for _ in range(m)] for _ in range(n)]
vertical = [[0 for _ in range(m)] for _ in range(n)]
# diagonal = dig here
dig = [[0 for _ in range(m)] for _ in range(n)]
print area, horizontal, vertical

for i in range(1, n):
    for j in range(1, m):
        # set the least possible area if it is one
        if not data[i][j] == '1':
            continue
        if area[i][j] == 0:
            area[i][j] = 1
        if horizontal[i][j] == 0:
            horizontal[i][j] = 1
        if vertical[i][j] == 0:
            vertical[i][j] = 1
        if dig[i][j] == 0:
            dig[i][j] = 1

        # compute all three params for horizontal, vertical and dig
        if data[i-1][j] == '1':
            horizontal[i][j] = horizontal[i-1][j] + 1
        if data[i][j-1] == '1':
            vertical[i][j] = vertical[i][j-1] + 1
        coords = [[i-1, j], [i, j-1], [i-1, j-1]]
        is_cont_rect = all(data[x][y] == '1' for x, y in coords)
        if is_cont_rect:
            x = horizontal[i-1][j] * vertical[i][j-1]
            y = horizontal[i][j-1] * vertical[i-1][j]
            dig[i][j] = max(x, y)
print horizontal
print vertical
print dig

for i in range(1, n):
    for j in range(1, m):
        if data[i][j] == '1':
            area[i][j] = max(area[i][j], horizontal[i][j], vertical[i][j], dig[i][j])

print area