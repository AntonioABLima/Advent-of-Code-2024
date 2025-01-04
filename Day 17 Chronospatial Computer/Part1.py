import math
import time

def processInput():
    with open('input.txt', 'r') as file:
        input_string = file.read()

    registers_part, program_part = input_string.split("\n\n")

    lines = registers_part.split('\n')
    registers = [int(line.split(': ')[1]) for line in lines]

    program_part = program_part.strip()
    program = program_part.split(': ')
    program = [int(x) for x in program[1].split(',')]

    return registers, program

def bitWiseXOR(number1, number2):
    return number1 ^ number2

def moduloEight(number):
    return number % 8

def main():
    [reg_a, reg_b, reg_c], program = processInput()
    i = 0
    output = []
    while i < len(program) - 1:
        instruction = program[i]
        literal_operand = program[i + 1]

        combo_operand = literal_operand
        if literal_operand == 4:
            combo_operand = reg_a
        elif literal_operand == 5:
            combo_operand = reg_b
        elif literal_operand == 6:
            combo_operand = reg_c

        if instruction == 0:
            reg_a = math.floor(reg_a / (2 ** combo_operand))
        elif instruction == 1:
            reg_b = bitWiseXOR(reg_b, literal_operand)
        elif instruction == 2:
            reg_b = moduloEight(combo_operand)
        elif instruction == 3:
            if reg_a != 0:
                i = literal_operand
                continue
        elif instruction == 4:
            reg_b = bitWiseXOR(reg_b, reg_c)
        elif instruction == 5:
            output.append(moduloEight(combo_operand))
        elif instruction == 6:
            reg_b = math.floor(reg_a / (2 ** combo_operand))
        elif instruction == 7:
            reg_c = math.floor(reg_a / (2 ** combo_operand))

        i += 2

    print(','.join(map(str, output)))


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")
