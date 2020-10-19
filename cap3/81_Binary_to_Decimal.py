#Read the binary number from the user as a string
b_num = input("Enter a binary number: ")

lenght = len(b_num)-1
count = 0
i=0

#Then it should compute the equivalent decimal number by processing each digit in the binary number. 
#Finally, your program should display the equivalent decimal number with an appropriate message.
while lenght>=0:
    count = count+int(b_num[lenght])*(2**i)
    lenght-=1
    i+=1

#Decimal number
d_num=count

#Display the result
print(b_num,"corresponds to ",d_num)
