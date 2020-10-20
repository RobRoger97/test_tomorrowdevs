import random

sm=0

# Display the table
for i in range(0,10):
    n=0
    q=0
    w=0
    while q!=3 and w!=3:
        coin = random.randint(0,1)
        tot=""
        if coin==1:
             print("H ", end="")
             q+=1
             w=0
        else:
            print("T ", end="")
            w+=1
            q=0
        n+=1
    print("(",n,"flips)")
    sm=sm+n

#Average
m=sm/10

#Display the result
print("On average,",m, " flips were needed.")

    