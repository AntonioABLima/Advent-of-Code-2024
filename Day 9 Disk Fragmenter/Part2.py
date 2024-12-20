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


def findFreeSpace(blocks, file_length):
    free_start = -1
    free_length = 0

    for i, block in enumerate(blocks):
        if block == '.':
            if free_start == -1:
                free_start = i
            free_length += 1

            if free_length == file_length:
                return free_start
        else:
            free_start = -1
            free_length = 0

    return None

def compactFiles(disk_map):
    blocks = parseDiskMap(disk_map)

    files = {}
    for i, block in enumerate(blocks):
        if block != '.' and int(block) not in files:
            files[int(block)] = {'start': i, 'length': blocks.count(block)}

    for file_id in sorted(files.keys(), reverse=True):
        file_info = files[file_id]
        start, length = file_info['start'], file_info['length']

        free_start = findFreeSpace(blocks, length)
        if free_start is not None and free_start < start:
            # Move o arquivo para o espaço livre
            for i in range(length):
                blocks[free_start + i] = str(file_id)
                blocks[start + i] = '.'

    return blocks

def calculateChecksum(blocks):
    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] == '.':
            continue
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
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.5f}s")
