from ex129_tokenizing_a_string import tokenList
from ex130_unary_and_binary_operators import identifyUnary
from ex131_infix_to_postfix import algorithm

#Evaluating a postfix expression is easier than evaluating an infix expression because
#it does not contain any parentheses and there are no operator precedence rules to
#consider. A postfix expression can be evaluated using the following algorithm:
def newalgorithm(t):
    tokens = algorithm(t)
    values = []

    for t in tokens:
        if t.isdigit(): #if the token is a number
            y = int(t)
            values.append(y)
        elif t=='u-':
            x = values.pop(len(values)-1)
            z = not(x)
            values.append(z)
        elif t=='+' or t=='-' or t=='*' or t=='/' or t=='^':
            right = values.pop(len(values)-1) #Remove an item from the end of values and call it right
            print(right)
            left = values.pop(len(values)-1) #Remove an item from the end of values and call it left
            print(left)
            #Compute the result of applying the operator to left and right
            if t=='+':
                result = left+right
            elif t=='-':
                result = left-right
            elif t=='*':
                result = left*right
            elif t=='/':
                result = left/right
            elif t=='^':
                result = left**right
            values.append(result) #Append the result to values
    #Return the first item in values as the value of the expression
    return values[0]
#define the main function
def main():
    #read a mathematical expression in infix form from the user
    infix = input("Enter a mathematical expression in infix form: ")
    exp = tokenList(infix)
    print(newalgorithm(exp))

#call the main function
main()