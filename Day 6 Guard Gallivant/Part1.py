import time

def isWithinBounds(coord, matrix):
    return 0 <= coord[0] < len(matrix) and 0 <= coord[1] < len(matrix[0])

def main():
    nome_arquivo = 'input.txt'
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    matrix = [list(linha.strip()) for linha in linhas]

    coord = [0, 0]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '^':
                coord = [i, j]
                break

    moves = {
        '^': (-1, 0),  
        'v': (1, 0),   
        '>': (0, 1),   
        '<': (0, -1)  
    }
    
    counter = 0
    while True:
        arrow = matrix[coord[0]][coord[1]]  
        ahead_coord = [coord[0] + moves[arrow][0], coord[1] + moves[arrow][1]] 

        if not isWithinBounds(ahead_coord, matrix):
            matrix[coord[0]][coord[1]] = 'X'
            counter += 1
            break   

        ahead_symbol = matrix[ahead_coord[0]][ahead_coord[1]] 

        if ahead_symbol in ['.', 'X']:
            matrix[ahead_coord[0]][ahead_coord[1]] = arrow
            matrix[coord[0]][coord[1]] = 'X'
            coord = ahead_coord
            if ahead_symbol == '.':
                counter += 1
            
        if ahead_symbol == '#' :
            arrow = turn(arrow)
            matrix[coord[0]][coord[1]] = arrow
    print(counter)

def turn(direction):
    turns = {
        '^': '>',
        'v': '<',
        '>': 'v',
        '<': '^'
    }

    return turns[direction]

if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.5f}s")