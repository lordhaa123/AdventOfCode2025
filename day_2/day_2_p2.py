def is_invalid(n):
    s = str(n)
    L = len(s)
    # Check for all possible lengths of the repeating unit 'm'
    # The unit must repeat at least twice, so m can be at most L // 2
    for m in range(1, L // 2 + 1):
        if L % m == 0:
            sub = s[:m]
            k = L // m
            if sub * k == s:
                return True
    return False

def solve():
    # Use the same input file as Part 1
    with open('input.txt', 'r') as f:
        content = f.read().replace('\n', '')
    
    ranges = content.split(',')
    total_sum = 0
    
    for r in ranges:
        if not r: continue
        start_str, end_str = r.split('-')
        start = int(start_str)
        end = int(end_str)
        
        for n in range(start, end + 1):
            if is_invalid(n):
                total_sum += n
                
    print(f"Total sum of invalid IDs (Part 2): {total_sum}")

if __name__ == "__main__":
    solve()
