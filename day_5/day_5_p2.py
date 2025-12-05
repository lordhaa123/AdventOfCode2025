
def solve():
    try:
        with open('day_5/input.txt', 'r') as f:
            lines = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        # Fallback if running from day_5 dir
        try:
            with open('input.txt', 'r') as f:
                lines = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print("Error: input.txt not found.")
            return

    ranges = []
    
    # Parse ranges only
    for line in lines:
        if not line:
            # Reached blank line, stop parsing ranges
            break
        
        try:
            # Format is start-end
            parts = line.split('-')
            if len(parts) == 2:
                start, end = map(int, parts)
                ranges.append((start, end))
        except ValueError:
            continue

    if not ranges:
        print("No ranges found.")
        return

    # Sort ranges by start time
    ranges.sort(key=lambda x: x[0])

    merged_ranges = []
    if ranges:
        curr_start, curr_end = ranges[0]
        
        for i in range(1, len(ranges)):
            next_start, next_end = ranges[i]
            
            if next_start <= curr_end + 1: # +1 because if 3-5 and 6-10 they can embrace to 3-10? 
                # Wait, "inclusive". 3-5 is 3,4,5. 
                # If next is 6-10 (6,7,8,9,10). 
                # Should I merge them? 
                # Problem says "The ranges can also overlap". 
                # "An ingredient ID is fresh if it is in any range."
                # Does "adjacent" mean they should merge? 
                # If I have 3-5 and 6-10. Elements are {3,4,5} U {6,7,8,9,10} = {3,4,5,6,7,8,9,10}.
                # This is equivalent to 3-10.
                # So yes, if next_start <= curr_end + 1, we can merge.
                # Careful: if they are just disjoint 3-5, 7-9. No merge.
                
                curr_end = max(curr_end, next_end)
            else:
                merged_ranges.append((curr_start, curr_end))
                curr_start, curr_end = next_start, next_end
        
        merged_ranges.append((curr_start, curr_end))

    total_fresh = 0
    for start, end in merged_ranges:
        total_fresh += (end - start + 1)

    print(f"Total fresh ingredient IDs: {total_fresh}")

if __name__ == "__main__":
    solve()
