import random


class Hand:
    """Represents each player's hand."""

    def __init__(self):
        self.current_hand = []

    def draw_letters(self, letters_bag):  # letters_bag should be an instance of the LettersBag class.
        """Draw letters from the bag."""
        for i in range(7 - len(self.current_hand)):
            letter = letters_bag.bag_list.pop(0)
            self.current_hand.append(letter)

    def place_word(self, word):
        """Removes the letters in the word from the player's hand."""
        for letter in word.upper():
            self.current_hand.remove(letter)
            # print(self.current_hand)

    def print_hand(self):
        """Print the hand."""
        print(self.current_hand, '\n')

    def shuffle_hand(self):
        """Shuffles the hand."""
        random.shuffle(self.current_hand)
