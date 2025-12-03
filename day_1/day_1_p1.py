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
            current_pos = (current_pos - distance) % 100
        elif direction == 'R':
            current_pos = (current_pos + distance) % 100
            
        if current_pos == 0:
            zero_count += 1
            
    print(f"Password: {zero_count}")

if __name__ == "__main__":
    solve()
