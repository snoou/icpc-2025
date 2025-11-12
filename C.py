import sys

def solve():
    
    try:
        n_line = sys.stdin.readline()
        if not n_line:
            return False 
        n = int(n_line.strip())
    except (IOError, ValueError):
        return False

   
    try:
        forbidden_line = sys.stdin.readline()
        if not forbidden_line:
            return False
        a, b, c = map(int, forbidden_line.strip().split())
    except (IOError, ValueError):
        return False

    
    forbidden = {a, b, c}

  
    infinity = 301 
    dp = [infinity] * (n + 1)

    
    dp[0] = 0

    for i in range(1, n + 1):
        if i in forbidden:
            continue

        val1 = dp[i-1] if i - 1 >= 0 else infinity
        val2 = dp[i-2] if i - 2 >= 0 else infinity
        val3 = dp[i-3] if i - 3 >= 0 else infinity

        min_prev = min(val1, val2, val3)

        if min_prev != infinity:
            dp[i] = 1 + min_prev

    result = dp[n]
    if result == infinity:
        print(-1)
    else:
        print(result)
        
    return True


while solve():
    pass
