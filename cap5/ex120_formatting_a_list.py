def format_list(s):
    if len(s)==0:
        return "empty"
    elif len(s)==1:
        return str(s[0])
    
    else:
        result = ""
        for i in range(0, len(s)-2):
            result+= str(s[i])+","

        result+= str(s[len(s)-2])+ " and "
        result+= str(s[len(s)-1]) 
    
    return result

# Read several items entered by the user and display them with nice formatting
def main():
    lis = []
# Read items from the user until a blank line is entered
    l = input("Enter an item (blank to quit): ")
    while l != "":
        lis+=[l]
        l = input("Enter an item (blank to quit): ")

# Format and display the items
    print("The items are %s" %format_list(lis))

# Call the main function
main() 