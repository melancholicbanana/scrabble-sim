# import letters_bag
# from letters_bag import LettersBag
from parse_check_position import check_position_validity, check_dictionary, parse_position
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
        self.letters_empty = False

    def play(self, player):

        successful = False
        while not successful:
            print("\n")
            self.current_board.print_board()
            print(f"YOUR TURN: {player.name.upper()}. Enter '!' to quit at any time.\n")
            player.hand.print_hand()

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
                if parse_position(self.position) is not None:
                    valid = check_position_validity(self.word, self.position, self.first_turn,
                                                self.current_board, player.hand.current_hand)
                    if valid:
                        full_word, in_dict = check_dictionary(self.current_board, self.word, self.position)
                        if in_dict:
                            new_board, board_values = update_board(self.current_board, self.word, self.position)
                            self.current_board = new_board
                            player.hand.place_word(self.word)
                            player.score += calculate_score(self.word, board_values)
                            player.print_score()
                            if len(player.hand.current_hand) == 0 and self.current_bag.check_bag_empty():
                                print("END OF GAME.")
                            else:
                                player.hand.draw_letters(self.current_bag)
                            successful = True
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
