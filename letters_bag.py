import random
import string


class LettersBag:
    """Represents the bag of letters."""

    def __init__(self):
        self.bag_list = []
        self.all_letters = list(string.ascii_uppercase) + ['#']
        self.letter_frequencies = {
            1: ['J', 'K', 'Q', 'X', 'Z'],
            2: ['B', 'C', 'F', 'H', 'M', 'P', 'V', 'W', 'Y', '#'],
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
