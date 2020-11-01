#Dictionary of the NATO phonetic alphabet
phonetic_alphabet = {'A':'Alpha','B':'Bravo','C':'Charlie','D':'Delta','E':'Echo',\
    'F':'Foxtrot','G':'Golf','H':'Hotel','I':'India','J':'Juliet','K':'Kilo','L':'Lima',\
    'M':'Mike','N':'November','O':'Oscar','P':'Papa','Q':'Quebec','R':'Romeo','S':'Sierra',\
    'T':'Tango','U':'Uniform','V':'Victor','W':'Whiskey','X':'Xray','Y':'Yankee','Z':'Zulu'}

#recursive function
def word_in_phonetic(word,ind):
    if ind == len(word):
        return "Enter a word"
    if word[ind] in phonetic_alphabet:
        print(phonetic_alphabet[word[ind]], end=' ')
        return word_in_phonetic(word,ind+1)

#read a word from the user
txt = (input("Enter a word: ")).upper()
word_in_phonetic(txt,0)
