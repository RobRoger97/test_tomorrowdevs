lis = []
down = []
up = []
equal = []
count=0

#Read number from the user until a black line is entered
num = input("Enter numbers unti a black line: ")

while num!="":
    n = int(num)
    lis+=[n]
    count+=1
    num = input("Enter numbers unti a black line: ")

m =sum(lis)/count

for n in lis:
    if n<m:
        down.append(n)
    elif n==m:
        equal.append(n)
    else:
        up.append(n)

print("The average values is:", m)

print("All of the below average values:", end="")
print(down)
print("All of the average values:", end="")
print(equal)
print("All of the above average values:", end="")
print(up)