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
import hand
import board
import player
import letters_bag
import update_board
import turn
from parse_check_position import parse_position, check_position_validity, get_board_values

if __name__ == '__main__':
    new_bag = letters_bag.LettersBag()
    new_bag.initialize_bag()

    first_hand = hand.Hand()
    first_hand.draw_letters(new_bag)
    # first_hand.print_hand()

    second_hand = hand.Hand()
    second_hand.draw_letters(new_bag)
    # second_hand.print_hand()

    new_board = board.Board()
    new_board.print_board()

    player_1 = player.Player("Oscar", first_hand)
    player_2 = player.Player("Rose", second_hand)

    # new_turn = turn.Turn(new_board, player_1, new_bag)

    # player_1.calculate_score('WORD', ['-', '2', '4', 'L', '-'])
    # check_position_validity('Word', 'A12A', False, new_board, ['W', 'O', 'R', 'D', 'A', 'A', 'A'])
    # get_board_values(new_board, 'Word', 'A1A')
    update_board.update_board(new_board, 'Word', 'O12A')
    """update_board is working except row O (across, any column) and column 15 (down, any column).
    Other things to do:
        - Dictionary checker
        - Allow blanks to be any letter
        - Turn system"""
    # Test comment
