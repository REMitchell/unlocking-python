###########################################################
# 
#    $$$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\  
#    $$  __$$\ $$  __$$\ $$ | $$  |$$  _____|$$  __$$\ 
#    $$ |  $$ |$$ /  $$ |$$ |$$  / $$ |      $$ |  $$ |
#    $$$$$$$  |$$ |  $$ |$$$$$  /  $$$$$\    $$$$$$$  |
#    $$  ____/ $$ |  $$ |$$  $$<   $$  __|   $$  __$$< 
#    $$ |      $$ |  $$ |$$ |\$$\  $$ |      $$ |  $$ |
#    $$ |       $$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ |
#    \__|       \______/ \__|  \__|\________|\__|  \__|#
#
# Hands are as follows (in order of winningness):
#   - Royal flush (All cards have the same suit, A, K, Q, J, 10)
#   - Straight flush
#   - four of a kind
#   - full house
#   - flush
#   - straight
#   - three of a kind
#   - two pairs
#   - pair
#   - high card
#
###########################################################

from random import shuffle 


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.index = Deck.values.index(self.value)

    def __str__(self):
        return f'{self.value}{self.suit}'
    
    def fromString(cardStr):
        return Card(cardStr[:-1], cardStr[-1])

class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♢', '♠', '♡', '♣']

    def __init__(self):
        self.cards = []
        for value in self.values:
            for suit in self.suits:
                self.cards.append(Card(value, suit))
        shuffle(self.cards)

    def deal(self, num=5):
        hand = Hand(self.cards[0:num])
        self.cards = self.cards[num:]
        return hand


class Hand:
    straightCombos = []
    for i in range(9):
        combo = Deck.values[i:i+5]
        combo = ''.join(combo)
        straightCombos.append(combo)
    straightCombos.append('A2345')

    def __init__(self, cards):
        self.cards = cards

        self.counts = self.getCounts()

    def __str__(self):
        return ', '.join([str(card) for card in self.cards])

    def fromString(handString):
        handArr = handString.split(', ')
        return Hand([Card.fromString(cardStr) for cardStr in handArr])

    def getCounts(self):
        counts = {}
        for card in self.cards:
            if card.index not in counts:
                counts[card.index] = 0
            counts[card.index] += 1
        return counts

    def getSortedRemainingValues(self, indexVal):
        remainingVals = [card.index for card in self.cards if card.index != indexVal]
        remainingVals.sort(reverse=True)
        return remainingVals
    
    def getSortedValues(self):
        vals = [card.index for card in self.cards]
        vals.sort(reverse=True)
        return vals

    def pair(self):
        for indexVal, count in self.counts.items():
            if count == 2:
                return [indexVal] * 2 + self.getSortedRemainingValues(indexVal)
        return False

    def threeOfAKind(self):
        for indexVal, count in self.counts.items():
            if count == 3:
                return [indexVal] * 3 + self.getSortedRemainingValues(indexVal)
        return False

    def fourOfAKind(self):
        for indexVal, count in self.counts.items():
            if count == 4:
                return [indexVal] * 4 + self.getSortedRemainingValues(indexVal)
        return False

    def fullHouse(self):
        if self.pair() and self.threeOfAKind():
            return self.threeOfAKind()
        return False

    def flush(self):
        suits = set()
        for card in self.cards:
            suits.add(card.suit)
        if len(suits) == 1:
            return self.getSortedValues()
        return False

    def cardValue(self, card):
        return Deck.values.index(card.value)

    def straight(self):
        self.cards.sort(key=self.cardValue, reverse=False)
        handVals = ''.join([card.value for card in self.cards])
        if handVals in self.straightCombos:
            return self.getSortedValues()
        return False

    def straightFlush(self):
        if self.straight() and self.flush():
            return self.getSortedValues()
        return False

    def royalFlush(self):
        self.cards.sort(key=self.cardValue, reverse=False)
        handVals = ''.join([card.value for card in self.cards])
        if handVals == '10JQKA' and self.flush():
            return self.getSortedValues()
        return False

    def twoPair(self):
        if sorted(self.counts.values()) == [1, 2, 2]:
            # should be two paired vals
            pairedVals = [val for val, count in self.counts.items() if count == 2]
            pairedVals.sort(reverse=True)
            unpairedVal = [val for val, count in self.counts.items() if count == 1][0]
            return [pairedVals[0], pairedVals[0], pairedVals[1], pairedVals[1], unpairedVal]

    def getScore(self):
        if self.royalFlush():
            return [9] + self.royalFlush()
        if self.straightFlush():
            return [8] + self.straightFlush()
        if self.fourOfAKind():
            return [7] + self.fourOfAKind()
        if self.fullHouse():
            return [6] +  self.fullHouse()
        if self.flush():
            return [5] + self.flush()
        if self.straight():
            return [4] + self.straight()
        if self.threeOfAKind():
            return [3] + self.threeOfAKind()
        if self.twoPair():
            return [2] + self.twoPair()
        if self.pair():
            return [1] + self.pair()
        
        return [0] + self.getSortedValues() 
        

deck = Deck()

hand1 = deck.deal()
hand2 = deck.deal()


def determineWinner(hand1, hand2):
    score1 = hand1.getScore()
    score2 = hand2.getScore()
    for i in range(6):
        if score1[i] > score2[i]:
            return 'HAND 1 WINS!'

        if score1[i] < score2[i]:
            return 'HAND 2 WINS!'

determineWinner(hand1, hand2)
