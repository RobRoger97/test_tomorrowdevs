from functools import lru_cache

@lru_cache(maxsize=1000)
#Euclid’s algorithm determine the greatest common divisor of two integers entered by the user.
def euclid_algorithm(a,b):   
    if b == 0:
        return a
    else:
        c = a%b
        return euclid_algorithm(b,c)

#define the main function
def main():
#read 2 integer from user
    a=int(input("Enter an integer: "))
    b=int(input("Enter an integer: "))
#greatest common divisor
    gcd = euclid_algorithm(a,b)
#display the result
    print("The greatest common divisor is",gcd)

#call the main function
main()