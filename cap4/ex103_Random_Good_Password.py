#Using your solutions to Exercises 100 and 102
from ex100_Random_Password import random_Pass
from ex102_Check_a_Password import goodpass

#Define main function
def main():
    b = False
    a = ''
    x = 0
    while b == False:
        a = random_Pass()
        b = goodpass(a)
        x+=1
        print(a,b)
#Display the result
    print('Find a good pass has taken',x,'tries')

# Call the main function if the file has not been imported
if __name__ == "__main__":
    main()
