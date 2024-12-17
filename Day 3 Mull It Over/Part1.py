import time

def findMulStr(_input):
    matriz = []
    i = 0
    while i < len(_input) - 7 :
        firts_num_digits = 0
        second_num_digits = 0

        mul_len = i+4
        if(_input[i:mul_len] == 'mul('):  
            for j in range(i+4, mul_len+4): 
                if _input[j].isnumeric():
                    firts_num_digits += 1

                num1 = 0
                if _input[j] == ',': 
                    num1 = int(_input[mul_len:mul_len+firts_num_digits])
                    comma_len = j+1
                    for k in range(comma_len, comma_len+4): 
                        if _input[k].isnumeric():
                            second_num_digits += 1

                        if _input[k] == ')':
                            num2= int(_input[comma_len:comma_len+second_num_digits])
                            matriz.append([num1, num2])
                            break

            i += 4 +  firts_num_digits + second_num_digits + 1
        else: 
            i+=1
            
    return matriz

def multAndAdd(_list):
    total_sum = 0
    for pair in _list:
        mult = pair[0] * pair[1]
        total_sum += mult

    return total_sum

def main():
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        _input = file.read()

    not_corruped_list = findMulStr(_input)

    answer = multAndAdd(not_corruped_list) 

    print(answer)

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")