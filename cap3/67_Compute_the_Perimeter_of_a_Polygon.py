import math

# Store the perimeter of the polygon
perimeter = 0

# Read the coordinate of the first point from user
first_x = float(input("Enter the first x-coordinate: "))
first_y = float(input("Enter the first y-coordinate: "))

# Provide initial values for prev x and prev y
prev_x = first_x
prev_y = first_y
# Read the remaining coordinates
line = input("Enter the next x-coordinate (blank to quit): ")
while line != "":
# Convert the x-coordinate to a number and read the y coordinate
    x = float(line)
    y = float(input("Enter the next y-coordinate: "))

# Compute the distance to the previous point and add it to the perimeter
    dist = math.sqrt((prev_x - x) ** 2 + (prev_y - y) ** 2)
    perimeter = perimeter + dist

# Set up prev x and prev y for the next loop iteration
    prev_x = x
    prev_y = y

# Read the next x-coordinate
    line = input("Enter the next x-coordinate (blank to quit): ")
# Compute the distance from the last point to the first point and add it to the perimeter
dist = math.sqrt((first_x - x) ** 2 + (first_y - y) ** 2)
perimeter = perimeter + dist
    
# Display the result
print("The perimeter of that polygon is", perimeter)