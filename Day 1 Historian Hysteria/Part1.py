import time

def main():
    list_a = []
    list_b = []

    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        lines = file.readlines()

    for line in lines:
        num1, num2 = map(int, line.strip().split())
        list_a.append(num1)
        list_b.append(num2)

    list_a.sort()
    list_b.sort()

    distance_sum = 0
    for i in range(len(list_a)):
        distance_between_pair = list_a[i] - list_b[i]
        distance_sum += abs(distance_between_pair)

    print(distance_sum)

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")