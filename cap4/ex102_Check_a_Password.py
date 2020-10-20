#Define goodpass function
def goodpass(x):
    s = 0
    res = False
    if len(x)>=8:
        for a in x:
            if 'a' <= a <= 'z':
                s = 1
                for a in x:
                    if 'A' <= a <='Z':
                        s=2
                        for a in x:
                            if '0' <= a <= '9':
                                s=3
                            else:
                                s= s
                    else:
                        s = s
            else:
                s = s

    if s==3:
        res = True
    else:
        res = False

    return res

#define main function
def main():
#read the password from the user
    password = str(input('Enter a password:'))
#display the result
    print(goodpass(password))

# Call the main function if the file has not been imported
if __name__ == "__main__":
    main()