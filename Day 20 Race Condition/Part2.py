import time

def findStartEnd(matrix):
    start = ()
    end = ()

    for y, row in enumerate(matrix):
        for x, i in enumerate(row):
            if i == 'S':
                start = (y, x)
            if i == 'E':
                end = (y, x)
            
            if start and end:
                return start, end

def isWithinBounds(coord, matrix):
    return 0 <= coord[0] < len(matrix) and 0 <= coord[1] < len(matrix[0])

def main():
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        lines = file.readlines()

    racetrack = [list(line.strip()) for line in lines]
    distance_map = racetrack.copy()

    start_pos, end_pos = findStartEnd(racetrack)
   
    picoseconds = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    y, x = start_pos
    while (y, x) != end_pos:

        distance_map[y][x] = picoseconds
        for direction in directions:
            ahead_y, ahead_x = ahead_pos = (direction[0] + y, direction[1] + x)

            if ahead_pos in visited:
                continue

            if isWithinBounds(ahead_pos, racetrack) and racetrack[ahead_y][ahead_x] != '#':
                visited.add((y, x))
                y, x = ahead_pos
                picoseconds += 1
                distance_map[y][x] = picoseconds
            
    cheats_possible = set()
    cheat_time = 20
    for y, row in enumerate(distance_map):
        for x, item in enumerate(row):
            found = False

            if (y, x) not in visited:
                continue
            
            for dy in range(-cheat_time, cheat_time + 1):
                for dx in range(-cheat_time, cheat_time + 1):
                    ny, nx = y + dy, x + dx
                    cheat_walked = abs(ny - y) + abs(nx - x)
                    
                    if cheat_walked > cheat_time or (ny, nx) == (y, x) or not isWithinBounds((ny, nx), distance_map):
                        continue
                    
                    if distance_map[ny][nx] != '#' and distance_map[ny][nx] > distance_map[y][x] + cheat_walked:
                        save_time = distance_map[ny][nx] - distance_map[y][x] - cheat_walked
                        
                        if save_time >= 100:
                            cheats_possible.add(((y, x), (ny, nx)))
                        
    print(len(cheats_possible))
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")
