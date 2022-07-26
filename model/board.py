from model.disk_color import DiskColor
from model.player import Player
from model.disk import Disk

class Board:
    ""

    def __init__(self, size) -> None:
        ""
        self.mat = [[''] * size for _ in range(size)]       
    

    def add_disk(self, player: Player, position: tuple):
        """Adds a disk object to the board at the given position.

        Args:
            player (Player): its color attribute will be assigned to the position
            in the board matrix
            position (tuple): given as an (x, y) coordinate for an imagined
            size x size board; 1 will be subtracted from each to fit matrix indices.
        """
        color_value = player.color_value        
        new_disk = Disk(DiskColor(color_value), position)
        new_disk_position = self.mat[position[1] - 1][position[0] - 1]
        
        
        


    def generate_starter_board():
        pass


    def update_board():
        pass
