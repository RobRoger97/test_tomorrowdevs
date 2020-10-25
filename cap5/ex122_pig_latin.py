#Read a line of text from the user
line = input("Enter a line of text: ")

string = str(line)
lis = string.split()


for i in lis:
    a = []
    b = list(i)
    if i[0]=='a' or i[0]=='e' or i[0]=='i'\
        or i[0]=='o' or i[0]=='u':
        b+=['way']
        space = ''
        result = space.join(b)
        print(' ', result, end=' ')
    else:
       for j in range(0,len(b)-1): 
            a+= i[j]
            if i[j+1]=='a' or i[j+1]=='e' or i[j+1]=='i'\
                or i[j+1]=='o' or i[j+1]=='u':
                c = b[j+1:] + a + ['ay']
                space = ''
                result = space.join(c)
                print(' ', result, end=' ')
                break

