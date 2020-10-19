##
# Convert a number from decimal (base 10) to binary (base 2).
#
New_Base = 2
# Read the number to convert from the user
n = int(input("Enter a non-negative integer: "))
# Generate the binary representation of num, storing it in result
result = ""
# Perform the body of the loop once
r = n % New_Base
result = str(r) + result
n = n // New_Base
# Keep on looping until q is 0
while n > 0:
    r = n % New_Base
    result = str(r) + result
    n = n // New_Base

# Display the result
print(n, "in decimal is", result, "in binary.")