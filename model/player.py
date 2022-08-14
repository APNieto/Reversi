from .board import Board
from model.disk_color import DiskColor

class Player:
    ""
    def __init__(self, color_obj: DiskColor, score=0) -> None:
        self.color_obj = color_obj
        self.color_name = color_obj.name    # Acceptable only because these values will not change
        self.color_value = color_obj.value  # unlike the Disk object case, where the "sub-object"
        self.score = score                  # attribute did change but this was not reflected in the original object


    def calculate_score(self, board: Board):
        """Calculates the score of the player for the given board object by
        counting the amount of disks with the same color object (DiskColor)
        as the player object calling the function."""
        self.score = 0                                                                 
        for row in enumerate(board.mat):
            for disk in enumerate(row[1]):                
                if disk[1].color_obj == self.color_obj:
                    self.score += 1