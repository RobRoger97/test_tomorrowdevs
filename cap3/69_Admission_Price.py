# Store the admission prices as constants
Baby_Price = 0.00
Child_Price = 14.00
Adult_Price = 23.00
Senior_Price = 18.00
# Create a variable to hold the total admission cost for all guests
total = 0
# Store the age limits as constants
B_Limit = 2
C_Limit = 12
A_Limit = 64

# Keep on reading ages until the user enters a blank line
line = input("Enter the age of the guest (blank to finish): ")
while line != "":
    age = int(line)
    # Add the correct amount to the total
    if age <= B_Limit:
        total = total + Baby_Price
    elif age <= C_Limit:
        total = total + Child_Price
    elif age <= A_Limit:
        total = total + Adult_Price
    else:
        total = total + Senior_Price
# Read the next age from the user
line = input("Enter the age of the guest (blank to finish): ")

# Display the total due for the group, formatted using two decimal places
print("The total for that group is $%.2f" % total)