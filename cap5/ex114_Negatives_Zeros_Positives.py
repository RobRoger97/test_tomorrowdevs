#Read integer from the user until the user enters a blank line
num=input("Enter a word (blank line to quit): ")

# Start with empty lists 
neg = []
z = []
pos = []

while num!="":
    n = int(num)
    if n<0:
        neg.append(n)
    elif n==0:
        z.append(n)
    else:
        pos.append(n)


    num=input("Enter a word (blank line to quit): ")

#Once all of the integers have been read your program should display all of the negative numbers, 
#followed by all of the zeros, followed by all of the positive numbers.Within each group the numbers 
# should be displayed in the same order that they were entered by the user.
for n in neg:
    print(n)
for n in z:
    print(n)
for n in pos:
    print(n)