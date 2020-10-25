#Read a collection of points from the user
line1 = input("Enter a x coordinate (blank to quit): ")
line2 = input("Enter a y coordinate (blank to quit): ")

#Empty lists
x_list = []
y_list = []
n=0
m1_list = []
m2_list = []
m2_list = []
m3_list = []
m4_list = []


while line1!='' or line2!='':
    n+=1
    x = float(line1)
    y = float(line2)
    x_list+= [x]
    y_list+= [y]

    line1 = input("Enter a x coordinate (blank to quit): ")
    line2 = input("Enter a y coordinate (blank to quit): ")

for i in range(0,n):
    m1_list.append(x_list[i]*y_list[i])
    m2_list.append(x_list[i])
    m3_list.append(y_list[i])
    m4_list.append((x_list[i])**2)

m = (sum(m1_list)-((sum(m2_list))*(sum(m3_list)))/n)/(sum(m4_list)-((sum(m2_list))**2)/n)

y_m = (sum(m3_list))/n
x_m = (sum(m2_list))/n

b = y_m - m*x_m

#display the result
print("y=%.2fx+%.2f" %(m,b))