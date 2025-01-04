import time
from collections import deque

def bfs(grid_size, corrupted_positions, start, end):
    corrupted = set(corrupted_positions)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([(start[0], start[1], 0)])  
    visited = set() 
    
    while queue:
        x, y, steps = queue.popleft()
        
        if (x, y) == end:
            return steps
        
        if (x, y) in visited or (x, y) in corrupted:
            continue
        
        visited.add((x, y))
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size: 
                queue.append((nx, ny, steps + 1))
    
    return -1

def main():
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        lines = file.readlines()

    bytes_pos = [tuple(map(int, line.strip().split(','))) for line in lines]

    kilobyte_pos = bytes_pos[:1024]
    steps = bfs(71, kilobyte_pos, (0, 0), (70, 70))       

    print(steps)

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")
