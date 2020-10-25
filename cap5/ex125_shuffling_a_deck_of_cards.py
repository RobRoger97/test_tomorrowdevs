from random import randrange

#It will use loops to create a complete deck of cards by storing the two-character abbreviations 
#for all 52 cards into a list. Return the list of cards as the function’s only result.
def createDeck():
    cards = []
# For each suit and each value
    for suit in ["s", "h", "d", "c"]:
        for value in ["2", "3", "4", "5", "6", "7", "8", "9", \
                        "T", "J", "Q", "K", "A"]:
# Construct the card and add it to the list
            cards.append(value + suit)
# Return the complete deck of cards
    return cards

def shuffle(cards):
# For each card
    for i in range(0, len(cards)):
# Pick a random index between the current index and the end of the list
        other_pos = randrange(i, len(cards))
# Swap the current card with the one at the random position
        temp = cards[i]
        cards[i] = cards[other_pos]
        cards[other_pos] = temp


# Display a deck of cards before and after it has been shuffled
def main():
    cards = createDeck()
    print("The original deck of cards is: ")
    print(cards)
    print()
    shuffle(cards)
    print("The shuffled deck of cards is: ")
    print(cards)
# Call the main function only if this file has not been imported into another program
if __name__ == "__main__":
    main()     