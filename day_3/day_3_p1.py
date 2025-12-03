def solve():
    total_joltage = 0
    
    with open("input.txt", 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        digits = [int(c) for c in line if c.isdigit()]
        max_joltage = 0
        
        # Iterate through all pairs (i, j) such that i < j
        for i in range(len(digits)):
            for j in range(i+1,len(digits)):
                current_joltage = digits[i] * 10 + digits[j]
                if current_joltage > max_joltage:
                    max_joltage = current_joltage
        total_joltage += max_joltage
        
    print(f"Total output joltage: {total_joltage}")
        


if __name__ == "__main__":
    solve()
