import time

def isWithinBounds(coord, matrix):
    return 0 <= coord[0] < len(matrix) and 0 <= coord[1] < len(matrix[0])

def lookAroundAndFindArea(coord, matrix, area):
    crop = matrix[coord[0]][coord[1]]
    area.add(coord)

    for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ahead_position = (coord[0] + direction[0], coord[1] + direction[1])
        
        if isWithinBounds(ahead_position, matrix) and ahead_position not in area:
            looked_crop = matrix[ahead_position[0]][ahead_position[1]]

            if looked_crop == crop:
                lookAroundAndFindArea(ahead_position, matrix, area)


def countPerimeter(area, matrix):
    perimeter = 0
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    for coord in area:
        for direction in directions:
            adjacent = (coord[0] + direction[0], coord[1] + direction[1])
            
            if not isWithinBounds(adjacent, matrix) or adjacent not in area:
                perimeter += 1 
    
    return perimeter

def main():
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        lines = file.readlines()

    matrix = [list(line.strip()) for line in lines]
    
    looked = set()
    areas = []
    for indexY, row in enumerate(matrix):
        for indexX, crop in enumerate(row):
            if(indexY, indexX) in looked:
                continue

            area = set()
            lookAroundAndFindArea((indexY, indexX), matrix, area)
            
            for coord in area:
                looked.add(coord) 
            areas.append(sorted(area))   

    print(sum(len(area) * countPerimeter(area, matrix) for area in areas))

        
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")