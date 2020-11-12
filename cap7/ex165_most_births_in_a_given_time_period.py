# Define the function that inserts the sum of the values ​​of the names into the dictionaries
def LoadAndAdd(filename, names):
    inf = open(filename, "r")
    for line in inf:
        parts=line.split()
        name = parts[0]
        value = int(parts[1])
        if name not in names:
            names[name]=value
        else:
            names[name]+=value
    inf.close()
    
# Define the main function
def main():
    #Have the user supply the first and last years of the range to analyze.
    first_year = int(input("Enter the first year: "))
    last_year = int(input("Enter the last year: "))
    print('-'*30)
    girls = {}
    boys = {}
# Process each year in the range of the user
    for year in range(first_year, last_year + 1):
        girl_filename = "C:/Users/Roberta/Desktop/Python/BabyNames/" + str(year) + "_GirlsNames.txt"
        boy_filename = "C:/Users/Roberta/Desktop/Python/BabyNames/" + str(year) + "_BoysNames.txt"
        LoadAndAdd(girl_filename, girls)
        LoadAndAdd(boy_filename, boys)
# Get the maximum values ​​of the dictionary
    max_value_f = max(girls.values())
    max_value_m = max(boys.values())
# Display the result for Girls and Boys
    for key,values in girls.items():
        if values == max_value_f:
            print("Girls’ name that reached #1:")
            print(" - ",key)
            print('-'*30)
#-----------------------------------------
    for key,values in boys.items():
        if values == max_value_m:
            print("Boys’ name that reached #1: ")
            print(" - ",key)
# Call the main function
main()