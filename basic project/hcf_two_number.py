def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print(f"The HCF of {number1} and {number2} is: {hcf(number1,number2)}")

