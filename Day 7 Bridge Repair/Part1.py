import time
import itertools 

def generateCombinations(n):
    operations = ['+', '*']
    combinations = itertools.product(operations, repeat=n-1)

    combinations_str = [''.join(comb) for comb in combinations]

    return combinations_str

def main():
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        lines = file.readlines()

    matrix = []
    for line in lines:
        parts = line.strip().replace(':', '').split()

        number = int(parts[0])
        sublist = list(map(int, parts[1:]))
        matrix.append([number, sublist])

    count = 0 
    for line in matrix:
        if isOperationTrue(line):
            count += line[0]

    print(count)

def isOperationTrue(line):
    size_line = len(line[1])

    combinations = generateCombinations(size_line)

    for comb in combinations:       
        num = line[1][0]
        result = num
        index = 1
        for operation in comb:
            if operation == '+':
                result += line[1][index]
            if operation == '*':
                result *= line[1][index]
            index +=1
            if(result == line[0]):
                return True
    return False


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")