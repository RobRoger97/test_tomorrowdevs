import sys

num_lines = 10

if len(sys.argv)!=2:
    print("Provide the file name as a command line argument.")
    quit()

try:
    # Open the file for reading
    inf = open(sys.argv[1], "r")
# Read the first line from the file
    line = inf.readline()
# Keep looping until we have either read and displayed 10 lines or we have reached the end
# of the file
    count = 0
    while count < num_lines and line != "":
# Remove the trailing newline character and count the line
        line = line.rstrip()
        count = count + 1
# Display the line
        print("%d : %s" %(count,line))
# Read the next line from the file
        line = inf.readline()
# Close the file
    inf.close()
except IOError:
# Display a message if something goes wrong while accessing the file
    print("An error occurred while accessing the file.")