from string import punctuation
#list of words that follow the rule
lis_right=[]
#list of words that don't follow the rule
lis_wrong=[]

word_file = "C:/Users/Roberta/Desktop/Python/words.txt"
inf = open(word_file, "r")

line = inf.read()
# Remove punctuation and turns into lowercase letters
line = line.translate(str.maketrans('', '', punctuation)).lower()
# Create a list containing the words of the file
words = line.split()
for i in range(len(words)):

    if "ie" in words[i]:
        if words[i] not in lis_right:
            if words[i] not in lis_wrong:
                lis_right.append(words[i])
        
    if "cei" in words[i]:
        if words[i] not in lis_right:
            lis_right.append(words[i])
#----------------------------------------
    if "ei" in words[i]:
        if words[i] not in lis_wrong:
            if words[i] not in lis_right:
                lis_wrong.append(words[i])        

    if "cie" in words[i]:
        if words[i] not in lis_wrong:
            lis_wrong.append(words[i])
#Report the lengths of the lists...
leng_right = len(lis_right)
leng_wrong = len(lis_wrong)
tot_len = len(words)

print("The words that follow the rule are:\n", lis_right)
print()
print("The words that do not follow the rule are:\n", lis_wrong)
print()
#...at the end of the program so that one can easily determine the proportion of
#the words in the file that respect the “I before E except after C” rule.
print("Therefore, making a proportion, out of %d words %d follow "\
      "the rule and %d do not follow the rule"%(tot_len,leng_right,leng_wrong))