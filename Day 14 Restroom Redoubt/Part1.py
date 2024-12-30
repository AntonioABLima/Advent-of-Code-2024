import time

def get_input(file_name):
    data = []

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                positions, velocities = line.split(' v=')
                
                p = positions.replace('p=', '')  
                p = tuple(map(int, p.split(','))) 
                
                v = tuple(map(int, velocities.split(','))) 
                
                data.append((p, v))

    return data

def posAfterTime(robot, row, col):
    sec = 0
    pos = robot[0]
    vel = robot[1]
    
    x = pos[0]
    y = pos[1]
    while sec < 100:
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
    
        sec += 1

    return [x, y]

def divideQuadrante(lista, row, col):
    pri = 0
    seg = 0
    ter = 0
    qua = 0
    
    for pos in lista:
        x = pos[0]
        y = pos[1]

        if x <= (col / 2) - 1 and  y <= (row / 2) - 1: # Pri
            pri += 1
        if x >= (col / 2) + 1 and  y <= (row / 2) - 1: # Seg
            seg += 1 
        if x <= (col / 2) - 1 and  y >= (row / 2) + 1: # ter
            ter += 1
        if x >= (col / 2) + 1 and  y >= (row / 2) + 1: # qua
            qua += 1


    return [pri, seg, ter, qua]

def main():
    file_name = 'input.txt'

    robots = get_input(file_name)

    pos_list = []
    for robot in robots:
        pos = posAfterTime(robot, 102, 100)
        pos_list.append(pos)
    
    quadrantes = divideQuadrante(pos_list, 102, 100)

    acc = 1
    for quadrante in quadrantes:
        acc *= quadrante

    print(acc)


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")