
#Read a integer from the user
integ = int(input("Enter a integer: "))

# Start with an empty list
lis=[]

#While loop
while integ!=0:
    lis+=[integ]
    print(lis)
    integ = int(input("Enter a integer: "))

#Sort the value of the list
lis.sort()  

#Display the values in ascending order
print("The values, sorted into ascending order, are:")
for integ in lis:
    print(integ)