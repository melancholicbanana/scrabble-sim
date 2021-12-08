def calculate_score(word, board_values):
    """Given a word and the tiles it was placed on,
    calculate the player's increase in score for this turn."""
    letter_points = {
        0: ['#'],
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

    def get_score_from_letter(given_letter):
        """Looks up a letter's score in letter_points above."""
        result = [key for key, values in letter_points.items() if given_letter in values]
        return result[0]

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
            print('TRIPLE LETTER SCORE: ' + letter + ' ' + str(word_score))
        elif board_value == '3':  # Double word score
            double_word_score += 1
            word_score += get_score_from_letter(letter)
            print('DOUBLE WORD SCORE: ' + letter + ' ' + str(word_score))
        elif board_value == '4':  # Triple word score
            triple_word_score += 1
            word_score += get_score_from_letter(letter)
            print('TRIPLE WORD SCORE: ' + letter + ' ' + str(word_score))
        else:
            word_score += get_score_from_letter(letter)
            print('REGULAR SCORE: ' + letter + ' ' + str(word_score))

    for i in range(double_word_score):
        word_score *= 2

    for j in range(triple_word_score):
        word_score *= 3

    print('FINAL WORD SCORE:', word_score)
    return word_score
