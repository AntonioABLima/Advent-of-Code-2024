import time

def change(stones):
    new_stones= []
    
    for i in range(len(stones)):
        if stones[i] == 0:
            new_stones.append(1)
        elif len(str(stones[i])) % 2 == 0:
            str_stone = str(stones[i])
            num_digits = len(str_stone)

            new_stones.append(int(str_stone[:num_digits//2]))
            new_stones.append(int(str_stone[num_digits//2:]))
        else:
            new_stones.append(stones[i] * 2024)
   
    return new_stones

def main():
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        line = file.readline()

    stones  = list(map(int, line.split()))
    blink = 0
 
    while blink < 25:
        stones = change(stones)
        blink+= 1

    print(len(stones))
    
if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.5f}s")