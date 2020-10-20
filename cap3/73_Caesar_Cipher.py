#Read a message and a shift value from the user
mess = (input('Enter your message:'))
shift = int(input('Enter the shift value:'))

#New message
new_mess = str('') 

#Check if shift value is valid, elif make it valid
if shift>26 or shift<-26: 
    shift= shift%26

#For loop
for x in mess:
    if 'a' <= x <= 'z' or 'A' <= x <= 'Z': #check if it's a letter of not
        x1 = (chr(ord(x)+shift))
        if 'a' <= x1 <= 'z' or 'A' <= x1 <= 'Z':  #check if the result is still a letter
            x1 = x1
        else: #if the result it's not a letter, make it a letter
            x1 = (chr(ord(x)-26+shift))
    else: #values that are not letters must stay the same
        x1 = x
    new_mess = new_mess + x1

# Display the shifted message
print("The shifted message is", new_mess)