from model.game_rules import GameRules
from model.disk_color import DiskColor
from model.player import Player
from model.disk import Disk

class Board:
    ""
    def __init__(self, size: int =8) -> None:
        ""
        self.size = size
        self.mat = [[''] * self.size for _ in range(self.size)]        
        self.generate_starter_board()      


    def generate_starter_board(self):
        """Fills the whole board with empty disk objects, then
        places the first for disks in their initial center-of-board places,
        assuming an n x n size board, where n is an even number.
        """
        self.fill_with_empty_disks()
        middle = (self.size // 2) - 1
        center_up_left = (middle, middle)
        center_up_right = (middle + 1, middle)
        center_down_left = (middle, middle + 1)
        center_down_right = (middle + 1, middle + 1)     
        self.mat[center_up_left[1]][center_up_left[0]] = Disk(DiskColor.WHITE)
        self.mat[center_down_right[1]][center_down_right[0]] = Disk(DiskColor.WHITE)
        self.mat[center_up_right[1]][center_up_right[0]] = Disk(DiskColor.BLACK)
        self.mat[center_down_left[1]][center_down_left[0]] = Disk(DiskColor.BLACK)        


    def display(self) -> str:
        """Display function for testing purposes. 
        Prints the names of the Disk objects in each cell.
        """        
        print('\n')                            
        show_mat = [[cell for cell in row] for row in self.mat]
        for row in enumerate(show_mat):
            for disk in enumerate(row[1]):                
                if isinstance(disk[1], Disk):
                    show_mat[row[0]][disk[0]] = disk[1].color_obj.name
            print(row[1])     


    def fill_with_empty_disks(self):
        for row in enumerate(self.mat):
            for cell in enumerate(row[1]):
                self.mat[row[0]][cell[0]] = Disk(DiskColor.EMPTY)


    def add_disk(self, player: Player, position: tuple):
        """Adds a disk object to the board at the given position.

        Args:
            player (Player): the player's color attribute-object will be assigned
            to the given position in the board matrix
            position (tuple): given as an (x, y) coordinate for an imagined
            size x size board; 1 will be subtracted from each to fit "1 to 8"
            matrix indices.
        """
        color_value = player.color_value        
        new_disk = Disk(DiskColor(color_value))
        self.mat[position[1] - 1][position[0] - 1] = new_disk     


    def convert_disks_in_all_dirs(self, start_pos):

        print(f'board.py, convert_disks_in_all_dirs, line 68 - GameRules.end_points_and_directions: {GameRules.end_points_and_directions}.')  # DEBUG LINE

        for tuple in GameRules.end_points_and_directions:
            self.convert_disks_in_one_dir(start_pos, tuple[0], tuple[1])


    def convert_disks_in_one_dir(self, start_pos, end_pos, conversion_direction):
        """Helper function"""
        start_pos = (start_pos[0] - 1, start_pos[1] - 1)
        end_pos = (end_pos[0] - 1, end_pos[1] - 1)        
        next_pos = (start_pos[0] + conversion_direction[0], start_pos[1] + conversion_direction[1])
        while next_pos != end_pos:  # Next position will never = end position, because the latter is not on the way of the conversion_direction.

            print(f'board.py, line 77 - start_pos: {start_pos}')  # DEBUG BLOCK
            print(f'board.py, line 78 - end_pos: {end_pos}')
            print(f'board.py, line 79 - next_pos: {next_pos}')

            self.mat[next_pos[1]][next_pos[0]].change_color()
            next_pos = (next_pos[0] + conversion_direction[0], next_pos[1] + conversion_direction[1])
