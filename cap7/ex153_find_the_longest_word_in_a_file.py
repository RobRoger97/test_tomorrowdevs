import sys
import re

if len(sys.argv)!=2:
    print("Provide the file name as a command line argument.")
    quit()

try:
    # Open the file for reading
    inf = open(sys.argv[1], "r")
# Read the first line from the file
    line = inf.readline()
    lines = re.split('[ \n]',line)
    mx=0
    while line!='':
        for word in lines:
            if word != ' ':
                if len(word)>mx:
                    mx = len(word)
                    lis = [word]
                elif len(word)==mx:
                    lis.append(word)
        line = inf.readline()
        lines = re.split('[ \n]',line)
    print(" the length of the longest word in the file is:",mx, \
        "\n all of the words of that length that occurred in the file are: \n",lis)
    # Close the file
    inf.close()
except IOError:
# Display a message if something goes wrong while accessing the file
    print("An error occurred while accessing the file.")