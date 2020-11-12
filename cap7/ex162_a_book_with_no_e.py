word_file = "C:/Users/Roberta/Desktop/Python/words.txt"
dict_words = {}
for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    dict_words[ch]=0

# Open the file, process each word, and update the counts dictionary
num_words = 0
inf = open(word_file, "r")
for word in inf:
# Convert the word to uppercase and remove the newline character
    word = word.upper().rstrip()
    unique = []
    for ch in word:
        if ch not in unique and ch >= "A" and ch <= "Z":
            unique.append(ch)
# Now increment the counts for all of the letters that are in the list of unique characters
    for ch in unique:
        dict_words[ch]+= 1
   # Keep track of the number of words that we have processed
    num_words+=  1
# Close the file
inf.close() 

smallest_count = min(dict_words.values())
for ch in sorted(dict_words):
    if dict_words[ch] == smallest_count:
        smallest_letter = ch
    percentage = dict_words[ch] / num_words * 100
    print(ch, "occurs in %.2f percent of words" % percentage)
# Display the letter that is easiest to avoid based on the number of words in which it appears
print()
print("The letter that is easiest to avoid is", smallest_letter)