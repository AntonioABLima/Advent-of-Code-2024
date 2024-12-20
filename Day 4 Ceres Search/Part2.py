import time

def findXShape(indexX, indexY, matrix):

    top_tip_left = matrix[indexY-1][indexX-1]
    top_tip_right = matrix[indexY-1][indexX+1]

    bottom_tip_left = matrix[indexY+1][indexX-1]
    botom_tip_right = matrix[indexY+1][indexX+1]

    if (
        top_tip_left in {'X', 'A'} or 
        botom_tip_right in {'X', 'A'} or 
        bottom_tip_left in {'X', 'A'} or 
        top_tip_right in {'X', 'A'} or 
        top_tip_left == botom_tip_right or 
        bottom_tip_left == top_tip_right
    ): 
        return 0
      
    return 1

def main():
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        lines = file.readlines()

    matrix = [list(line.strip()) for line in lines]

    occurrences = 0
    for i in range(len(matrix)):
        if (i < 1 or i > len(matrix) - 2 ):
            continue
        for j in range(len(matrix[0])):
            if j < 1 or j > len(matrix[0]) - 2:
                continue
            
            if(matrix[i][j] == 'A'):
                occurrences += findXShape(j, i, matrix)
            
    print(occurrences)

if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.5f}s")