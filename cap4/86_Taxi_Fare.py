

def distance(d):
    base_fare = 4.00
    every_140 = 0.25
    if d<140:
        cost=d*base_fare
    else:
        q=d//140
        cost=d*base_fare+q*every_140
    return cost

def main():
#Read the distance from the user
    dis = int(input("Enter the distance in Km: "))

#Display the result
    print("The",dis,"Km fare is: $",distance(dis))

# Call the main function
main()