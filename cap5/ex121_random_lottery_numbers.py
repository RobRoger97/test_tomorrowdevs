from random import randrange

mn = 1
mx = 49
n_nms =6

# Use a list to store the numbers on the ticket
ticket = []

for i in range(n_nms):
    # Generate a number that isn’t already on the ticket
    rand = randrange(mn, mx + 1)
    while rand in ticket:
        rand = randrange(mn, mx + 1)
    
    ticket+=[rand]

# Sort the numbers into ascending order and display them
ticket.sort()
print("Your numbers are: ", end="")
for n in ticket:
    print(n, end=" ")