from model.disk_color import DiskColor
from model.player import Player

class SimpleAI(Player):
    ""
    def __init__(self, color_obj: DiskColor, score=0) -> None:
        super().__init__(color_obj, score)
    