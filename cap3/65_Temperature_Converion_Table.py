#Title of the tab
print("Equivalence Celsius-Fahrenheit")

#For loop to create a tab
for i in range(0,10+1,1):
    p = i*10
    d = (i*(9/5))+32
    print("           %5d       %5.2f" %(p,d))
