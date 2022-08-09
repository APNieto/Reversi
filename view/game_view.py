from abc import ABC, abstractmethod
from model.game import ReversiGame
from model.player import Player

class GameView(ABC):
    ""
    def __init__(self, game: ReversiGame, board_size=8) -> None:
        self.board_size = board_size     
        self.game = game   

    def get_game_mode(self):
        pass

    def pass_board_to_board_cons_view(self):
        pass

    def display_welcome_meessage(self):
        pass
    
    def get_board_size(self):
        pass

    def display_score(self, player: Player):
        pass

    def get_move(self, player: Player, position):
        pass

    def display_board(self):
        pass

    def print_skip_turn(self, player):
        pass

    def display_winner(self, players_list):
        pass

    def ask_for_replay(self):
        pass


