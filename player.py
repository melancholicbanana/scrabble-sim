class Player:
    """Represents a player in the game."""

    def __init__(self, name, hand):
        """Initializes a player."""
        self.name = name
        self.hand = hand
        self.score = 0

    def print_score(self):
        print('YOUR SCORE IS NOW:', self.score)
