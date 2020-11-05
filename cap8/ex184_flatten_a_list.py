#define a flatten list 
def flatten(data):
# If data is empty then there is no work to do
    if data == []:
        return []
# If the first element in data is a list
    if type(data[0]) == list:
# Flatten the first element and flatten the remaining elements in the list
        return flatten(data[0]) + flatten(data[1:])
    else:
# The first element in data is not a list so only the remaining elements in the list need
# to be flattened
        return [data[0]] + flatten(data[1:])

# Demonstrate the flatten function
def main():
    print(flatten([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))
    print(flatten([1, [2, [3, [4, [5, [6, [7, [8, [9, \
                  [10]]]]]]]]]]))
    print(flatten([[[[[[[[[[1], 2], 3], 4], 5], 6], 7], 8], 9], \
                  10]))
    print(flatten([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(flatten([]))


if __name__ == "__main__":
    main()