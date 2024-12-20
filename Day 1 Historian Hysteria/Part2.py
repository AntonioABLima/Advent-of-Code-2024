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

    similarity_sum = 0
    for i in range(len(list_a)):
        num_occurrences = list_b.count(list_a[i])
        similarity_sum += (num_occurrences * list_a[i])

    print(similarity_sum)

if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.5f}s")