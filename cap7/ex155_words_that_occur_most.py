import nltk
# Read the file name from the user
fname = input("Enter the file name: ")
file_opened = False
while file_opened == False:
# Attempt to open the file
    try:
        # Open the current file for reading
        inf = open(fname, "r")
        file_opened = True
# Read the first line from the file
        line = inf.readline()
        counts = {}
        while line!='':
            lines = nltk.word_tokenize(line.upper())
            for i in lines:
                if i!='!'and i!='?'and i!="'"and i!=';'and i!=','and i!=':'and i!='.'and i!='-'and i!='_':
                    if i in counts:
                        counts[i] = counts[i]+1
                    else: 
                        counts[i] = 1
            line = inf.readline()
        #Display the result
        print("The frequencies of all of the words in that file are:\n",counts)
        #Close file
        inf.close()
    except FileNotFoundError:
# Display an error message and read another file name if the file was not
# opened successfully
        print("’%s’ wasn’t found. Please try again."%(fname))
        fname = input("Enter the file name: ")