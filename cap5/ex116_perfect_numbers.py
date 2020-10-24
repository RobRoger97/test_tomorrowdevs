from ex115_list_of_proper_divisors import proper_divisors

mx = 10000

def perfect_num(n):
    div = proper_divisors(n)
    if sum(div)==n:
        result = True
    else:
        result = False
    
    return result

def main():
    print ("The perfect numbers between 1 and 10.000 are:")
    for i in range(1,mx+1,1):
        if perfect_num(i):
            print(" ",i)

# Call the main function
main()

