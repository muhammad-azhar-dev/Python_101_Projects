n = int(input("Enter the number of terms: "))
f1,f2 = 0,1
print("Fibonacci sequece: ")
for _ in range(n):
    print(f1, end=" ")
    f1, f2 = f2, f1 + f2