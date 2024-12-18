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
    for antinode in antinodes:
        matrix[antinode[0]][antinode[1]] = '#' 

    for linha in matrix:
        print(''.join(linha))

def findAntinodesForAntenna(antenna, matrix, antinodes):
    positions = getAntennaPositions(antenna, matrix)

    for i in range(len(positions) - 1):
        for j in range(i+1, len(positions)):
            y_distance = positions[j][0] - positions[i][0] 
            x_distance = positions[j][1] - positions[i][1] 
            
            antinode1 = (positions[i][0] - y_distance, positions[i][1] - x_distance)
            antinode2 = (positions[j][0] + y_distance, positions[j][1] + x_distance)

            ifCanThanAdd(antinode1, antinodes, matrix)
            ifCanThanAdd(antinode2, antinodes, matrix)

def ifCanThanAdd(antinode, antinodes, matrix):
    if(0 <= antinode[0] < len(matrix) and 0 <= antinode[1] < len(matrix[0])):
        antinodes.add(antinode)

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")