import time

def process_input(file_name):
    with open(file_name, 'r') as file:
        input_string = file.read()

    grid_part, movements_part = input_string.split("\n\n")
    
    grid = [list(line) for line in grid_part.split("\n")]
    commands = [char for char in movements_part.strip() if char != '\n']

    return grid, commands

def findRobot(matrix):
    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            if item == '@':
                return [i, j]
            
def walk(pos, direction): #y x
    return [pos[0] + direction[0], pos[1] + direction[1]]

def shift(num, pos, moviment, matrix):
    y = pos[0]
    x = pos[1]
    matrix[y][x] = '.'
    y, x = walk(pos, moviment)
    matrix[y][x] = '@'

    for i in range(num):
        y, x = walk([y, x], moviment)
        matrix[y][x] = 'O'

def printWharehouse(matrix):
    for row in matrix:
        for item in row:
            print(item, end='')
        print()

def sumBoxCoord(matrix):
    total = 0
    for y, row in enumerate(matrix):
        for x, item in enumerate(row):
            if item == 'O':
                total = total + (100 * y) + x

    return total    

def main():
    file_name = 'input.txt'

    warehouse, movements = process_input(file_name)
    pos = findRobot(warehouse)

    num_movements = len(movements)
    
    moves = {
        '^': [-1, 0],  
        'v': [1, 0],   
        '>': [0, 1],   
        '<': [0, -1]  
    }

    for i in range(num_movements):
        movement = moves[movements[i]]
        pos_ahead = walk(pos, movement)
        ahead_symbol = warehouse[pos_ahead[0]][pos_ahead[1]]
        
        if(ahead_symbol == '#'):
            continue
        
        if ahead_symbol == '.':
            warehouse[pos[0]][pos[1]] = '.'
            warehouse[pos_ahead[0]][pos_ahead[1]] = '@'
            pos = pos_ahead
        
        if(ahead_symbol == 'O'):
            tiles_looked = 0
            temp_pos = pos_ahead

            while True:
                temp_pos = walk(temp_pos, movement)
                tiles_looked +=1

                tile_symbol = warehouse[temp_pos[0]][temp_pos[1]]
                if tile_symbol == 'O':  
                    continue

                if tile_symbol == '.':
                    shift(tiles_looked, pos, movement, warehouse)
                    pos = pos_ahead
                    break

                if tile_symbol == '#':
                    break
    
    printWharehouse(warehouse)
    print(sumBoxCoord(warehouse))



if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")
