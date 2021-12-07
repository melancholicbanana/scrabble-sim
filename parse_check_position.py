import re
import string


def parse_position(position_str):
    """Parses the entered position."""
    pattern = "([A-O])([1-9][0-5]{0,1})(D|A)"
    match = re.match(pattern, position_str)
    try:
        row = match.group(1)
        column = match.group(2)
        across_down = match.group(3)
        return list(string.ascii_uppercase).index(row), int(column) - 1, across_down
    except AttributeError:
        print("Invalid position, try again!")


def get_board_values(board, word, position_str):
    """Given a word and position, this retrieves the tiles on the board if the word were placed."""
    row, column, across_down = parse_position(position_str)
    word_length = len(word)
    board_values = []
    empty_tiles = ['4', '3', '2', '-']

    for i in range(word_length):
        if across_down == 'A':
            successful = False
            while not successful:
                board_value = board.board[row][column + i]
                board_values.append(board_value)
                # print('BOARD_VAL:', board_value, 'ROW:', row, 'COL:', column + i, 'i:', i, 'LETTER:', word[i].upper())
                if board_value in empty_tiles:
                    # print('FOUND EMPTY TILE')
                    successful = True
                else:
                    # print('SKIPPED COLUMN', str(column + i), ", COLUMN IS NOW", column + i + 1)
                    column += 1
        else:
            successful = False
            while not successful:
                board_value = board.board[row + i][column]
                board_values.append(board_value)
                # print('BOARD_VAL:', board_value, 'ROW:', row + i, 'COL:', column, 'i:', i, 'LETTER:', word[i].upper())
                if board_value in empty_tiles:
                    # print('FOUND EMPTY TILE')
                    successful = True
                else:
                    # print('SKIPPED ROW', str(row + i), ", ROW IS NOW", row + i + 1)
                    row += 1

    print(word.upper(), board_values)
    return board_values


def check_position_validity(word, position_str, first_turn, board, hand):
    """Ensures the word fits on the board."""
    for letter in word.upper():  # Check that letters are in hand
        if letter in hand:
            continue
        else:
            print("Letters not in hand.")
            return False

    try:  # Check that the word's end point is within the board
        board_values = get_board_values(board, word, position_str)
    except IndexError:
        print("Word out of bounds.")
        return False

    if first_turn:
        row, column, across_down = parse_position(position_str)
        if across_down == 'A' and row != 7:
            print("Incorrect row for first turn.")
            return False
        elif across_down == 'D' and column != 7:
            print("Incorrect column for first turn.")
            return False
        elif '3' not in board_values:
            print("Middle tile not covered, try again.")
            return False
    else:
        empty_tiles = ['4', '3', '2', '-']
        if all(item in set(empty_tiles) for item in board_values):  # Ensure there is a connecting tile
            print("No connecting tiles. Try again!")
            return False
        else:
            print("Found connecting tile.")
            return True


def assign_blanks(word):
    """If a blank character is included in the word,
    replaces it with a letter of the player's choice."""
    if '#' in word:
        for index, letter in enumerate(word):
            if letter == '#':
                successful = False
                while not successful:
                    new_letter = input("You have used a blank. Enter your preferred letter.")
                    if len(new_letter) > 1:
                        print("One character only, try again.")
                    else:
                        successful = True
                        word[index] = new_letter
    return word


def check_dictionary(board, word, position_str):
    """Checks if the word is in the SOWPODS dictionary."""
    empty_tiles = ['4', '3', '2', '-']
    board_values = get_board_values(board, word, position_str)
    word_as_list = list(assign_blanks(word))
    # print("LIST:", word_as_list)
    for index, value in enumerate(board_values):
        if value not in empty_tiles:
            # print("VALUE:", value, "INDEX:", index)
            word_as_list.insert(index, value)
    full_word = "".join(word_as_list)
    # print(full_word)

    dictionary = open("sowpods.txt").read().splitlines()
    if full_word.lower() in dictionary:
        return full_word, True
    else:
        print("Word not in dictionary.\n")
        return None, False
