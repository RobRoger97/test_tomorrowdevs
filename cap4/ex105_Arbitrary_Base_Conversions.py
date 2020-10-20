from ex_104_Hexadecimal_and_Decimal_Digits import*

def dec2n(num, new_base):
# Generate the representation of num in base new base, storing it in result
    result = ""
    q = num

# Perform the body of the loop once
    r = q % new_base
    result = int2hex(r) + result
    q = q // new_base

# Continue looping until q is 0
    while q > 0:
        r = q % new_base
        result = int2hex(r) + result
        q = q // new_base
# Return the result
    return result

def n2dec(num, b):
    decimal = 0
    # Process each digit in the base b number
    for i in range(len(num)):
        decimal = decimal * b
        decimal+= hex2int(num[i])
# Return the result
    return decimal
# Convert a number between two arbitrary bases
def main():
# Read the base and number from the user
    from_base = int(input("Base to convert from (2-16): "))
    if from_base < 2 or from_base > 16:
        print("Only bases between 2 and 16 are supported.")
        print("Quitting...")
        quit()
    from_num = input("Sequence of digits in that base: ")
# Convert to base 10 and display the result
    dec = n2dec(from_num, from_base)
    print("That’s %d in base 10." % dec)
# Convert to the new base and display the result
    to_base = int(input("Enter the base to convert to (2-16): "))
    if to_base < 2 or to_base > 16:
        print("Only bases between 2 and 16 are supported.")
        print("Quitting...")
        quit()
    to_num = dec2n(dec, to_base)
    print("That’s %s in base %d." % (to_num, to_base))

# Call the main function if the file has not been imported
if __name__ == "__main__":
    main()

