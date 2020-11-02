def editDistance (s,t):
    if len(s)==0:
        return len(t)
    elif len(t)==0:
        return len(s)
    else:
        cost = 0

        if s[len(s)-1]!=t[len(t)-1]:
            cost=1

        d1 = editDistance(s[0 : len(s) - 1], t) + 1
        d2 = editDistance(s, t[0 : len(t) - 1]) + 1
        d3 = editDistance(s[0 : len(s) - 1] , t[0 : len(t) - 1]) + cost
# Return the minimum distance
        return min(d1, d2, d3)

# Compute the edit distance between two strings entered by the user
def main():
# Read two strings from the user
    s1 = input("Enter a string: ")
    s2 = input("Enter another string: ")
# Compute and display the edit distance
    print("The edit distance between %s and %s is %d." % \
         (s1, s2, editDistance(s1, s2)))
# Call the main function
main()