import time

def lookForward(index, frase):
    if index > len(frase) - 4:
        return 0

    word = ''.join(frase[index + i] for i in range(4))
    return 1 if word == 'XMAS' else 0

def lookBackward(index, frase):
    if index < 3:
        return 0

    word = ''.join(frase[index - i] for i in range(4))
    return 1 if word == 'XMAS' else 0

def lookUp(indexX, indexY, matrix):
    if indexY < 3:
        return 0

    word = ''.join(matrix[indexY - i][indexX] for i in range(4))
    return 1 if word == 'XMAS' else 0

def lookDown(indexX, indexY, matrix):
    if indexY > len(matrix) - 4:
        return 0

    word = ''.join(matrix[indexY + i][indexX] for i in range(4))
    return 1 if word == 'XMAS' else 0


def lookDiagonalsRight(indexX, indexY, matrix):
    if indexX > len(matrix[0]) - 4:
        return 0

    occurrences = 0
    occurrences += lookDiagonalsRightUp(indexX, indexY, matrix)
    occurrences += lookDiagonalsRightDown(indexX, indexY, matrix)

    return occurrences

def lookDiagonalsRightUp(indexX, indexY, matrix):  # ↗
    if indexY < 3 or indexX > len(matrix[0]) - 4:
        return 0

    word = ''.join(matrix[indexY - i][indexX + i] for i in range(4))
    return 1 if word == 'XMAS' else 0

def lookDiagonalsRightDown(indexX, indexY, matrix):  # ↘
    if indexY > len(matrix) - 4 or indexX > len(matrix[0]) - 4:
        return 0

    word = ''.join(matrix[indexY + i][indexX + i] for i in range(4))
    return 1 if word == 'XMAS' else 0


def lookDiogonalsLeft(indexX, indexY, matrix):
    if indexX < 3:
        return 0

    occurrences = 0
    occurrences += lookDiogonalsLeftUp(indexX, indexY, matrix)
    occurrences += lookDiogonalsLeftDown(indexX, indexY, matrix)

    return occurrences

def lookDiogonalsLeftUp(indexX, indexY, matrix):  # ↖
    if indexY < 3 or indexX < 3:
        return 0

    word = ''.join(matrix[indexY - i][indexX - i] for i in range(4))
    return 1 if word == 'XMAS' else 0

def lookDiogonalsLeftDown(indexX, indexY, matrix):  # ↙
    if indexY > len(matrix) - 4 or indexX < 3:
        return 0

    word = ''.join(matrix[indexY + i][indexX - i] for i in range(4))
    return 1 if word == 'XMAS' else 0

def main():
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        lines = file.readlines()

    matrix = [list(line.strip()) for line in lines]

    occurrences = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            occurrences += lookForward(j, matrix[i])
            occurrences += lookBackward(j, matrix[i])
            occurrences += lookDown(j, i, matrix)
            occurrences += lookUp(j, i, matrix)
            occurrences += lookDiagonalsRight(j, i, matrix)
            occurrences += lookDiogonalsLeft(j, i, matrix)

    print(occurrences)


if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.5f}s")