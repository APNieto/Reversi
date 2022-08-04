from model.disk_color import DiskColor
from model.player import Player
from model.game_rules import GameRules
from model.board import Board


class ReversiGame:
    ""
    def __init__(self, size:int =8) -> None:
        """Creates an instance of Reversi, including the board, rules, move and validity checks functions.

        Args:
            board (_type_): creates a Board object.
            size (int, optional): Must be set to an even number. Defaults to 8.
        """
        self.board_size = size
        self.board = Board(size)
        self.matrix = self.board.mat

        print('\ngame.py, line 20: Prints actual board matrix with disk objects: ')  # DEBUG (block)
        for row in self.board.mat:                                                    
            print(row)                                                                
        print('')  

        self.players_list = [Player(DiskColor.BLACK), Player(DiskColor.WHITE)]
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


    def convert_disks(self, start_pos, end_pos, direction, matrix):  # TESTING STAGE -- TODO    PASAR ESTA FUNCIÓN AL MÓDULO matrix
        start_pos = (start_pos[0] - 1, start_pos[1] - 1)
        end_pos = (end_pos[0] - 1, end_pos[1] - 1)
        next_pos = (start_pos[0] + direction[0], start_pos[1] + direction[1])
        while next_pos != end_pos:
            print(next_pos)  # TEST PRINT
            print(matrix[next_pos[1]][next_pos[0]])  # TEST PRINT
            print(f'Disk obj value pre-conversion: {matrix[next_pos[1]][next_pos[0]].color_obj.value}'  # TEST PRINT
            f'\nDisk obj name pre-conversion: {matrix[next_pos[1]][next_pos[0]].color_obj.name}')
            matrix[next_pos[1]][next_pos[0]].change_color()
            print(f'Disk obj value post-conversion: {matrix[next_pos[1]][next_pos[0]].color_obj.value}'  # TEST PRINT
            f'\nDisk obj name post-conversion: {matrix[next_pos[1]][next_pos[0]].color_obj.name}')
            next_pos = (next_pos[0] + direction[0], next_pos[1] + direction[1])
        return matrix



        


    def update_score(self):
        pass


    def check_winner(self):
        pass



