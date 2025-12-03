def is_invalid(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]

def solve():
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
                
    print(f"Total sum of invalid IDs: {total_sum}")

if __name__ == "__main__":
    solve()
