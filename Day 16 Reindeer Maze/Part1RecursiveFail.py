import time

moves = {
    '^': [-1, 0],  
    'v': [1, 0],   
    '>': [0, 1],   
    '<': [0, -1]  
}

def printMaze(matrix):
    for row in matrix:
        for item in row:
            print(item, end='')
        print()

def findSymbolInMaze(symbol, matrix):
    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            if item == symbol:
                return (i, j)

def possibleDirections(direction):
    turns = {
        '^': ['>', '^', '<'],
        'v': ['>', 'v', '<'],
        '>': ['v', '>', '^'],
        '<': ['v', '<', '^']
    }

    return turns[direction]

def walk(pos, direction): 
    return (pos[0] + moves[direction][0], pos[1] + moves[direction][1])

def isWithinBounds(coord, matrix):
    return 0 <= coord[0] < len(matrix) and 0 <= coord[1] < len(matrix[0])

def countScore(_list):
    score = -1
    old_direction = _list[0][1]
    for positon in _list:
        if old_direction != positon[1]:
            score += 1000
            old_direction = positon[1]
        score += 1

    return score

def main():
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        lines = file.readlines()

    maze = [list(line.strip()) for line in lines]

    start_pos = findSymbolInMaze('S' ,maze)
    end_pos = findSymbolInMaze('E' ,maze)

    direction = '>'
    y, x = start_pos

    visited = []
    visited.append((start_pos, direction))

    print(min(exploreMaze(start_pos, direction, visited, maze)))


def exploreMaze(pos, direction, visited, matrix):
    visited_copy = visited.copy()
    visited_copy.append((pos, direction))
        
    possible_directions = possibleDirections(direction)

    scores = []
    for direction in possible_directions:
        ahead_pos = walk(pos, direction)

        if not ahead_pos in [visited_pos[0] for visited_pos in visited_copy] and \
            isWithinBounds(ahead_pos, matrix) and \
            matrix[ahead_pos[0]][ahead_pos[1]] != '#':
            
            if matrix[ahead_pos[0]][ahead_pos[1]] == 'E':
                scores.append(countScore(visited_copy))

            scores.extend(exploreMaze(ahead_pos, direction, visited_copy, matrix))
    
    return scores

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")