def characterCounts(s):
    counts = {}

    for ch in s:
        if ch in counts:
            counts[ch] = counts[ch] + 1
        else: 
            counts[ch] = 1

    return counts

def main():
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")

    counts1 = characterCounts(s1)
    counts2 = characterCounts(s2)

    if counts1 == counts2:
        print("Those strings are anagrams.")
    else:
        print("Those strings are not anagrams.")

# Call the main function
main()