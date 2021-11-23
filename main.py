"""
Plan:
- Simulate the scrabble game. Each turn has four states:
    - Board
    - Letters in hand
    - Remaining letters in bag
    - Player scores
    And three actions:
    - Place letters (changes board)
    - Tally points (changes scores)
    - Draw new letters (changes letters in hand AND letters in bag)

- Then focus on the decision-making each time. Start basic:
    - Look at all possible slots
    - See how many letters fit in each slot
    - Search CSW for words given that:
        - Letters in a single row/column + letters from hand complete one or more continuous words
    Then look at improvements:
    - Make long-term (not greedy) decisions.
    - Try adding letters onto the end of words to make a new slot
"""

import string
import random


class LettersBag:
    """Represents the bag of letters."""
    def __init__(self):
        self.bag_list = []
        self.all_letters = list(string.ascii_uppercase) + ['blank']
        self.letter_points = {0: ['blank'],
                              1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
                              2: ['D', 'G'],
                              3: ['B', 'C', 'M', 'P'],
                              4: ['F', 'H', 'V', 'W', 'Y'],
                              5: ['K'],
                              8: ['J', 'X'],
                              10: ['Q', 'Z']
                              }
        self.letter_frequencies = {1: ['J', 'K', 'Q', 'X', 'Z'],
                                   2: ['B', 'C', 'F', 'H', 'M', 'P', 'V', 'W', 'Y', 'blank'],
                                   3: ['G'],
                                   4: ['D', 'L', 'S', 'U'],
                                   6: ['N', 'R', 'T'],
                                   8: ['O'],
                                   9: ['A', 'I'],
                                   12: ['E']
                                   }

    def initialize_bag(self):
        """Initialize the full bag of letters."""
        for freq, letters in self.letter_frequencies.items():
            for letter in letters:
                for i in range(freq):
                    self.bag_list.append(letter)
        random.shuffle(self.bag_list)
        print(self.bag_list, '\n')


class Hand:
    """Represents each player's hand."""
    def __init__(self):
        self.current_hand = []
        self.letters_in_hand = len(self.current_hand)

    def draw_letters(self, letters_bag):
        if self.letters_in_hand < 7:
            for i in range(7 - self.letters_in_hand):
                letter = letters_bag.bag_list.pop(0)
                self.current_hand.append(letter)

    def print_hand(self):
        print(self.current_hand)


if __name__ == '__main__':

    new_bag = LettersBag()
    new_bag.initialize_bag()

    first_hand = Hand()
    first_hand.draw_letters(new_bag)
    first_hand.print_hand()

    second_hand = Hand()
    second_hand.draw_letters(new_bag)
    second_hand.print_hand()
