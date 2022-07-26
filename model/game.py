from model.disk_color import DiskColor
from model.player import Player
from model.game_rules import GameRules


class ReversiGame:
    ""
    def __init__(self, board, size=8) -> None:
        self.board = board
        self.players_list = [Player(DiskColor.BLACK), Player(DiskColor.WHITE)]
        self.curr_player = self.players_list[0]

    def change_player(self):
        if self.curr_player == self.players_list[0]:
            self.curr_player = self.players_list[1]     # This will not create a new object,
        else:                                           # self.curr_player will now point
            self.curr_player = self.players_list[0]     # to the 2nd element in the list
                                                        

    def check_available_moves(self, player):
        return GameRules.check_available_moves(player)


    def is_valid_move(self, player, position):
        return GameRules.is_valid_move(player, position)


    def make_move(self, position):
        pass


    def update_score(self, player):
        pass


    def check_winner(self):
        pass



# Question 1, about separating game logic from main game module:
#       -encapsulated is_valid_move and check_available_moves, was that OK?