from ex98_Is_a_Number_Prime import isPrime

def nextPrime(x):
    a = False
    if x>0:
        while a == False:
            x = x + 1
            a = isPrime(x)

    return x

def main():
    n = int(input('Enter an int:'))
    print(nextPrime(n))

# Call the main function if the file has not been imported
if __name__ == "__main__":
    main()