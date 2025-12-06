
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
    is_separator = []
    for j in range(width):
        col_is_space = all(grid[i][j] == ' ' for i in range(height))
        is_separator.append(col_is_space)

    # Split into chunks based on separators
    problems = []
    j = 0
    while j < width:
        while j < width and is_separator[j]:
            j += 1
        
        if j >= width:
            break
            
        start = j
        while j < width and not is_separator[j]:
            j += 1
        end = j
        
        chunk = [row[start:end] for row in grid]
        problems.append(chunk)

    total_sum = 0
    
    for p_idx, chunk in enumerate(problems):
        chunk_width = len(chunk[0])
        # Find operator in the last row
        # It should be the only non-space character, or just strip it
        operator_row = chunk[height - 1]
        op_char = operator_row.strip()
        
        # We need to find the operator carefully if necessary, 
        # but usually strip() on the row works if there's only one char.
        # Let's assume there is exactly one operator char.
        op = op_char
        
        numbers = []
        # Iterate columns Right-to-Left
        for col in range(chunk_width - 1, -1, -1):
            # Build number from top to bottom (rows 0 to height-2)
            num_str_parts = []
            for row in range(height - 1):
                char = chunk[row][col]
                if char != ' ':
                    num_str_parts.append(char)
            
            if num_str_parts:
                num_str = "".join(num_str_parts)
                try:
                    val = int(num_str)
                    numbers.append(val)
                except ValueError:
                    pass
        
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
            # Maybe operator is empty if it's a weird chunk?
            # But based on problem description, there's always an operator.
            print(f"Unknown or missing operator in problem {p_idx}")
            continue
            
        # print(f"Problem {p_idx}: {numbers} {op} -> {res}")
        total_sum += res

    print(f"Grand Total: {total_sum}")

if __name__ == "__main__":
    solve()
