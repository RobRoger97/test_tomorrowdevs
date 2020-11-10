from random import randrange

word_file = "C:/Users/Roberta/Desktop/Python/cicci.txt"

# Read all of the words from the file, only keeping those between 3 and 7 letters in length,
# and store them in a list
words = []
inf = open(word_file, "r")
for line in inf:
# Remove the newline character
    line = line.rstrip()
# Keep words that are between 3 and 7 letters long
    if len(line) >= 3 and len(line) <= 7:
        words.append(line)
# Close the file
inf.close()
# Randomly select the first word for the password. It can be any word.
first = words[randrange(0, len(words))]
first = first.capitalize()
# Keep selecting a second word until we find one that doesn’t make the password too short
# or too long
password = first
while len(password) < 8 or len(password) > 10:
    second = words[randrange(0, len(words))]
    second = second.capitalize()
    password = first + second
# Display the random password
print("The random password is:", password)