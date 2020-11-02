#Roman numerals are constructed from the letters M, D, C, L, X, V and I which
#represent 1000, 500, 100, 50, 10, 5 and 1 respectively.
roman_numerals = {'M':1000,'D':500,'C':100,'L':50,'X':10,'I':1}

#define a recursive function that converts a Roman numeral to an integer.
def rom_num(word,ind):
    if ind == len(word):
        return 0
    if word[ind] in roman_numerals:#Your function should process one or two characters at the beginning of the string, 
                                    #and then call itself recursively on all of the unprocessed characters.
        if ind+1<len(word):
            if roman_numerals[word[ind]]<roman_numerals[word[ind+1]]:
                result = roman_numerals[word[ind+1]]-roman_numerals[word[ind]]
                s=result
                return s+int(rom_num(word,ind+2))
        
        s=(roman_numerals[word[ind]])
        return s+int(rom_num(word,ind+1))

#read a Roman numeral from the user   
num = input("Enter a roman number: ").upper()
#displays its value
print(rom_num(num,0))
