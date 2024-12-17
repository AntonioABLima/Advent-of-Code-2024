import copy
import time


nome_arquivo = 'input.txt'
with open(nome_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()

matrix = [list(linha.strip()) for linha in linhas]

start = [0, 0]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == '^':
            start = [i, j]
            break

moves = {
    '^': (-1, 0),  
    'v': (1, 0),   
    '>': (0, 1),   
    '<': (0, -1)  
}

def isWithinBounds(y, x, matrix):
    return 0 <= y < len(matrix) and 0 <= x < len(matrix[0])

def turn(arrow):
    turns = {
        '^': '>',
        'v': '<',
        '>': 'v',
        '<': '^'
    }

    return turns[arrow]

def saveVisitedPositions(matrix,  moves):
    coord = copy.deepcopy(start)
    visited = set()
    while True:
        direction = matrix[coord[0]][coord[1]]
        visited.add(tuple(coord))  
        new_y_position = coord[0] + moves[direction][0]
        new_x_position = coord[1] + moves[direction][1]

        if not isWithinBounds(new_y_position, new_x_position, matrix):
            break  

        new_position_letter = matrix[new_y_position][new_x_position]

        if new_position_letter == '.':
            matrix[new_y_position][new_x_position] = direction
            matrix[coord[0]][coord[1]] = '.'
            coord = [new_y_position, new_x_position]
        elif new_position_letter == '#':
            direction = turn(direction)
            matrix[coord[0]][coord[1]] = direction

    return visited

def main():
    visited_positions = saveVisitedPositions(copy.deepcopy(matrix), moves)
    
    counter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            
            if matrix[i][j] == '#' or [i, j] == start or not (i, j) in visited_positions:
                continue
            
            visited_new = set()
            
            new_obstacle_matrix = copy.deepcopy(matrix)
            new_obstacle_matrix[i][j] = '#'
            coord = copy.deepcopy(start)
            
            while True:
                arrow = new_obstacle_matrix[coord[0]][coord[1]] 
                visited_new.add((tuple(coord), arrow))
                
                ahead_coord = [coord[0] + moves[arrow][0], coord[1] + moves[arrow][1]]
                if not isWithinBounds(ahead_coord[0], ahead_coord[1], matrix):
                    break

                ahead_symbol = new_obstacle_matrix[ahead_coord[0]][ahead_coord[1]]

                if ahead_symbol in '.':
                    new_obstacle_matrix[ahead_coord[0]][ahead_coord[1]] = arrow
                    new_obstacle_matrix[coord[0]][coord[1]] = '.'
                    coord = ahead_coord
                    
                    if (tuple(coord), arrow) in visited_new:
                        counter+=1
                        break

                if ahead_symbol == '#':
                    arrow = turn(arrow)
                    new_obstacle_matrix[coord[0]][coord[1]] = arrow

    print(counter) 

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Tempo de execucao: {end_time - start_time:.2f} segundos")

# Tempo de execucao pyton 3.10  33.34
# Tempo de execucao pypy3        8.17 