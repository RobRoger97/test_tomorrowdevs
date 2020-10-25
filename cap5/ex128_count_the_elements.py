def countRange(data, mn, mx):
# Count the number of elements within the acceptable range
    count = 0
    for e in data:
# Check each element
        if mn <= e and e < mx:
            count = count + 1
# Return the result
    return count

# Demonstrate the countRange function
def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Test a case where some elements are within the range
    print("Counting the elements in [1..10] between 5 and 7...")
    print("Result: %d Expected: 2" % countRange(data, 5, 7))
# Test a case where all elements are within the range
    print("Counting the elements in [1..10] between -5 and 77...")
    print("Result: %d Expected: 10" % countRange(data, -5, 77))
# Test a case where no elements are within the range
    print("Counting the elements in [1..10] between 12 and 17...")
    print("Result: %d Expected: 0" % countRange(data, 12, 17))
# Test a case where the list is empty
    print("Counting the elements in [] between 0 and 100...")
    print("Result: %d Expected: 0" % countRange([], 0, 100))

# Test a case with duplicate values
    data = [1, 2, 3, 4, 1, 2, 3, 4]
    print("Counting the elements in", data, "between 2 and 4...")
    
    print("Result: %d Expected: 4" % countRange(data, 2, 4))
# Call the main program
main()