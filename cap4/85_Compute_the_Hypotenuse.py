import math

#Function that that takes the lengths of the two shorter sides of a right triangle as
#its parameters. Return the hypotenuse of the triangle
def triangle(l1,l2):
    h=math.sqrt(l1**2+l2**2)
    return h

def main():
#Read the lenghts from the user
    q1 = float(input("Enter the first lenght: "))
    q2 = float(input("Enter the second lenght: "))

#Display the result
    print("A triangle with the lengths of the two shorter sides: ",q1 ,\
    "and",q2,"has the hypotenuse: %.2f" %(triangle(q1,q2)))

# Call the main function
main()