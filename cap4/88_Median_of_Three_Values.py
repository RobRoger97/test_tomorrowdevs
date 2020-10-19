#Median's function
def Median_function(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)

# Display the median of 3 values entered by the user
def main():
    x = float(input("Enter the first value: "))
    y = float(input("Enter the second value: "))
    z = float(input("Enter the third value: "))

    print("The median value is:", Median_function(x, y, z))

# Call the main function
main()