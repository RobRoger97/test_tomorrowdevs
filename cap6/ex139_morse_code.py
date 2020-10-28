#dictionary of Morse Code
dic = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....',\
       'I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.',\
       'Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',\
       'Y':'-.--','Z':'--..','0':'----','1':'.----','2':'..---','3':'...--','4':'....-',\
       '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'}

#read a message from the user
mess = input("Enter a message: ").upper()
m = list(mess)

#empty list
string = []

for i in m:
    for d in dic:
        if i == d:
            string+=[dic[d]]

space = ' '
result = space.join(string)
#display the morse code
print("The Morse code of",mess,"is",result)