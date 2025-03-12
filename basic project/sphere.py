import math 

r = float(input("Enter the radius of the sphere: "))
surface_area = 4 * math.pi * r ** 2
volume = (4/3) * math.pi * r**3
print(f"Surface area of the sphere is: {surface_area:.2f}")
print(f"Volume of the sphere is: {volume:.2f}")