#Pi value
pi=3.0
op=1

#For loop
for i in range(2,2*15+1,2):
    pi=pi+4/(i*(i+1)*(i+2))*op
    op*=-1

#Display the result
print("15 approximations of π is:",pi)
