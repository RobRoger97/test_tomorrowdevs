Rais_Factor = 2400.00
Unacceptable = 0
Acceptable = 0.4
Meritorious = 0.6

# Read the rating from the user
rating = float(input("Enter the rating: "))

# Classify the performance
if rating == Unacceptable:
    performance = "Unacceptable"
elif rating == Acceptable:
    performance = "Acceptable"
elif rating >= Meritorious:
    performance = "Meritorious"
else:
    performance = ""

# Display the result
if performance == "":
    print("That wasn’t a valid rating.")
else:
    print("Based on that rating, your performance is %s." % performance)
    print("You will receive a raise of $%.2f." % (rating * Rais_Factor))