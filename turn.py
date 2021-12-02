from parse_check_position import check_position_validity
from calculate_score import calculate_score
from update_board import update_board


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
                    self.player.score += calculate_score(self.word, board_values)
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
