from ex125_shuffling_a_deck_of_cards import *

#define the deal function
def deal(num,cards,deck):           #takes the number of hands, the number of cards per hand, 
                                    #and a deck of cards as its three parameters
    hands = [[]for n in range(num)] #Each hand will be represented as a list of cards.
    for card in range(cards):
        for hand in hands:
            hand.append(deck.pop(0))
#return a list containing all of the hands that were dealt
    return hands

#define the main function
def main():
    deck = createDeck()
    print("The original deck of cards is: \n",deck)
    print()
    shuffle(deck)
    print("The shuffled deck of cards is: \n",deck)
    print()
    print("Cards for each hand dealt:\n",deal(4, 5, deck))
    print()
    print("Cards remaining:\n",deck)

#call the main function
main()


