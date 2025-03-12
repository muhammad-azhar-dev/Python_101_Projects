import math 

# Get input for radius and height
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the Height of the cylinder: "))

# calculate the volume and surface area
volume = math.pi*radius**2*height
surface_area = 2*math.pi*radius**2+2*math.pi*radius*height

# display the result
print("Volume of the cylinder is: " ,round(volume,2))
print("surface area of the cylinder is: ", round(surface_area,2))