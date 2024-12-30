import time

moves = {
        '^': [-1, 0],  
        'v': [1, 0],   
        '>': [0, 1],   
        '<': [0, -1]  
    }

def process_input(file_name):
    with open(file_name, 'r') as file:
        input_string = file.read()

    grid_part, movements_part = input_string.split("\n\n")
    
    grid = [list(line) for line in grid_part.split("\n")]
    commands = [char for char in movements_part.strip() if char != '\n']

    return grid, commands

def transformToNewLayout(matrix):
    new_layout = []
    for row in matrix:
        new_row  = []
        for item in row:
            if item == '#':
                new_row.append('#')
                new_row.append('#')
            if item == 'O':
                new_row.append('[')
                new_row.append(']')
            if item == '.':
                new_row.append('.')
                new_row.append('.')
            if item == '@':
                new_row.append('@')
                new_row.append('.')
    
        new_layout.append(new_row)

    return new_layout
            
def findRobot(matrix):
    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            if item == '@':
                return [i, j]
            
def walk(pos, direction): #y x
    return [pos[0] + moves[direction][0], pos[1] + moves[direction][1]]

def shiftRightLeft(num, pos, direction, matrix):
    y = pos[0]
    x = pos[1]
    matrix[y][x] = '.'
    y, x = walk(pos, direction)
    matrix[y][x] = '@'

    for i in range(num // 2):
        if direction == '<':
            y, x = walk([y, x], direction)
            matrix[y][x] = ']'
            y, x = walk([y, x], direction)
            matrix[y][x] = '['
        
        if direction == '>' :
            y, x = walk([y, x], direction)
            matrix[y][x] = '['
            y, x = walk([y, x], direction)
            matrix[y][x] = ']'

def lookUpOrDown(pos, direction, matrix):
    y, x = walk(pos, direction)
    positions = {}

    if matrix[y][x] == '#':
        positions[(y, x)] = matrix[y][x]

    if matrix[y][x] == ']':
        positions[(y, x)] = matrix[y][x]
        y, x = walk([y, x], '<')
        positions[(y, x)] = matrix[y][x]

    if matrix[y][x] == '[':
        positions[(y, x)] = matrix[y][x]
        y, x = walk([y, x], '>')
        positions[(y, x)] = matrix[y][x]

    return positions

def shiftUpDown(initial_pos, box_positions, direction, matrix):
    for y, row in enumerate(reversed(box_positions)): 
        for x, coord_key in enumerate(reversed(row)):
            if coord_key:
                matrix[coord_key[0]][coord_key[1]] = '.'
                new_value = walk(coord_key, direction)
                matrix[new_value[0]][new_value[1]] = row[coord_key]

    y = initial_pos[0]
    x = initial_pos[1]
    matrix[y][x] = '.'
    y, x = walk(initial_pos, direction)
    matrix[y][x] = '@'

def printWharehouse(matrix):
    for row in matrix:
        for item in row:
            print(item, end='')
        print()
    print()
    
def sumBoxCoord(matrix):
    total = 0
    for y, row in enumerate(matrix):
        for x, item in enumerate(row):
            if item == '[':
                total = total + (100 * y) + x

    return total    

def main():
    file_name = 'input.txt'

    warehouse, movements = process_input(file_name)
    warehouse = transformToNewLayout(warehouse)
    pos = findRobot(warehouse)

    num_movements = len(movements)
    
    for i in range(num_movements):
        pos_ahead = walk(pos, movements[i])
        ahead_symbol = warehouse[pos_ahead[0]][pos_ahead[1]]
        
        if(ahead_symbol == '#'):
            continue
        
        if ahead_symbol == '.':
            warehouse[pos[0]][pos[1]] = '.'
            warehouse[pos_ahead[0]][pos_ahead[1]] = '@'
            pos = pos_ahead
        
        if(ahead_symbol in ['[', ']'] and  movements[i] in ['<', '>']):
            tiles_looked = 0
            temp_pos = pos_ahead

            while True:
                temp_pos = walk(temp_pos, movements[i])
                tiles_looked +=1

                tile_symbol = warehouse[temp_pos[0]][temp_pos[1]]
                if tile_symbol in ['[', ']']:  
                    continue

                if tile_symbol == '.':
                    shiftRightLeft(tiles_looked, pos, movements[i], warehouse)
                    pos = pos_ahead
                    break

                if tile_symbol == '#':
                    break
    
        if(ahead_symbol in ['[', ']'] and  movements[i] in ['v', '^']):
            
            positions = []
            positions.append(lookUpOrDown(pos, movements[i], warehouse))
            
            found_barrier = False
            for row in positions:
                for position in row.keys():
                    teste = lookUpOrDown(position, movements[i], warehouse)
                    if '#' in teste.values():
                        found_barrier = True
                        break
                    positions.append(teste)
                if found_barrier:
                    break

            if not found_barrier :   
                positions = list(filter(bool, positions))
                shiftUpDown(pos, positions, movements[i], warehouse)
                pos = pos_ahead

    printWharehouse(warehouse)
    print(sumBoxCoord(warehouse))

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")
