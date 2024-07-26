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


class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♢', '♠', '♡', '♣']

    def __init__(self):
        self.cards = []
        for value in self.values:
            for suit in self.suits:
                self.cards.append(Card(value, suit))
        shuffle(self.cards)

    def deal(self):
        hand = Hand(self.cards[0:5])
        self.cards = self.cards[5:]
        return hand


class Hand:
    straightCombos = []
    for i in range(9):
        combo = Deck.values[i:i + 5]
        combo = ''.join(combo)
        straightCombos.append(combo)
    straightCombos.append('A2345')

    def __init__(self, cards):
        self.cards = cards

        self.counts = self.get_counts()

    def __str__(self):
        return ', '.join([str(card) for card in self.cards])

    def get_counts(self):
        counts = {}
        for card in self.cards:
            if card.index not in counts:
                counts[card.index] = 0
            counts[card.index] += 1
        return counts

    def get_sorted_remaining_values(self, indexVal):
        remainingVals = [
            card.index for card in self.cards if card.index != indexVal]
        remainingVals.sort(reverse=True)
        return remainingVals

    def get_sorted_values(self):
        vals = [card.index for card in self.cards]
        vals.sort(reverse=True)
        return vals

    def pair(self):
        for indexVal, count in self.counts.items():
            if count == 2:
                return [indexVal] * 2 + \
                    self.get_sorted_remaining_values(indexVal)
        return False

    def three_of_a_kind(self):
        for indexVal, count in self.counts.items():
            if count == 3:
                return [indexVal] * 3 + \
                    self.get_sorted_remaining_values(indexVal)
        return False

    def four_of_a_kind(self):
        for indexVal, count in self.counts.items():
            if count == 4:
                return [indexVal] * 4 + \
                    self.get_sorted_remaining_values(indexVal)
        return False

    def full_house(self):
        if self.pair() and self.three_of_a_kind():
            return self.three_of_a_kind()
        return False

    def flush(self):
        suits = set()
        for card in self.cards:
            suits.add(card.suit)
        if len(suits) == 1:
            return self.get_sorted_values()
        return False

    def card_value(self, card):
        return Deck.values.index(card.value)

    def straight(self):
        self.cards.sort(key=self.card_value, reverse=False)
        handVals = ''.join([card.value for card in self.cards])
        if handVals in self.straightCombos:
            return self.get_sorted_values()
        return False

    def straight_flush(self):
        if self.straight() and self.flush():
            return self.get_sorted_values()
        return False

    def royalFlush(self):
        self.cards.sort(key=self.card_value, reverse=False)
        handVals = ''.join([card.value for card in self.cards])
        if handVals == '10JQKA' and self.flush():
            return self.get_sorted_values()
        return False

    def two_pair(self):
        if sorted(self.counts.values()) == [1, 2, 2]:
            # should be two paired vals
            pairedVals = [
                val for val,
                count in self.counts.items() if count == 2]
            pairedVals.sort(reverse=True)
            unpairedVal = [
                val for val,
                count in self.counts.items() if count == 1][0]
            return [
                pairedVals[0],
                pairedVals[0],
                pairedVals[1],
                pairedVals[1],
                unpairedVal]

    def getScore(self):
        if self.royalFlush():
            return [9] + self.royalFlush()
        if self.straight_flush():
            return [8] + self.straight_flush()
        if self.four_of_a_kind():
            return [7] + self.four_of_a_kind()
        if self.full_house():
            return [6] + self.full_house()
        if self.flush():
            return [5] + self.flush()
        if self.straight():
            return [4] + self.straight()
        if self.three_of_a_kind():
            return [3] + self.three_of_a_kind()
        if self.two_pair():
            return [2] + self.two_pair()
        if self.pair():
            return [1] + self.pair()

        return [0] + self.get_sorted_values()


deck = Deck()

hand1 = deck.deal()
hand2 = deck.deal()


def determineWinner(hand1, hand2):
    print(hand1)
    print(hand2)
    score1 = hand1.getScore()
    score2 = hand2.getScore()

    for i in range(6):
        if score1[i] > score2[i]:
            print('HAND 1 WINS!')
            return
        if score1[i] < score2[i]:
            print('HAND 2 WINS!')
            return


determineWinner(hand1, hand2)
