#define a recursive function that implements the run-length compression technique
def rl_enc(rl):
    if len(rl)==0:
        return[]
    index=1
    while index<len(rl) and rl[index] == rl[index-1]:
        index+=1
#encode the current character group
    lis = [rl[0],index]
# Use recursion to process the characters from index to the end of the string
    return lis + rl_enc(rl[index:len(rl)])

#define the main function
def main():
#read a string from the user
    string = input("Enter some characters: ")

    print("The run-lenght compressed list of: \n",string,"\n is: \n", rl_enc(string))

#Call the main function
main()