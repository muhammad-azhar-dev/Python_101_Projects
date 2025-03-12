numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
even_sum = sum(num for num in numbers if num % 2 == 0)
print(f"The sum of even numbers is: {even_sum}")