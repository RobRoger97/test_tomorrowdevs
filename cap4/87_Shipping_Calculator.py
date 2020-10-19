def order(n):
    first_rate = 10.95
    next_rate = 2.95
    if n>1:
        cost=first_rate+(n-1)*next_rate
    else:
        cost=first_rate
    return cost

def main():
#Read the number of items purchased from the user
    num = int(input("Enter the number of items: "))

#Display the result
    print("The shipping charge for",num,"orders is: $",order(num))
    
# Call the main function
main()