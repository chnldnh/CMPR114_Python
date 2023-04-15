
# m7homework7b-SetsDictionaries_1
# Blackjack Simulation

import random

def main():
  
    #create a deck of cards
    deck = create_deck()
   
    deal_cards(deck)
      
def create_deck():
    deck = {'Ace of Spades':1,  '2 of Spades':2, '3 of Spades':3,
                '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
               '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
               '10 of Spades':10, 'Jack of Spades':10,
               'Queen of Spades':10, 'King of Spades':10,
               
               'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
               '4 of Hearts':4, '5 of hearts':5, '6 of Hearts':6,
               '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
               '10 of Hearts':10, 'Jack of Hearts':10,
               'Queen of Hearts':10, 'King of Hearts':10,
               
               'Ace of Clubs':1,  '2 of Clubs':2, '3 of Clubs':3,
                '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
               '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
               '10 of Clubs':10, 'Jack of Clubs':10,
               'Queen of Clubs':10, 'King of Clubs':10,
               
               'Ace of Diamonds':1,  '2 of Diamonds':2, '3 of Diamonds':3,
                '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
               '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
               '10 of Diamonds':10, 'Jack of Diamonds':10,
               'Queen of Diamonds':10, 'King of Diamonds':10,}

    return deck

def deal_cards(deck):
    hand_value = 0 # accumulator
    hand_value2 = 0 # accumulator
    hand_score = 0
    hand_score2 = 0
    value = 0
    value2 = 0
   
    for count in range(len(deck)//2): # deal the card and accumulate their values
        card = random.choice(list(deck.keys())) # get a randomly selected key from diction
        value += deck[card]
        print('card - ' + card)
       
        if card.startswith('Ace ') and (11 + hand_value) < 21:
            value = 11
        else:
            value = 1      
            
        hand_value = hand_value + value       
       
        card2 = random.choice(list(deck.keys()))       
        value2 += deck[card2]
        print('card2 - ' + card2)
        if card2.startswith('Ace') and (11 + hand_value2) < 21:     
            value2 = 11
        else:
            value2 = 1   

        hand_value2 = hand_value2 + value2

        print()
        hand_value, hand_value2 = total(hand_value, hand_value2)
        print('Player1: ', hand_value)  
        print('Player2: ', hand_value2)  
        if hand_value > 21 and hand_value2 > 21:
            print('No one wins')
            hand_value = 0
            hand_value2 = 0
        elif hand_value > 21 and hand_value2 <= 21:
            print('Player 2 wins')
            hand_score2 += 1
            hand_value = 0
            hand_value2 = 0
        elif hand_value2 > 21 and hand_value <= 21:
            print('Player 1 wins')
            hand_score += 1
            hand_value = 0
            hand_value2 = 0
        else:
            'Round Continues.'
    
    print('Player 1:',hand_score)
    print('Player 2:',hand_score2)
    if hand_score > hand_score2:
        print('Player 1 wins!')
    elif hand_score2 > hand_score:
        print('Player 2 wins!')
    else:
        print('It is a TIE!')

def total(hand_value, hand_value2):
    total1 = 0
    total2 = 0
    total1 += hand_value
    total2 += hand_value2

    return total1, total2

main()

