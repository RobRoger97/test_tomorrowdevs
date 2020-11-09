# Read the file name from the user
fname = input("Enter the file name: ")
file_opened = False
while file_opened == False:
# Attempt to open the file
    try:
        # Open the current file for reading
        inf = open(fname, "r")
        # Open a new file that the program will create
        fout = open('C:/Users/Roberta/Desktop/Python/copy_wn.txt', 'w')
        file_opened = True
        count = 1
        for line in inf:
            st = str(count)+":"+" "+line #Each line in the output file should begin with the line number, followed by a colon and a space,
            fout.write(st)               #followed by the line from the input file.
            count+=1
        # Close files
        fout.close()
        inf.close()
    except FileNotFoundError:
# Display an error message and read another file name if the file was not
# opened successfully
        print("’%s’ wasn’t found. Please try again."%(fname))
        fname = input("Enter the file name: ")