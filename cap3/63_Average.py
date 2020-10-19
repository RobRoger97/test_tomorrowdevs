#Read a value from user
num = int(input("Enter a number: "))
sm=0.00
count=0

#Loop
if num==0:
    print("Error message: the first number can't be 0")
else:
    while num!=0:
        count=count+1
        sm = sm+num 
        num = int(input("Enter a number: "))
        
#Compute the average
average=sm/count

#Display the result
print("The average is:",average)