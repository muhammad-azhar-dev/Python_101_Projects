numbers = sorted(map(int, input("Enter numbers separated by spaces: ").split()))
n = len(numbers)
if n % 2 == 0:
    median = (numbers[n//2 - 1] + numbers[n//2]) / 2
else:
    median = numbers[n//2]

print(f"the median is: {median}")