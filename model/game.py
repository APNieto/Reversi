from model.disk_color import DiskColor
from model.player import Player
from model.game_rules import GameRules
from model.board import Board
from datetime import datetime
from .simpleAI import SimpleAI


class ReversiGame:
    ""
    def __init__(self) -> None:
        """Creates an instance of Reversi, including the board, rules, move and validity checks functions.

        Args:
            board (_type_): creates a Board object.
            size (int, optional): Must be set to an even number. Defaults to 8.
        """
        self.game_mode = 0


    def create_board(self, size:int =8):
        self.board_size = size
        self.board = Board(size)
        self.matrix = self.board.mat        
    

    def create_players(self, player_mode):
        # Players creation for 2-player mode
        if player_mode[0] == 2:
            self.players_list = [Player(DiskColor.BLACK), Player(DiskColor.WHITE)]
            
        # Players creation for vs. computer mode
        elif player_mode[0] == 1:
            if player_mode[1] == 'b':
                self.players_list = [Player(DiskColor.BLACK), SimpleAI(DiskColor.WHITE)]                
            elif player_mode[1] == 'w':
                self.players_list = [SimpleAI(DiskColor.BLACK), Player(DiskColor.WHITE)]                                
        
        # The first player will always be color Black
        self.curr_player = self.players_list[0]      


    def change_player(self):
        ""
        if self.curr_player == self.players_list[0]:
            self.curr_player = self.players_list[1]     # This will not create a new object,
        else:                                           # self.curr_player will now point
            self.curr_player = self.players_list[0]     # to the 2nd element in the list
                                                       

    def is_valid_move(self, player, new_position):
        ""
        return GameRules.is_valid_move(player, new_position, self.board_size)


    def make_move(self, position: tuple):
        ""
        self.board.add_disk(self.curr_player, position)


    def calculate_score(self, player: Player):
        ""
        player.score = 0                                                                 
        for row in enumerate(self.board.mat):
            for disk in enumerate(row[1]):                
                if disk[1].color_obj == player.color_obj:
                    player.score += 1


    def calculate_scores(self):
        ""                                                                 
        for player in self.players_list:
            self.calculate_score(player)             


    def record_score(self, result_text):
        raw_time = datetime.now()
        formatted_time = raw_time.strftime('%d of %b, %Y - %H:%M')
        with open('Reversi_results.txt', 'a') as f:
            print(f"---Game of {formatted_time}---\n{result_text}\n{'-'*41}\n", file=f)