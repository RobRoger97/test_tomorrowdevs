#defin precedence function
def precedence(x):
    if x=='-' or x =='+':
        res = 1
    elif x=='*' or x=='/':
        res = 2
    elif x=='ˆ':
        res=3
    else:
        res=-1
        print('What you entered is not an operator')

    return res

def main():
    a = str(input('Enter a matematical operator:'))
    print(precedence(a))

if __name__ == "__main__":
        main()