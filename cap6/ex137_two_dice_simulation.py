from random import randrange

num_runs = 1000 #simulate 1,000 rolls of two dice
d_max = 6

#define a function that simulates rolling a pair of six-sided dice
def twoDice():
    d1 = randrange(1,d_max+1)
    d2 = randrange(1,d_max+1)
#return the total that was rolled on two dice as its only result
    return d1+d2

#main program that uses your function to simulate rolling two 
#six-sided dice 1,000 times.
def main():
    # Create a dictionary of expected proportions
    expected = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, \
                7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, \
                11: 2/36, 12: 1/36}

    # Create a dictionary that maps from the total of two dice to the number of occurrences
    counts = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, \
              8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

    # Simulate num runs rolls, and count each roll
    for i in range(num_runs):
        t = twoDice()
        counts[t] = counts[t] + 1

    # Display the simulated proportions and the expected proportions
    print("Total    Simulated   Expected")
    print("           Percent    Percent")
    for i in sorted(counts.keys()):
        print("%5d %11.2f %8.2f" % \
        (i, counts[i] / num_runs * 100, expected[i] * 100))

# Call the main function
main()