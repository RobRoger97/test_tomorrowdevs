def isPalindrome(s):
    if len(s)<=1:
        return True
    return s[0]==s[len(s)-1] and isPalindrome(s[1:len(s)-1])
#define main function
def main():
    line = input("Enter a string: ")

    if isPalindrome(line):
        print("That was a palindrome!")
    else:
        print("That is not a palindrome.")
#call the main function
main()