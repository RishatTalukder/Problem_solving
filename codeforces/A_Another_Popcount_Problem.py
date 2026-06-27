import sys

def solve():
    # Fast I/O
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx+1])
        idx += 2
        
        total_popcount = 0
        
        # Iterate from the lowest bit (cheapest) to the highest bit
        for j in range(31):
            cost = 1 << j
            if cost > n:
                # If a single bit exceeds remaining n, higher bits will too
                break
                
            # Take at most k bits or what we can afford
            take = min(k, n // cost)
            
            total_popcount += take
            n -= take * cost
            
        results.append(str(total_popcount))
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
