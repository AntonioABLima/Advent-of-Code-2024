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


def countSides(area):
    corner_candidates = set()

    for r, c in area:
        for corner_r, corner_c in [(r - 0.5, c - 0.5), (r + 0.5, c - 0.5), (r + 0.5, c + 0.5), (r - 0.5, c + 0.5)]:
            corner_candidates.add((corner_r, corner_c))

    corners = 0
    for corner_r, corner_c in corner_candidates:
        config = [(sr, sc) in area for sr, sc in [
            (corner_r - 0.5, corner_c - 0.5), 
            (corner_r + 0.5, corner_c - 0.5), 
            (corner_r + 0.5, corner_c + 0.5), 
            (corner_r - 0.5, corner_c + 0.5)
        ]]
        num = sum(config)
        if num == 1:
            corners += 1
        elif num == 2:
            if config == [True, False, True, False] or config == [False, True, False, True]:
                corners += 2
        elif num == 3:
            corners += 1

    return corners

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

    print(sum(len(area) * countSides(area) for area in areas))

        
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")