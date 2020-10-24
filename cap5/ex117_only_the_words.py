import re

def words_function(s):
    t = re.split('[:;!?.:,-_ ]',s)
    for i in range(0,len(t)-2):
        if t[i]=='':
            del t[i]
    if t[len(t)-1]=='':
        del t[len(t)-1]
    return t

def main():
    string = input("Enter a string: ")
    print(words_function(string))

# Call the main function if the file has not been imported
if __name__ == "__main__":
    main()