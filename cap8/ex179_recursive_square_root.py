#define a recursive square root function
def recursive_sr(n,guess=1.0):
    if abs((guess**2)-n)<(10**(-12)):#The base case occurs when guess2 is within 10^(−12) of n.
        return guess
    else:
        return recursive_sr(n,(guess+(n/guess))/2)
#define the main function
def main():
    #Read a number, x, entered by the user
    x = int(input("Entered a number: "))
    print("Approximation:",recursive_sr(x))

#call the main function
main()