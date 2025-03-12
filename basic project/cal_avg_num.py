numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
average = sum(numbers) / len(numbers)
print(f"The average of the numbers is: {average:.3f}")
