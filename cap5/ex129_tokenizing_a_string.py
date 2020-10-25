def tokenList(s) :
# Remove all of the spaces from s
    s = s.replace(" ", "")
# Loop through all of the characters in the string, identifying the tokens and adding them to
# the list
    tokens = []
    i = 0
    while i < len(s):
# Handle the tokens that are always a single character: *, /, ˆ, ( and )
        if s[i] == "*" or s[i] == "/" or s[i] == "ˆ" or \
            s[i] == "(" or s[i] == ")" or s[i] == "+" or s[i] == "-":
            tokens.append(s[i])
            i = i + 1
        # Handle a number without a leading + or -
        elif s[i] >= "0" and s[i] <= "9":
            num = ""
# Keep on adding characters to the token as long as they are digits
            while i < len(s) and s[i] >= "0" and s[i] <= "9":
                num = num + s[i]
                i = i + 1
            tokens.append(num)
# Any other character means the expression is not valid. Return an empty list to indicate
# that an error occurred.
        else:
            return []
    return tokens
# Read an expression from the user, tokenize it, and display the result
def main():
    exp = input("Enter a mathematical expression: ")
    tokens = tokenList(exp)
    print("The tokens are:", tokens)
# Call the main function only if this file has not been imported into another program
if __name__ == "__main__":
    main()