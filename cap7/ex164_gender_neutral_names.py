def LoadAndAdd(filename, names):
# Open the file, read the first line, and extract the name
    inf = open(filename, "r")
    for line in inf:
    
     parts = line.split()
     name = parts[0]
# Add the name to the list if it is not already present
     if name not in names:
        names.append(name)
    inf.close()
    
# Def the main function
def main():
  year = input("Enter the year: ")
  try:
# Create two lists to store the most popular names
    girls = []
    boys = []
# Process the year entered from the uter, reading all names of boys and girls...

    girl_filename = "C:/Users/Roberta/Desktop/Python/BabyNames/" + year + "_GirlsNames.txt"
    boy_filename = "C:/Users/Roberta/Desktop/Python/BabyNames/" + year + "_BoysNames.txt"
    LoadAndAdd(girl_filename, girls) #... and add them in lists
    LoadAndAdd(boy_filename, boys)
    lis_neutral =[]
    for n in girls: # determines all of the baby names that were used for both boys and girls in a year specified by the user...
        if n in boys and n not in lis_neutral:
            lis_neutral.append(n)
    #... and display the result
    if lis_neutral==[]:
        print("In that year there were no neutral names.")
    else:
        str_lis = " , ".join(lis_neutral)
        print("The neutral name(s) in that year is(are):",str_lis)
  # Display an appropriate error message if you do not have data for the year requested by the user.  
  except FileNotFoundError:
      print("There aren't data for the year requested!")
# Call the main
main()