import time

def getUniqueCharacters(matrix):
    unique_chars = set()  
    for row in matrix:
        for char in row:
            if char != '.':
                unique_chars.add(char)
    return unique_chars  

def getAntennaPositions(antenna, matrix):
    positions = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == antenna:
                positions.append((i, j))
    
    return positions

def ifCanThanAdd(antinode, antinodes, matrix):
    if(0 <= antinode[0] < len(matrix) and 0 <= antinode[1] < len(matrix[0])):
        antinodes.add(antinode)
        return True
    return False
    
def moveAntinodes(start_pos, y_distance, x_distance, direction, antinodes, matrix):
    loop = 1
    while True:
        antinode = (start_pos[0] + (y_distance * loop * direction), start_pos[1] + (x_distance * loop * direction))
        if not ifCanThanAdd(antinode, antinodes, matrix):
            break
        loop += 1

def findAntinodesForAntenna(antenna, matrix, antinodes):
    positions = getAntennaPositions(antenna, matrix)

    if len(positions) >= 3:
        for position in positions:
            antinodes.add(position)

    for i in range(len(positions) - 1):
        for j in range(i+1, len(positions)):
            y_distance = positions[j][0] - positions[i][0] 
            x_distance = positions[j][1] - positions[i][1] 
            
            moveAntinodes(positions[i], y_distance, x_distance, -1, antinodes, matrix)
            moveAntinodes(positions[j], y_distance, x_distance, 1, antinodes, matrix)

def main():
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        lines = file.readlines()

    matrix = [list(line.strip()) for line in lines]

    antinodes = set()
    unique_char = getUniqueCharacters(matrix)

    for antenna in unique_char:
        findAntinodesForAntenna(antenna, matrix, antinodes)
    
    print(len(antinodes))

if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.5f}s")