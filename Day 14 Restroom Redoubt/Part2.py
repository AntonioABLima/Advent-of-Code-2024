import time

def get_input(file_name):
    data = []

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                positions, velocities = line.split(' v=')
                
                p = positions.replace('p=', '')  
                p = list(map(int, p.split(','))) 
                
                v = list(map(int, velocities.split(','))) 
                
                data.append([p, v])

    return data

def posAfterTime(robot, row, col):
    pos = robot[0]
    vel = robot[1]
    
    x = pos[0]
    y = pos[1]
    x += vel[0]
    y += vel[1]

    if y < 0:
        y += row + 1
    if x < 0:
        x += col + 1

    if y > row:
        y -= row + 1
    
    if x > col:
        x -= col + 1

    return [x, y]

def printAll(lista, row, col):
    for i in range(col):

        for j in range(row):
            if [j, i] in lista:
                print('x', end='')
            else:
                print('.', end='')
        print()

def main():
    file_name = 'input.txt'

    robots = get_input(file_name)
    tam = len(robots)

    pos_list = []
    sec = 0
    while sec < 15000:
        pos_list = []
        pos_set = set()
            
        for i in range(len(robots)):
            pos = posAfterTime(robots[i], 102, 100)
            pos_list.append(pos)
            pos_set.add((pos[0], pos[1]))
            robots[i][0] = pos
            
        sec+=1
        if tam == len(pos_set):
            print(sec)
            printAll(pos_list, 102, 100)
            break
             
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")