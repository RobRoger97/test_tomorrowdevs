Width = 80

def center(s, width):
# If the string is too long to center, then the original string is returned
    if width < len(s):
        return s
# Compute the number of spaces needed and generate the result
    spaces = (width - len(s)) // 2
    result = " " * spaces + s
    return result
# Demonstrate the center function
def main():
    print(center("A Famous Story", Width))
    print(center("by:", Width))
    print(center("Someone Famous", Width))
    print()
    print("Once upon a time...")
# Call the main function
main()