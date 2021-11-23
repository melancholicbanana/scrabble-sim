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
        self.letter_points = {
            0: ['blank'],
            1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
            2: ['D', 'G'],
            3: ['B', 'C', 'M', 'P'],
            4: ['F', 'H', 'V', 'W', 'Y'],
            5: ['K'],
            8: ['J', 'X'],
            10: ['Q', 'Z']
        }
        self.letter_frequencies = {
            1: ['J', 'K', 'Q', 'X', 'Z'],
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
        # print(self.bag_list, '\n')


class Hand:
    """Represents each player's hand."""

    def __init__(self):
        self.current_hand = []
        self.letters_in_hand = len(self.current_hand)

    def draw_letters(self, letters_bag):  # letters_bag should be an instance of the LettersBag class.
        """Draw letters from the bag."""
        if self.letters_in_hand < 7:
            for i in range(7 - self.letters_in_hand):
                letter = letters_bag.bag_list.pop(0)
                self.current_hand.append(letter)

    def print_hand(self):
        """Print the hand."""
        print(self.current_hand, '\n')


class Board:
    """Represents the scrabble board."""

    def __init__(self):
        """Initialize an empty board with bonus tiles marked."""
        self.board = [['-'] * 15 for _ in range(15)]
        double_word_coords = [
            (1, 1), (1, 13),
            (2, 2), (2, 12),
            (3, 3), (3, 11),
            (4, 4), (4, 10),
            (7, 7),
            (10, 4), (10, 10),
            (11, 3), (11, 11),
            (12, 2), (12, 12),
            (13, 1), (13, 13)
        ]
        triple_word_coords = [
            (0, 0), (0, 7), (0, 14),
            (7, 0), (7, 14),
            (14, 0), (14, 7), (14, 14)
        ]
        double_letter_coords = [
            (0, 3), (0, 11), (2, 6), (2, 8),
            (3, 0), (3, 7), (3, 14),
            (6, 2), (6, 6), (6, 8), (6, 12),
            (7, 3), (7, 11),
            (8, 2), (8, 6), (8, 8), (8, 12),
            (11, 0), (11, 7), (11, 14),
            (12, 6), (12, 8), (14, 3), (14, 11)
        ]
        triple_letter_coords = [
            (1, 5), (1, 9),
            (5, 1), (5, 5), (5, 9), (5, 13),
            (9, 1), (9, 5), (9, 9), (9, 13),
            (13, 5), (13, 9)
        ]

        for i in double_word_coords:
            self.board[i[0]][i[1]] = 'w'

        for j in triple_word_coords:
            self.board[j[0]][j[1]] = 'W'

        for a in double_letter_coords:
            self.board[a[0]][a[1]] = 'l'

        for b in triple_letter_coords:
            self.board[b[0]][b[1]] = 'L'

    def print_board(self):
        """Print the board."""
        for row in self.board:
            for item in row:
                print(str(item) + "  ", end="")
            print(' ')


if __name__ == '__main__':
    new_bag = LettersBag()
    new_bag.initialize_bag()

    first_hand = Hand()
    first_hand.draw_letters(new_bag)
    first_hand.print_hand()

    second_hand = Hand()
    second_hand.draw_letters(new_bag)
    second_hand.print_hand()

    new_board = Board()
    new_board.print_board()
