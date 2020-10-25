#import nltk module
import nltk

#Read a line of text from the user
line = input("Enter a line of text: ")
text = nltk.word_tokenize(line)
z=0

#For lood
for k in text:
    x=0
    if k!=('!' or '.' or ',' or '?' or ':' or ';' or '-' or '_' or ' '):
        a = [] 
        lis = list(k)
        #case where the first letter is a vowel
        if k[0]=='a' or k[0]=='e' or k[0]=='i'\
            or k[0]=='o' or k[0]=='u' or k[0]=='A'\
            or k[0]=='E' or k[0]=='I' or k[0]=='O' or k[0]=='U':
            lis+=['way']
            space = ''
            result = space.join(lis)
            text[z]=result
        else: #case where the first letter is a consonant
            for j in range(0,len(lis)-1):  
                a+= lis[j]
                #case where the first letter is capitalized
                if j==0 and ord(a[0])>=66 and ord(a[0])<=90 and ord(a[0])!=(69 or 73 or 79 or 85):
                    a[0] = chr(ord(a[0])+32)
                    if lis[j+1]=='a' or lis[j+1]=='e' or lis[j+1]=='i'\
                        or lis[j+1]=='o' or lis[j+1]=='u':
                        c = lis[j+1:] + a + ['ay']
                        c[0]=chr(ord(c[0])-32)
                        space = ''
                        result = space.join(c)
                        text[z]=result
                        break
                else:#case where the first letter is lowercase
                    if k[j+1]=='a' or k[j+1]=='e' or k[j+1]=='i'\
                        or k[j+1]=='o' or k[j+1]=='u':
                        c = lis[j+1:] + a + ['ay']
                        space = ''
                        result = space.join(c)
                        text[z] = result
                        break
            x+=1        
    z+=1
#Display the result with join
space=' '
print(space.join(text))