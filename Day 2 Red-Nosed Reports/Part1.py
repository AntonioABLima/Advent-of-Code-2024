import time

def checkAllIncreasing (report):
	for i in range(len(report) - 1):
		if report[i] > report[i + 1]:
			return False
	
	return True
	
def checkAllDecreasing (report):
	for i in range(len(report) - 1):
		if report[i] < report[i + 1]:
			return False
	
	return True

def checkDiffer(report):
	for i in range(len(report) - 1):
		differ = abs(report[i] - report[i + 1])
		if(differ == 0 or differ > 3):
			return False
	
	return True

def allChecks(report):
	allIncreasing = checkAllIncreasing(report)
	allDecreasing = checkAllDecreasing(report)
	differRight = checkDiffer(report)
	return (allIncreasing or allDecreasing) and differRight

def main():
	file_name = 'input.txt'
	with open(file_name, 'r') as file:
		lines = file.readlines()

	matrix = []

	for line in lines:
		nums = line.strip().split()
		matrix.append([int(num) for num in nums])


	safe_reports_sum = 0
	for linha in matrix:
		if(allChecks(linha)):
			safe_reports_sum += 1

	print(safe_reports_sum)

if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.5f}s")