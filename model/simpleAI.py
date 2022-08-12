from model.disk_color import DiskColor
from model.player import Player


class SimpleAI(Player):
    ""
    def __init__(self, color_obj: DiskColor, score=0) -> None:
        super().__init__(color_obj, score)
    
    # 1.Look for convertible disks, store them in a list of tuples with (position, direction)


    # 2.Copy the current-state board, "dummy-board" (watch out for aliasing)


    # 3.Convert the disks in the dummy board according to the list created in 1.


    # 4.Calculate and add the score of this new hypothetical board to the corresponding tuple in list from 1.


    # 5.Repeat steps 2-4 for all the convertible disks from list in 1.


    # 6.Find the move with the highest score and perform it.

