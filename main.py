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
import re


class LettersBag:
    """Represents the bag of letters."""

    def __init__(self):
        self.bag_list = []
        self.all_letters = list(string.ascii_uppercase) + ['blank']
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

    def draw_letters(self, letters_bag):  # letters_bag should be an instance of the LettersBag class.
        """Draw letters from the bag."""
        for i in range(7 - len(self.current_hand)):
            letter = letters_bag.bag_list.pop(0)
            self.current_hand.append(letter)

    def place_word(self, word):
        """Removes the letters in the word from the player's hand."""
        for letter in word.upper():
            self.current_hand.remove(letter)
            print(self.current_hand)

    def print_hand(self):
        """Print the hand."""
        print(self.current_hand, '\n')

    def shuffle_hand(self):
        """Shuffles the hand."""
        random.shuffle(self.current_hand)


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
            self.board[i[0]][i[1]] = '3'

        for j in triple_word_coords:
            self.board[j[0]][j[1]] = '4'

        for a in double_letter_coords:
            self.board[a[0]][a[1]] = '1'

        for b in triple_letter_coords:
            self.board[b[0]][b[1]] = '2'

    def print_board(self):
        """Print the board."""
        counter = 0
        print("\t\t", end="")
        for i in range(15):
            if i <= 8:
                print(str(i + 1) + "  ", end="")
            else:
                print(str(i + 1) + " ", end="")
        print("\n")
        for row in self.board:
            print(list(string.ascii_uppercase)[counter], end="\t\t")
            counter += 1
            for item in row:
                print(str(item) + "  ", end="")
            print(' ')
        print("\n")


class Player:
    """Represents a player in the game."""

    def __init__(self, name, hand):
        """Initializes a player."""
        self.name = name
        self.hand = hand
        self.score = 0

    def calculate_score(self, word, board_values):
        letter_points = {
            0: ['blank'],
            1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
            2: ['D', 'G'],
            3: ['B', 'C', 'M', 'P'],
            4: ['F', 'H', 'V', 'W', 'Y'],
            5: ['K'],
            8: ['J', 'X'],
            10: ['Q', 'Z']
        }
        empty_tiles = ['4', '3', '2', '1', '-']
        word_score = 0
        skipped = 0
        triple_word_score = 0
        double_word_score = 0

        def get_score_from_letter(letter):
            for key, values in letter_points.items():
                if letter in values:
                    return key

        for index, letter in enumerate(word):
            board_value = board_values[index + skipped]
            while board_value not in empty_tiles:
                word_score += get_score_from_letter(board_value)  # For when the value is a connecting letter
                print('FOUND CONNECTING LETTER:', board_value, 'REGULAR SCORE:', word_score)
                skipped += 1
                board_value = board_values[index + skipped]
            if board_value == '1':  # Double letter score
                word_score += get_score_from_letter(letter) * 2
                print('DOUBLE LETTER SCORE ON "' + letter + '": ' + str(word_score))
            elif board_value == '2':  # Triple letter score
                word_score += get_score_from_letter(letter) * 3
                print('TRIPLE LETTER SCORE ' + letter + ' ' + str(word_score))
            elif board_value == '3':  # Double word score
                double_word_score += 1
                word_score += get_score_from_letter(letter)
                print('DOUBLE WORD SCORE ' + letter + ' ' + str(word_score))
            elif board_value == '4':  # Triple word score
                triple_word_score += 1
                word_score += get_score_from_letter(letter)
                print('TRIPLE WORD SCORE ' + letter + ' ' + str(word_score))
            else:
                word_score += get_score_from_letter(letter)
                print('REGULAR SCORE: ' + letter + ' ' + str(word_score))

        for i in range(double_word_score):
            word_score *= 2

        for j in range(triple_word_score):
            word_score *= 3

        print('FINAL WORD SCORE:', word_score)
        return word_score


def parse_position(position_str):
    """Parses the entered position."""
    pattern = "([A-O])([1-9][0-4]{0,1})(D|A)"
    match = re.match(pattern, position_str)
    try:
        row = match.group(1)
        column = match.group(2)
        across_down = match.group(3)
        print(list(string.ascii_uppercase).index(row), int(column), across_down)
        return list(string.ascii_uppercase).index(row), int(column), across_down
    except AttributeError:
        print("Invalid position, try again!")


def check_position_validity(word, position_str, first_turn, board, hand):
    """Ensures the word fits on the board."""
    row, column, across_down = parse_position(position_str)
    word_length = len(word)

    for letter in word.upper():
        if letter in hand:
            continue
        else:
            print("Letters not in hand.")
            return False

    if across_down == 'D':
        end_point = row + word_length - 1
    else:
        end_point = column + word_length - 1
    if end_point > 14:
        print("Word out of bounds!")
        return False

    if first_turn:
        pass  # Write something here for the first turn
    else:
        get_board_values = []
        empty_tiles = ['4', '3', '2', '-']
        try:
            for i in range(word_length):
                if across_down == 'A':
                    get_board_values.append(board.board[row][column + i - 1])
                else:
                    get_board_values.append(board.board[row + i][column - 1])
            print(get_board_values)

            print('BOARD VALUES SET', set(get_board_values))
            print('EMPTY TILES SET', set(empty_tiles))
            if all(item in set(empty_tiles) for item in get_board_values):
                print("No connecting tiles. Try again!")
                return False
            else:
                print("Found connecting tile.")
                return True, hand
        except IndexError:
            print("Word out of bounds!")
            return False

    # Possible errors:
    # Not connected to existing word (unless first turn)


def update_board(board, word, position_str):
    """Updates the board with the new word,
    skipping any tiles that are already full."""
    word_length = len(word)
    empty_tiles = ['4', '3', '2', '-']
    board_values = []
    row, column, across_down = parse_position(position_str)
    for i in range(word_length):
        if across_down == 'A':
            successful = False
            while not successful:
                board_value = board.board[row][column + i - 1]
                board_values.append(board_value)
                print('BOARD VALUE:', board_value, 'ROW:', row, 'COLUMN:', column + i - 1, 'i:', i, 'LETTER:',
                      word[i].upper())
                if board_value in empty_tiles:
                    board.board[row][column + i - 1] = word[i].upper()
                    print('LETTER PLACED SUCCESSFULLY')
                    successful = True
                else:
                    print('SKIPPED COLUMN', str(column + i - 1), ", COLUMN IS NOW", column + i)
                    column += 1
        else:
            successful = False
            while not successful:
                board_value = board.board[row + i][column - 1]
                board_values.append(board_value)
                print('BOARD VALUE:', board_value, 'ROW:', row + i, 'COLUMN:', column - 1, 'i:', i, 'LETTER:',
                      word[i].upper())
                if board_value in empty_tiles:
                    board.board[row + i][column - 1] = word[i].upper()
                    print('LETTER PLACED SUCCESSFULLY')
                    successful = True
                else:
                    print('SKIPPED ROW', str(row + i), ", ROW IS NOW", row + i + 1)
                    row += 1
    board.print_board()
    return board_values


class Turn:
    """Allows a player to take a turn."""

    def __init__(self, current_board, player, letters_bag):
        self.current_board = current_board
        self.player = player
        self.word = ""
        self.position = ""
        self.current_bag = letters_bag

        print(f"YOUR TURN: {player.name.upper()}. Enter '!' to quit at any time.\n")
        self.player.hand.print_hand()

        while True:
            quit_message = "\nYou have quit the game."
            self.word = input("Word: ")
            if self.word == '!':
                print(quit_message)
                break
            self.position = input("Position (e.g. A1D): ")
            if self.position == '!':
                print(quit_message)
                break
            else:
                valid = check_position_validity(self.word, self.position, False,
                                                self.current_board, self.player.hand.current_hand)
                if valid:
                    board_values = update_board(self.current_board, self.word, self.position)
                    print(board_values)
                    self.player.hand.place_word(self.word)
                    self.player.calculate_score(self.word, board_values)
                    self.player.hand.draw_letters(self.current_bag)
            break

    # Things that happen in a turn:
    # Call for input word
    # Call for input position
    # Check position is legal. If yes,
    # Update board
    # Remove from player hand
    # Player draws new letters
    # Calculate new player score
    # Start new turn for different player


if __name__ == '__main__':
    new_bag = LettersBag()
    new_bag.initialize_bag()

    first_hand = Hand()
    first_hand.draw_letters(new_bag)
    # first_hand.print_hand()

    second_hand = Hand()
    second_hand.draw_letters(new_bag)
    # second_hand.print_hand()

    new_board = Board()
    new_board.print_board()

    player_1 = Player("Oscar", first_hand)
    player_2 = Player("Rose", second_hand)

    new_turn = Turn(new_board, player_1, new_bag)

    # player_1.calculate_score('WORD', ['-', '2', '4', 'L', '-'])
    # check_position_validity('Word', 'B1D', False, new_board)
    # update_board(new_board, 'Word', 0, 1, 'D')
