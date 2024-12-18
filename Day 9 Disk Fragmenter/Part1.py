import time

def parseDiskMap(disk_map):
    blocks = []
    _id = 0
    flag = True
    for numero in disk_map:
        char = str(_id) if flag else '.'
        blocks.extend([char] * int(numero))
        if flag:
            _id += 1
        flag = not flag

    return blocks

def compactFiles(disk_map):
    blocks = parseDiskMap(disk_map)

    dot_positions = []
    for i in range(len(blocks)):
        if blocks[i] == '.':
            dot_positions.append(i)
    
    num = 0
    for i in range(len(blocks) - 1, -1, -1):
        if(blocks[i] == '.'): continue
       
        blocks[dot_positions[num]] = blocks[i]
        blocks[i] = '.'
        num+=1
        
        if not '.' in blocks[:i]: break

    return blocks

def calculateChecksum(blocks):
    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] == '.':
            break
        checksum += i * int(blocks[i])

    return checksum


def main():
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        line = list(file.readline())
    
    final_blocks = compactFiles(line)
    checksum = calculateChecksum(final_blocks)

    print(checksum)

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")
