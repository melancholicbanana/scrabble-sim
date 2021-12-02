import re
import string


def parse_position(position_str):
    """Parses the entered position."""
    pattern = "([A-O])([1-9][0-4]{0,1})(D|A)"
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
        pass  # Write something here for the first turn
    else:
        empty_tiles = ['4', '3', '2', '-']
        if all(item in set(empty_tiles) for item in board_values):  # Ensure there is a connecting tile
            print("No connecting tiles. Try again!")
            return False
        else:
            print("Found connecting tile.")
            return True, hand
