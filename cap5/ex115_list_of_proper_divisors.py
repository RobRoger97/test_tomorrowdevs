#Define a function that finds porper divisors of an integer
def proper_divisors(n):
    lis =[]
    for i in range (1,n,1):
        if n%i==0:
            lis+=[i]
    return lis

#Define the main function
def main():
#Read an integer from the user
    num = int(input("Enter an integer: "))

#Display the result
    print("Proper divisors of",num,\
        "are:", proper_divisors(num))

# Call the main function if the file has not been imported
if __name__ == "__main__":
    main()
