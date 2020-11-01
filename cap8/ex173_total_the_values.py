def recorse():
#read values from the user until a blank line is entered
    line = input("Enter values (blank to quit): ")

    if line == '':
        return 0.0
    else: 
        return float(line)+recorse()

#define the main function
def main():
#compute the total whit recors funtion
    total = recorse()
#display the total
    print("The total of all number is", total)

#call the main function
main()
