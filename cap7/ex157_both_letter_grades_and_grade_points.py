letter_grade = {'A_plus':4.0,'A':4.0,'A_minus':3.7,'B_plus':3.3,'B':3.0,'B_minus':2.7,'C_plus':2.3,'C':2.0,\
                'C_minus':1.7,'D_plus':1.3,'D':1.0,'F':0,'Invalid':-1}


# Read the first line of input from the user
line = input("Enter a letter grade or a grade point: ").upper()
# Keep reading until the user enters a blank line
while line != "":
    try:
# Try and convert the line to a number
        num = float(line)
# convert each value entered by the user from a number of grade points to a letter grade
        for key,value in letter_grade.items():
            if value == num:
                if num == 4.0:
                    print("That grade point corresponds to A_plus or A!")
                else:    
                    print("That grade point corresponds to", key)
        if num not in letter_grade.values():
            print("Please, enter a valid grade point!")
# If an exception occurs during this process... 
    except ValueError:
# Try and convert the line to a string
        st = str(line)
#...then your program should attempt to convert 
# the value from a letter grade to a number of grade points.
        for key,value in letter_grade.items():
            if key == st:
                print("That letter grade corrisponds to",value)      
        if st not in letter_grade.keys():
            print("Please, enter a valid letter grade!")
# Read the next number
    line = input("Enter a letter grade or a grade point: ").upper()