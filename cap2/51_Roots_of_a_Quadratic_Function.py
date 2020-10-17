import math

#Read a, b and c from uter
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

#Compute discriminant
dis = b**2-4*a*c

#If the discriminant is negative then the quadratic equation does not have any real roots. If the discriminant is 0, 
# then the equation has one real root. Otherwise the equation has two real roots, and the expression must be evaluated 
# twice, once using a plus sign, and once using a minus sign, when computing the numerator.
if dis<0:
    print("The discriminant is negative then the quadratic equation does not have any real roots.")
elif dis==0:
    root = (-b)/(2*a)
    print("The discriminant is 0, then the equation has one real root: %.2f" %root)
else:
    sqr = math.sqrt(dis)
    root1 = (-b+sqr)/(2*a)
    root2 = (-b-sqr)/(2*a)
    print("The equation has two real roots: %.2f and %.2f" %(root1,root2))