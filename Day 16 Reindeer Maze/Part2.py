"""
This code is inspired by and partially based on a solution by 'nitekat'.
Special thanks to 'nitekat' for the idea and structure of the algorithm.

"""
import time

def find_routes(start, end, matrix):
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    routes = []
    visited = {}

    queue = [(start, [start], 0, 0)] 
    while queue:
        (y, x), history, curr_score, curr_dir = queue.pop(0)

        if (y, x) == end:
            routes.append((history, curr_score))
            continue

        if ((y, x), curr_dir) in visited and visited[((y, x), curr_dir)] < curr_score:
            continue

        visited[((y, x), curr_dir)] = curr_score

        for _dir, (dy, dx) in enumerate(directions):
            if (curr_dir + 2) % 4 == _dir: 
                continue

            ny, nx = y + dy, x + dx
            if matrix[ny][nx] != "#" and (ny, nx) not in history:
                if _dir == curr_dir:
                    queue.append(((ny, nx), history + [(ny, nx)], curr_score + 1, _dir))  # move forward
                else:
                    queue.append(((y, x), history, curr_score + 1000, _dir))  # turn

    return routes

def main():
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        lines = file.readlines()

    maze = [list(line.strip()) for line in lines]

    start = None
    end = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            if maze[i][j] == 'E':
                end = (i, j)

    routes = find_routes(start, end, maze)
    best_score  = min([paths[1] for paths in  routes])
    best_routes = [paths for paths in routes if paths[1] == best_score]
    tiles = {tile for route in best_routes for tile in route[0]}
    print(len(tiles))

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")