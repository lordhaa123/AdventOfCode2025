
def solve():
    try:
        with open('input.txt', 'r') as f:
            lines = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("Error: day_5/input.txt not found.")
        return

    ranges = []
    ids = []
    
    # Parse input
    is_ranges_section = True
    for line in lines:
        if not line:
            is_ranges_section = False
            continue
        
        if is_ranges_section:
            try:
                start, end = map(int, line.split('-'))
                ranges.append((start, end))
            except ValueError:
                print(f"Skipping invalid range line: {line}")
        else:
            try:
                ids.append(int(line))
            except ValueError:
                print(f"Skipping invalid ID line: {line}")

    fresh_count = 0
    for ingredient_id in ids:
        is_fresh = False
        for start, end in ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break
        if is_fresh:
            fresh_count += 1
            
    print(f"Fresh ingredients count: {fresh_count}")

if __name__ == "__main__":
    solve()
