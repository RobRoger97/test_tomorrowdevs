# Read two positive integers from the user
n = int(input("Enter a positive integer: "))
m = int(input("Enter a positive integer: "))

#Initialize d to the smaller of m and n.
#While d does not evenly divide m or d does not evenly divide n do
#Decrease the value of d by 1
#Report d as the greatest common divisor of n and m

# Initialize 
d = min(n, m)

# Use a while loop to find the greatest common divisor of n and m
while n % d != 0 or m % d != 0:
    d-=1

#Display the result
print("The greatest common divisor of", n, "and", m, "is", d)