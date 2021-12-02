import string


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
