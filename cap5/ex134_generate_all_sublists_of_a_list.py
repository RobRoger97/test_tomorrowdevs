def allSublists(data):
# Start out with the empty list as the only sublist of data
    sublists = [[]]
# Generate all of the sublists of data from length 1 to len(data)
    for length in range(1, len(data) + 1):
# Generate the sublists starting at each index
        for i in range(0, len(data) - length + 1):
# Add the current sublist to the list of sublists
            sublists.append(data[i : i + length])
# Return the result
    return sublists
# Demonstrate the allSublists function
def main():
    print("The sublists of [] are: ")
    print(allSublists([]))
    print("The sublists of [1] are: ")
    print(allSublists([1]))
    print("The sublists of [1, 2] are: ")
    print(allSublists([1, 2]))
    print("The sublists of [1, 2, 3] are: ")
    print(allSublists([1, 2, 3]))
    print("The sublists of [1, 2, 3, 4] are: ")
    print(allSublists([1, 2, 3, 4]))
# Call the main function
main()