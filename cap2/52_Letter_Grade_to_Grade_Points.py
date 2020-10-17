# Convert from a letter grade to a number of grade points.
A = 4.0
A_minus = 3.7
B_plus = 3.3
B = 3.0
B_minus = 2.7
C_plus = 2.3
C = 2.0
C_minus = 1.7
D_plus = 1.3
D = 1.0
F =0
Invalid = -1
# Read the letter grade from the user
letter = input("Enter a letter grade: ")
letter = letter.upper()

# Convert from a letter grade to a number of grade points using -1 grade points as a sentinel
# value indicating invalid input
if letter == "A+" or letter == "A":
    gp = A
elif letter == "A-":
    gp = A_minus
elif letter == "B+":
    gp = B_plus
elif letter == "B":
    gp = B
elif letter == "B-":
    gp = B_minus
elif letter == "C+":
    gp = C_plus
elif letter == "C":
    gp = C
elif letter == "C-":
    gp = C_minus
elif letter == "D+":
    gp = D_plus
elif letter == "D":
    gp = D
elif letter == "F":
    gp = F
else:
    gp = Invalid

# Report the result
if gp == Invalid:
    print("That wasn’t a valid letter grade.")
else:
    print("A(n)", letter, "is equal to", gp, "grade points.")