
import os
import math

def solve():
    file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(file_path, 'r') as f:
        lines = [line.rstrip('\n') for line in f]

    if not lines:
        print("No input lines")
        return

    # Normalize grid width
    max_len = max(len(line) for line in lines)
    grid = [line.ljust(max_len) for line in lines]
    
    height = len(grid)
    width = max_len

    # Identify separator columns (all spaces)
    # A column j is a separator if grid[i][j] == ' ' for all i
    is_separator = []
    for j in range(width):
        col_is_space = all(grid[i][j] == ' ' for i in range(height))
        is_separator.append(col_is_space)

    # Split into chunks based on separators
    problems = []
    start_col = 0
    
    # We want to identify contiguous blocks of non-separator columns
    j = 0
    while j < width:
        # Skip separators
        while j < width and is_separator[j]:
            j += 1
        
        if j >= width:
            break
            
        # Found start of a problem
        start = j
        
        # Find end of this problem
        while j < width and not is_separator[j]:
            j += 1
        
        end = j
        
        # Extract this chunk
        chunk = [row[start:end] for row in grid]
        problems.append(chunk)

    total_sum = 0
    
    for p_idx, chunk in enumerate(problems):
        # Parse numbers from rows 0 to height-2
        numbers = []
        for r in range(height - 1):
            row_str = chunk[r].strip()
            if row_str:
                try:
                    numbers.append(int(row_str))
                except ValueError:
                    pass
        
        # Parse operator from the last row
        operator_row = chunk[height - 1].strip()
        op = operator_row
        
        if not numbers:
            continue
            
        res = 0
        if op == '+':
            res = sum(numbers)
        elif op == '*':
            res = 1
            for n in numbers:
                res *= n
        else:
            print(f"Unknown operator: {op} in problem {p_idx}")
            continue
            
        # print(f"Problem {p_idx}: {numbers} {op} -> {res}")
        total_sum += res

    print(f"Grand Total: {total_sum}")

if __name__ == "__main__":
    solve()
