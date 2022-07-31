from abc import ABC, abstractmethod
from model.game import ReversiGame
from model.player import Player

class GameView(ABC):
    ""
    def __init__(self, game: ReversiGame, board_size=8) -> None:
        self.board_size = board_size     
        self.game = game   

    def display_welcome_meessage(self):
        pass

    def display_score(self, player: Player):
        pass

    def get_move(self, player: Player, position):
        pass

    def display_winner(self, player: Player):
        pass



