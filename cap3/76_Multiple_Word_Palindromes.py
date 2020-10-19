#Read a string from user
line=input("Enter a string: ")

#Data
lenght=len(line)
start=0
end=lenght-1
palindrome=True
i=0

#While loop to scroll through the string
while(end-i>=1):
#If the character of the string is not a letter of the alphabet, ignore it and move on.
    if (line[i]).isalpha()==False:
        i+=1
#If the character of the string is not a letter of the alphabet, ignore it and move on.
    if (line[end]).isalpha()==False: 
        end-=1
    print(line[i],"vs",line[end]) #TEST
    if line[i]!=line[end]:
        palindrome=False
    end-=1
    i+=1

#Display a meaningful output message
if palindrome:
    print("La parola è palindroma.")
else:
    print("La parola non è palindroma")