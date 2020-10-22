#Read words from the user until the user enters a blank line
word=input("Enter a word (blank line to quit): ")

# Start with an empty list
lis = []

#While loop
while word != "":
    
    if not(word in lis):
        lis.append(word)

    word=input("Enter a word (blank line to quit): ")

#Display the result
for word in lis:
    print(word)
 

