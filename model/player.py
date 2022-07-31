from model.disk_color import DiskColor

class Player:
    ""

    def __init__(self, color: DiskColor, score=0) -> None:
        self.color = color
        self.color_name = color.name
        self.color_value = color.value
        self.valid_moves = []
        self.score = score      


    def search_valid_moves(self):
        pass