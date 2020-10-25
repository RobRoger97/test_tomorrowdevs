from ex129_tokenizing_a_string import tokenList

def identifyUnary(tokens):
    retval = []
# Process each token in the list
    for i in range(len(tokens)):
# If the first token in the list is + or - then it is a unary operator
        if i == 0 and (tokens[i] == "+" or tokens[i] == "-"):
            retval.append("u" + tokens[i])
# If the token is a + or - and the previous token is an operator or an open parenthesis
# then it is a unary operator
        elif i > 0 and (tokens[i] == "+" or tokens[i] == "-") and \
            (tokens[i-1] == "+" or tokens[i-1] == "-" or
            tokens[i-1] == "*" or tokens[i-1] == "/" or
            tokens[i-1] == "("):
            retval.append("u" + tokens[i])
# Any other token is not a unary operator so it is appended to the result without modification
        else:
            retval.append(tokens[i])
# Return the new list of tokens where the unary operators have been marked
    return retval

# Demonstrate that unary operators are marked correctly
def main():
# Read an expression from the user, tokenize it, and display the result
    exp = input("Enter a mathematical expression: ")
    tokens = tokenList(exp)
    print("The tokens are:", tokens)
# Identify the unary operators in the list of tokens
    marked = identifyUnary(tokens)
    print("With unary operators marked: ", marked)

# Call the main function only if this file has not been imported into another program
if __name__ == "__main__":
    main()