import time
import math

def main():
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        lines = file.readlines()
    lines = [line for line in lines if line.strip()]
    
    available_towel_patterns = list(lines[0].strip().split(', '))
    desired_patterns = list(pattern.strip() for pattern in lines[1:])
    
    count = 0
    for pattern in desired_patterns:
        if canFormPattern(pattern, available_towel_patterns):
            count += 1

    print(count)


def canFormPattern(pattern, available_patterns):
    dp = [False] * (len(pattern) + 1)
    dp[0] = 1

    for i in range(1, len(pattern) + 1):
        for available in available_patterns:
            if i >= len(available) and pattern[i - len(available):i] == available:
                dp[i] += dp[i - len(available)]
                
    return dp[len(pattern)]


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.5f}s")
