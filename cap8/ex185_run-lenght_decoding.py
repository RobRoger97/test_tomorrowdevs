from ex184_flatten_a_list import flatten
#define a recursive function that decompresses a run-length encoded list.
def rl_dec(rl):
    if rl==[]:
        return []
    else:
        char = rl[0]
        n = rl[1]
        return [char]* n + flatten(rl_dec(rl[2:]))

#define main 
def main():
    lis = ['A', 12, 'B', 4, 'A', 6, 'B', 3]
    print("The list \n", \
          lis,"\n would be decompressed as: \n",\
          rl_dec(lis))
    
#call the main function
main()