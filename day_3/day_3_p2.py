
def solve():
    
    total_joltage = 0
    
    with open("input.txt", 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        digits = [int(c) for c in line if c.isdigit()]
            
        result_digits = []
        current_idx = 0
        digits_needed = 12
        
        while digits_needed > 0:
            end_search_idx = len(digits) - digits_needed
            
            best_digit = -1
            best_digit_idx = -1
            
            for i in range(current_idx, end_search_idx + 1):
                if digits[i] == 9:
                    best_digit = 9
                    best_digit_idx = i
                    break
                if digits[i] > best_digit:
                    best_digit = digits[i]
                    best_digit_idx = i
            
            result_digits.append(best_digit)
            current_idx = best_digit_idx + 1
            digits_needed -= 1
        
        line_value = int("".join(map(str, result_digits)))
        total_joltage += line_value
        
    print(f"Total output joltage: {total_joltage}")

if __name__ == "__main__":
    solve()
