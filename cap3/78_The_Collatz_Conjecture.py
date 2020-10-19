#Read a integer number from user
num = int(input("Enter a number: "))
#Start with any positive integer as the only term in the sequence
print(num)

#While the last term in the sequence is not equal to 1 do
#If the last term is even then
#Add another term to the sequence by dividing the last term by 2 using floor division
#Else
#Add another term to the sequence by multiplying the last term by 3 and adding 1
while num!=1:
    if num%2==0:
        num=num/2
    else:
        num=(num*3)+1
    print(num)