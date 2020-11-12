import re
elements_file = "C:/Users/Roberta/Desktop/Python/elements.txt"
# Read and input from the user.
input_user = input("Enter a name, symbol or number of protons of the element: ")

while input_user!='':
    # Open the file for reading
    inf = open(elements_file,'r')
    # Empty dict and list
    element_dic = {}
    lis=[]
    for line in inf:
        line = line.replace("\n", "")
        lis = re.split(',',line.lower())
        element_dic[int(lis[0])]=lis[1:len(lis)]
    # Close the file
    inf.close()
    try:
        integer_value = int(input_user) # Consider the value as an integer
        if integer_value in element_dic.keys():
            space = ' '
            elem = space.join(element_dic[integer_value]) # Creates a string with the elements of the list separated by a space
            print("That number of protons corresponds to", str(elem).capitalize())
        else: # Display an appropriate error message if no element exists for the number of protons entered.
            print("There isn't no element with %d proton number(s)" %(integer_value))
    except ValueError: # If the user enters a non-integer value
        for key,values in element_dic.items():
            if input_user in values:
                print("That symbol (or name) corresponds to %d proton number(s)"%(key))
        # Display an appropriate error message if no element exists for the name or symbol entered.        
        if input_user not in element_dic.values():              # These lines of code are problematic
                print("ERROR: this element doesn't exist.")
                print("Please, try again...")
                
    # Continue to read input from the user until a blank line is entered.
    input_user = input("Enter a name, symbol or number of protons of the element (blank line to quit): ")