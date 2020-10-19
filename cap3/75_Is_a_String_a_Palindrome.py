# Read the string from the user
line = input("Enter a string: ")

is_palindrome = True
i = 0

#While loop to scroll through the string
while i < len(line) / 2 and is_palindrome:
# If the characters do not match then mark that the string is not a palindrome
    if line[i] != line[len(line) - i - 1]:
        is_palindrome = False
        
# Move to the next character
    i+=1

# Display a meaningful output message
if is_palindrome:
    print(line, "is a palindrome")
else:
    print(line, "is not a palindrome")