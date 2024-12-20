import time
from functools import cache

@cache
def change(stone, steps):
    if steps == 0:
        return 1
    
    if stone == 0:
        return change(1, steps - 1)

    elif len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        num_digits = len(str(stone))
        
        first_half = int(str_stone[:num_digits//2])
        second_half = int(str_stone[num_digits//2:])

        return change(first_half, steps - 1) + change(second_half, steps - 1)
    else:
        return change(stone * 2024, steps - 1)

def main():
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        line = file.readline()

    stones = list(map(int, line.split()))

    num_stones = 0
    for stone in stones:
        num_stones += change(stone, 75)
 
    print(num_stones)

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")