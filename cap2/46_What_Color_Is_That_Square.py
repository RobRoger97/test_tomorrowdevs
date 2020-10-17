#Read the position from user
p = input("Enter the position on the chess: ")

#divide the position into letter and number
l=p[0]
n=int(p[1])

#Use an if statement to determine if the column begins with a black square or a white square.
if (l=="a" or l=="c" or \
    l=="e" or l=="g") and (n%2==1):
    print("The square is black!")
else:
    print("The square is white!")