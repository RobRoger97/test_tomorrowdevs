import sys
# Verify that at least one file name has been provided as a command line argument
if len(sys.argv) == 1:
    print("At least one filename must be provided as a", \
          "command line argument.")
    print("Quitting...")
    quit()

# Process each file provided as a command line argument
for filename in sys.argv[1 : len(sys.argv)]:
# Attempt to process the file
    try:
        inf = open(filename, "r")
        prev = " "
        linenum = 1

        # Check each line in the current file
        for line in inf:
# If the line is a function definition and the previous line is not a comment
            if line.startswith("def ") and prev[0] != "#":
# Find the first ( on the line so that we know where the function name ends
                bracket_pos = line.index("(")
                name = line[4 : bracket_pos]
# Display information about the function that is missing its comment
                print("%s line %d: %s" % (filename, linenum, name))
# Save the current line and update the line counter
            prev = line
            linenum+= 1
# Close the current file
        inf.close()
    except:
        print("A problem was encountered with file ’%s’." % filename)
        print("Moving on to the next file...")