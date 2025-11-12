import sys

sys.setrecursionlimit(2000)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.num_components = n
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def unite(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.num_components -= 1
            return True
        return False

def solve():
    try:
        data = sys.stdin.readline().split()
        if not data:
            return
        n, m = map(int, data)
    except EOFError:
        return
    except ValueError:
        return

    try:
        a = [0] + list(map(int, sys.stdin.readline().split())) 
    except ValueError:
        return
    except EOFError:
        return
        
    already_sorted = True
    for i in range(1, n + 1):
        if a[i] != i:
            already_sorted = False
            break

    if already_sorted:
        print("sorted")
        return

    edges = []
    for _ in range(m):
        try:
            x, y, p = map(int, sys.stdin.readline().split())
            edges.append((p, x, y))
        except ValueError:
            continue
        except EOFError:
            break

    
    edges.sort(key=lambda x: x[0], reverse=True)

    dsu = DSU(n)
    
    max_min_power = 0
    
    for power, u, v in edges:
        if dsu.unite(u, v):
            if dsu.num_components == 1:
                print(power)
                return

    if dsu.num_components > 1:
        print("impossible")
    
if __name__ == "__main__":
    solve()
