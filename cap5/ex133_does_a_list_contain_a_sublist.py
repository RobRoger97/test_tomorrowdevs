#A function that determines whether or not one list is a sublist of another.
def isSublist(larger,smaller): #take two lists, larger and smaller, as its only parameters.
    if len(smaller)<=len(larger):
        for j in range(0,len(larger),1):
            c=larger[j:len(smaller)+j]
            if smaller==c:
                return True #It should return True if and only if smaller is a sublist of larger.
        if smaller!=c:
            return False   
    else:
        return False

#main program          
def main():
    l=[1,2,3,4,5,6,7]
    s=[3,4,5]
    print("Is",s,"a sublist of",l,"?",isSublist(l,s))
    l=[1,2,3,4,5,6,7]
    s=[8]
    print("Is",s,"a sublist of",l,"?",isSublist(l,s))
    l=[1,2,3,4,5,6,7]
    s=[]
    print("Is",s,"a sublist of",l,"?",isSublist(l,s))
    l=[1,2,3,4,5,6,7]
    s=[1,2,3,4,5,6,7]
    print("Is",s,"a sublist of",l,"?",isSublist(l,s))
    l=[1,2,3,4,5,6,7]
    s=[1,3,5]
    print("Is",s,"a sublist of",l,"?",isSublist(l,s))

#call the main program
main()