#Write a function named reverseLookup that finds all of the keys in a dictionary
#that map to a specific value.
def reverseLookup(data,value): #The function will take the dictionary and the value to
                               #search for as its only parameters.
    keys = []

    for key in data:
        if data[key] == value:
            keys.append(key)
    #It will return a (possibly empty) list of keys from
    #the dictionary that map to the provided value.    
    return keys

def main():
    #main program should create a dictionary 
    fr_to_en = {"le" : "the", "la" : "the", "livre" : "book", \
                "pomme" : "apple"}
    #show that the reverseLookup function works correctly  
    print("The french words for 'the' are: ", \
    reverseLookup(fr_to_en, "the"))
    print("Expected: ['le', 'la']")#when it returns multiple keys,
    print()
    print("The french word for 'book' is: ", \
    reverseLookup(fr_to_en, "book"))
    print("Expected: ['livre']")#a single key,
    print()
    print("The french word for 'asdf' is: ", \
    reverseLookup(fr_to_en, "tvb"))
    print("Expected: []")#and no keys.

# Call the main function only if this file has not been imported into another program
if __name__ == "__main__":
    main()