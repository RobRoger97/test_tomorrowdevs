#Read the side lenghts from the user
side1 = float(input("Enter the lenght of side 1: "))
side2 = float(input("Enter the lenght of side 2: "))
side3 = float(input("Enter the lenght of side 3: "))

#Determine the triangle's type
if side1==side2 and side2==side3:
    t_type = "equilateral"
elif side1==side2 or side2==side3 or side3==side1:
    t_type = "isosceles"
else:
    t_type = "scalene"

#Display the triangle's type
print("That's a ", t_type, " triangle")