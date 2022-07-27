from model.disk_color import DiskColor
from model.board import Board

class Player:
    ""

    def __init__(self, color: DiskColor, score=0) -> None:
        self.color = color.name
        self.color_value = color.value
        self.score = score      


    def calculate_score(self, board: Board):
        return self.score

    