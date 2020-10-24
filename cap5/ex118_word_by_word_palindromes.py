import re

#Read a string from user
line=input("Enter a string: ")

lis = re.split('[:;!?.:,-_ ]',line)
for i in range(0,len(lis)-2):
    if lis[i]=='':
        del lis[i]
    if lis[len(lis)-1]=='':
        del lis[len(lis)-1]
        
#Data
lenght=len(lis)
start=0
is_palindrome = True
i = 0

#While loop to scroll through the list
while i < lenght / 2 and is_palindrome:

    if lis[i] != lis[lenght - i - 1]:
        is_palindrome = False
        
# Move to the next word
    i+=1


# Display a meaningful output message
if is_palindrome:
    print(line, "is a palindrome")
else:
    print(line, "is not a palindrome")