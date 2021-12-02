from parse_check_position import parse_position, get_board_values


def update_board(board, word, position_str):
    """Updates the board with the new word,
    skipping any tiles that are already full."""
    word_length = len(word)
    empty_tiles = ['4', '3', '2', '-']
    board_values = get_board_values(board, word, position_str)
    row, column, across_down = parse_position(position_str)
    skipped = 0
    for i in range(word_length):
        if across_down == 'A':
            successful = False
            while not successful:
                board_value = board_values[i + skipped]
                if board_value in empty_tiles:
                    board.board[row][column + i + skipped] = word[i].upper()
                    # print('LETTER PLACED SUCCESSFULLY')
                    successful = True
                else:
                    # print('SKIPPED COLUMN', str(column + i + skipped), ", COLUMN IS NOW", column + i + skipped + 1)
                    skipped += 1
        else:
            successful = False
            while not successful:
                board_value = board_values[i + skipped]
                if board_value in empty_tiles:
                    board.board[row + i + skipped][column] = word[i].upper()
                    # print('LETTER PLACED SUCCESSFULLY')
                    successful = True
                else:
                    # print('SKIPPED ROW', str(row + i + skipped), ", ROW IS NOW", row + i + skipped + 1)
                    skipped += 1
    board.print_board()
    return board_values
