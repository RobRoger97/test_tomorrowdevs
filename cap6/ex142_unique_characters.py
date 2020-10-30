#read the string from the user
s = input("Enter a string: ")

characters = {}

for ch in s:
    characters[ch] = True

# Display the result
print("That string contained", len(characters), \
"unique character(s).")