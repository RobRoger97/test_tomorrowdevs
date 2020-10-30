from random import randrange
NUMS_PER_LETTER = 15

def createCard():
    card = {}
# The range of integers that can be generated for the current letter
    lower = 1
    upper = 1 + NUMS_PER_LETTER
# For each of the five letters
    for letter in ["B", "I", "N", "G", "O"]:
# Start with an empty list for the letter
        card[letter] = []
# Keep generating random numbers until we have 5 unique ones
        while len(card[letter]) != 5:
            next_num = randrange(lower, upper)
# Ensure that we do not include any duplicate numbers
            if next_num not in card[letter]:
                card[letter].append(next_num)
# Update the range of values that will be generated for the next letter
        lower = lower + NUMS_PER_LETTER
        upper = upper + NUMS_PER_LETTER
# Return the card
    return card

def displayCard(card):
# Display the headings
    print("B I N G O")
# Display the numbers on the card
    for i in range(5):
        for letter in ["B", "I", "N", "G", "O"]:
            print("%2d " % card[letter][i], end="")
        print()
# Create a random Bingo card and display it
def main():
    card = createCard()
    displayCard(card)
# Call the main function only if this file has not been imported into another program
if __name__ == "__main__":
    main()