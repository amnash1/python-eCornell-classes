"""
Module for scoring blackjack hands.

In blackjack, face cards are worth 10, number cards are worth their value, and Aces
are worth either 1 or 11, whichever is more advantageous. The latter is what makes
scoring blackjack so tricky.

In this module, we assume that a card hand is represented by a tuple of strings, where
each string is two characters representing a card.  The first character is the rank of
the card: '2'-'9' for numerical cards, 'T' for 10, 'J' for Jack, 'Q' for Queen, 'K' for
King and 'A' for Ace.  The second character is the suit: 'H' for hearts, 'D' for diamonds,
'C' for clubs, and 'S' for spades.

For example ('KS','AD') is a blackjack hand with the King of Spades and Ace of Diamonds.

Author: Andy Nash
Date: 2022-12-01
"""
import introcs


def bjack(hand):
    """
    Returns the score of the blackjack hand.

    When scoring the hand, number cards are always worth their value and face cards
    (Jack, Queen, King) are always worth 10.  However, Aces are either worth 1 or 11,
    which ever is more advantageous.

    When determining how to value a hand, the score should be as high as possible without
    going over 21.  If the hand is worth more than 21 points, then all Aces should be
    worth 1 point.

    Examples:
        bjack(('KS','AD')) returns 21
        bjack(('KS','9C','AD')) returns 20
        bjack(('AS','AC','KH')) returns 12
        bjack(('AS','AC','KH','TD')) returns 22
        bjack(()) returns 0

    Parameter hand: the blackjack hand to score
    Precondition: hand is a (possibly empty) tuple of 2-character strings representing
    cards. The first character of each string is '2'-'9', 'T', 'J', 'Q', 'K', or 'A'.
    The second character of each string is 'H', 'D', 'C', or 'S'.
    """
    # Hint: Keep track of whether you have seen any aces in the hand that are worth 11
    # If so, subtract 10 from the accumulator if you go over.
    score = 0
    cards_scored = 0
    stop = False

    ###debugging
    #limit = 12
    while cards_scored < len(hand) and not stop:
    #   print('the row being looked at is '+str(row))
    #    if limit > 0:
    #        limit = limit - 1
    #    else:
    #        break

        card = hand[cards_scored]
        #print ('card being scored is '+str(card))
        if introcs.isnumeric(card[0]) == True:
            value = int(card[0])
        #    print ('this cards value is '+str(value))
            score = score + value
            cards_scored = cards_scored + 1
        #    print ('the current score is '+(str(score)))

        elif introcs.isnumeric(card[0]) == False and (card[0] != 'A'):
            value = 10
        #    print ('this cards value is '+str(value))
            score = score + value
            cards_scored = cards_scored + 1
        #    print ('the current score is '+(str(score)))

        elif introcs.isnumeric(card[0]) == False and (card[0] == 'A'):
            #print('the score so far is less than or equal 10')
            value = 11
        #    print ('this cards value is '+str(value))
            #if score + value > 21:
            #score = score -10
            score = score + value
            cards_scored = cards_scored + 1
                #print ('Ace scored as 1 '+(str(score)))
    #print('now the score is '+str(score))


    #if the tuple has Aces , count the aces and subtract 10 for each

    ace = ()
    ace_result = 0
    for card in hand:
        if score > 21 and card[0] == 'A':
            ace = ace + (card,)
            ace_result = len(ace)
    #print(ace_result)

    return score - (ace_result*10)




#bjack(('AS','AC','KH','TD'))
