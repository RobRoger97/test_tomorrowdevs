def isInteger(s):
# Remove whitespace from the beginning and end of the string
    s = s.strip()
# Determine if the remaining characters form a valid integer
    if (s[0] == "+" or s[0] == "-") and s[1:].isdigit():
        return True
    if s.isdigit():
        return True
    return False

# Demonstrate the isInteger function
def main():
    s = input("Enter a string: ")
    if isInteger(s):
        print("That string represents an integer.")
    else:
        print("That string does not represent an integer.")

# Only call the main function when this file has not been imported
if __name__ == "__main__":
    main()