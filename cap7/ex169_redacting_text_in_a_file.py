# Get the name of the input file and open it
inf_name = input("Enter the name of the text file to redact: ")
inf = open(inf_name, "r")
# Get the name of the sensitive words file and open it
sen_name = input("Enter the name of the sensitive words file: ")
sen = open(sen_name, "r")
# Load all of the sensitive words into a list
words_list = []
line = sen.readline()
while line != "":
    line = line.rstrip()
    words_list.append(line)
    line = sen.readline()
# Close the sensitive words file
sen.close()

# Get the name of the output file and open it
outf_name = input("Enter the name for the new redacted file: ")
outfile = open(outf_name, "w")
# Read each line from the input file. Replace all of the sensitive words with asterisks. Then
# write the line to the output file.
line = inf.readline()
while line != "":
# Check for and replace each sensitive word. The number of asterisks matches the number
# of letters in the word being redacted.
    for word in words_list:
        line = line.replace(word, "*" * len(word))
# Write the modified line to the output file
    outfile.write(line)
# Read the next line from the input file
    line = inf.readline()
# Close the input and output files
inf.close()
outfile.close()