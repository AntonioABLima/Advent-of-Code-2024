import time
import copy

def lookAround(initial_coord, coord, matrix, old_height, zero_map, is_first=False):
    if not (0 <= coord[0] < len(matrix) and 0 <= coord[1] < len(matrix[0])):
        return 
    
    current_heigt = matrix[coord[0]][coord[1]]
    if old_height > current_heigt or \
        not is_first and current_heigt - old_height != 1:
        return

    if current_heigt == 9:
        zero_map[initial_coord].append(coord)
    
    lookAround(initial_coord, (coord[0], coord[1] + 1), matrix, current_heigt, zero_map)  # Right
    lookAround(initial_coord, (coord[0] + 1, coord[1]), matrix, current_heigt, zero_map)  # Down
    lookAround(initial_coord, (coord[0] - 1, coord[1]), matrix, current_heigt, zero_map)  # Up
    lookAround(initial_coord, (coord[0], coord[1] - 1), matrix, current_heigt, zero_map)  # Left
    
def main():

    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        lines = file.readlines()

    matrix = [list(map(int, line.strip())) for line in lines]

    zero_map = {
        (index_y, index_x): []
        for index_y, row in enumerate(matrix)
        for index_x, value in enumerate(row)
        if value == 0
    }
    
    for index_y, row in enumerate(matrix):
        for index_x, item in enumerate(row):
            if item == 0:
                new_matrix = copy.deepcopy(matrix)
                lookAround((index_y, index_x), (index_y, index_x), new_matrix, 0, zero_map, is_first=True)

    teste = 0
    for key, value in zero_map.items(): 
        teste += len(value)  

    print(teste)
if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.5f}s")