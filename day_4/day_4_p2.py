
def solve():
    try:
        with open('input.txt', 'r') as f:
            grid = [list(line.strip()) for line in f.readlines()]
    except FileNotFoundError:
        print("Error: input.txt not found.")
        return

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    total_removed = 0

    while True:
        to_remove = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    neighbor_count = 0
                    # Check all 8 neighbors
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue
                            
                            nr, nc = r + dr, c + dc
                            
                            if 0 <= nr < rows and 0 <= nc < cols:
                                if grid[nr][nc] == '@':
                                    neighbor_count += 1
                    
                    if neighbor_count < 4:
                        to_remove.append((r, c))
        
        if not to_remove:
            break
            
        total_removed += len(to_remove)
        
        # Apply removals
        for r, c in to_remove:
            grid[r][c] = '.'
            
    print(f"Total rolls removed: {total_removed}")

if __name__ == "__main__":
    solve()
