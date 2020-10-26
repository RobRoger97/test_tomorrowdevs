#Write a function that determines whether or not a list of values is in sorted order
#(either ascending or descending).
def sorted_order(lis):
    if lis==sorted(lis) or lis==sorted(lis,reverse=1):
        return True #The function should return True if the list is already sorted.
    elif lis==[]:
        return True
    else:
        return False #Otherwise it should return False.

#main program
def main():
#read a list of numbers from the user
    num = input("Enter a number (blank to quit): ")
    l=[]
    while num!='':
        n = int(num)
        l+=[n]
        num = input("Enter a number (blank to quit): ")

#use the function to report whether or not the list is sorted.
    if sorted_order(l):
        print("That list of values is in sorted order!")
    else:
        print("That list of values is NOT in sorted order!")    

#call the main program
main()