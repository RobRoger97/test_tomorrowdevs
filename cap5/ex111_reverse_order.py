#read integer from the user
n = int(input("Enter a integer: "))
lis = []
#store them in a list
while n!=0:
    lis+=[n]
    n = int(input("Enter a integer: "))

for i in range(len(lis)-1,0-1,-1):
    print(lis[i])

