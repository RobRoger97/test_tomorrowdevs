def remove_list(lis,n):
    new_copy = sorted(lis)
#Remove n smallest and n largest values
    for i in range(n):
        new_copy.pop(0)
        new_copy.pop()

#Return the result
    return new_copy

#Define the main function
def main():
#Read values from the user until a blank line is entered
    v = input("Enter a value (blank line to quit): ")
    values = []

    while v != "":
        num = float(v)
        values+=[num]
        v = input("Enter a value (blank line to quit): ")

#Display the result or an appropriate error message
    if len(values)<4:
        print("You didn't enter enough values.")
    else:
        print("Removing the outliers from the original list:", values, \
            ",  we have obtained:",remove_list(values,2))
#Call the main function
main()