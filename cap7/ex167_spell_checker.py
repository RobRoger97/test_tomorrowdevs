from string import digits, punctuation
import sys

word_file = "C:/Users/Roberta/Desktop/Python/words.txt"

# Ensure that the program has the correct number of command line arguments
if len(sys.argv) != 2:
    print("One command line argument must be provided.")
    print("Quitting...")
    quit()

try:
    inf = open(sys.argv[1],'r')
except:
    print("Failed to open ’%s’ for reading. Quitting..." % \
          sys.argv[1])
    quit()

# word, but it is never used.
valid = {}
words_file = open(word_file, "r")
for word in words_file:
# Convert the word to lowercase and remove the trailing newline character
    word = word.lower().rstrip()
# Add the word to the dictionary
    valid[word] = 0
words_file.close()

# Read each line from the file, adding any misspelled words to the list of misspellings
misspelled = []
for line in inf:
# Discard the punctuation marks by calling the function developed in Exercise 117
    line = line.translate(str.maketrans('', '', digits))
    line = line.translate(str.maketrans('', '', punctuation)).lower()
    for word in line.split():
# Only add to the misspelled list if the word is misspelled and not already in the list
        if word not in valid and word not in misspelled:
            misspelled.append(word)
# Close the file being checked
inf.close()
# Display the misspelled words, or a message indicating that no words are misspelled
if len(misspelled) == 0:
    print("No words were misspelled.")
else:
    print("The following words are misspelled:")
    for word in misspelled:
        print(" ", word)