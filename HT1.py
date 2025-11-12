n, m = map(int, input().split())
grid = []
for _ in range(n):
    line = input().strip()
    grid.append(line)

bin_grid = []
for i in range(n):
    row = []
    for j in range(m):
        if grid[i][j] == 'K':
            row.append(0)
        else:
            row.append(1)
    bin_grid.append(row)

consistent = True
for i in range(n):
    for j in range(m):
        if bin_grid[i][j] ^ bin_grid[0][j] ^ bin_grid[i][0] ^ bin_grid[0][0] != 0:
            consistent = False
            break
    if not consistent:
        break

if not consistent:
    print(-1)
else:
    r = [0] * n
    c = [0] * m
    r[0] = 0
    for j in range(m):
        c[j] = bin_grid[0][j]
    for i in range(1, n):
        r[i] = bin_grid[i][0] ^ bin_grid[0][0]
    total1 = sum(r) + sum(c)
    total2 = n - sum(r) + m - sum(c)
    print(min(total1, total2))