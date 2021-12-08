from parse_check_position import check_position_validity, check_dictionary
from calculate_score import calculate_score
from update_board import update_board


class Turn:
    """Allows a player to take a turn."""

    def __init__(self, current_board, letters_bag, first_turn):
        self.current_board = current_board
        # self.player = player
        self.word = ""
        self.full_word = ""
        self.position = ""
        self.current_bag = letters_bag
        self.first_turn = first_turn

    def play(self, player):

        print(f"YOUR TURN: {player.name.upper()}. Enter '!' to quit at any time.\n")
        player.hand.print_hand()

        quit_message = "\nYou have quit the game."
        self.word = input("Word: ")
        if self.word == '!':
            print(quit_message)
        self.position = input("Position (e.g. A1D): ")
        if self.position == '!':
            print(quit_message)
        else:
            valid = check_position_validity(self.word, self.position, self.first_turn,
                                            self.current_board, player.hand.current_hand)
            print("POSITION VALID:", valid)
            full_word, in_dict = check_dictionary(self.current_board, self.word, self.position)
            print("FULL WORD:", full_word, "IN_DICT:", in_dict)
            print("DICTIONARY CHECK COMPLETE")
            if valid and in_dict:
                print("VALID AND IN DICT")
                new_board, board_values = update_board(self.current_board, self.word, self.position)
                self.current_board = new_board
                # print(board_values)
                print("UPDATE BOARD COMPLETE")
                player.hand.place_word(self.word)
                print("PLACE WORD COMPLETE")
                player.score += calculate_score(self.word, board_values)
                player.hand.draw_letters(self.current_bag)
                player.print_score()
                if self.first_turn:
                    self.first_turn = False
                return self.current_board, self.current_bag, self.first_turn

    # Things that happen in a turn:
    # Call for input word
    # Call for input position
    # Check position is legal. If yes,
    # Update board
    # Remove from player hand
    # Player draws new letters
    # Calculate new player score
    # Start new turn for different player
