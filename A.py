import sys

def solve():
    try:
        line = sys.stdin.readline()
        if not line:
            return False  
    except IOError:
        return False

    try:
        l, r, x, y = map(int, line.strip().split())
    except (ValueError, EOFError):
        return False 

    start_overlap = max(l, x)
    
    end_overlap = min(r, y)
    

    overlap_length = max(0, end_overlap - start_overlap + 1)
    
    print(overlap_length)
    return True


solve()
