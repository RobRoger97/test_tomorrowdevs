Pennies_Per_Nickel = 5
Nickel = 0.05

# Track the total cost for all of the items
total = 0.00

# Read the price of the first item as a string
line = input("Enter the price of the item (blank to quit): ")

# Continue reading items until a blank line is entered
while line != "":
    total = total + float(line)
    line = input("Enter the price of the item (blank to quit): ")
    print("The exact amount payable is %.02f" % total)

# Compute the number of pennies that would be left if the total was paid using nickels
rounding_indicator = total * 100 % Pennies_Per_Nickel

if rounding_indicator < Pennies_Per_Nickel / 2:
    cash_total = total - rounding_indicator / 100
else:
    cash_total = total + Nickel - rounding_indicator / 100

# Display amount due when paying with cash
print("The cash amount payable is %.02f" % cash_total)