#Name and value
G_Wash = "George Washington"
T_Jeff = "Thomas Jefferson"
A_Lin  = "Abraham Lincoln"
A_Ham  = "Alexander Hamilton"
A_Jack = "Andrew Jackson"
U_Sg   = "Ulysses S. Grant"
B_Fran = "Benjamin Franklin"

#Read the denomination from user
d = int(input("Enter the denomination of a banknote: "))

#Check of name and denomination of banknote
if d==1:
    name = G_Wash
elif d==2:
    name = T_Jeff
elif d==5:
    name = A_Lin
elif d==10:
    name = A_Ham
elif d==20:
    name = A_Jack
elif d==50:
    name = U_Sg
elif d==100:
    name = B_Fran
else:
    name = ""

#Display result
if name == "":
    print("There is no denomination that corresponds to a bankonote.")
else:
    print("This denomination ",d," corresponds to ", name, " face.")