def solve():
    with open('input.txt', 'r') as f:
        lines = f.readlines()


    current_pos = 50
    zero_count = 0
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        direction = line[0]
        try:
            distance = int(line[1:])
        except ValueError:
            print(f"Invalid format: {line}")
            continue
            
        if direction == 'L':
            dist_to_first_zero = current_pos if current_pos != 0 else 100
            if distance >= dist_to_first_zero:
                zero_count += 1 + (distance - dist_to_first_zero) // 100
            current_pos = (current_pos - distance) % 100
            
        elif direction == 'R':
            dist_to_first_zero = (100 - current_pos) if current_pos != 0 else 100
            if distance >= dist_to_first_zero:
                zero_count += 1 + (distance - dist_to_first_zero) // 100
            current_pos = (current_pos + distance) % 100
            
        else:
            print(f"Unknown direction: {direction}")
            continue
            
    print(f"Password: {zero_count}")

if __name__ == "__main__":
    solve()
