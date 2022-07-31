from inspect import currentframe, getframeinfo
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
        print('\n\n')                            
        show_mat = [[cell for cell in row] for row in self.mat]
        for row in enumerate(show_mat):
            for disk in enumerate(row[1]):                
                if isinstance(disk[1], Disk):
                    show_mat[row[0]][disk[0]] = disk[1].color_name
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