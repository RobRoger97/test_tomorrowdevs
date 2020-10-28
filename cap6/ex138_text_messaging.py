#read a message from the user
mess = input("Enter a message: ")
#the program handles both uppercase and lowercase letters.
n = mess.upper()
m = list(n)

#empty list
string = []
#dictionary 
dic = {1 : ['.',',','?','!',':'], 2 : ['A','B','C'], 3 : ['D','E','F'], 4 : ['G','H','I'], 5 : ['J','K','L'], \
              6 : ['M','N','O'], 7 : ['P','Q','R','S'], 8 :  ['T','U','V'], 9 : ['W','X','Y','Z'], 0 : [' ']}

for i in m:
    for d in dic:
        v = dic[d]
        for k in range(0, len(v)):
            if i == v[k]:
                string+=[str(d)]*(k+1)
                break       

s = ''
result = s.join(string)
#display the presses needed for the user’s message
print(result)


