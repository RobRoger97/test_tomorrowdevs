from ex129_tokenizing_a_string import tokenList
from ex130_unary_and_binary_operators import identifyUnary
#from cap4.ex96_Does_a_String_Represent_an_Integer import isInteger
def isInteger(s):
# Remove whitespace from the beginning and end of the string
    s = s.strip()
# Determine if the remaining characters form a valid integer
    if (s[0] == "+" or s[0] == "-") and s[1:].isdigit():
        return True
    if s.isdigit():
        return True
    return False
#from cap4.ex97_Operator_Precedence import precedence
def precedence(x):
    if x=='-' or x =='+':
        res = 1
    elif x=='*' or x=='/':
        res = 2
    elif x=='u+' or x=='u-':
        res=3
    elif x=='ˆ':
        res=4
    else:
        res=-1
        print('What you entered is not an operator')
    return res
#One can convert an infix expression to postfix form using the following algorithm:
def algorithm(tokens):
    marked = identifyUnary(tokens)
    operators =[]
    postfix = []

    for t in marked:
        if isInteger(t):
            postfix.append(t)
        elif t=='+' or t=='-' or t=='*' or t=='/' or t=='^' or t=='u-' or t=='u+':
            while operators!=[] and operators[len(operators)-1]!='(' \
              and precedence(t)<precedence(operators[len(operators)-1]):
                x = operators.pop(len(operators)-1)
                postfix.append(x)
            operators.append(t)
        elif t=='(':
            operators.append(t)
        elif t==')':
            while operators[len(operators)-1]!='(':
                x = operators.pop(len(operators)-1)
                postfix.append(x)
            operators.remove('(')

    while operators!=[]:
        x = operators.pop(len(operators)-1)
        postfix.append(x)

    return postfix
#main function          
def main():
    exp = input("Enter a mathematical expression: ")
    tokens = tokenList(exp) 
    print(algorithm(tokens))
#call the main function
main()