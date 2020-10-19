from random import randrange
Num_Items = 100
# Generate the first number and display it
mx_value = randrange(1, Num_Items + 1)
print(mx_value)
# Count the number of times the maximum value is updated
num_updates = 0
# For each of the remaining numbers
for i in range(1, Num_Items):
# Generate a new random number
    current = randrange(1, Num_Items + 1)
# If the generated number is the largest one we have seen so far
    if current > mx_value:
# Update the maximum and count the update
        mx_value = current
        num_updates = num_updates + 1
    # Display the number, noting that an update occurred
        print(current, "<== Update")
    else:
# Display the number
        print(current)

# Display the other results
print("The maximum value found was", mx_value)
print("The maximum value was updated", num_updates, "times")