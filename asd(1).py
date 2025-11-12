import sys

def solve():
 
    try:

        n = int(sys.stdin.readline())

        if n == 0:
            print(0)
            return


        A = list(map(int, sys.stdin.readline().split()))
        
    except:

        print(0)
        return


    def check(k):
        if k == 0:
            return True
        
     
        count = 0
        for val in A:
            if val >= k:
                count += 1
            else:
                
                count = 0
            
            
            if count >= k:
                return True
        
        return False

    low = 1
    high = n
    max_k = 0 

    while low <= high:
        mid = (low + high) // 2
        
        if check(mid):
          
            max_k = mid
           
            low = mid + 1
        else:
            
            high = mid - 1
            
    print(max_k)

if __name__ == "__main__":
    
    solve()