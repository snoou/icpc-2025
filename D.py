import sys

def solve():
    try:
        n, m = map(int, sys.stdin.readline().split())
    except (ValueError, IOError):
        return False

    old_grid = []
    for _ in range(n):
        row_str = sys.stdin.readline().strip()
        if not row_str:
            return False # ورودی ناقص
        old_grid.append([int(char) for char in row_str])

    new_grid = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            
            forbidden_colors = set()

            forbidden_colors.add(old_grid[i][j])

            if i > 0:
                forbidden_colors.add(new_grid[i-1][j])

            if j > 0:
                forbidden_colors.add(new_grid[i][j-1])

            for color in range(1, 5): 
                if color not in forbidden_colors:
                    new_grid[i][j] = color
                    break  

    for i in range(n):
        print("".join(map(str, new_grid[i])))
        
    return True


while solve():
    pass
