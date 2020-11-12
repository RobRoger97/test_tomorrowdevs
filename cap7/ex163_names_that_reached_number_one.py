def LoadAndAdd(filename, names):
# Open the file, read the first line, and extract the name
    inf = open(filename, "r")
    line = inf.readline()
    inf.close()
    parts = line.split()
    name = parts[0]
# Add the name to the list if it is not already present
    if name not in names:
        names.append(name)
    
# Display the girls’ and boys’ names that reached #1 in at least one year between 1900 and 2012
def main():
# Create two lists to store the most popular names
    girls = []
    boys = []
# Process each year in the range, reading the first line out of the girl file and the boy file
    for year in range(1900, 2012 + 1):
        girl_filename = "C:/Users/Roberta/Desktop/Python/BabyNames/" + str(year) + "_GirlsNames.txt"
        boy_filename = "C:/Users/Roberta/Desktop/Python/BabyNames/" + str(year) + "_BoysNames.txt"
        LoadAndAdd(girl_filename, girls)
        LoadAndAdd(boy_filename, boys)
    # Display the lists
    print("Girls’ names that reached #1:")
    for name in girls:
        print(" ", name)
    print()
#-----------------------------------------
    print("Boys’ names that reached #1: ")
    for name in boys:
        print(" ", name)
# Call the main function
main()