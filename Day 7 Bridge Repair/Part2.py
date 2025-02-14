import time
import itertools 

def generateCombinations(n):
    operations = ['+', '*', '|']
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
            next_num = line[1][index]
            if operation == '+':
                result += next_num
            if operation == '*':
                result *= next_num
            if operation == '|':
                left_part = str(result)
                right_part = str(next_num)
                result = int(left_part+right_part) 
            index +=1
        
        if(result == line[0]):
            return True
        
    return False


if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.5f}s")