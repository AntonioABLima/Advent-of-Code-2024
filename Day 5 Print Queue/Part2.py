import time
def verifyUpdate(update, _dict):
    for i in range(len(update)):
        for j in range(i + 1, len(update) - 1):
            if(not(update[j] in _dict[update[i]][1])): 
                return False
        
        for j in range(i - 1, -1, -1):  
            if not(update[j] in _dict[update[i]][0]):
                return False
        
    return True
            
def findMiddle(_list):
    return _list[len(_list) // 2]

def process_input(lines):
    ordering_rules = []
    updates = []

    gap_flag = False
    for linha in lines:
        if(linha == '\n'):
            gap_flag = True
            continue

        if(not(gap_flag)):
            nums = linha.split('|')
            ordering_rules.append([int(numero) for numero in nums])
        else:
            nums = linha.split(',')
            updates.append([int(numero) for numero in nums])

    return ordering_rules, updates


def main():
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        lines = file.readlines()

    ordering_rules, updates  = process_input(lines)

    unique_page_numbers_list = set(num for sub_list in ordering_rules for num in sub_list)
    unique_page_numbers_dict = {item: [[], []] for item in unique_page_numbers_list}

    for rule in ordering_rules:
        unique_page_numbers_dict[rule[0]][1].append(rule[1]) 
        unique_page_numbers_dict[rule[1]][0].append(rule[0]) 

    wrong_updates = []
    for update in updates:
        if(not (verifyUpdate(update, unique_page_numbers_dict))):
            wrong_updates.append(update)


    for update in wrong_updates:
        while not(verifyUpdate(update, unique_page_numbers_dict)):
            for i in range(len(update)):
                for j in range(i + 1, len(update) - 1):
                    if(not(update[j] in unique_page_numbers_dict[update[i]][1])): 
                        aux = update[j]
                        update[j] =  update[i]
                        update[i] = aux

                for j in range(i - 1, -1, -1):  
                    if not(update[j] in unique_page_numbers_dict[update[i]][0]):
                        aux = update[j]
                        update[j] =  update[i]
                        update[i] = aux

    correct_updates_sum = 0
    for update in wrong_updates:
        if(verifyUpdate(update, unique_page_numbers_dict)):
            middle = findMiddle(update)
            correct_updates_sum += middle   

    print(correct_updates_sum)
    
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")