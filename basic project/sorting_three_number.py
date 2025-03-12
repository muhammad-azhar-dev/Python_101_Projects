a = int(input("please enter the first number: "))
b = int(input("please enter the second number: "))
c = int(input("please enter the third number: "))

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print("Sorted numbers: ", a, b, c)