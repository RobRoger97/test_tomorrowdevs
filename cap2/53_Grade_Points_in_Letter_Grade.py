# Convert from a letter grade to a number of grade points.
A = 4.0
D = 1.0
F = 0
Invalid = -1

#Read the number from user
n = float(input("Enter a grade point: "))


if n >= A:
     Letter = "A+ (or A if grade point is 4.0)"
elif n < A and n>=3.9:
     Letter = "A"
elif n <= 3.8 and n>=3.6:
    Letter = "A-"
elif n <= 3.5 and n>=3.2:
    Letter = "B+"
elif n <= 3.1 and n>=2.9:
    Letter = "B"
elif n <=2.8 and n>=2.6:
    Letter = "B-"
elif n <=2.5 and n>=2.2:
    Letter = "C+"
elif n <=2.1 and n>=1.9:
    Letter = "C"
elif n <=1.8 and n>1.6:
    Letter = "C-"
elif n <=1.5 and n>1.2:
    Letter = "D+"
elif n == D:
    Letter = "D"
elif n == F:
    Letter = "F"
else:
    Letter = Invalid

#Display the result
if Letter == Invalid:
    print("That wasn’t a valid letter grade.")
else:
    print("A(n)", n, "is equal to", Letter, "letter grade.")