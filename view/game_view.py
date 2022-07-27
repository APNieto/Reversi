from abc import ABC, abstractmethod

class GameView(ABC):
    ""
    def __init__(self, board_size=8) -> None:
        self.board_size = board_size        

    def display_welcome_meessage(self):
        pass

    def display_score(self, player_1, player_2):
        pass

    def get_move(self, player, position):
        pass

    def display_winner(self, player):
        pass



