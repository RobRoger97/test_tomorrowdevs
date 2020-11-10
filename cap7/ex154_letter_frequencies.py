import sys

if len(sys.argv)!=2:
    print("Provide the file name as a command line argument.")
    quit()

try:
    # Open the file for reading
    inf = open(sys.argv[1], "r")
# Read the first line from the file
    line = inf.readline()
    lines = list(line.upper())
    counts = {}
    while line!='':
        for i in lines:
            if i.isalpha():#If the character of the string is a letter of the alphabet, move on.
                if i in counts:
                    counts[i] = counts[i]+1
                else: 
                    counts[i] = 1
        line = inf.readline()
        lines = list(line.upper())        
    #Display the result
    print("The frequencies of all of the letters in that file are:\n",counts)
    #Close file
    inf.close()
except IOError:
# Display a message if something goes wrong while accessing the file
    print("An error occurred while accessing the file.")