import time

def get_input(file_name):
    new_list = []
    
    with open(file_name, 'r') as file:
        data = file.read().strip().split('\n\n') 
        
        for block in data:
            lines = block.split('\n')  
            
            button_a = list(map(int, lines[0].replace('Button A: X+', '').replace('Y+', '').split(', ')))
            button_b = list(map(int, lines[1].replace('Button B: X+', '').replace('Y+', '').split(', ')))
            prize = list(map(int, lines[2].replace('Prize: X=', '').replace('Y=', '').split(', ')))
            
            new_list.append([button_a, button_b, prize])
    
    return new_list 

def sistem(lista):
    btn_a = [lista[0][0], lista[1][0]]
    btn_b = [lista[0][1], lista[1][1]]
    prize = [lista[2][0] +  10000000000000, lista[2][1] +  10000000000000]

    eq1_x = btn_a[0] * btn_b[1]
    eq1_result = (prize[0]) * btn_b[1]

    eq2_x = btn_b[0] * btn_a[1]
    eq2_result = (prize[1]) * btn_a[1]

    token1 = (eq1_result - eq2_result)/(eq1_x - eq2_x)
    token2 = (prize[0] - (btn_a[0] * token1)) / btn_a[1]

    return token1 * 3 + token2

def main():
    file_name = 'input.txt'
    claw_machines = get_input(file_name)

    tokens_sum = 0
    for claw in claw_machines:
        tokens = sistem(claw)
        if tokens.is_integer():
            tokens_sum += tokens

    print(tokens_sum)   


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")
